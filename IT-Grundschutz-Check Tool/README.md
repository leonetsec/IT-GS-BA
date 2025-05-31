# IT-Grundschutz-Check-Tool

## Einleitung
Dieses Tool vereinfacht den IT-Grundschutz-Check ([Version 2023](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium/checklisten_2023.html)) nach BSI Standard 200-2, indem es diverse Analysen und repetitive Aufgaben automatisiert durchführen kann.

## Installation
- Aktuelle IT-Grundschutz-Checklisten herunterladen
- Ggf. Kompendium im Docx-Format herunterladen
- Dateien des Tools herunterladen 
- Requirements installieren

## Nutzung
```python IT-Grundschutz-Check-Tool.py [--param] C://Path//To//FileOrDir```

Das Tool funktioniert mit den Checklisten im Format "Checkliste_XXX.X.X_xlsx", deren Blätter nach dem Kürzel des Bausteins benannt sind.

Übergibt man dem Tool nur einen Pfad ohne Parameter werden folgende Analysen durchgeführt:
- Einzelne Datei: Gesamtanzahl an Anforderungen, Umgesetzte Anforderungen, Teilweise umgesetzte Anforderungen, Entbehrliche Anforderungen, Nicht umgesetzte Anforderungen (aufgeschlüsselt nach Basis, Standard, erhöhter Schutzbedarf), Summierte Kostenschätzung, Verantwortliche.
- Alle Dateien eines Ordners: Zahl analysierter Tabellen, Gesamtanzahl an Anforderungen, Umgesetzte Anforderungen, Teilweise umgesetzte Anforderungen, Entbehrliche Anforderungen, Nicht umgesetzte Anforderungen (insgesamt aufgeschlüsselt nach Basis, Standard, erhöhter Schutzbedarf), Summierte Kostenschätzung.

Weitere Funktionen mittels Parameter, die sowohl auf einzelne Dateien als auch ganze Ordner anwendbar sind:
- ```--mapping```: Anzeige des vollständigen Bausteinnamen für die jeweilige Datei, z.B. Checkliste_APP.1.1.xlsx &#8594; Office Produkte
- ```--profil```: Auswahl eines von 23 [IT-Grundschutz-Profilen](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Profile/Profile/itgrundschutzProfile_Profile_node.html), nicht relevante Dateien werden in einen Ordner verschoben
- ```--prozent```: Prozentuale Anzeige der Umsetzung für eine Datei. Entfallene und entbehrliche Anforderungen werden ignoriert, teilweise umgesetzte Anforderungen zählen als nicht umgesetzt
- ```--ignore-standard```: Setzt alle leeren Standard-Anforderungen auf entbehrlich
- ```--ignore-hoch```: Setzt alle Anforderungen des erhöhten Schutzbedarfs auf entbehrlich
- ```--fully```: (Mit ```--ignore-X```) Setzt auch Anforderungen wo Umsetzung Ja/Nein/Teilweise ist auf entbehrlich
- ```--list```: Listet alle Dateien eines Ordners nach 15 verschiedenen Kriterien absteigend auf
- ```--wiba-transfer```: Setzt alle leeren WiBA-Anforderungen als umgesetzt
- ```--set-scale```: Modifiziert die Skala in der Umsetzungsspalte. Im Code können Default-Werte festgelegt werden.
- ```--export```: Exportiert beliebige Spalten der Datei(en) in verschiedene Formate
- ```--report```: Erstellt mehrseitigen PDF-Report, in dem diverse Auswertungen stattfinden, für einzelne oder alle Bausteine zusammen
- ```--merge```: Verbindet den Inhalt von zwei gleichartigen Tabellen inkl. Konfliktbehandlung
- ```--modify```: Modifiziert alle Bausteine eines Ordners im Docx Format, indem gewünschte Abschnitte oder Anforderungen entfernt werden
- ```--search```: Durchsucht alle Tabellen auf verschiedene Arten und speichert das Suchergebnis ab
- ```--risks```: Zeigt die abgedeckten elementaren Gefährdungen nach Kreuzreferenztabelle an, entweder für eine Datei oder einen ganzen Ordner

Hinweis: Aus Sicherheitsgründen können Basis-Anforderungen und als nicht entbehrlich markierte Anforderungen nicht automatisch als entbehrlich gesetzt werden.