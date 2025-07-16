# Readme Richtlinien Tool

## Installation
- [Mark](https://github.com/kovetskiy/mark) installieren
- ```richtlinien_tool.py``` und ```mapping.py``` müssen sich im selben Ordner befinden
- Config erstellen, Confluence API Key erstellen und in ```config``` einfügen (s.u.)
- Aktuelles IT-Grundschutz-Jahr, Ort der config und Default Confluence Zielort in ```richtlinien_tool.py``` festlegen
- Optional: Richtlinien Template in ```mapping.py``` ändern (evtl. funktioniert Tool dann nicht mehr wie gewünscht)
- Eventuell ```mapping.py``` anpassen, wenn in Zukunft der Aufbau oder die Links des IT-Grundschutzes geändert werden
- ```IT-Grundschutz.json``` einfügen/anpassen (für --check-reqs). Dafür mit IT-Grundschutz-Check Tool exportieren (Entfallene Anforderungen entfernen, zu einer Datei zusammenfassen)

## Einführung

Mark kann genutzt werden, um Markdown Dokumente nach Confluence Seiten zu parsen.
Dafür ist es wichtig das in den Markdown (.md) Dateien ein Mark Tool Header existiert.
In unserem Fall besteht er aus einem **Space**, mehreren **Parents** und einem **Title**.
Der Header sehen deshalb wie folgt aus. <br>
```
Space: <!-- Space: SPACE --> 
Parent: <!-- Parent: FIRST PARENT -->
Parent: <!-- Parent: SECOND PARENT -->
Parent: <!-- Parent: THIRD PARENT-->
Title: <!-- Title: Titel der Richtline -->
```

Um Mark zu benutzen ist folgender Befehl notwendig: ```mark --config mark.conf -f Test.md```
Hier wird mit```--config``` eine Konfigurationsdatei angegeben in der ein Confluence API Key, die Confluence base URL, ob der Titel aus der ersten Überschrift übernommen und ob die erste Überschrift entfernt werden soll definiert wird.
Dies kann wie folgt aussehen: <br>
```
password = "api-key"
base-url = "https://confluence.test.com" <br>
title-from-h1 = true
drop-h1 = true
```
Als zweiter Parameter unter ```-f``` benötigt der Mark-Befehl das die Datei die hochgeladen werden soll.

Um den Prozess zu automatisieren, kann das Script **richtlinien_tool.py** benutzt werden.
Es arbeitet wie folgt.
- Es entfernt einen Yaml-Block mit Metadaten am Anfang und fügt die Metadaten an den Anfang bzw. in den Referenzteil
- Es werden Referenzen zu den BSI Richtlinien als Hyperlink gesetzt und der Name des Bausteins hinterlegt
- Doppelte Referenzen werden zusammengefasst
- Referenzen auf einzelne Anforderungen der Richtlinie werden als Referenz auf die gesamte Richtlinie aufgefasst
- Aus den Metadaten wird der Mark Tool Header erstellt
- Die Richtline als .md Datei wird in Confluence unter dem Verzeichnis im Mark Tool Header abgelegt und hochgeladen

## Nutzung

Um eine Markdown Datei wie gewünscht umzuwandeln und auf Confluence zu parsen wird folgender Befehl benötigt: ```python3 richtlinien_tool.py [path to file]```

Weitere Befehle, die das Tool unterstützt sind:

- --all: Verarbeite alle Dateien im angegebenen Verzeichnis
- --include-folders: (Mit --all) Verarbeite alle Dateien inkl. denen in Unterordnern
- --keep-structure_ (Mit --include-folders) Behalte die Unterordnerstruktur für Confluence bei
- --space: Space für den Mark-Header einmalig ändern 
- --parent: Parent-Ordner für den Mark-Header einmalig ändern
- --config: Config einmalig ändern
- --folder: Füge Datei(en) in neuen oder spezifischen Ordner im/in Parent-Ordner(n) ein
- --compile-only: Zeige kompiliertes HTML ohne es auf Confluence hochzuladen
- --minor-edit: Sende keine Benachrichtigung wenn das Dokument auf Confluence aktualisiert wird
- --changes-only: Nur geänderte Dokumente hochladen
- --mark-arg: Argument(e) an Mark-Tool weitergeben
- --new: Erstellt eine neue Richtlinien nach Template
- --check-reqs: Überprüft, ob die in den Metadaten vorkommenden Bausteine in der Richtlinie abgedeckt werden
- --typ: (Mit --check-regs): Definiert, ob für die Überprüfung der Schutzbedarfstyp Basis, Standard oder Hoch ausgewählt wird, Default: Standard

Sollten bereits Dateien mit dem gleichen Namen im gleichen Verzeichnis vorhanden sein werde diese mit dem Hochladen auf Confluence überschrieben. Der Seitenname für Confluence wird aus den Metadaten entnommen, als erste Überschrift eingefügt und dann entfernt.

Bei der Nutzung von --check-reqs muss in Markdown-Kommentaren hinterlegt werden, welche Anforderungen durch die Richtlinie umgesetzt werden
Format der Kommentare: 
```
<!-- APP.2.1.1A3[: Umsetzungsstand] -->
<!-- APP.2.1.1A4: entbehrlich -->
<!-- APP.3.3.2A5: teilweise -->
<!-- APP.1.1.1A1 --> == <-- APP.1.1.1A1: erfüllt -->
<!-- APP.1.1.1A1, APP.1.1.1A2, APP.1.1.1A3  --> 
```