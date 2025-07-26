# Readme Richtlinien Check Tool

Unterstützt bei der Arbeit mit Richtlinien, indem es automatisiert prüft, ob die in den Metadaten vorkommenden Bausteine (siehe Template) vollständig durch die Richtlinie abgedeckt werden.
Dafür muss in Markdown-Kommentaren die Umsetzung von Anforderungen hinterlegt werden (siehe unten).

## Installation
- Requirements installieren
- Optional: Richtlinien Template in ```template.py``` ändern
- ```IT-Grundschutz.json``` einfügen/anpassen. Dafür mit IT-Grundschutz-Check Tool exportieren (Entfallene Anforderungen entfernen, Bausteinnamen hinzufügen, zu einer Datei zusammenfassen)

## Nutzung

```python richtlinien_check.py [file, directory or string] --argument```

Befehle, die das Tool unterstützt:

- --check: Überprüft, ob die in den Metadaten vorkommenden Bausteine in der Richtlinie abgedeckt werden
- --typ (Mit --check): Definiert, ob für die Überprüfung der Schutzbedarfstyp Basis, Standard oder Hoch ausgewählt wird, Default: Standard
- --status (Mit --check): Zeigt in jeder Zeile den Umsetzungsstatus an 
- --details (Mit --check): Zeigt zusätzlich Baustein, Typ und Inhalt an
- --explain: Zeigt die Details zu einer gegebenen Anforderungs-ID an
- --new: Erstellt eine neue Richtlinie nach Template
- --fill-checklists: Füllt automatisch die passenden Checklisten anhand der Richtlinien aus
- --verbose: Zeigt Infos und Warnungen an, zum Beispiel zu ungültigen Referenzen und ignorierten Kommentaren

Format der Kommentare, um die Umsetzung zu markieren: 
```
<!-- BAU.N.N.AN[,BAU.N.N.AN[,...]][:{erfüllt|entbehrlich|teilweise}] -->
```

Beispiele:
```
<!-- APP.2.1.A3 -->
<!-- APP.2.1.A3: erfüllt -->
<!-- APP.2.1.A4: entbehrlich -->
<!-- APP.3.3.A5: teilweise -->
<!-- APP.1.1.A2 --> == <!-- APP.1.1.A2: erfüllt -->
<!-- APP.2.1.A4, APP.2.1.A5: entbehrlich --> == beide entbehrlich
<!-- APP.1.1.A2, APP.1.1.A3, APP.1.1.A4 --> 
```
