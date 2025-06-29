# KRT-Tool

## Einleitung
Dieses Tool vereinfacht die Arbeit mit den [Kreuzreferenztabellen](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium/krt2023_Excel.html) des BSI IT-Grundschutzes, indem es sie durchsuchbarer, interaktiver und informativer macht. Die Tabellen ordnen den Anforderungen die abgedeckten [elementaren Gefährdungen](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/Elementare-Gefaehrdungen/elementare_gefaehrdungen.html) zu. 

## Installation
- Dateien des Tools herunterladen 
- ggf. ```mapping.py``` mittels ```--update``` aktualisieren, wenn ein anderer Stand als 2023 benötigt wird und die KRT ihr Format beibehalten. Geänderte Bausteine und Gefahren müssen manuell ergänzt werden.
- ggf. ```profiles.py``` aktualisieren, wenn ein anderes Profil benötigt wird oder Profile verändert wurden (Manche Profile sind außerdem Platzhalter, da die Daten nicht öffentlich verfügbar sind)


## Nutzung
```python KRT-Tool.py```

Das Tool funktioniert nur mit der Datei ```mapping.py``` im selben Ordner. Dort können auch weitere Gefährdungen manuell hinzugefügt und den Anforderungen zugeordnet werden.

Es können Anforderungen nach Gefährdungen, Bausteinen, Schutzzielen, Profilen und Top-Anforderungen gefiltert werden sowie nach Strings durchsucht werden.
Siehe IT-Grundschutz-Check-Tool für weitere Funktionen, die die Informationen mit den Checklisten verknüpfen.