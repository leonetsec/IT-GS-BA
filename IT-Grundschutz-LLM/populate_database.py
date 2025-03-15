import argparse
import os
import shutil
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from get_embedding_function import get_embedding_function
from langchain_chroma import Chroma

CHROMA_PATH = os.path.join(os.path.dirname(__file__), "chroma")
DATA_PATH = os.path.join(os.path.dirname(__file__), "data")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", action="store_true", help="Reset the database.")
    args = parser.parse_args()
    if args.reset:
        print("Clearing Database")
        clear_database()

    documents = load_documents()
    # print(documents[0])
    chunks = split_documents(documents)
    add_to_chroma(chunks)


def load_documents():
    document_loader = PyPDFDirectoryLoader(DATA_PATH)
    return document_loader.load()

# Stellschraube für Embedding
def split_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_documents(documents)


def add_to_chroma(chunks: list[Document]):
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=get_embedding_function())

    chunks_with_ids = calculate_chunk_ids(chunks)

    existing_items = db.get(include=[])
    existing_ids = set(existing_items["ids"])
    print(f"Number of existing document chunks in DB: {len(existing_ids)}")

    new_chunks = []
    for chunk in chunks_with_ids:
        if chunk.metadata["id"] not in existing_ids:
            new_chunks.append(chunk)

    if len(new_chunks) > 0:
        print(f"Total new document chunks to add: {len(new_chunks)}")
        try:
            chunk_batch_size = 3000
            for i in range(0, len(new_chunks), chunk_batch_size):
                chunk_batch = new_chunks[i:i + chunk_batch_size]
                new_chunk_ids = [chunk.metadata["id"] for chunk in chunk_batch]
                print(f"Adding batch {int((i/chunk_batch_size)+1)} with {len(chunk_batch)} chunks to the database")
                db.add_documents(chunk_batch, ids=new_chunk_ids)

            print("All new chunks added successfully.")
        except Exception as e:
            print(
                "Error: Unable to connect to the Ollama Embedding model. Please check your model setup and try again.")
            print(f"Details: {e}")
            return
    else:
        print("No new documents to add")

# Berechnet Chunk Namen basierend auf der Stelle in der PDF
def calculate_chunk_ids(chunks):
    last_page_id = None
    current_chunk_index = 1

    for chunk in chunks:
        source = chunk.metadata.get("source")
        filename = os.path.basename(source)
        page = chunk.metadata.get("page") + 1
        current_page_id = f"{filename}_page_{page}"

        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 1

        chunk_id = f"{current_page_id}_chunk_{current_chunk_index:02d}"
        last_page_id = current_page_id

        chunk.metadata["id"] = chunk_id

    return chunks


def clear_database():
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)
    print("Database cleared")


if __name__ == "__main__":
    main()
