import re
import yaml
import argparse
import os
import pandas as pd
from template import template

# Erstellt eine neue Markdown-Datei nach Template, falls sie nicht existiert                
def new_file_with_template(directory):
    if not os.path.isdir(directory):
        print(f"{directory} ist kein gültiger Ordner, bitte Zielordner angeben.")
        return
    filepath = f"{directory}/neue_richtlinie.md"
    os.makedirs(directory, exist_ok=True)

    # Datei nur erstellen, wenn sie nicht existiert
    if not os.path.exists(filepath):
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(template)
        print(f"Markdown-Datei '{filepath}' wurde erstellt.")
    else:
        print(f"Die Datei '{filepath}' existiert bereits. Vorgang abgebrochen")

# Vereinheitlicht IDs, falls eindeutige IDs verwendet werden
def id_unify(id):
    id = id.upper()
    if id[-1].isalpha():
        id = id[:-1]
    if 'A' in id and '.A' not in id:
        last_a_index = id.rfind('A')
        if last_a_index != -1:
            id = id[:last_a_index] + '.' + id[last_a_index:]
    return id

# Überprüft den Umsetzungsstatus von Anforderungen in Richtlinien
def check(path, typ):
    files = set()
    if os.path.isfile(path):
        files.add(path)
    elif os.path.isdir(path):
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path) and file_path.endswith(('.md', '.markdown')):
                files.add(file_path)
    else:
        print("Kein gültiger Pfad, Vorgang wird abgebrochen.")
        return

    try:
        script_dir = os.path.dirname(__file__)
        json_path = os.path.join(script_dir, "IT-Grundschutz.json")
        it_gs = pd.read_json(json_path, orient="records")
    except FileNotFoundError:
        print("\nFehler: Die Datei 'IT-Grundschutz.json' wurde nicht im Skriptverzeichnis gefunden.")
        return

    it_gs['Baustein_ID'] = it_gs['ID-Anforderung'].str.split('.A', expand=True)[0]
    it_gs['ID_unified'] = it_gs['ID-Anforderung'].apply(id_unify)

    inhalt_choice = input("\nInhalt der Anforderungen mit ausgeben? Antwort (j/N): ")
    if inhalt_choice.lower() in ["j", "ja"]:
        inhalt = True
    else:
        inhalt = False

    for file_path in files:

        baustein_references = set()

        with open(file_path, 'r') as file:
            content = file.read()

        metadata_match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
        if not metadata_match:
            print(f"\nKeine Metadaten in {file_path} gefunden.")
            continue

        metadata_block = metadata_match.group(1)
        metadata = yaml.safe_load(metadata_block)
        bsi_references = metadata.get("refs", [{}])[0].get("bsi")

        if not bsi_references:
            print(f"\nKeine BSI IT-Grundschutz Referenzen in den Metadaten von {file_path} gefunden.")
            continue

        for bsi_reference in bsi_references:
            main_reference = bsi_reference.upper()
            main_reference = main_reference.split('.A')[0]

            main_reference = main_reference.replace("-", ".")

            baustein_references.add(main_reference)

        comment_pattern = re.compile(r"<!--\s*(.*?)\s*-->", re.DOTALL)

        comment_contents = comment_pattern.findall(content)

        erfuellt = []
        teilweise = []
        entbehrlich = []

        for item in comment_contents:
            cleaned_item = item.strip()

            status = "erfüllt"
            ids_part = cleaned_item

            if ':' in cleaned_item:
                parts = cleaned_item.rsplit(':', 1)
                ids_part = parts[0].strip()
                status = parts[1].strip().lower()


            ids = re.split(r'[\s,;]+', ids_part)

            for single_id in ids:
                if not single_id:
                    continue

                unified_id = id_unify(single_id.strip().upper())

                if status == "erfüllt":
                    erfuellt.append(unified_id)
                elif status == "teilweise":
                    teilweise.append(unified_id)
                elif status == "entbehrlich":
                    entbehrlich.append(unified_id)

        relevante_anforderungen = it_gs[it_gs['Baustein_ID'].isin(baustein_references)].copy()

        if typ == 'basis':
            relevante_anforderungen = relevante_anforderungen[relevante_anforderungen['Typ'] == 'Basis']
        elif typ == 'standard':
            relevante_anforderungen = relevante_anforderungen[
                relevante_anforderungen['Typ'].isin(['Basis', 'Standard'])]
        # Bei hoch werden alle beibehalten

        dokumentierte_ids = set(erfuellt + teilweise + entbehrlich)
        alle_relevanten_ids = set(relevante_anforderungen['ID_unified'])
        nicht_umgesetzte_ids = list(alle_relevanten_ids - dokumentierte_ids)

        print(f"\n\n========================================================")
        print(f"   Analyse für Datei: {os.path.basename(file_path)}")
        print(f"========================================================")

        print("\n--- Übersicht ---")
        print(f"Schutzbedarfstyp: {typ.capitalize()}")
        print(f"Umgesetzt: {len(erfuellt)}")
        print(f"Teilweise umgesetzt: {len(teilweise)}")
        print(f"Entbehrlich: {len(entbehrlich)}")
        print(f"Nicht umgesetzt / Nicht dokumentiert: {len(nicht_umgesetzte_ids)}")

        # Hilfsfunktion für formatierte Ausgabe
        def print_section(title, ids, df, inhalt):
            print(f"\n--- {title} ({len(ids)}) ---")
            if not ids:
                print("Keine")
                return

            grouped_items = {}

            for anforderung_id in ids:
                details = df[df['ID_unified'] == anforderung_id]
                if not details.empty:
                    for index, detail in details.iterrows():
                        key = (detail['ID_unified'], detail['Titel'])
                        if key not in grouped_items:
                            grouped_items[key] = []
                        grouped_items[key].append(detail['Inhalt'])

            sorted_keys = sorted(grouped_items.keys())

            for id_title_key in sorted_keys:
                anforderung_id, title = id_title_key
                contents = grouped_items[id_title_key]
                print(f"\n{anforderung_id} - {title}")
                if inhalt:
                    unique_contents = []
                    [unique_contents.append(x) for x in contents if x not in unique_contents]
                    print(f"{' '.join(unique_contents)}")

        print_section("Umgesetzt", erfuellt, relevante_anforderungen, inhalt)
        print_section("Teilweise umgesetzt", teilweise, relevante_anforderungen, inhalt)
        print_section("Entbehrlich", entbehrlich, relevante_anforderungen, inhalt)
        print_section("Nicht umgesetzt / Nicht dokumentiert", nicht_umgesetzte_ids, relevante_anforderungen, inhalt)

# Hauptprogramm zur Verarbeitung von Kommandozeilenargumenten
def main():
    parser = argparse.ArgumentParser(description='Verarbeitet Markdown-Richtlinien und lädt sie mit Mark hoch.')
    parser.add_argument('file_dir_or_string', help='Pfad zu Datei, Verzeichnis oder String')
    parser.add_argument("--check", action="store_true", help="Prüft die Anforderungen von Richtlinien auf Vollständigkeit")
    parser.add_argument('--typ', choices=['basis', 'standard', 'hoch'], default='standard', help='(Mit --check-reqs) Gibt den Typ bei der Anforderungsprüfung an (Default: standard).')
    parser.add_argument("--new", action="store_true", help="Erstellt eine neue Richtlinien nach Template")

    args = parser.parse_args()

    if args.check:
        check(args.file_dir_or_string, args.typ)
        return

    elif args.new:
        new_file_with_template(args.file_or_dir)
        return

    else: print("Kein Argument ausgewählt")

if __name__ == '__main__':
    main()