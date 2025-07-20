# Readme Richtlinien Check Tool

## Installation
- Requirements installieren
- Optional: Richtlinien Template in ```template.py``` ändern
- ```IT-Grundschutz.json``` einfügen/anpassen. Dafür mit IT-Grundschutz-Check Tool exportieren (Entfallene Anforderungen entfernen, Bausteinnamen hinzufügen, zu einer Datei zusammenfassen)

## Nutzung

```python richtlinien_check.py [file, directory or string] --argument```

Befehle, die das Tool unterstützt:

- --check: Überprüft, ob die in den Metadaten vorkommenden Bausteine in der Richtlinie abgedeckt werden
- --typ: (Mit --check-regs): Definiert, ob für die Überprüfung der Schutzbedarfstyp Basis, Standard oder Hoch ausgewählt wird, Default: Standard
- --new: Erstellt eine neue Richtlinie nach Template

Bei der Nutzung von --check muss in Markdown-Kommentaren hinterlegt werden, welche Anforderungen durch die Richtlinie umgesetzt werden

Format der Kommentare: 
```
<!-- BAU.N.N.AN[,BAU.N.N.AN[,...]][:{erfüllt|entbehrlich|teilweise}] -->
```

Beispiele:
```
<!-- APP.2.1.A3 -->
<!-- APP.2.1.A3: erfüllt -->
<!-- APP.2.1.A4: entbehrlich -->
<!-- APP.3.3.A5: teilweise -->
<!-- APP.1.1.A2 --> == <-- APP.1.1.A2: erfüllt -->
<!-- APP.2.1.A4, APP.2.1.A5: entbehrlich --> == beide entbehrlich
<!-- APP.1.1.A2, APP.1.1.A3, APP.1.1.A4 --> 
```
