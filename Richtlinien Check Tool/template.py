# Richtlinien Template (nicht vom BSI)
template = """---
title: Richtlinie Template
author: 
date: 2025-06-12
approver:
approved:
refs:
  - bsi:
    - orp-4-a16-2
---

# Richtlinie Template

Dies ist ein Template für Richtlinien. Es zeigt die allgemeine Struktur einer
Richtlinie.

Nicht Teil der Richtlinie ist/sind:
  - Gefährdungslage
Diese können in einem internen Dokument festgehalten werden.


# Einleitung

Die Einleitung beschreibt kurz den Kontext der Richtlinie.
Dies ist keine Zusammenfassung der Richtlinie, sondern eine kurze Einführung in die Thematik.


# Ziel

Das Ziel der Richtlinie wird hier beschrieben.

# Anwendungsbereich (Geltungsbereich)

Allgemein für alle Mitarbeitenden: "Die Richtlinie gilt für alle Mitarbeitenden."

Für spezifische Abteilung: "Die Richtlinie gilt für alle Mitarbeitenden der [Abteilungsname]."

Für Rollen oder Verantwortliche: "Die Richtlinie gilt für alle Mitarbeitenden in der Rolle [Rollenname], die für [Systeme/Prozesse] verantwortlich sind."

Für spezifische Systeme: "Die Richtlinie gilt für alle [Systemart]-Systeme."

Für Abteilungen und Systeme kombiniert: "Die Richtlinie gilt für alle Mitarbeitenden der Abteilung [Abteilungsname], die für die Verwaltung und den Betrieb von [Systemart]-Systemen zuständig sind."

Für Rollen und Systeme kombiniert: "Die Richtlinie gilt für alle Mitarbeitenden in der Rolle [Rollenname], die für die Verwaltung und den Betrieb von [Systemart]-Systemen verantwortlich sind."

Für spezifische Personen: "Die Richtlinie gilt für den/die [(Titel der) Person, z. B. Informationssicherheitsbeauftragte(n), Datenschutzbeauftragte(n)], der/die für [Aufgabe] verantwortlich ist."

# Verantwortlichkeiten

Hier wird beschrieben, wer für die Einhaltung der Richtlinie verantwortlich ist.
An dieser Stelle nur interne Stellen verwenden.

[Für die Richtline: Sicherheitsbeauftragter/Leitung]

Für die Umsetzung: Mitarbeiter:innen (für allgemeines wie Passwörter)
                   Administratoren der Dienste (für technische Umsetzung)

# Anforderungen

Hier werden die Regelungen der Richtlinie beschrieben.
Anforderungen so konkkret wie möglich formulieren.

<!-- APP.1.1.A2 --> um zu vermerken, dass eine Anforderung erfüllt ist

<!-- # Ausnahmen
In übergeordneter Leitlinie festlegen, dass Ausnahmen nur in begründeten Fällen und mit Zustimmung der Leitung möglich sind.
Und dokumentiert erfolgen.
-->

# Kontrolle

Hier wird beschrieben, wer die Einhaltung kontrolliert
und wie die Einhaltung der Richtlinie kontrolliert wird.
Muss durch eine unabhängige Stelle erfolgen.

"Die Einhaltung der Richtlinie wird _regelmäßig_ _stichprobenartig_ durch den Sicherheitsbeauftragten überprüft."
siehe: Richtlinie internes Audit

regelmäßig: mindestens einmal im Jahr
stichprobenartig: nicht immer die gleichen Systeme

# Referenzen

Hier werden Referenzen zu anderen Richtlinien oder Gesetzen angegeben.

## BSI-Grundschutz

Hier werden die Anforderungen aus den BSI IT-Grundschutzkatalogen aufgeführt, die
durch die Richtlinie abgedeckt werden.

## Sonstige Referenzen

Hier werden sonstige Referenzen aufgeführt. Beispielsweise Rundschreiben, Standards (ISO, DIN, etc.), Hilfestellungen in Confluence, etc.

# Anhang

Hier können Anhänge zur Richtlinie aufgeführt werden. Beispiele sind
Musterformulare, Checklisten, etc.
"""
