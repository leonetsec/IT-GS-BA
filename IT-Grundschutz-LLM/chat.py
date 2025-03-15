import os
import re
import time
import PyPDF2
from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
from get_embedding_function import get_embedding_function

# Hier festlegen, ob Chathistorie aktiviert sein soll (längere Ausführungszeit) und wie viele Quellen geladen werden sollen (Default: 8)
history = False
number_of_sources = 8

# Hier Datenbank festlegen
def get_database():
    return Chroma(persist_directory=os.path.join(os.path.dirname(__file__), "chroma"), embedding_function=get_embedding_function())

# Hier Ollama LLM festlegen
def get_llm():
    return OllamaLLM(model="llama3.2")

PROMPT_TEMPLATE = """
        Du bist ein RAG-Sprachmodell, das Fragen zum BSI IT-Grundschutz beantwortet. 
        Beantworte die nachfolgende Frage ausschließlich basierend auf dem folgenden Kontext: {context} 
        Hier ist die Frage: {question}
        """

EMB_PROMPT_TEMPLATE = """
        Du bist Teil eines RAG-Sprachmodells, das Fragen zum BSI IT-Grundschutz beantwortet.
        Fasse zusammen was der User wissen möchte, basierend auf dem bisherigen Chatverlauf und der nachfolgenden Frage des Users.
        Hier ist der Chatverlauf: {chat_history}
        Hier ist die Frage: {question} 
        Antworte ausschließlich welche Informationen der User anfordert, beantworte die Frage nicht und sage nichts darüber hinaus.
        """

# Holt gewünschte Quelle aus der Datenbank
def get_source_by_id(source_id: str):
    db = get_database()
    try:
        results = db.get(ids=[source_id])
        if "documents" in results and results["documents"]:
            return results["documents"][0]
        else:
            print(f"Source with ID {source_id} not found.")
    except Exception as e:
        print(f"Error getting the source: {e}")
    return None

# Behandelt die Quellen, um dem Nutzer bei Bedarf den Text anzuzeigen
def process_sources(command, numbered_sources, chat_history):
    query_parts = command.split(" ")

    if len(query_parts) > 1 and query_parts[1].isdigit():
        source_number = query_parts[1]
        source_id = numbered_sources.get(source_number)
        if source_id:
            source_text = get_source_by_id(source_id)
            print(f"\nSource {source_number}: {source_text}")
            chat_history.append(f"\nSource {source_number}: {source_text}")
        else:
            print(f"\nWrong source number: {source_number}")
        return True

    if len(query_parts) == 1 and numbered_sources:
        print("Listing all sources:")
        for number, source_id in numbered_sources.items():
            source_text = get_source_by_id(source_id)
            print(f"\nSource {number}: {source_text}")
            chat_history.append(f"\nSource {number}: {source_text}")
        print("\n")
        return True
    return False

# Speichert den Chatverlauf in einer Datei
def save_file(chat_history):
    save_prompt = input("Do you want to save the chat history? [Y/n]: ").strip().lower()
    if save_prompt in ('y', 'yes', ''):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        timestamp = time.strftime("%Y-%m-%d_%H-%M")
        filename = f"chat_history_{timestamp}.txt"
        file_path = os.path.join(script_dir, filename)

        with open(file_path, "w") as file:
            for line in chat_history:
                file.write(line + "\n")
        print(f"Chat history saved to '{file_path}'.")
        return

# Wiederholt die Frage mit der doppelten Zahl an Quellen
def repeat_question(chat_history):
    global number_of_sources
    original_sources = number_of_sources
    number_of_sources = 2 * original_sources

    query_text = None
    for entry in reversed(chat_history):
        if entry.startswith("\nUser:"):
            query_text = entry.split("\nUser:", 1)[1].split("\n")[0].strip()
            break

    if not query_text:
        print("Error: No previous query found to repeat.")
        number_of_sources = original_sources
        return

    print(f"\nRepeating the last query '{query_text}' with {number_of_sources} instead of {original_sources} sources...\n")

    response, numbered_sources = query_rag(query_text, chat_history)

    if response:
        chat_history.append(f"\nUser (repeat): {query_text}\nChatbot: {response}\nSource list: {numbered_sources}")
    number_of_sources = original_sources

# Handler für eine Folgefrage des Nutzers
def followup(chat_history):
    global history
    original_history = history
    history = True
    followup_query = input("Follow-up question: ").strip()
    print("\nProcessing...\n")
    response, numbered_sources = query_rag(followup_query, chat_history)
    if response:
        chat_history.append(f"\nUser (follow-up): {followup_query}\nChatbot: {response}\nSource list: {numbered_sources}")
    history = original_history

# Stellt nur die Anfrage an das Embeddingmodell und gibt dieses Ergebnis aus
def search_mode(chat_history):
    global number_of_sources
    db = get_database()
    original_sources = number_of_sources
    query_text = input("Question: ").strip()
    number_of_sources = int(input("Number of sources to load: ").strip())

    try:
        start_time = time.time()
        results = db.similarity_search_with_score(query_text, k=number_of_sources)
        print("Embedding time:", time.time() - start_time, "s")
    except Exception as e:
        print("Error: Unable to use the Ollama Embedding model. Please check your setup and try again.")
        print(f"Details: {e}")
        return
    chat_history.append(f"\nUser: {query_text}")

    sources = [doc.metadata.get("id", None) for doc, _score in results]
    numbered_sources = {str(index + 1): source for index, source in enumerate(sources)}

    print("\nSource list:\n")
    for number, source_id in numbered_sources.items():
        print(f"{number}: {source_id}")

    source_id: str
    for number, source_id in numbered_sources.items():
        source_text = get_source_by_id(source_id)
        print(f"\nSource {number} {source_id}:\n {source_text}")
        chat_history.append(f"\nSource {number}: {source_text}")
    print("\n")
    number_of_sources = original_sources

# Behandelt das Einlesen von Dateien
def read_file(file_path: str) -> str:
    try:
        _, file_extension = os.path.splitext(file_path)
        if file_extension.lower() == ".pdf":
            text = extract_text_from_pdf(file_path)
        elif file_extension.lower() in [".md", ".txt"]:
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()
        else:
            raise ValueError(f"Unsupported file type: {file_extension}")
        return text
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return ""

# Erstellt den Kontext für das Sprachmodell auf dem Ergebnis des Embeddingmodells
def generate_context(results, query_text, final_query_text):
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    file_paths = extract_file_paths_from_message(query_text)
    for file_path in file_paths:
        file_content = read_file(file_path)
        if file_content:
            context_text += f"\n\n---\n\nInhalt der Datei '{file_path}':\n{file_content}"
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=final_query_text)
    return prompt

# Extrahiert Text einer PDF
def extract_text_from_pdf(file_path: str) -> str:
    text = ""
    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
    return text

# Schaut mit Regex ob sich gültige Dateipfade für pdf, md oder txt in Nachricht befinden
def extract_file_paths_from_message(message: str):
    pattern = r"(?:[a-zA-Z]:)?(?:[\\/][\w\s.-]+)+\.(?:pdf|txt|md)"
    file_paths = re.findall(pattern, message)
    return [path for path in file_paths if os.path.isfile(path)]

# Hauptfunktion, stellt die Anfrage an Embedding- und Sprachmodell
def query_rag(query_text: str, chat_history: list):
    start_time = time.time()
    db = get_database()

    if not history:
        try:
            results = db.similarity_search_with_score(query_text, k=number_of_sources)
            print("Embedding time:", time.time() - start_time, "s")
            final_query_text = query_text

        except Exception as e:
            print("Error: Unable to use the Ollama Embedding model. Please check your setup and try again.")
            print(f"Details: {e}")
            return

    else:
        emb_prompt_template = ChatPromptTemplate.from_template(EMB_PROMPT_TEMPLATE)
        chat_history_text = "\n".join(chat_history)
        emb_prompt = emb_prompt_template.format(chat_history=chat_history_text, question=query_text)

        try:
            history_extra_start = time.time()
            model = get_llm()
            final_query_text = model.invoke(emb_prompt)
            print("History extra time: ", time.time() - history_extra_start,"s")
            #print(final_query_text)
            results = db.similarity_search_with_score(final_query_text, k=number_of_sources)

        except Exception as e:
            print("Error: Unable to use the Ollama models. Please check your setup and try again.")
            print(f"Details: {e}")
            return

    context_start = time.time()
    prompt = generate_context(results, query_text, final_query_text)
    context_end = time.time()
    print("Context fetching time:", context_end - context_start, "s")

    try:
        model = get_llm()
        response_text = model.invoke(prompt)
    except Exception as e:
        print("Error: Unable to connect to the Ollama language model. Please check your model setup and try again.")
        print(f"Details: {e}")
        return

    llm_time = time.time()
    print("LLM time:", llm_time - context_end, "s")

    print(f"Response: {response_text}\n")

    sources = [doc.metadata.get("id", None) for doc, _score in results]
    numbered_sources = {str(index + 1): source for index, source in enumerate(sources)}

    print("\nSources (Type \"/Source n\" to view single source, type \"/Sources\" to view all sources):\n")
    for number, source_id in numbered_sources.items():
        print(f"{number}: {source_id}")

    overall_time = time.time()
    print("Overall time:", overall_time - start_time, "s")

    return response_text, numbered_sources

# Listet mögliche Befehle bei /help auf
def list_commands():
    commands = {
        "/exit": "Exit the chat and optionally save the chat history.",
        "/repeat": "Repeat the last query with twice as many sources for the LLM.",
        "/source [n]": "Show the content of source number [n].",
        "/sources": "Show all sources.",
        "/followup": "Ask a follow-up question.",
        "/search-mode": "Only get search results from the sources that are most likely to match the query.",
        "/help": "Show this list of commands."
    }
    print("\nAvailable Commands:\n")
    for command, description in commands.items():
        print(f"  {command:20} - {description}")
    print()

# Behandelt gegebene Befehle
def command_handler(chat_history, numbered_sources, query_text):
    command = query_text[1:].lower()
    if command == "exit":
        save_file(chat_history)
        print("\nGoodbye!")
        return False
    elif command in ("repeat", "retry"):
        repeat_question(chat_history)
    elif command.startswith("source"):
        if process_sources(command, numbered_sources, chat_history):
            return True
    elif command == "followup":
        followup(chat_history)
    elif command == "search-mode":
        search_mode(chat_history)
    elif command in ("help", "h", "?"):
        list_commands()
    else:
        print(f"Unknown command: {query_text}")
    return True



def main():
    print("Starting chat! Type '/exit' to end the conversation. Type '/help' for help\n")
    numbered_sources = {}
    chat_history = []

    while True:
        query_text = input("You: ").strip()

        if query_text.startswith(("/", "\\")):
            if not command_handler(chat_history, numbered_sources, query_text):
                break
            continue

        print("\nProcessing...\n")

        response, numbered_sources = query_rag(query_text, chat_history)

        if response:
            chat_history.append(f"\nUser: {query_text}\nChatbot: {response}\nSource list: {numbered_sources}")
        print("\n")


if __name__ == "__main__":
    main()
