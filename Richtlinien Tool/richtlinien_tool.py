import re
import yaml
import subprocess
import argparse
import os
from mapping import bsi_ref_mapping, bsi_ref_titles, template

# Jahr festlegen auf aktuellen IT-Grundschutz
year = '2023'

# Pfad der Config festlegen
default_config = "mark.config"

# Mark Header für Confluence
default_space = "SPACE"
default_parent = [
    "FIRST PARENT",
    "SECOND PARENT",
    "THIRD PARENT"
]

def generate_bsi_link(reference):

    # Verschiedene Schreibweisen abfangen
    reference = reference.replace("-", ".").replace(" ", "")
    reference = re.sub(r'([A-Za-z]+)(\d+)', r'\1.\2', reference)

    
    # Finde Referenzen auf einzelne Anforderungen
    position = reference.lower().find('.a')
    
    # Wenn ".A" oder ".a" gefunden wird, den Teil davor extrahieren
    if position != -1:
        reference = reference[:position]
    
    # Den verbleibenden Teil in Großbuchstaben umwandeln
    base_reference = reference.upper()  
    
    # Überprüfe, ob der Präfix in unserem Mapping ist 
    prefix_match = re.match(r'([A-Za-z]+)', base_reference)
    if prefix_match:
        prefix = prefix_match.group(1).upper()
        
        if prefix in bsi_ref_mapping and base_reference in bsi_ref_titles:
            directory = bsi_ref_mapping[prefix]
            title = bsi_ref_titles[base_reference]

            # Anpassung der Linkerstellung basierend auf den Inkonsistenzen in der Linkgenerierung
            if base_reference.startswith('ORP.') and base_reference != 'ORP.1': # Rechtschreibfehler "Editon"
                link = (
                    f"https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_{year}/"
                    f"{directory}/{title}_Editon_{year}.pdf"
                )
            elif base_reference in ['DER.2.2', 'SYS.3.2.3']: #Edition_Jahr fehlt
                link = (
                    f"https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_{year}/"
                    f"{directory}/{title}.pdf"
                )
            else:  # Für alle anderen Referenzen
                link = (
                    f"https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_{year}/"
                    f"{directory}/{title}_Edition_{year}.pdf"
                )
            return link
            
    return "Kein gültiger BSI-Link verfügbar"

# Funktion, um den Metadatenblock zu extrahieren, verarbeiten und den neuen Inhalt zu generieren
def process_content(content, space, parents):
    used_references = set()  # Doppelte Referenzen für die aktuelle Datei verhindern
    
    # Entfernen des Abschnitts "### BSI-Grundschutz" und dessen Inhalt falls vorhanden
    content = re.sub(r"(?s)### BSI-Grundschutz.*?###", "###", content, flags=re.DOTALL)
    
    # Extrahiere den YAML-Metadatenblock
    metadata_match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if metadata_match:
        metadata_block = metadata_match.group(1)
        
        # Entferne den Metadatenblock aus dem Originalinhalt und speichere den Inhalt
        content_without_metadata = re.sub(r"^---\n(.*?)\n---\n", "", content, flags=re.DOTALL)
        
        # Verarbeite den YAML-Block
        metadata = yaml.safe_load(metadata_block)
        
        # Generiere den neuen Inhalt mit den Metadaten, falls nicht vorhanden setze ihn 
        author = metadata.get("editor", "Missing")
        date = metadata.get("date", "Missing")
        approved_date = metadata.get("approved", "Missing")
        title = metadata.get("title", "Missing")

        # Hole die BSI-Referenzen und generiere Links für jede Hauptreferenz
        bsi_references = metadata.get("refs", [{}])[0].get("bsi", ["Kein Link verfügbar"])
        bsi_links = []
        #used_references = set()  # Set zur Verfolgung verwendeter Referenzen

        for bsi_reference in bsi_references:
            # Splitte die Referenz bei ".A" und behalte nur den Hauptteil
            main_reference = bsi_reference.split('.A')[0]  # z.B. aus "OPS.1.A7" wird "OPS.1"
            
            main_reference = main_reference.upper()
            
            # Überprüfe, ob die Hauptreferenz bereits verwendet wurde
            if main_reference not in used_references:
                used_references.add(main_reference)  # Füge die verlinkte Referenz hinzu
                bsi_links.append(f"- [{main_reference}]({generate_bsi_link(main_reference)})")

        parents_str = "\n".join([f"<!-- Parent: {p} -->" for p in parents])
        mark_header = f"""<!-- Space: {space} -->\n{parents_str}\n<!-- Title: {title} -->"""

        # Füge die BSI-Links in das Markdown-Dokument ein
        bsi_links_str = "\n".join(bsi_links) if bsi_links else "Keine BSI-Referenzen verfügbar."
        
         # Teile den Inhalt an der Stelle "## Anhang"
        parts = re.split(r"(## Anhang)", content_without_metadata, maxsplit=1)
        
        if len(parts) > 1:
            content_before_split = parts[0]
            split_section = "".join(parts[1:])  # "## Anhang" und der Rest
        else:
            content_before_split = content_without_metadata
            split_section = ""

        # Dokument zusammenbauen
        new_content = f"""
{mark_header}

{content_before_split}

## Metadaten und BSI IT-Grundschutz-Referenzen

**Autor**: {author}  
**Datum**: {date}  
**Abnahmedatum**: {approved_date}  
**BSI-Grundschutz-Kompendium**:  
{bsi_links_str}

{split_section}
"""
        return new_content.strip()

# Funktion, um eine Markdown-Datei einzulesen, zu verarbeiten und wieder zu speichern
def process_markdown_file(file_path, space, parent, config, keep_structure, folder, mark_arg):
    if "_processed" in file_path:
        print(f"Ignoriere Datei: {file_path} (bereits verarbeitet)")
        return
    
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Ordnerstruktur beibehalten falls keep_structure aktiviert ist
    rel_path = os.path.relpath(file_path, start=os.getcwd())
    folder_structure = os.path.dirname(rel_path).split(os.sep) if keep_structure else []
    
    # Ordnerstruktur festlegen
    parents = parent + folder_structure
    if folder:
        parents.append(folder)
    
    # Markdown verarbeiten
    processed_content = process_content(content, space, parents)
    
    # Zielverzeichnis festlegen, falls keep_structure aktiv ist
    output_dir = os.path.join(os.getcwd(), *folder_structure) if keep_structure else os.getcwd()
    os.makedirs(output_dir, exist_ok=True)
    
    # Verarbeitete Datei speichern, löschen falls bereits existierend
    output_path = os.path.join(output_dir, os.path.basename(file_path).replace(".md", "_processed.md"))
    if os.path.exists(output_path):
        print(f"Lösche existierende Datei: {output_path}")
        os.remove(output_path)
    with open(output_path, 'w') as file:
        file.write(processed_content)
    print(f"Verarbeitete Datei gespeichert unter: {output_path}")
    
    # Datei mit Mark hochladen
    try:
        subprocess.run(["mark", "--config", config, "-f", output_path, mark_arg], check=True)
        print(f"Datei erfolgreich hochgeladen: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Hochladen der Datei: {e}")

# Funktion, um alle Dateien in einem Verzeichnis zu verarbeiten
def process_all_files_in_directory(directory, space, parent, config, keep_structure, folder, mark_arg):
    for filename in os.listdir(directory):
        if filename.endswith(".md") and "_processed" not in filename:
            file_path = os.path.join(directory, filename)
            print(f"Verarbeite Datei: {file_path}")
            process_markdown_file(file_path, space, parent, config, keep_structure, folder, mark_arg)
        else:
            print(f"Ignoriere Datei: {filename} (bereits verarbeitet)")
            
# Funktion, um alle Dateien auch in Unterordnern zu verarbeiten             
def process_all_files_including_subdirectories(directory, space, parent, config, keep_structure, folder, mark_arg):
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".md") and "_processed" not in filename:
                file_path = os.path.join(root, filename)
                print(f"Verarbeite Datei in Unterordner: {file_path}")
                process_markdown_file(file_path, space, parent, config, keep_structure, folder, mark_arg)
            else:
                print(f"Ignoriere Datei: {filename} (bereits verarbeitet)")

# Erstellt eine neue Markdown-Datei nach Template, falls sie nicht existiert                
def new_file_with_template(directory):
    filepath = f"{directory}/neue_richtlinie.md"
    os.makedirs(directory, exist_ok=True)  # Ordner erstellen, falls nicht vorhanden

    # Datei nur erstellen, wenn sie nicht existiert
    if not os.path.exists(filepath):
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(template)
        print(f"Markdown-Datei '{filepath}' wurde erstellt.")
    else:
        print(f"Die Datei '{filepath}' existiert bereits. Vorgang abgebrochen")


# Hauptprogramm zur Verarbeitung von Kommandozeilenargumenten
def main():
    parser = argparse.ArgumentParser(description='Verarbeitet Markdown-Richtlinien und lädt sie mit Mark hoch.')
    parser.add_argument('file_or_dir', help='Pfad zur Datei oder zum Verzeichnis')
    parser.add_argument('--all', action='store_true', help='Verarbeite alle Dateien im angegebenen Verzeichnis')
    parser.add_argument('--include-folders', action='store_true', help='(Mit --all) Verarbeite alle Dateien inkl. denen in Unterordnern')
    parser.add_argument('--keep-structure', action='store_true', help='(Mit --include-folders) Behalte die Unterordnerstruktur für Confluence bei')
    parser.add_argument('--space', default=default_space, help=f'Space für den Mark-Header einmalig ändern (Default: {default_space})')
    parser.add_argument('--parent', nargs="+", default=default_parent, help=f'Parent-Ordner für den Mark-Header einmalig ändern (Default: {default_parent})')
    parser.add_argument('--config', default=default_config, help=f'Config einmalig ändern (Default: {default_config})')
    parser.add_argument('--folder', default="", help='Füge Datei(en) in neuen oder spezifischen Ordner im/in Parent-Ordner(n) ein')
    parser.add_argument('--compile-only', action='store_true', help='Zeige kompiliertes HTML ohne es auf Confluence hochzuladen')
    parser.add_argument('--minor-edit', action='store_true', help='Sende keine Benachrichtigung wenn das Dokument auf Confluence aktualisiert wird')
    parser.add_argument('--changes-only', action='store_true', help='Nur geänderte Dokumente hochladen')
    parser.add_argument('--mark-arg', default="", help='Argument(e) an Mark-Tool weitergeben')
    parser.add_argument("--new", action="store_true", help="Erstellt eine neue Richtlinien nach Template")
    args = parser.parse_args()
    
    if args.new:
        new_file_with_template(args.file_or_dir)
        return
        
        
    mark_arg = []
    if args.compile_only:
        mark_arg.append("--compile-only")
    if args.minor_edit:
        mark_arg.append("--minor-edit")
    if args.changes_only:
        mark_arg.append("--changes-only")
    if args.mark_arg:
        mark_arg.append(args.mark_arg)
    
    mark_arg_str = " ".join(mark_arg)
    
    if args.all and args.include_folders:
        if os.path.isdir(args.file_or_dir):
            process_all_files_including_subdirectories(args.file_or_dir, args.space, args.parent, args.config, args.keep_structure, args.folder, mark_arg_str)
        else:
            print(f"{args.file_or_dir} ist kein gültiges Verzeichnis.")
    elif args.all:
        if os.path.isdir(args.file_or_dir):
            process_all_files_in_directory(args.file_or_dir, args.space, args.parent, args.config, args.keep_structure, args.folder, mark_arg_str)
        else:
            print(f"{args.file_or_dir} ist kein gültiges Verzeichnis.")
    else:
        if os.path.isfile(args.file_or_dir):
            process_markdown_file(args.file_or_dir, args.space, args.parent, args.config, args.keep_structure, args.folder, mark_arg_str)
        else:
            print(f"{args.file_or_dir} ist keine gültige Datei.")

if __name__ == '__main__':
    main()