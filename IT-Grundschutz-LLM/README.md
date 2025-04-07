# IT-Grundschutz LLM

## Installation
- Requirements installieren
- Ollama installieren https://ollama.com/download
- Modelle installieren:
  - `ollama run llama3.2`
  - `ollama pull jina/jina-embeddings-v2-base-de`
- PDFs in data-Ordner einfügen (Siehe Readme dort)

## PDFs einpflegen
- Bei Bedarf: Datenbank zurücksetzen: `python populate_database.py --reset`
- Gewünschte PDFs in den `data` Ordner einfügen (einzelne PDFs mit aussagekräftigen Namen besser als große Sammlungen)
- `python populate_database.py` ausführen

## Nutzung
- `python chat.py` ausführen (Ollama wird automatisch im Hintergrund gestartet, solange es in PATH hinterlegt ist)
- Beliebig viele Fragen in der Kommandozeile stellen 
- Dokumente (.pdf, .md, .txt) können per Pfad in der Nachricht übergeben werden
- Quellen können mit "/Sources" oder "/Source n" angezeigt werden
- Der Chat wird mit "/exit" verlassen und kann gespeichert werden
- Mit "/repeat" wird eine Frage mit doppelter Quellenanzahl wiederholt
- Mit "/followup" kann eine Folgefrage gestellt werden, wofür einmalig die Chathistorie aktiviert wird
- Mit "/search-mode" werden nur die Quellen geladen und angezeigt, wodurch sich die Laufzeit erheblich verkürzt
- Mit "/help" werden einem alle Befehle angezeigt

## Hinweise
- Aus Effizienzgründen ist der Chatbot so konzeptioniert, dass er keine vorherigen Nachrichten lesen oder Antworten mit einbezieht.
Deshalb muss jede Frage genug Kontext bereithalten, um beantwortet zu werden. 
Es ist möglich mit der Variable "history = True" diese Funktion im Code zu aktivieren
- Um andere Modelle und Datenbanken zu verwenden müssen diese bei Ollama installiert und im Code namentlich eingefügt werden
- Eine Beispiel API Implementierung ist in get_embedding_function.py hinterlegt
- In "LLM Fragen.xlsx" befindet sich eine ausführliche Evaluation und Vergleich von leistungsstarken IT-Grundschutz Chatbots