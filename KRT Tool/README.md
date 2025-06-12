# KRT-Tool

## Einleitung
Dieses Tool vereinfacht die Arbeit mit den [Kreuzreferenztabellen](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium/krt2023_Excel.html) des BSI IT-Grundschutzes, indem es sie durchsuchbarer, interaktiver und informativer macht. Die Tabellen ordnen den Anforderungen die abgedeckten [elementaren Gefährdungen](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/Elementare-Gefaehrdungen/elementare_gefaehrdungen.html) zu. 

## Installation
- Dateien des Tools herunterladen 
- ggf. ```mapping.py``` aktualisieren, wenn ein anderer Stand als 2023 benötigt wird

## Nutzung
```python KRT-Tool.py```

Das Tool funktioniert nur mit der Datei ```mapping.py``` im selben Ordner. Dort können auch weitere Gefährdungen manuell hinzugefügt und den Anforderungen zugeordnet werden.

Es können Anforderungen nach Gefährdungen, Bausteinen und Schutzzielen gefiltert werden sowie nach Strings durchsucht werden. Siehe IT-Grundschutz-Check-Tool für weitere Funktionen.

Mit ```--update``` können die Kreuzreferenztabellen in Zukunft aktualisiert werden, wenn sie ihr grundsätzliches Format beibehalten.