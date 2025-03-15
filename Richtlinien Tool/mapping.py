# Richtlinien Template (nicht vom BSI)
template = """---
title: Richtlinie Template
editor: 
date: 2023-05-15
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


## Einleitung

Die Einleitung beschreibt kurz den Kontext der Richtlinie.
Dies ist keine Zusammenfassung der Richtlinie, sondern eine kurze Einführung in die Thematik.


## Ziel

Das Ziel der Richtlinie wird hier beschrieben.
"Ziel der Richtlinie ist es, die Sicherheit zu erhöhen." ;-)

## Anwendungsbereich (Geltungsbereich)

Allgemein für alle Mitarbeitenden: "Die Richtlinie gilt für alle Mitarbeitenden."

Für spezifische Abteilung: "Die Richtlinie gilt für alle Mitarbeitenden der [Abteilungsname]."

Für Rollen oder Verantwortliche: "Die Richtlinie gilt für alle Mitarbeitenden in der Rolle [Rollenname], die für [Systeme/Prozesse] verantwortlich sind."

Für spezifische Systeme: "Die Richtlinie gilt für alle [Systemart]-Systeme."

Für Abteilungen und Systeme kombiniert: "Die Richtlinie gilt für alle Mitarbeitenden der Abteilung [Abteilungsname], die für die Verwaltung und den Betrieb von [Systemart]-Systemen zuständig sind."

Für Rollen und Systeme kombiniert: "Die Richtlinie gilt für alle Mitarbeitenden in der Rolle [Rollenname], die für die Verwaltung und den Betrieb von [Systemart]-Systemen verantwortlich sind."

Für spezifische Personen: "Die Richtlinie gilt für den/die [(Titel der) Person, z. B. Informationssicherheitsbeauftragte(n), Datenschutzbeauftragte(n)], der/die für [Aufgabe] verantwortlich ist."

## Verantwortlichkeiten

Hier wird beschrieben, wer für die Einhaltung der Richtlinie verantwortlich ist.
An dieser Stelle nur interne Stellen verwenden.

[Für die Richtline: Sicherheitsbeauftragter/Leitung]

Für die Umsetzung: Mitarbeiter:innen (für allgemeines wie Passwörter)
                   Administratoren der Dienste (für technische Umsetzung)

## Anforderungen

Hier werden die Regelungen der Richtlinie beschrieben.
Anforderungen so konkret wie möglich formulieren.

<!-- ## Ausnahmen
In übergeordneter Leitlinie festlegen, dass Ausnahmen nur in begründeten Fällen und mit Zustimmung der Leitung möglich sind.
Und dokumentiert erfolgen.
-->

## Kontrolle

Hier wird beschrieben, wer die Einhaltung kontrolliert
und wie die Einhaltung der Richtlinie kontrolliert wird.
Muss durch eine unabhängige Stelle erfolgen.

"Die Einhaltung der Richtlinie wird _regelmäßig_ _stichprobenartig_ durch den Sicherheitsbeauftragten überprüft."
siehe: Richtlinie internes Audit

regelmäßig: mindestens einmal im Jahr
stichprobenartig: nicht immer die gleichen Systeme

## Referenzen

Hier werden Referenzen zu anderen Richtlinien oder Gesetzen angegeben.

### BSI-Grundschutz

Hier werden die Anforderungen aus den BSI IT-Grundschutzkatalogen aufgeführt, die
durch die Richtlinie abgedeckt werden.

### Sonstige Referenzen

Hier werden sonstige Referenzen aufgeführt. Beispielsweise Rundschreiben, Standards (ISO, DIN, etc.), Hilfestellungen in Confluence, etc.

## Anhang

Hier können Anhänge zur Richtlinie aufgeführt werden. Beispiele sind
Musterformulare, Checklisten, etc.
"""


# Mapping auf Kategorie
bsi_ref_mapping = {
    'ISMS': '01_ISMS_Sicherheitsmanagement',
    'ORP': '02_ORP_Organisation_und_Personal',
    'CON': '03_CON_Konzepte_und_Vorgehensweisen',
    'OPS': '04_OPS_Betrieb',
    'DER': '05_DER_Detektion_und_Reaktion',
    'APP': '06_APP_Anwendungen',
    'SYS': '07_SYS_IT_Systeme',
    'IND': '08_IND_Industrielle_IT',
    'NET': '09_NET_Netze_und_Kommunikation',
    'INF': '10_INF_Infrastruktur'
}

# Mapping auf Titel des Bausteins
bsi_ref_titles = {
    'ISMS.1': 'ISMS_1_Sicherheitsmanagement',
    'ORP.1': 'ORP_1_Organisation',
    'ORP.2': 'ORP_2_Personal',
    'ORP.3': 'ORP_3_Sensibilisierung_und_Schulung_zur_Informationssicherheit',
    'ORP.4': 'ORP_4_Identitaets_und_Berechtigungsmanagement',
    'ORP.5': 'ORP_5_Compliance_Management',
    'CON.1': 'CON_1_Kryptokonzept',
    'CON.2': 'CON_2_Datenschutz',
    'CON.3': 'CON_3_Datensicherungskonzept',
    'CON.6': 'CON_6_Loeschen_und_Vernichten',
    'CON.7': 'CON_7_Informationssicherheit_auf_Auslandsreisen',
    'CON.8': 'CON_8_Software_Entwicklung',
    'CON.9': 'CON_9_Informationsaustausch',
    'CON.10': 'CON_10_Entwicklung_von_Webanwendungen',
    'CON.11.1': 'CON_11_1_Geheimschutz',
    'OPS.1.1.1': 'OPS_1_1_1_Allgemeiner_IT_Betrieb',
    'OPS.1.1.2': 'OPS_1_1_2_Ordnungsgemaesse_IT_Administration',
    'OPS.1.1.3': 'OPS_1_1_3_Patch_und_Aenderungsmanagement',
    'OPS.1.1.4': 'OPS_1_1_4_Schutz_vor_Schadprogrammen',
    'OPS.1.1.5': 'OPS_1_1_5_Protokollierung',
    'OPS.1.1.6': 'OPS_1_1_6_Software_Tests_und_Freigaben',
    'OPS.1.1.7': 'OPS_1_1_7_Systemmanagement',
    'OPS.1.2.2': 'OPS_1_2_2_Archivierung',
    'OPS.1.2.4': 'OPS_1_2_4_Telearbeit',
    'OPS.1.2.5': 'OPS_1_2_5_Fernwartung',
    'OPS.1.2.6': 'OPS_1_2_6_NTP_Zeitsynchronisation',
    'OPS.2.2': 'OPS_2_2_Cloud_Nutzung',
    'OPS.2.3': 'OPS_2_3_Nutzung_von_Outsourcing',
    'OPS.3.2': 'OPS_3_2_Anbieten_von_Outsourcing',
    'DER.1': 'DER_1_Detektion_von_sicherheitsrelevanten_Ereignissen',
    'DER.2.1': 'DER_2_1_Behandlung_von_Sicherheitsvorfaellen',
    'DER.2.2': 'DER_2_2_Vorsorge_fuer_die_IT_Forensik_2023',
    'DER.2.3': 'DER_2_3_Bereinigung_weitreichender_Sicherheitsvorfaelle',
    'DER.3.1': 'DER_3_1_Audits_und_Revisionen',
    'DER.3.2': 'DER_3_2_Revisionen_auf_Basis_des_Leitfadens_IS_Revisionen',
    'DER.4': 'DER_4_Notfallmanagement',
    'APP.1.1': 'APP_1_1_Office_Produkte',
    'APP.1.2': 'APP_1_2_Webbrowser',
    'APP.1.4': 'APP_1_4_Mobile_Anwendungen',
    'APP.2.1': 'APP_2_1_Allgemeiner_Verzeichnisdienst',
    'APP.2.2': 'APP_2_2_Active_Directory_Domain_Services',
    'APP.2.3': 'APP_2_3_OpenLDAP',
    'APP.3.1': 'APP_3_1_Webanwendungen_und_Webservices',
    'APP.3.2': 'APP_3_2_Webserver',
    'APP.3.3': 'APP_3_3_Fileserver',
    'APP.3.4': 'APP_3_4_Samba',
    'APP.3.6': 'APP_3_6_DNS_Server',
    'APP.4.2': 'APP_4_2_SAP_ERP_System',
    'APP.4.3': 'APP_4_3_Relationale_Datenbanksysteme',
    'APP.4.4': 'APP_4_4_Kubernetes',
    'APP.4.6': 'APP_4_6_SAP_ABAP_Programmierung',
    'APP.5.2': 'APP_5_2_Microsoft_Exchange_und_Outlook',
    'APP.5.3': 'APP_5_3_Allgemeiner_Email_Client_und_Server',
    'APP.5.4': 'APP_5_4_Unified_Communications_und_Collaboration',
    'APP.6': 'APP_6_Allgemeine_Software',
    'APP.7': 'APP_7_Entwicklung_von_Individualsoftware',
    'SYS.1.1': 'SYS_1_1_Allgemeiner_Server',
    'SYS.1.2.2': 'SYS_1_2_2_Windows_Server_2012',
    'SYS.1.2.3': 'SYS_1_2_3_Windows_Server',
    'SYS.1.3': 'SYS_1_3_Server_unter_Linux_und_Unix',
    'SYS.1.5': 'SYS_1_5_Virtualisierung',
    'SYS.1.6': 'SYS_1_6_Containerisierung',
    'SYS.1.7': 'SYS_1_7_IBM_Z',
    'SYS.1.8': 'SYS_1_8_Speicherloesungen',
    'SYS.1.9': 'SYS_1_9_Terminalserver',
    'SYS.2.1': 'SYS_2_1_Allgemeiner_Client',
    'SYS.2.2.3': 'SYS_2_2_3_Clients_unter_Windows',
    'SYS.2.3': 'SYS_2_3_Clients_unter_Linux_und_Unix',
    'SYS.2.4': 'SYS_2_4_Clients_unter_macOS',
    'SYS.2.5': 'SYS_2_5_Client_Virtualisierung',
    'SYS.2.6': 'SYS_2_6_Virtual_Desktop_Infrastructure',
    'SYS.3.1': 'SYS_3_1_Laptops',
    'SYS.3.2.1': 'SYS_3_2_1_Allgemeine_Smartphones_und_Tablets',
    'SYS.3.2.2': 'SYS_3_2_2_Mobile_Device_Management',
    'SYS.3.2.3': 'SYS_3_2_3_iOS_for_Enterprise_2023',
    'SYS.3.2.4': 'SYS_3_2_4_Android',
    'SYS.3.3': 'SYS_3_3_Mobiltelefon',
    'SYS.4.1': 'SYS_4_1_Drucker_Kopierer_und_Multifunktionsgeraete',
    'SYS.4.3': 'SYS_4_3_Eingebettete_Systeme',
    'SYS.4.4': 'SYS_4_4_Allgemeines_IoT_Geraet',
    'SYS.4.5': 'SYS_4_5_Wechseldatentraeger',
    'IND.1': 'IND_1_Prozessleit_und_Automatisierungstechnik',
    'IND.2.1': 'IND_2_1_Allgemeine_ICS_Komponente',
    'IND.2.2': 'IND_2_2_Speicherprogrammierbare_Steuerung',
    'IND.2.3': 'IND_2_3_Sensoren_und_Aktoren',
    'IND.2.4': 'IND_2_4_Maschine',
    'IND.2.7': 'IND_2_7_Safety_Instrumented_Systems',
    'IND.3.2': 'IND_3_2_Fernwartung_im_industriellen_Umfeld',
    'NET.1.1': 'NET_1_1_Netzarchitektur_und_design',
    'NET.1.2': 'NET_1_2_Netzmanagement',
    'NET.2.1': 'NET_2_1_WLAN_Betrieb',
    'NET.2.2': 'NET_2_2_WLAN_Nutzung',
    'NET.3.1': 'NET_3_1_Router_und_Switches',
    'NET.3.2': 'NET_3_2_Firewall',
    'NET.3.3': 'NET_3_3_VPN',
    'NET.3.4': 'NET_3_4_Network_Access_Control',
    'NET.4.1': 'NET_4_1_TK_Anlagen',
    'NET.4.2': 'NET_4_2_VoIP',
    'NET.4.3': 'NET_4_3_Faxgeraete_und_Faxserver',
    'INF.1': 'INF_1_Allgemeines_Gebaeude',
    'INF.2': 'INF_2_Rechenzentrum_und_Serverraum',
    'INF.5': 'INF_5_Raum_sowie_Schrank_fuer_technische_Infrastruktur',
    'INF.6': 'INF_6_Datentraegerarchiv',
    'INF.7': 'INF_7_Bueroarbeitsplatz',
    'INF.8': 'INF_8_Haeuslicher_Arbeitsplatz',
    'INF.9': 'INF_9_Mobiler_Arbeitsplatz',
    'INF.10': 'INF_10_Besprechungs_Veranstaltungs_und_Schulungsraeume',
    'INF.11': 'INF_11_Allgemeines_Fahrzeug',
    'INF.12': 'INF_12_Verkabelung',
    'INF.13': 'INF_13_Technisches_Gebaeudemanagement',
    'INF.14': 'INF_14_Gebaeudeautomation',
}