# Enthält alle Mappings für Bausteinnamen und die Kreuzreferenztabellen

# Mapping auf Titel des Bausteins
bsi_ref_titles = {
    'ISMS.1': 'Sicherheitsmanagement',
    'ORP.1': 'Organisation',
    'ORP.2': 'Personal',
    'ORP.3': 'Sensibilisierung und Schulung zur Informationssicherheit',
    'ORP.4': 'Identitäts- und Berechtigungsmanagement',
    'ORP.5': 'Compliance Management',
    'CON.1': 'Kryptokonzept',
    'CON.2': 'Datenschutz',
    'CON.3': 'Datensicherungskonzept',
    'CON.6': 'Löschen und Vernichten',
    'CON.7': 'Informationssicherheit auf Auslandsreisen',
    'CON.8': 'Software Entwicklung',
    'CON.9': 'Informationsaustausch',
    'CON.10': 'Entwicklung von Webanwendungen',
    'CON.11.1': 'Geheimschutz',
    'OPS.1.1.1': 'Allgemeiner IT Betrieb',
    'OPS.1.1.2': 'Ordnungsgemäße IT Administration',
    'OPS.1.1.3': 'Patch und Änderungsmanagement',
    'OPS.1.1.4': 'Schutz vor Schadprogrammen',
    'OPS.1.1.5': 'Protokollierung',
    'OPS.1.1.6': 'Software, Tests und Freigaben',
    'OPS.1.1.7': 'Systemmanagement',
    'OPS.1.2.2': 'Archivierung',
    'OPS.1.2.4': 'Telearbeit',
    'OPS.1.2.5': 'Fernwartung',
    'OPS.1.2.6': 'NTP Zeitsynchronisation',
    'OPS.2.2': 'Cloud Nutzung',
    'OPS.2.3': 'Nutzung von Outsourcing',
    'OPS.3.2': 'Anbieten von Outsourcing',
    'DER.1': 'Detektion von sicherheitsrelevanten Ereignissen',
    'DER.2.1': 'Behandlung von Sicherheitsvorfällen',
    'DER.2.2': 'Vorsorge für die IT-Forensik',
    'DER.2.3': 'Bereinigung weitreichender Sicherheitsvorfälle',
    'DER.3.1': 'Audits und Revisionen',
    'DER.3.2': 'Revisionen auf Basis des Leitfadens IS-Revisionen',
    'DER.4': 'Notfallmanagement',
    'APP.1.1': 'Office Produkte',
    'APP.1.2': 'Webbrowser',
    'APP.1.4': 'Mobile Anwendungen',
    'APP.2.1': 'Allgemeiner Verzeichnisdienst',
    'APP.2.2': 'Active Directory Domain Services',
    'APP.2.3': 'OpenLDAP',
    'APP.3.1': 'Webanwendungen und Webservices',
    'APP.3.2': 'Webserver',
    'APP.3.3': 'Fileserver',
    'APP.3.4': 'Samba',
    'APP.3.6': 'DNS Server',
    'APP.4.2': 'SAP ERP System',
    'APP.4.3': 'Relationale Datenbanksysteme',
    'APP.4.4': 'Kubernetes',
    'APP.4.6': 'SAP ABAP Programmierung',
    'APP.5.2': 'Microsoft Exchange und Outlook',
    'APP.5.3': 'Allgemeiner Email Client und Server',
    'APP.5.4': 'Unified Communications und Collaboration',
    'APP.6': 'Allgemeine Software',
    'APP.7': 'Entwicklung von Individualsoftware',
    'SYS.1.1': 'Allgemeiner Server',
    'SYS.1.2.2': 'Windows Server 2012',
    'SYS.1.2.3': 'Windows Server',
    'SYS.1.3': 'Server unter Linux und Unix',
    'SYS.1.5': 'Virtualisierung',
    'SYS.1.6': 'Containerisierung',
    'SYS.1.7': 'IBM Z',
    'SYS.1.8': 'Speicherlösungen',
    'SYS.1.9': 'Terminalserver',
    'SYS.2.1': 'Allgemeiner Client',
    'SYS.2.2.3': 'Clients unter Windows',
    'SYS.2.3': 'Clients unter Linux und Unix',
    'SYS.2.4': 'Clients unter macOS',
    'SYS.2.5': 'Client Virtualisierung',
    'SYS.2.6': 'Virtual Desktop Infrastructure',
    'SYS.3.1': 'Laptops',
    'SYS.3.2.1': 'Allgemeine Smartphones und Tablets',
    'SYS.3.2.2': 'Mobile Device Management',
    'SYS.3.2.3': 'iOS for Enterprise',
    'SYS.3.2.4': 'Android',
    'SYS.3.3': 'Mobiltelefon',
    'SYS.4.1': 'Drucker, Kopierer und Multifunktionsgeräte',
    'SYS.4.3': 'Eingebettete Systeme',
    'SYS.4.4': 'Allgemeines IoT-Gerät',
    'SYS.4.5': 'Wechseldatenträger',
    'IND.1': 'Prozessleit- und Automatisierungstechnik',
    'IND.2.1': 'Allgemeine ICS Komponente',
    'IND.2.2': 'Speicherprogrammierbare Steuerung',
    'IND.2.3': 'Sensoren und Aktoren',
    'IND.2.4': 'Maschine',
    'IND.2.7': 'Safety Instrumented Systems',
    'IND.3.2': 'Fernwartung im industriellen Umfeld',
    'NET.1.1': 'Netzarchitektur und -design',
    'NET.1.2': 'Netzmanagement',
    'NET.2.1': 'WLAN Betrieb',
    'NET.2.2': 'WLAN Nutzung',
    'NET.3.1': 'Router und Switches',
    'NET.3.2': 'Firewall',
    'NET.3.3': 'VPN',
    'NET.3.4': 'Network Access Control',
    'NET.4.1': 'TK-Anlagen',
    'NET.4.2': 'VoIP',
    'NET.4.3': 'Faxgeräte und Faxserver',
    'INF.1': 'Allgemeines Gebäude',
    'INF.2': 'Rechenzentrum und Serverraum',
    'INF.5': 'Raum sowie Schrank für technische Infrastruktur',
    'INF.6': 'Datenträgerarchiv',
    'INF.7': 'Büroarbeitsplatz',
    'INF.8': 'Häuslicher Arbeitsplatz',
    'INF.9': 'Mobiler Arbeitsplatz',
    'INF.10': 'Besprechungs-, Veranstaltungs- und Schulungsräume',
    'INF.11': 'Allgemeines Fahrzeug',
    'INF.12': 'Verkabelung',
    'INF.13': 'Technisches Gebäudemanagement',
    'INF.14': 'Gebäudeautomation'
}

cia = {
    "C": "Vertraulichkeit",
    "I": "Integrität",
    "A": "Verfügbarkeit"
}

gefahren = {
    "G 0.1": "Feuer",
    "G 0.2": "Ungünstige klimatische Bedingungen",
    "G 0.3": "Wasser",
    "G 0.4": "Verschmutzung, Staub, Korrosion",
    "G 0.5": "Naturkatastrophen",
    "G 0.6": "Katastrophen im Umfeld",
    "G 0.7": "Großereignisse im Umfeld",
    "G 0.8": "Ausfall oder Störung der Stromversorgung",
    "G 0.9": "Ausfall oder Störung von Kommunikationsnetzen",
    "G 0.10": "Ausfall oder Störung von Versorgungsnetzen",
    "G 0.11": "Ausfall oder Störung von Dienstleistern",
    "G 0.12": "Elektromagnetische Störstrahlung",
    "G 0.13": "Abfangen kompromittierender Strahlung",
    "G 0.14": "Ausspähen von Informationen (Spionage)",
    "G 0.15": "Abhören",
    "G 0.16": "Diebstahl von Geräten, Datenträgern oder Dokumenten",
    "G 0.17": "Verlust von Geräten, Datenträgern oder Dokumenten",
    "G 0.18": "Fehlplanung oder fehlende Anpassung",
    "G 0.19": "Offenlegung schützenswerter Informationen",
    "G 0.20": "Informationen oder Produkte aus unzuverlässiger Quelle",
    "G 0.21": "Manipulation von Hard- oder Software",
    "G 0.22": "Manipulation von Informationen",
    "G 0.23": "Unbefugtes Eindringen in IT-Systeme",
    "G 0.24": "Zerstörung von Geräten oder Datenträgern",
    "G 0.25": "Ausfall von Geräten oder Systemen",
    "G 0.26": "Fehlfunktion von Geräten oder Systemen",
    "G 0.27": "Ressourcenmangel",
    "G 0.28": "Software-Schwachstellen oder -Fehler",
    "G 0.29": "Verstoß gegen Gesetze oder Regelungen",
    "G 0.30": "Unberechtigte Nutzung oder Administration von Geräten und Systemen",
    "G 0.31": "Fehlerhafte Nutzung oder Administration von Geräten und Systemen",
    "G 0.32": "Missbrauch von Berechtigungen",
    "G 0.33": "Personalausfall",
    "G 0.34": "Anschlag",
    "G 0.35": "Nötigung, Erpressung oder Korruption",
    "G 0.36": "Identitätsdiebstahl",
    "G 0.37": "Abstreiten von Handlungen",
    "G 0.38": "Missbrauch personenbezogener Daten",
    "G 0.39": "Schadprogramme",
    "G 0.40": "Verhinderung von Diensten (Denial of Service)",
    "G 0.41": "Sabotage",
    "G 0.42": "Social Engineering",
    "G 0.43": "Einspielen von Nachrichten",
    "G 0.44": "Unbefugtes Eindringen in Räumlichkeiten",
    "G 0.45": "Datenverlust",
    "G 0.46": "Integritätsverlust schützenswerter Informationen",
    "G 0.47": "Schädliche Seiteneffekte IT-gestützter Angriffe"
}

krt = [
    {
        'id': 'APP.1.1.A2',
        'name': 'Einschränken von Aktiven Inhalten',
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.39']
    },
    {
        'id': 'APP.1.1.A3',
        'name': 'Sicheres Öffnen von Dokumenten aus externen Quellen',
        'cia': None,
        'gefahren': ['G 0.39']
    },
    {
        'id': 'APP.1.1.A6',
        'name': 'Testen neuer Versionen von Office-Produkten',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.46']
    },
    {
        'id': 'APP.1.1.A10',
        'name': 'Regelung der Software-Entwicklung durch Endbenutzende',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'APP.1.1.A11',
        'name': 'Geregelter Einsatz von Erweiterungen für Office-Produkte',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'APP.1.1.A12',
        'name': 'Verzicht auf Cloud-Speicherung',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'APP.1.1.A13',
        'name': 'Verwendung von Viewer-Funktionen',
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.39']
    },
    {
        'id': 'APP.1.1.A14',
        'name': 'Schutz gegen nachträgliche Veränderungen von Dokumenten',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.46']
    },
    {
        'id': 'APP.1.1.A15',
        'name': 'Einsatz von Verschlüsselung und Digitalen Signaturen',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22', 'G 0.46']
    },
    {
        'id': 'APP.1.1.A16',
        'name': 'Integritätsprüfung von Dokumenten',
        'cia': 'I',
        'gefahren': ['G 0.22', 'G 0.46']
    },
    {
        'id': 'APP.1.1.A17',
        'name': 'Sensibilisierung zu spezifischen Office-Eigenschaften',
        'cia': None,
        'gefahren': ['G 0.31']
    },
    {
        'id': 'APP.1.2.A1',
        'name': 'Verwendung von grundlegenden Sicherheitsmechanismen',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.28']
    },
    {
        'id': 'APP.1.2.A2',
        'name': 'Unterstützung sicherer Verschlüsselung der Kommunikation',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.22', 'G 0.46']
    },
    {
        'id': 'APP.1.2.A3',
        'name': 'Verwendung von vertrauenswürdigen Zertifikaten',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.30', 'G 0.46']
    },
    {
        'id': 'APP.1.2.A6',
        'name': 'Kennwortmanagement im Webbrowser',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'APP.1.2.A7',
        'name': 'Datensparsamkeit in Webbrowsern',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19']
    },
    {
        'id': 'APP.1.2.A9',
        'name': 'Einsatz einer isolierten Webbrowser-Umgebung',
        'cia': 'CI',
        'gefahren': ['G 0.23']
    },
    {
        'id': 'APP.1.2.A10',
        'name': 'Verwendung des privaten Modus',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.19']
    },
    {
        'id': 'APP.1.2.A11',
        'name': 'Überprüfung auf schädliche Inhalte',
        'cia': 'C',
        'gefahren': ['G 0.28', 'G 0.39']
    },
    {
        'id': 'APP.1.2.A12',
        'name': 'Zwei-Browser-Strategie',
        'cia': 'A',
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.1.2.A13',
        'name': 'Nutzung von DNS-over-HTTPS',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.19', 'G 0.22']
    },
    {
        'id': 'APP.1.4.A1',
        'name': 'Anforderungsanalyse für die Nutzung von Apps',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.14', 'G 0.15', 'G 0.16', 'G 0.17', 'G 0.18', 'G 0.19', 'G 0.25', 'G 0.26', 'G 0.38']
    },
    {
        'id': 'APP.1.4.A3',
        'name': 'Verteilung schutzbedürftiger Apps',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.20', 'G 0.21', 'G 0.23', 'G 0.32', 'G 0.39']
    },
    {
        'id': 'APP.1.4.A5',
        'name': 'Minimierung und Kontrolle von App-Berechtigungen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.21', 'G 0.32', 'G 0.38', 'G 0.39', 'G 0.42']
    },
    {
        'id': 'APP.1.4.A7',
        'name': 'Sichere Speicherung lokaler App-Daten',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.17', 'G 0.19']
    },
    {
        'id': 'APP.1.4.A8',
        'name': 'Verhinderung von Datenabfluss',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.38']
    },
    {
        'id': 'APP.1.4.A12',
        'name': 'Sichere Deinstallation von Apps',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.38']
    },
    {
        'id': 'APP.1.4.A14',
        'name': 'Unterstützung zusätzlicher Authentisierungsmerkmale bei Apps',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.17', 'G 0.18', 'G 0.19', 'G 0.23', 'G 0.32', 'G 0.36']
    },
    {
        'id': 'APP.1.4.A15',
        'name': 'Durchführung von Penetrationstests für Apps',
        'cia': 'CIA',
        'gefahren': ['G 0.21', 'G 0.23', 'G 0.25', 'G 0.26', 'G 0.28']
    },
    {
        'id': 'APP.1.4.A16',
        'name': 'Mobile Application Management',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'APP.2.1.A1',
        'name': 'Erstellung einer Sicherheitsrichtlinie für Verzeichnisdienste',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.2.1.A2',
        'name': 'Planung des Einsatzes von Verzeichnisdiensten',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'APP.2.1.A3',
        'name': 'Einrichtung von Zugriffsberechtigungen auf Verzeichnisdienste',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30']
    },
    {
        'id': 'APP.2.1.A5',
        'name': 'Sichere Konfiguration und Konfigurationsänderungen von Verzeichnisdiensten',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.45']
    },
    {
        'id': 'APP.2.1.A6',
        'name': 'Sicherer Betrieb von Verzeichnisdiensten',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30']
    },
    {
        'id': 'APP.2.1.A8',
        'name': 'Planung einer Partitionierung im Verzeichnisdienst',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.45']
    },
    {
        'id': 'APP.2.1.A9',
        'name': 'Geeignete Auswahl von Komponenten für Verzeichnisdienste',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.2.1.A11',
        'name': 'Einrichtung des Zugriffs auf Verzeichnisdienste',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'APP.2.1.A12',
        'name': 'Überwachung von Verzeichnisdiensten',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'APP.2.1.A13',
        'name': 'Absicherung der Kommunikation mit Verzeichnisdiensten',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'APP.2.1.A14',
        'name': 'Geregelte Außerbetriebnahme eines Verzeichnisdienstes',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.27', 'G 0.45']
    },
    {
        'id': 'APP.2.1.A15',
        'name': 'Migration von Verzeichnisdiensten',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30']
    },
    {
        'id': 'APP.2.1.A16',
        'name': 'Erstellung eines Notfallplans für den Ausfall eines Verzeichnisdienstes',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'APP.2.1.A17',
        'name': 'Absicherung von schutzbedürftigen Anmeldeinformationen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.45']
    },
    {
        'id': 'APP.2.1.A18',
        'name': 'Planung einer Replikation im Verzeichnisdienst',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'APP.2.1.A19',
        'name': 'Umgang mit anonymen Zugriffen auf Verzeichnisdienste',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.30']
    },
    {
        'id': 'APP.2.1.A20',
        'name': 'Absicherung der Replikation',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.23']
    },
    {
        'id': 'APP.2.1.A21',
        'name': 'Hochverfügbarkeit des Verzeichnisdienstes',
        'cia': 'A',
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.27', 'G 0.45']
    },
    {
        'id': 'APP.2.2.A1',
        'name': 'Planung von Active Directory Domain Services',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30']
    },
    {
        'id': 'APP.2.2.A3',
        'name': 'Planung der Gruppenrichtlinien unter Windows',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30']
    },
    {
        'id': 'APP.2.2.A5',
        'name': 'Absicherung des Domänencontrollers',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.45']
    },
    {
        'id': 'APP.2.2.A6',
        'name': 'Sichere Konfiguration von Vertrauensbeziehungen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.38', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.2.2.A7',
        'name': 'Umsetzung sicherer Verwaltungsmethoden für Active Directory',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.30', 'G 0.37']
    },
    {
        'id': 'APP.2.2.A8',
        'name': 'Absicherung des „Sicheren Kanals“',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.43']
    },
    {
        'id': 'APP.2.2.A9',
        'name': 'Schutz der Authentisierung beim Einsatz von AD DS',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.23', 'G 0.30', 'G 0.46']
    },
    {
        'id': 'APP.2.2.A12',
        'name': 'Datensicherung für Domänencontroller',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.28', 'G 0.30', 'G 0.45']
    },
    {
        'id': 'APP.2.2.A15',
        'name': 'Auslagerung der Administration in eine eigene Gesamtstruktur',
        'cia': 'CIA',
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'APP.2.2.A16',
        'name': 'Härtung der AD-DS-Konten',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.30', 'G 0.32', 'G 0.38', 'G 0.45']
    },
    {
        'id': 'APP.2.2.A17',
        'name': 'Anmelderestriktionen für hochprivilegierte Konten der Gesamtstruktur auf Clients und Servern',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'APP.2.2.A18',
        'name': 'Einschränken des Hinzufügens neuer Computer-Objekte zur Domäne',
        'cia': None,
        'gefahren': ['G 0.30', 'G 0.32']
    },
    {
        'id': 'APP.2.2.A19',
        'name': 'Betrieb von virtualisierten Domänencontrollern',
        'cia': 'A',
        'gefahren': ['G 0.18', 'G 0.23']
    },
    {
        'id': 'APP.2.2.A20',
        'name': 'Trennung von Organisationseinheiten',
        'cia': 'CI',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.2.2.A21',
        'name': 'Konfiguration eines Schichtenmodells',
        'cia': 'CI',
        'gefahren': ['G 0.19', 'G 0.32']
    },
    {
        'id': 'APP.2.2.A22',
        'name': 'Zeitlich befristete Berechtigungen für die Administration',
        'cia': 'CI',
        'gefahren': ['G 0.18', 'G 0.32']
    },
    {
        'id': 'APP.2.2.A23',
        'name': 'Regelmäßige Analyse von Berechtigungen und resultierenden Angriffspfaden',
        'cia': 'CI',
        'gefahren': ['G 0.18', 'G 0.32']
    },
    {
        'id': 'APP.2.3.A1',
        'name': 'Planung und Auswahl von Backends und Overlays für OpenLDAP',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.2.3.A3',
        'name': 'Sichere Konfiguration von OpenLDAP',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.30']
    },
    {
        'id': 'APP.2.3.A4',
        'name': 'Konfiguration der durch OpenLDAP verwendeten Datenbank',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18']
    },
    {
        'id': 'APP.2.3.A5',
        'name': 'Sichere Vergabe von Zugriffsrechten auf dem OpenLDAP',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30']
    },
    {
        'id': 'APP.2.3.A6',
        'name': 'Sichere Authentisierung gegenüber OpenLDAP',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.30']
    },
    {
        'id': 'APP.2.3.A8',
        'name': 'Einschränkungen von Attributen bei OpenLDAP',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.2.3.A9',
        'name': 'Partitionierung und Replikation bei OpenLDAP',
        'cia': None,
        'gefahren': ['G 0.27', 'G 0.45']
    },
    {
        'id': 'APP.2.3.A10',
        'name': 'Sichere Aktualisierung von OpenLDAP',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.45']
    },
    {
        'id': 'APP.2.3.A11',
        'name': 'Einschränkung der OpenLDAP-Laufzeitumgebung',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18']
    },
    {
        'id': 'APP.3.1.A1',
        'name': 'Authentisierung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'APP.3.1.A4',
        'name': 'Kontrolliertes Einbinden von Dateien und Inhalten',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.23', 'G 0.30', 'G 0.43']
    },
    {
        'id': 'APP.3.1.A7',
        'name': 'Schutz vor unerlaubter automatisierter Nutzung',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'APP.3.1.A8',
        'name': 'Systemarchitektur',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.3.1.A9',
        'name': 'Beschaffung von Webanwendungen und Webservices',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'APP.3.1.A11',
        'name': 'Sichere Anbindung von Hintergrundsystemen',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.23', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'APP.3.1.A12',
        'name': 'Sichere Konfiguration',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'APP.3.1.A14',
        'name': 'Schutz vertraulicher Daten',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'APP.3.1.A20',
        'name': 'Einsatz von Web Application Firewalls',
        'cia': 'CIA',
        'gefahren': ['G 0.23']
    },
    {
        'id': 'APP.3.1.A21',
        'name': 'Sichere HTTP-Konfiguration bei Webanwendungen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.23']
    },
    {
        'id': 'APP.3.1.A22',
        'name': 'Penetrationstest und Revision',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'APP.3.2.A1',
        'name': 'Sichere Konfiguration eines Webservers',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.46']
    },
    {
        'id': 'APP.3.2.A2',
        'name': 'Schutz der Webserver-Dateien',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.46']
    },
    {
        'id': 'APP.3.2.A3',
        'name': 'Absicherung von Datei-Uploads und -Downloads',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.39', 'G 0.40']
    },
    {
        'id': 'APP.3.2.A4',
        'name': 'Protokollierung von Ereignissen',
        'cia': None,
        'gefahren': ['G 0.26', 'G 0.30']
    },
    {
        'id': 'APP.3.2.A5',
        'name': 'Authentisierung',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.22', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'APP.3.2.A7',
        'name': 'Rechtliche Rahmenbedingungen für Webangebote',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'APP.3.2.A8',
        'name': 'Planung des Einsatzes eines Webservers',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.31']
    },
    {
        'id': 'APP.3.2.A9',
        'name': 'Festlegung einer Sicherheitsrichtlinie für den Webserver',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.31']
    },
    {
        'id': 'APP.3.2.A10',
        'name': 'Auswahl eines geeigneten Webhosters',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'APP.3.2.A11',
        'name': 'Verschlüsselung über TLS',
        'cia': None,
        'gefahren': ['G 0.15']
    },
    {
        'id': 'APP.3.2.A12',
        'name': 'Geeigneter Umgang mit Fehlern und Fehlermeldungen',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'APP.3.2.A13',
        'name': 'Zugriffskontrolle für Webcrawler',
        'cia': None,
        'gefahren': ['G 0.30']
    },
    {
        'id': 'APP.3.2.A14',
        'name': 'Integritätsprüfungen und Schutz vor Schadsoftware',
        'cia': None,
        'gefahren': ['G 0.39', 'G 0.46']
    },
    {
        'id': 'APP.3.2.A15',
        'name': 'Redundanz',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.39']
    },
    {
        'id': 'APP.3.2.A16',
        'name': 'Penetrationstest und Revision',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.23']
    },
    {
        'id': 'APP.3.2.A18',
        'name': 'Schutz vor Denial-of-Service-Angriffen',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.40']
    },
    {
        'id': 'APP.3.2.A20',
        'name': 'Benennung von Anzusprechenden',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.27']
    },
    {
        'id': 'APP.3.3.A2',
        'name': 'Einsatz von RAID-Systemen',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.46']
    },
    {
        'id': 'APP.3.3.A3',
        'name': 'Einsatz von Viren-Schutzprogrammen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.39']
    },
    {
        'id': 'APP.3.3.A6',
        'name': 'Beschaffung eines Fileservers und Auswahl eines Dienstes',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.27']
    },
    {
        'id': 'APP.3.3.A7',
        'name': 'Auswahl eines Dateisystems',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.27', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.3.3.A8',
        'name': 'Strukturierte Datenhaltung',
        'cia': None,
        'gefahren': ['G 0.45']
    },
    {
        'id': 'APP.3.3.A9',
        'name': 'Sicheres Speichermanagement',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.27', 'G 0.45']
    },
    {
        'id': 'APP.3.3.A11',
        'name': 'Einsatz von Speicherbeschränkungen',
        'cia': None,
        'gefahren': ['G 0.27']
    },
    {
        'id': 'APP.3.3.A12',
        'name': 'Verschlüsselung des Datenbestandes',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.39']
    },
    {
        'id': 'APP.3.3.A13',
        'name': 'Replikation zwischen Standorten',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.45']
    },
    {
        'id': 'APP.3.3.A14',
        'name': 'Einsatz von Error-Correction-Codes',
        'cia': None,
        'gefahren': ['G 0.26', 'G 0.46']
    },
    {
        'id': 'APP.3.3.A15',
        'name': 'Planung von Fileservern',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.27']
    },
    {
        'id': 'APP.3.4.A1',
        'name': 'Planung des Einsatzes eines Samba-Servers',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.3.4.A2',
        'name': 'Sichere Grundkonfiguration eines Samba-Servers',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.23', 'G 0.27', 'G 0.28', 'G 0.32']
    },
    {
        'id': 'APP.3.4.A3',
        'name': 'Sichere Konfiguration des Samba-Servers',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.27', 'G 0.30']
    },
    {
        'id': 'APP.3.4.A4',
        'name': 'Vermeidung der NTFS-Eigenschaften auf einem Samba-Server',
        'cia': None,
        'gefahren': ['G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.3.4.A5',
        'name': 'Sichere Konfiguration der Zugriffssteuerung bei einem Samba-Server',
        'cia': None,
        'gefahren': ['G 0.32', 'G 0.46']
    },
    {
        'id': 'APP.3.4.A6',
        'name': 'Sichere Konfiguration von Winbind unter Samba',
        'cia': None,
        'gefahren': ['G 0.32']
    },
    {
        'id': 'APP.3.4.A7',
        'name': 'Sichere Konfiguration von DNS unter Samba',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.3.4.A8',
        'name': 'Sichere Konfiguration von LDAP unter Samba',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.32']
    },
    {
        'id': 'APP.3.4.A9',
        'name': 'Sichere Konfiguration von Kerberos unter Samba',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'APP.3.4.A10',
        'name': 'Sicherer Einsatz externer Programme auf einem Samba-Server',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.20', 'G 0.28']
    },
    {
        'id': 'APP.3.4.A12',
        'name': 'Schulung der Administrierenden eines Samba-Servers',
        'cia': None,
        'gefahren': ['G 0.31']
    },
    {
        'id': 'APP.3.4.A13',
        'name': 'Regelmäßige Sicherung wichtiger Systemkomponenten eines Samba-Servers',
        'cia': None,
        'gefahren': ['G 0.45']
    },
    {
        'id': 'APP.3.4.A15',
        'name': 'Verschlüsselung der Datenpakete unter Samba',
        'cia': 'CI',
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.46']
    },
    {
        'id': 'APP.3.6.A1',
        'name': 'Planung des DNS-Einsatzes',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.3.6.A2',
        'name': 'Einsatz redundanter DNS-Server',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.40']
    },
    {
        'id': 'APP.3.6.A3',
        'name': 'Verwendung von separaten DNS-Servern für interne und externe Anfragen',
        'cia': None,
        'gefahren': ['G 0.22']
    },
    {
        'id': 'APP.3.6.A4',
        'name': 'Sichere Grundkonfiguration eines DNS-Servers',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30', 'G 0.31', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'APP.3.6.A6',
        'name': 'Absicherung von dynamischen DNS-Updates',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.30']
    },
    {
        'id': 'APP.3.6.A7',
        'name': 'Überwachung von DNS-Servern',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'APP.3.6.A8',
        'name': 'Verwaltung von Domainnamen',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'APP.3.6.A9',
        'name': 'Erstellen eines Notfallplans für DNS-Server',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.40', 'G 0.45']
    },
    {
        'id': 'APP.3.6.A10',
        'name': 'Auswahl eines geeigneten DNS-Server-Produktes',
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.29']
    },
    {
        'id': 'APP.3.6.A11',
        'name': 'Ausreichende Dimensionierung der DNS-Server',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.27', 'G 0.40']
    },
    {
        'id': 'APP.3.6.A13',
        'name': 'Einschränkung der Sichtbarkeit von Domain-Informationen',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'APP.3.6.A14',
        'name': 'Platzierung der Nameserver',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'APP.3.6.A15',
        'name': 'Auswertung der Logdaten',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.25', 'G 0.27', 'G 0.30']
    },
    {
        'id': 'APP.3.6.A16',
        'name': 'Integration eines DNS-Servers in eine "P-A-P"-Struktur',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30', 'G 0.43']
    },
    {
        'id': 'APP.3.6.A17',
        'name': 'Einsatz von DNSSEC',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.30', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'APP.3.6.A18',
        'name': 'Erweiterte Absicherung von Zonentransfers',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.30', 'G 0.46']
    },
    {
        'id': 'APP.3.6.A19',
        'name': 'Aussonderung von DNS-Servern',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'APP.3.6.A20',
        'name': 'Prüfung des Notfallplans auf Durchführbarkeit',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.27', 'G 0.40', 'G 0.45']
    },
    {
        'id': 'APP.3.6.A21',
        'name': 'Hidden-Master',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'APP.3.6.A22',
        'name': 'Anbindung der DNS-Server über unterschiedliche Provider',
        'cia': 'IA',
        'gefahren': ['G 0.9']
    },
    {
        'id': 'APP.4.2.A1',
        'name': 'Sichere Konfiguration des SAP-ABAP-Stacks',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.2.A2',
        'name': 'Sichere Konfiguration des SAP-JAVA-Stacks',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.2.A3',
        'name': 'Netzsicherheit',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.43']
    },
    {
        'id': 'APP.4.2.A4',
        'name': 'Absicherung der ausgelieferten SAP-Standard-Konten',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.2.A5',
        'name': 'Konfiguration und Absicherung der SAP-Konten-Verwaltung',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.2.A6',
        'name': 'Erstellung und Umsetzung eines Konten- und Berechtigungskonzeptes',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.2.A7',
        'name': 'Absicherung der SAP-Datenbanken',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.2.A8',
        'name': 'Absicherung der SAP-RFC-Schnittstelle',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.2.A9',
        'name': 'Absicherung und Überwachung des Message-Servers',
        'cia': None,
        'gefahren': ['G 0.25']
    },
    {
        'id': 'APP.4.2.A11',
        'name': 'Sichere Installation eines SAP-ERP-Systems',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.2.A12',
        'name': 'SAP-Berechtigungsentwicklung',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.22', 'G 0.32', 'G 0.46']
    },
    {
        'id': 'APP.4.2.A13',
        'name': 'SAP-Passwortsicherheit',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'APP.4.2.A14',
        'name': 'Identifizierung kritischer SAP-Berechtigungen',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'APP.4.2.A15',
        'name': 'Sichere Konfiguration des SAP-Routers',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'APP.4.2.A16',
        'name': 'Umsetzung von Sicherheitsanforderungen für das Betriebssystem Windows',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'APP.4.2.A17',
        'name': 'Umsetzung von Sicherheitsanforderungen für das Betriebssystem Unix',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'APP.4.2.A18',
        'name': 'Abschaltung von unsicherer Kommunikation',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.23']
    },
    {
        'id': 'APP.4.2.A19',
        'name': 'Definition der Sicherheitsrichtlinien für Konten',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'APP.4.2.A20',
        'name': 'Sichere SAP-GUI-Einstellungen',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'APP.4.2.A22',
        'name': 'Schutz des Spools im SAP-ERP-System',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.22', 'G 0.46']
    },
    {
        'id': 'APP.4.2.A23',
        'name': 'Schutz der SAP-Hintergrundverarbeitung',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.22', 'G 0.46']
    },
    {
        'id': 'APP.4.2.A24',
        'name': 'Aktivierung und Absicherung des Internet Communication Frameworks',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'APP.4.2.A25',
        'name': 'Sichere Konfiguration des SAP Web Dispatchers',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'APP.4.2.A26',
        'name': 'Schutz von selbstentwickeltem Code im SAP-ERP-System',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.30', 'G 0.39', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.2.A27',
        'name': 'Audit des SAP-ERP-Systems',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'APP.4.2.A28',
        'name': 'Erstellung eines Notfallkonzeptes',
        'cia': None,
        'gefahren': ['G 0.25']
    },
    {
        'id': 'APP.4.2.A29',
        'name': 'Einrichten von Notfall-Konten',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.2.A30',
        'name': 'Implementierung eines kontinuierlichen Monitorings der Sicherheitseinstellungen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.2.A31',
        'name': 'Konfiguration von SAP Single-Sign-On',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'APP.4.2.A32',
        'name': 'Echtzeiterfassung und Alarmierung von irregulären Vorgängen',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.3.A1',
        'name': 'Erstellung einer Sicherheitsrichtlinie für Datenbanksysteme',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'APP.4.3.A3',
        'name': 'Basishärtung des Datenbankmanagementsystems',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.22', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'APP.4.3.A4',
        'name': 'Geregeltes Anlegen neuer Datenbanken',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.4.3.A9',
        'name': 'Datensicherung eines Datenbanksystems',
        'cia': None,
        'gefahren': ['G 0.27', 'G 0.45']
    },
    {
        'id': 'APP.4.3.A11',
        'name': 'Ausreichende Dimensionierung der Hardware',
        'cia': None,
        'gefahren': ['G 0.27']
    },
    {
        'id': 'APP.4.3.A12',
        'name': 'Einheitlicher Konfigurationsstandard von Datenbankmanagementsystemen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'APP.4.3.A13',
        'name': 'Restriktive Handhabung von Datenbank-Links',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.22', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'APP.4.3.A16',
        'name': 'Verschlüsselung der Datenbankanbindung',
        'cia': None,
        'gefahren': ['G 0.15']
    },
    {
        'id': 'APP.4.3.A17',
        'name': 'Datenübernahme oder Migration',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.3.A18',
        'name': 'Überwachung des Datenbankmanagementsystems',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'APP.4.3.A19',
        'name': 'Schutz vor schädlichen Datenbank-Skripten',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.3.A20',
        'name': 'Regelmäßige Audits',
        'cia': None,
        'gefahren': ['G 0.28', 'G 0.31']
    },
    {
        'id': 'APP.4.3.A21',
        'name': 'Einsatz von Datenbank Security Tools',
        'cia': 'CI',
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'APP.4.3.A22',
        'name': 'Notfallvorsorge',
        'cia': 'CIA',
        'gefahren': ['G 0.27']
    },
    {
        'id': 'APP.4.3.A23',
        'name': 'Archivierung',
        'cia': 'IA',
        'gefahren': ['G 0.18', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.3.A24',
        'name': 'Datenverschlüsselung in der Datenbank',
        'cia': 'C',
        'gefahren': ['G 0.14', 'G 0.45']
    },
    {
        'id': 'APP.4.3.A25',
        'name': 'Sicherheitsprüfungen von Datenbanksystemen',
        'cia': 'CIA',
        'gefahren': ['G 0.23', 'G 0.31']
    },
    {
        'id': 'APP.4.4.A1',
        'name': 'Planung der Separierung der Anwendungen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.28', 'G 0.46']
    },
    {
        'id': 'APP.4.4.A2',
        'name': 'Planung der Automatisierung mit CI/CD',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.20', 'G 0.21', 'G 0.23', 'G 0.25', 'G 0.27', 'G 0.28', 'G 0.30', 'G 0.37', 'G 0.39', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.4.A3',
        'name': 'Identitäts- und Berechtigungsmanagement bei Kubernetes',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.30', 'G 0.37', 'G 0.46']
    },
    {
        'id': 'APP.4.4.A4',
        'name': 'Separierung von Pods',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.28', 'G 0.39', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.4.A5',
        'name': 'Datensicherung im Cluster',
        'cia': None,
        'gefahren': ['G 0.45']
    },
    {
        'id': 'APP.4.4.A6',
        'name': 'Initialisierung von Pods',
        'cia': None,
        'gefahren': ['G 0.25']
    },
    {
        'id': 'APP.4.4.A7',
        'name': 'Separierung der Netze bei Kubernetes',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.28', 'G 0.39', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.4.A8',
        'name': 'Absicherung von Konfigurationsdateien bei Kubernetes',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.28', 'G 0.39', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.4.A9',
        'name': 'Nutzung von Kubernetes Service-Accounts',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.21', 'G 0.30']
    },
    {
        'id': 'APP.4.4.A10',
        'name': 'Absicherung von Prozessen der Automatisierung',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.25', 'G 0.30']
    },
    {
        'id': 'APP.4.4.A11',
        'name': 'Überwachung der Container',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.27']
    },
    {
        'id': 'APP.4.4.A12',
        'name': 'Absicherung der Infrastruktur-Anwendungen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.28', 'G 0.39', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.4.A13',
        'name': 'Automatisierte Auditierung der Konfiguration',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.30', 'G 0.39', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.4.A14',
        'name': 'Verwendung dedizierter Nodes',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.28', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.4.A15',
        'name': 'Trennung von Anwendungen auf Node- und Cluster-Ebene',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.28', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.4.A16',
        'name': 'Verwendung von Operatoren',
        'cia': 'CIA',
        'gefahren': ['G 0.25']
    },
    {
        'id': 'APP.4.4.A17',
        'name': 'Attestierung von Nodes',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.28', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.4.A18',
        'name': 'Verwendung von Mikro-Segmentierung',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.28', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.4.A19',
        'name': 'Hochverfügbarkeit von Kubernetes',
        'cia': 'A',
        'gefahren': ['G 0.25']
    },
    {
        'id': 'APP.4.4.A20',
        'name': 'Verschlüsselte Datenhaltung bei Pods',
        'cia': 'C',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.28', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.4.A21',
        'name': 'Regelmäßiger Restart von Pods',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.28', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.6.A1',
        'name': 'Absicherung von Reports mit Berechtigungsprüfungen',
        'cia': None,
        'gefahren': ['G 0.30']
    },
    {
        'id': 'APP.4.6.A2',
        'name': 'Formal korrekte Auswertung von Berechtigungsprüfungen',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A3',
        'name': 'Berechtigungsprüfung vor dem Start einer Transaktion',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A4',
        'name': 'Verzicht auf proprietäre Berechtigungsprüfungen',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A5',
        'name': 'Erstellung einer Richtlinie für die ABAP-Entwicklung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'APP.4.6.A6',
        'name': 'Vollständige Ausführung von Berechtigungsprüfungen',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A7',
        'name': 'Berechtigungsprüfung während der Eingabeverarbeitung',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A8',
        'name': 'Schutz vor unberechtigten oder manipulierenden Zugriffen auf das Dateisystem',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A9',
        'name': 'Berechtigungsprüfung in remote-fähigen Funktionsbausteinen',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A10',
        'name': 'Verhinderung der Ausführung von Betriebssystemkommandos',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A11',
        'name': 'Vermeidung von eingeschleustem Schadcode',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A12',
        'name': 'Vermeidung von generischer Modulausführung',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A13',
        'name': 'Vermeidung von generischem Zugriff auf Tabelleninhalte',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A14',
        'name': 'Vermeidung von nativen SQL-Anweisungen',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A15',
        'name': 'Vermeidung von Datenlecks',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A16',
        'name': 'Verzicht auf systemabhängige Funktionsausführung',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A17',
        'name': 'Verzicht auf mandantenabhängige Funktionsausführung',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A18',
        'name': 'Vermeidung von Open-SQL-Injection-Schwachstellen',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A19',
        'name': 'Schutz vor Cross-Site-Scripting',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A20',
        'name': 'Keine Zugriffe auf Daten eines anderen Mandanten',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A21',
        'name': 'Verbot von verstecktem ABAP-Quelltext',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A22',
        'name': 'Einsatz von ABAP-Codeanalyse Werkzeugen',
        'cia': 'CIA',
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.5.2.A1',
        'name': 'Planung des Einsatzes von Exchange und Outlook',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.5.2.A2',
        'name': 'Auswahl einer geeigneten Exchange-Infrastruktur',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.5.2.A3',
        'name': 'Berechtigungsmanagement und Zugriffsrechte',
        'cia': None,
        'gefahren': ['G 0.30']
    },
    {
        'id': 'APP.5.2.A5',
        'name': 'Datensicherung von Exchange',
        'cia': None,
        'gefahren': ['G 0.45']
    },
    {
        'id': 'APP.5.2.A7',
        'name': 'Migration von Exchange-Systemen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'APP.5.2.A9',
        'name': 'Sichere Konfiguration von Exchange-Servern',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.25', 'G 0.27', 'G 0.46']
    },
    {
        'id': 'APP.5.2.A10',
        'name': 'Sichere Konfiguration von Outlook',
        'cia': None,
        'gefahren': ['G 0.30', 'G 0.31']
    },
    {
        'id': 'APP.5.2.A11',
        'name': 'Absicherung der Kommunikation zwischen Exchange-Systemen',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'APP.5.2.A12',
        'name': 'Einsatz von Outlook Anywhere, MAPI over HTTP und Outlook im Web',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.36']
    },
    {
        'id': 'APP.5.2.A17',
        'name': 'Verschlüsselung von Exchange-Datenbankdateien',
        'cia': 'C',
        'gefahren': ['G 0.19']
    },
    {
        'id': 'APP.5.3.A1',
        'name': 'Sichere Konfiguration der E-Mail-Clients',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.30', 'G 0.39']
    },
    {
        'id': 'APP.5.3.A2',
        'name': 'Sicherer Betrieb von E-Mail-Servern',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.40']
    },
    {
        'id': 'APP.5.3.A3',
        'name': 'Datensicherung und Archivierung von E-Mails',
        'cia': None,
        'gefahren': ['G 0.45']
    },
    {
        'id': 'APP.5.3.A4',
        'name': 'Spam- und Virenschutz auf dem E-Mail-Server',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.39']
    },
    {
        'id': 'APP.5.3.A5',
        'name': 'Festlegung von Vertretungsregelungen bei E-Mail-Nutzung',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.29', 'G 0.33']
    },
    {
        'id': 'APP.5.3.A6',
        'name': 'Festlegung einer Sicherheitsrichtlinie für E-Mail',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.5.3.A7',
        'name': 'Schulung zu Sicherheitsmechanismen von E-Mail-Clients für Benutzende',
        'cia': None,
        'gefahren': ['G 0.36', 'G 0.39', 'G 0.42']
    },
    {
        'id': 'APP.5.3.A8',
        'name': 'Umgang mit Spam durch Benutzende',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.39']
    },
    {
        'id': 'APP.5.3.A9',
        'name': 'Erweiterte Sicherheitsmaßnahmen auf dem E-Mail-Server',
        'cia': None,
        'gefahren': ['G 0.36', 'G 0.42']
    },
    {
        'id': 'APP.5.3.A10',
        'name': 'Ende-zu-Ende-Verschlüsselung',
        'cia': 'C',
        'gefahren': ['G 0.19']
    },
    {
        'id': 'APP.5.3.A11',
        'name': 'Einsatz redundanter E-Mail-Server',
        'cia': 'A',
        'gefahren': ['G 0.25']
    },
    {
        'id': 'APP.5.3.A12',
        'name': 'Überwachung öffentlicher Block-Listen',
        'cia': 'A',
        'gefahren': ['G 0.25']
    },
    {
        'id': 'APP.5.3.A13',
        'name': 'TLS-Reporting',
        'cia': 'CIA',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.5.4.A1',
        'name': 'Planung von UCC',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.5.4.A2',
        'name': 'Berücksichtigung von UCC in der Netzplanung',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.5.4.A3',
        'name': 'Initiales und regelmäßiges Testen der UCC-Dienste',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'APP.5.4.A4',
        'name': 'Deaktivierung nicht benötigter Funktionen und Dienste',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.23']
    },
    {
        'id': 'APP.5.4.A5',
        'name': 'Rollen- und Berechtigungskonzept für UCC',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'APP.5.4.A6',
        'name': 'Verschlüsselung von UCC-Daten',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.30']
    },
    {
        'id': 'APP.5.4.A7',
        'name': 'Regelungen für eine sichere Benutzung der UCC-Dienste',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'APP.5.4.A8',
        'name': 'Einsatz eines Session Border Controller am Provider-Übergang',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'APP.5.4.A9',
        'name': 'Sichere Konfiguration von UCC',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.18', 'G 0.19', 'G 0.30', 'G 0.39']
    },
    {
        'id': 'APP.5.4.A10',
        'name': 'Absicherung und Einschränkung von Auswertungen von Inhalten',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'APP.5.4.A11',
        'name': 'Sicherstellung der Verfügbarkeit von Kommunikationsdiensten',
        'cia': 'A',
        'gefahren': ['G 0.9', 'G 0.25', 'G 0.27']
    },
    {
        'id': 'APP.5.4.A12',
        'name': 'Einbindung von UCC in die Notfallplanung',
        'cia': 'A',
        'gefahren': ['G 0.18', 'G 0.25']
    },
    {
        'id': 'APP.5.4.A13',
        'name': 'Sichere Administration von SIP-Trunks',
        'cia': 'CIA',
        'gefahren': ['G 0.31', 'G 0.32']
    },
    {
        'id': 'APP.5.4.A14',
        'name': 'Ende-zu-Ende-Verschlüsselung',
        'cia': 'CI',
        'gefahren': ['G 0.15']
    },
    {
        'id': 'APP.5.4.A15',
        'name': 'Einschränkung von KI-Funktionen',
        'cia': 'C',
        'gefahren': ['G 0.19']
    },
    {
        'id': 'APP.5.4.A16',
        'name': 'Einsatz eines SBC an weiteren Netzübergängen',
        'cia': 'CIA',
        'gefahren': ['G 0.23']
    },
    {
        'id': 'APP.5.4.A17',
        'name': 'Einschränkung der Benutzung von UCC-Diensten',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'APP.5.4.A18',
        'name': 'Einbindung von UCC in ein Sicherheitsmonitoring',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.25']
    },
    {
        'id': 'APP.6.A1',
        'name': 'Planung des Software-Einsatzes',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.6.A2',
        'name': 'Erstellung eines Anforderungskatalogs für Software',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.29']
    },
    {
        'id': 'APP.6.A3',
        'name': 'Sichere Beschaffung von Software',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.20', 'G 0.28']
    },
    {
        'id': 'APP.6.A4',
        'name': 'Regelung für die Installation von Software',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.20', 'G 0.28', 'G 0.31']
    },
    {
        'id': 'APP.6.A5',
        'name': 'Sichere Installation von Software',
        'cia': None,
        'gefahren': ['G 0.31']
    },
    {
        'id': 'APP.6.A6',
        'name': 'Berücksichtigung empfohlener Sicherheitsanforderungen',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.6.A7',
        'name': 'Auswahl und Bewertung potentieller Software',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.6.A8',
        'name': 'Regelung zur Verfügbarkeit der Installationsdateien',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.45']
    },
    {
        'id': 'APP.6.A9',
        'name': 'Inventarisierung  von Software',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'APP.6.A10',
        'name': 'Erstellung einer Software-Richtlinie',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.6.A11',
        'name': 'Verwendung von Plug-ins und Erweiterungen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'APP.6.A12',
        'name': 'Geregelte Außerbetriebnahme von Software',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25']
    },
    {
        'id': 'APP.6.A13',
        'name': 'Deinstallation von Software',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.6.A14',
        'name': 'Nutzung zertifizierter Software',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'APP.7.A1',
        'name': 'Erweiterung der Planung des Software-Einsatzes um Aspekte von Individualsoftware',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'APP.7.A2',
        'name': 'Festlegung von Sicherheitsanforderungen an den Prozess der Software-Entwicklung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.22', 'G 0.29']
    },
    {
        'id': 'APP.7.A3',
        'name': 'Festlegung der Sicherheitsfunktionen zur Systemintegration',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'APP.7.A4',
        'name': 'Anforderungsgerechte Beauftragung',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.7.A5',
        'name': 'Geeignete Steuerung der Anwendungsentwicklung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'APP.7.A6',
        'name': 'Dokumentation der Anforderungen an die Individualsoftware',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.7.A7',
        'name': 'Sichere Beschaffung von Individualsoftware',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.27']
    },
    {
        'id': 'APP.7.A8',
        'name': 'Frühzeitige Beteiligung der Fachverantwortlichen bei entwicklungsbegleitenden  Software-Tests',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'APP.7.A9',
        'name': 'Treuhänderische Hinterlegung',
        'cia': 'A',
        'gefahren': ['G 0.45']
    },
    {
        'id': 'APP.7.A10',
        'name': 'Beauftragung zertifizierter Software-Entwicklungsunternehmen',
        'cia': 'CIA',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'CON.1.A1',
        'name': 'Auswahl geeigneter kryptografischer Verfahren',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'CON.1.A2',
        'name': 'Datensicherung beim Einsatz kryptografischer Verfahren',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'CON.1.A4',
        'name': 'Geeignetes Schlüsselmanagement',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.20', 'G 0.45']
    },
    {
        'id': 'CON.1.A5',
        'name': 'Sicheres Löschen und Vernichten von kryptografischen Schlüsseln',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'CON.1.A9',
        'name': 'Festlegung von Kriterien für die Auswahl von Hard- oder Software mit kryptographischen Funktionen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.20', 'G 0.26', 'G 0.28', 'G 0.29', 'G 0.31']
    },
    {
        'id': 'CON.1.A10',
        'name': 'Erstellung eines Kryptokonzepts',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'CON.1.A11',
        'name': 'Test von Hardware mit kryptografischen Funktionen',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.20', 'G 0.31']
    },
    {
        'id': 'CON.1.A15',
        'name': 'Reaktion auf praktische Schwächung eines Kryptoverfahrens',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'CON.1.A16',
        'name': 'Physische Absicherung von Hardware mit kryptografischen Funktionen',
        'cia': 'CIA',
        'gefahren': ['G 0.21', 'G 0.22']
    },
    {
        'id': 'CON.1.A17',
        'name': 'Abstrahlsicherheit',
        'cia': 'C',
        'gefahren': ['G 0.13']
    },
    {
        'id': 'CON.1.A18',
        'name': 'Kryptografische Ersatzhardware',
        'cia': 'A',
        'gefahren': ['G 0.19', 'G 0.25', 'G 0.27']
    },
    {
        'id': 'CON.1.A19',
        'name': 'Erstellung eines Krypto-Katasters',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'CON.1.A20',
        'name': 'Manipulationserkennung für Hard- oder Software mit kryptografischen Funktionen',
        'cia': 'CIA',
        'gefahren': ['G 0.21']
    },
    {
        'id': 'CON.10.A1',
        'name': 'Authentisierung bei Webanwendungen',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A2',
        'name': 'Zugriffskontrolle bei Webanwendungen',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A3',
        'name': 'Sicheres Session-Management',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A4',
        'name': 'Kontrolliertes Einbinden von Inhalten bei Webanwendungen',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A5',
        'name': 'Upload-Funktionen',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A6',
        'name': 'Schutz vor unerlaubter automatisierter Nutzung von Webanwendungen',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A7',
        'name': 'Schutz vertraulicher Daten',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A8',
        'name': 'Umfassende Eingabevalidierung und Ausgabekodierung',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A9',
        'name': 'Schutz vor SQL-Injection',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A10',
        'name': 'Restriktive Herausgabe sicherheitsrelevanter Informationen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'CON.10.A11',
        'name': 'Softwarearchitektur einer Webanwendung',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A12',
        'name': 'Verifikation essenzieller Änderungen',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A13',
        'name': 'Fehlerbehandlung',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A14',
        'name': 'Sichere HTTP-Konfiguration bei Webanwendungen',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A15',
        'name': 'Verhinderung von Cross-Site-Request-Forgery',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A16',
        'name': 'Mehr-Faktor-Authentisierung',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A17',
        'name': 'Verhinderung der Blockade von Ressourcen',
        'cia': 'CIA',
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A18',
        'name': 'Kryptografische Absicherung vertraulicher Daten',
        'cia': 'CIA',
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.11.1.A1',
        'name': 'Einhaltung der Grundsätze zur VS-Verarbeitung mit IT nach § 3, 4 und 6 und Nr. 1 Anlage V zur VSA',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A2',
        'name': 'Erstellung und Fortschreibung der VS-IT-Dokumentation nach § 12 und Nr. 2.2 Anlage II zur VSA',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A3',
        'name': 'Einsatz von IT-Sicherheitsprodukten nach §§ 51, 52 VSA',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A4',
        'name': 'Beschaffung von VS-IT nach § 49 VSA',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A5',
        'name': 'Verpflichtung bei Zugang zu VS nach § 4 und Anlage V zur VSA',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A6',
        'name': 'Beaufsichtigung und Begleitung von Fremdpersonal für VS-IT nach §§ 3, 4 VSA',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.24', 'G 0.29', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'CON.11.1.A7',
        'name': 'Kennzeichnung von elektronischen VS und Datenträgern nach §§ 20, 54 und Anlage III, V und VIII zur VSA',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A8',
        'name': 'Verwaltung und Nachweis von elektronischen VS nach § 21 VSA',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A9',
        'name': 'Speicherung elektronischer VS nach § 23 und Nr. 5 Anlage V zur VSA',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A10',
        'name': 'Elektronische Übertragung von VS nach §§ 24, 53, 55 und Nr. 6.2 Anlage V zur VSA',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.22', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A11',
        'name': 'Mitnahme elektronischer VS nach § 28 VSA und Nr. 7 Anlage V zur VSA',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A12',
        'name': 'Archivierung elektronischer VS nach §§ 30, 31 VSA',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A13',
        'name': 'Löschung elektronischer VS, Vernichtung von Datenträgern und IT-Produkten nach §§ 32, 56 und Nr. 8 Anlage V zur VSA',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A14',
        'name': 'Zugangs- und Zugriffsschutz nach § 3 VSA (B)',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.19', 'G 0.21', 'G 0.24', 'G 0.29', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.41', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'CON.11.1.A15',
        'name': 'Handhabung von Datenträgern und IT-Produkten nach § 54 und Anlage V zur VSA',
        'cia': None,
        'gefahren': ['G 0.16', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A16',
        'name': 'Zusammenschaltung von VS-IT nach § 58 VSA',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.23', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A17',
        'name': 'Wartungs- und Instandsetzungsarbeiten von VS-IT nach § 3 Abs. 3 VSA',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.19', 'G 0.23', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A18',
        'name': 'Fernwartung von VS-IT nach § 3 Abs. 3 VSA',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.21', 'G 0.23', 'G 0.29']
    },
    {
        'id': 'CON.2.A1',
        'name': 'Umsetzung Standard-Datenschutzmodell',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'CON.3.A1',
        'name': 'Erhebung der Einflussfaktoren für Datensicherungen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'CON.3.A2',
        'name': 'Festlegung der Verfahrensweisen für die Datensicherung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.39']
    },
    {
        'id': 'CON.3.A4',
        'name': 'Erstellung von Datensicherungsplänen',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'CON.3.A5',
        'name': 'Regelmäßige Datensicherung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.45']
    },
    {
        'id': 'CON.3.A6',
        'name': 'Entwicklung eines Datensicherungskonzepts',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'CON.3.A7',
        'name': 'Beschaffung eines geeigneten Datensicherungssystems',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'CON.3.A9',
        'name': 'Voraussetzungen für die Online- Datensicherung',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'CON.3.A12',
        'name': 'Sichere Aufbewahrung der Speichermedien für die Datensicherungen',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.2', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'CON.3.A13',
        'name': 'Einsatz kryptografischer Verfahren bei der Datensicherung',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.22', 'G 0.46']
    },
    {
        'id': 'CON.3.A14',
        'name': 'Schutz von Datensicherungen',
        'cia': None,
        'gefahren': ['G 0.16', 'G 0.19', 'G 0.22', 'G 0.45']
    },
    {
        'id': 'CON.3.A15',
        'name': 'Regelmäßiges Testen der Datensicherungen',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'CON.6.A1',
        'name': 'Regelung der Vorgehensweise für die Löschung und Vernichtung von Informationen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.2']
    },
    {
        'id': 'CON.6.A2',
        'name': 'Ordnungsgemäße Entsorgung von schützenswerten Betriebsmitteln und Informationen',
        'cia': None,
        'gefahren': ['G 0.16', 'G 0.18', 'G 0.19']
    },
    {
        'id': 'CON.6.A4',
        'name': 'Auswahl geeigneter Verfahren zur Löschung oder Vernichtung von Datenträgern',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'CON.6.A8',
        'name': 'Erstellung einer Richtlinie für die Löschung und Vernichtung von Informationen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'CON.6.A11',
        'name': 'Vernichtung von Datenträgern durch externe Dienstleistende',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'CON.6.A12',
        'name': 'Mindestanforderungen an die Verfahrensweise zur Löschung und Vernichtung',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'CON.6.A13',
        'name': 'Vernichtung digitaler Datenträger bei fehlender Möglichkeit zur sicheren Löschung',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'CON.6.A14',
        'name': 'Vernichten von Datenträgern auf erhöhter Sicherheitsstufe',
        'cia': 'C',
        'gefahren': ['G 0.19']
    },
    {
        'id': 'CON.7.A1',
        'name': 'Sicherheitsrichtlinie zur Informationssicherheit auf Auslandsreisen',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'CON.7.A2',
        'name': 'Sensibilisierung der Mitarbeitenden zur Informationssicherheit auf Auslandsreisen',
        'cia': None,
        'gefahren': ['G 0.17', 'G 0.18', 'G 0.29', 'G 0.31']
    },
    {
        'id': 'CON.7.A3',
        'name': 'Identifikation länderspezifischer Regelungen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'CON.7.A4',
        'name': 'Verwendung von Sichtschutz-Folien',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19']
    },
    {
        'id': 'CON.7.A5',
        'name': 'Verwendung der Bildschirm-/Code-Sperre',
        'cia': None,
        'gefahren': ['G 0.30']
    },
    {
        'id': 'CON.7.A6',
        'name': 'Zeitnahe Verlustmeldung',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.30']
    },
    {
        'id': 'CON.7.A7',
        'name': 'Sicherer Remote-Zugriff auf das Netz der Institution',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'CON.7.A8',
        'name': 'Sichere Nutzung von öffentlichen WLANs',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.23']
    },
    {
        'id': 'CON.7.A9',
        'name': 'Sicherer Umgang mit mobilen Datenträgern',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.39']
    },
    {
        'id': 'CON.7.A10',
        'name': 'Verschlüsselung tragbarer IT-Systeme und Datenträger',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.29']
    },
    {
        'id': 'CON.7.A11',
        'name': 'Einsatz von Diebstahl-Sicherungen',
        'cia': None,
        'gefahren': ['G 0.16']
    },
    {
        'id': 'CON.7.A12',
        'name': 'Sicheres Vernichten von schutzbedürftigen Materialien und Dokumenten',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.29', 'G 0.31']
    },
    {
        'id': 'CON.7.A13',
        'name': 'Mitnahme notwendiger Daten und Datenträger',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'CON.7.A14',
        'name': 'Kryptografisch abgesicherte E-Mail-Kommunikation',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.46']
    },
    {
        'id': 'CON.7.A15',
        'name': 'Abstrahlsicherheit tragbarer IT-Systeme',
        'cia': 'C',
        'gefahren': ['G 0.13']
    },
    {
        'id': 'CON.7.A16',
        'name': 'Integritätsschutz durch Check-Summen oder digitale Signaturen',
        'cia': 'I',
        'gefahren': ['G 0.45', 'G 0.46']
    },
    {
        'id': 'CON.7.A17',
        'name': 'Verwendung vorkonfigurierter Reise-Hardware',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'CON.7.A18',
        'name': 'Eingeschränkte Berechtigungen auf Auslandsreisen',
        'cia': 'CI',
        'gefahren': ['G 0.30']
    },
    {
        'id': 'CON.8.A1',
        'name': 'Definition von Rollen und Zuständigkeiten',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'CON.8.A2',
        'name': 'Auswahl eines Vorgehensmodells',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'CON.8.A3',
        'name': 'Auswahl einer Entwicklungsumgebung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.20']
    },
    {
        'id': 'CON.8.A5',
        'name': 'Sicheres Systemdesign',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'CON.8.A6',
        'name': 'Verwendung von externen Bibliotheken aus vertrauenswürdigen Quellen',
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.46']
    },
    {
        'id': 'CON.8.A7',
        'name': 'Durchführung von entwicklungsbegleitenden Software-Tests',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.8.A8',
        'name': 'Bereitstellung von Patches',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.28', 'G 0.29']
    },
    {
        'id': 'CON.8.A10',
        'name': 'Versionsverwaltung des Quellcodes',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'CON.8.A11',
        'name': 'Erstellung einer Richtlinie für die Software-Entwicklung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.31']
    },
    {
        'id': 'CON.8.A12',
        'name': 'Ausführliche Dokumentation',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.45']
    },
    {
        'id': 'CON.8.A14',
        'name': 'Schulung des Projektteams zur Informationssicherheit',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.8.A16',
        'name': 'Geeignete Steuerung der Software-Entwicklung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'CON.8.A17',
        'name': 'Auswahl vertrauenswürdiger Entwicklungswerkzeuge',
        'cia': 'CI',
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.8.A18',
        'name': 'Regelmäßige Sicherheitsaudits für die Entwicklungsumgebung',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'CON.8.A19',
        'name': 'Regelmäßige Integritätsprüfung der Entwicklungsumgebung',
        'cia': 'I',
        'gefahren': ['G 0.22', 'G 0.31', 'G 0.46']
    },
    {
        'id': 'CON.8.A20',
        'name': 'Überprüfung von externen Komponenten',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.28']
    },
    {
        'id': 'CON.8.A21',
        'name': 'Bedrohungsmodellierung',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'CON.8.A22',
        'name': 'Sicherer Software-Entwurf',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'CON.9.A1',
        'name': 'Festlegung zulässiger Empfangender',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.29']
    },
    {
        'id': 'CON.9.A2',
        'name': 'Regelung des Informationsaustausches',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'CON.9.A3',
        'name': 'Unterweisung des Personals zum Informationsaustausch',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.29']
    },
    {
        'id': 'CON.9.A4',
        'name': 'Vereinbarungen zum Informationsaustausch mit Externen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'CON.9.A5',
        'name': 'Beseitigung von Restinformationen vor Weitergabe',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'CON.9.A6',
        'name': 'Kompatibilitätsprüfung des Sende- und Empfangssystems',
        'cia': None,
        'gefahren': ['G 0.25']
    },
    {
        'id': 'CON.9.A7',
        'name': 'Sicherungskopie der übermittelten Daten',
        'cia': None,
        'gefahren': ['G 0.45']
    },
    {
        'id': 'CON.9.A8',
        'name': 'Verschlüsselung und Signatur',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.22']
    },
    {
        'id': 'CON.9.A9',
        'name': 'Vertraulichkeitsvereinbarungen',
        'cia': 'C',
        'gefahren': ['G 0.19']
    },
    {
        'id': 'DER.1.A1',
        'name': 'Erstellung einer Sicherheitsrichtlinie für die Detektion von sicherheitsrelevanten Ereignissen',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'DER.1.A2',
        'name': 'Einhaltung rechtlicher Bedingungen bei der Auswertung von Protokollierungsdaten',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.38']
    },
    {
        'id': 'DER.1.A3',
        'name': 'Festlegung von Meldewegen für sicherheitsrelevante Ereignisse',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.33']
    },
    {
        'id': 'DER.1.A4',
        'name': 'Sensibilisierung der Mitarbeitenden',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.31']
    },
    {
        'id': 'DER.1.A5',
        'name': 'Einsatz von mitgelieferten Systemfunktionen zur Detektion',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.39']
    },
    {
        'id': 'DER.1.A6',
        'name': 'Kontinuierliche Überwachung und Auswertung von Protokollierungsdaten',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.22', 'G 0.25', 'G 0.26', 'G 0.27', 'G 0.29']
    },
    {
        'id': 'DER.1.A7',
        'name': 'Schulung von Zuständigen',
        'cia': None,
        'gefahren': ['G 0.27', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'DER.1.A9',
        'name': 'Einsatz zusätzlicher Detektionssysteme',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.39']
    },
    {
        'id': 'DER.1.A10',
        'name': 'Einsatz von TLS-/SSL-Proxies',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.29', 'G 0.30', 'G 0.39']
    },
    {
        'id': 'DER.1.A11',
        'name': 'Nutzung einer zentralen Protokollierungsinfrastruktur für die Auswertung sicherheitsrelevanter Ereignisse',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.39']
    },
    {
        'id': 'DER.1.A12',
        'name': 'Auswertung von Informationen aus externen Quellen',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'DER.1.A13',
        'name': 'Regelmäßige Audits der Detektionssysteme',
        'cia': None,
        'gefahren': ['G 0.27', 'G 0.29', 'G 0.39']
    },
    {
        'id': 'DER.1.A14',
        'name': 'Auswertung der Protokollierungsdaten durch spezialisiertes Personal',
        'cia': 'CI',
        'gefahren': ['G 0.27', 'G 0.31', 'G 0.33']
    },
    {
        'id': 'DER.1.A15',
        'name': 'Zentrale Detektion und Echtzeitüberprüfung von Ereignismeldungen',
        'cia': 'CIA',
        'gefahren': ['G 0.29', 'G 0.37', 'G 0.39', 'G 0.46']
    },
    {
        'id': 'DER.1.A16',
        'name': 'Einsatz von Detektionssystemen nach Schutzbedarfsanforderungen',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.21', 'G 0.23', 'G 0.29', 'G 0.40', 'G 0.46']
    },
    {
        'id': 'DER.1.A17',
        'name': 'Automatische Reaktion auf sicherheitsrelevante Ereignisse',
        'cia': 'CI',
        'gefahren': ['G 0.29']
    },
    {
        'id': 'DER.1.A18',
        'name': 'Durchführung regelmäßiger Integritätskontrollen',
        'cia': 'CI',
        'gefahren': ['G 0.29', 'G 0.32', 'G 0.46']
    },
    {
        'id': 'DER.2.1.A1',
        'name': 'Definition eines Sicherheitsvorfalls',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.20', 'G 0.29']
    },
    {
        'id': 'DER.2.1.A2',
        'name': 'Erstellung einer Richtlinie zur Behandlung von Sicherheitsvorfällen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.29']
    },
    {
        'id': 'DER.2.1.A3',
        'name': 'Festlegung von Verantwortlichkeiten und Ansprechpersonen bei Sicherheitsvorfällen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.29', 'G 0.33']
    },
    {
        'id': 'DER.2.1.A4',
        'name': 'Benachrichtigung betroffener Stellen bei Sicherheitsvorfällen',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.20', 'G 0.29']
    },
    {
        'id': 'DER.2.1.A5',
        'name': 'Behebung von Sicherheitsvorfällen',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.19', 'G 0.25', 'G 0.27', 'G 0.29']
    },
    {
        'id': 'DER.2.1.A6',
        'name': 'Wiederherstellung der Betriebsumgebung nach Sicherheitsvorfällen',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.19', 'G 0.25', 'G 0.29', 'G 0.30', 'G 0.32', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.1.A7',
        'name': 'Etablierung einer Vorgehensweise zur Behandlung von Sicherheitsvorfällen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.29']
    },
    {
        'id': 'DER.2.1.A8',
        'name': 'Aufbau von Organisationsstrukturen zur Behandlung von Sicherheitsvorfällen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.29', 'G 0.33']
    },
    {
        'id': 'DER.2.1.A9',
        'name': 'Festlegung von Meldewegen für Sicherheitsvorfälle',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.20', 'G 0.22', 'G 0.27', 'G 0.29', 'G 0.33']
    },
    {
        'id': 'DER.2.1.A10',
        'name': 'Eindämmen der Auswirkung von Sicherheitsvorfällen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.29', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.1.A11',
        'name': 'Einstufung von Sicherheitsvorfällen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.29']
    },
    {
        'id': 'DER.2.1.A12',
        'name': 'Festlegung der Schnittstellen der Sicherheitsvorfallbehandlung zur Störungs- und Fehlerbehebung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.27', 'G 0.46']
    },
    {
        'id': 'DER.2.1.A13',
        'name': 'Einbindung in das Sicherheits- und Notfallmanagement',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.46']
    },
    {
        'id': 'DER.2.1.A14',
        'name': 'Eskalationsstrategie für Sicherheitsvorfälle',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.20', 'G 0.22', 'G 0.29', 'G 0.46']
    },
    {
        'id': 'DER.2.1.A15',
        'name': 'Schulung der Mitarbeitenden des Service Desks',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.20', 'G 0.29']
    },
    {
        'id': 'DER.2.1.A16',
        'name': 'Dokumentation der Behandlung von Sicherheitsvorfällen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'DER.2.1.A17',
        'name': 'Nachbereitung von Sicherheitsvorfällen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.20', 'G 0.22', 'G 0.29', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.1.A18',
        'name': 'Weiterentwicklung der Prozesse durch Erkenntnisse aus Sicherheitsvorfällen und Branchenentwicklungen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.20', 'G 0.29', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.1.A19',
        'name': 'Festlegung von Prioritäten für die Behandlung von Sicherheitsvorfällen',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.27', 'G 0.33', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.1.A20',
        'name': 'Einrichtung einer dedizierten Meldestelle für Sicherheitsvorfälle',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.20', 'G 0.22', 'G 0.27', 'G 0.29', 'G 0.32', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.1.A21',
        'name': 'Einrichtung eines Teams von Fachleuten für die Behandlung von Sicherheitsvorfällen',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.20', 'G 0.27', 'G 0.29', 'G 0.32', 'G 0.33', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.1.A22',
        'name': 'Überprüfung der Effizienz des Managementsystems zur Behandlung von Sicherheitsvorfällen',
        'cia': 'CIA',
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.19', 'G 0.20', 'G 0.22', 'G 0.25', 'G 0.27', 'G 0.29', 'G 0.33', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.2.A1',
        'name': 'Prüfung rechtlicher und regulatorischer Rahmenbedingungen zur Erfassung und Auswertbarkeit',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'DER.2.2.A2',
        'name': 'Erstellung eines Leitfadens für Erstmaßnahmen bei einem IT-Sicherheitsvorfall',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'DER.2.2.A3',
        'name': 'Vorauswahl von Forensik-Dienstleistenden',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'DER.2.2.A4',
        'name': 'Festlegung von Schnittstellen zum Krisen- und Notfallmanagement',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'DER.2.2.A5',
        'name': 'Erstellung eines Leitfadens für Beweissicherungsmaßnahmen bei IT-Sicherheitsvorfällen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.31']
    },
    {
        'id': 'DER.2.2.A6',
        'name': 'Schulung des Personals für die Umsetzung der forensischen Sicherung',
        'cia': None,
        'gefahren': ['G 0.31']
    },
    {
        'id': 'DER.2.2.A7',
        'name': 'Auswahl von Werkzeugen zur Forensik',
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.21', 'G 0.26']
    },
    {
        'id': 'DER.2.2.A8',
        'name': 'Auswahl und Reihenfolge der zu sichernden Beweismittel',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31', 'G 0.45']
    },
    {
        'id': 'DER.2.2.A9',
        'name': 'Vorauswahl forensisch relevanter Daten',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'DER.2.2.A10',
        'name': 'IT-forensische Sicherung von Beweismitteln',
        'cia': None,
        'gefahren': ['G 0.17', 'G 0.22', 'G 0.31', 'G 0.37', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.2.A11',
        'name': 'Dokumentation der Beweissicherung',
        'cia': None,
        'gefahren': ['G 0.37']
    },
    {
        'id': 'DER.2.2.A12',
        'name': 'Sichere Verwahrung von Originaldatenträgern und Beweismitteln',
        'cia': None,
        'gefahren': ['G 0.17', 'G 0.18', 'G 0.30']
    },
    {
        'id': 'DER.2.2.A13',
        'name': 'Rahmenverträge mit externen Dienstleistenden',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'DER.2.2.A14',
        'name': 'Festlegung von Standardverfahren für die Beweissicherung',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'DER.2.2.A15',
        'name': 'Durchführung von Übungen zur Beweissicherung',
        'cia': 'CIA',
        'gefahren': ['G 0.31']
    },
    {
        'id': 'DER.2.3.A1',
        'name': 'Einrichtung eines Leitungsgremiums',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.40', 'G 0.41', 'G 0.42', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.3.A2',
        'name': 'Entscheidung für eine Bereinigungsstrategie',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.16', 'G 0.18', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.24', 'G 0.32', 'G 0.39', 'G 0.41', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.3.A3',
        'name': 'Isolierung der betroffenen Netzabschnitte',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.22', 'G 0.23', 'G 0.32', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.3.A4',
        'name': 'Sperrung und Änderung von Zugangsdaten und kryptografischen Schlüsseln',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.16', 'G 0.18', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.24', 'G 0.32', 'G 0.39', 'G 0.40', 'G 0.41', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.3.A5',
        'name': 'Schließen des initialen Einbruchswegs',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.18', 'G 0.23', 'G 0.28', 'G 0.32', 'G 0.41', 'G 0.42']
    },
    {
        'id': 'DER.2.3.A6',
        'name': 'Rückführung in den Produktivbetrieb',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.28', 'G 0.29', 'G 0.31']
    },
    {
        'id': 'DER.2.3.A7',
        'name': 'Gezielte Systemhärtung',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.16', 'G 0.18', 'G 0.20', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.24', 'G 0.28', 'G 0.32', 'G 0.39', 'G 0.40', 'G 0.41', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.3.A8',
        'name': 'Etablierung sicherer, unabhängiger Kommunikationskanäle',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.16', 'G 0.18', 'G 0.22', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.3.A9',
        'name': 'Hardwaretausch betroffener IT-Systeme',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.16', 'G 0.18', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.39', 'G 0.41', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'DER.2.3.A10',
        'name': 'Umbauten zur Erschwerung eines erneuten Angriffs durch dieselben Angreifenden',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.16', 'G 0.18', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.24', 'G 0.28', 'G 0.32', 'G 0.39', 'G 0.41', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'DER.3.1.A1',
        'name': 'Definition von Verantwortlichkeiten',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.46']
    },
    {
        'id': 'DER.3.1.A2',
        'name': 'Vorbereitung eines Audits oder einer Revision',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'DER.3.1.A3',
        'name': 'Durchführung eines Audits',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.1.A4',
        'name': 'Durchführung einer Revision',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.1.A5',
        'name': 'Integration in den Informationssicherheitsprozess',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.46']
    },
    {
        'id': 'DER.3.1.A6',
        'name': 'Definition der Prüfungsgrundlage und eines einheitlichen Bewertungsschemas',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.1.A7',
        'name': 'Erstellung eines Auditprogramms',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.46']
    },
    {
        'id': 'DER.3.1.A8',
        'name': 'Erstellung einer Revisionsliste',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.46']
    },
    {
        'id': 'DER.3.1.A9',
        'name': 'Auswahl eines geeigneten Audit- oder Revionsteams',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.46']
    },
    {
        'id': 'DER.3.1.A10',
        'name': 'Erstellung eines Audit- oder Revisionsplans',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.1.A11',
        'name': 'Kommunikation und Verhalten während der Prüfungen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'DER.3.1.A12',
        'name': 'Durchführung eines Auftaktgesprächs',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'DER.3.1.A13',
        'name': 'Sichtung und Prüfung der Dokumente',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.1.A14',
        'name': 'Auswahl von Stichproben',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'DER.3.1.A15',
        'name': 'Auswahl von geeigneten Prüfmethoden',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.1.A16',
        'name': 'Ablaufplan der Vor-Ort-Prüfung',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.1.A17',
        'name': 'Durchführung der Vor-Ort-Prüfung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'DER.3.1.A18',
        'name': 'Durchführung von Interviews',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'DER.3.1.A19',
        'name': 'Überprüfung des Risikobehandlungsplans',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'DER.3.1.A20',
        'name': 'Durchführung einer Abschlussbesprechung',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.1.A21',
        'name': 'Auswertung der Prüfungen',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.1.A22',
        'name': 'Erstellung eines Auditberichts',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.46']
    },
    {
        'id': 'DER.3.1.A23',
        'name': 'Dokumentation der Revisionsergebnisse',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.46']
    },
    {
        'id': 'DER.3.1.A24',
        'name': 'Abschluss des Audits oder der Revision',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.29', 'G 0.46']
    },
    {
        'id': 'DER.3.1.A25',
        'name': 'Nachbereitung eines Audits',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'DER.3.1.A26',
        'name': 'Überwachen und Anpassen des Auditprogramms',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.29', 'G 0.46']
    },
    {
        'id': 'DER.3.1.A27',
        'name': 'Aufbewahrung und Archivierung von Unterlagen zu Audits und Revisionen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.46']
    },
    {
        'id': 'DER.3.2.A1',
        'name': 'Benennung von Verantwortlichen für die IS-Revision',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'DER.3.2.A2',
        'name': 'Erstellung eines IS-Revisionshandbuches',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.2.A3',
        'name': 'Definition der Prüfungsgrundlage',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.2.A4',
        'name': 'Erstellung einer Planung für die IS-Revision',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'DER.3.2.A5',
        'name': 'Auswahl eines geeigneten IS-Revisionsteams',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'DER.3.2.A6',
        'name': 'Vorbereitung einer IS-Revision',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.2.A7',
        'name': 'Durchführung einer IS-Revision',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.2.A8',
        'name': 'Aufbewahrung von IS-Revisionsberichten',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.46']
    },
    {
        'id': 'DER.3.2.A9',
        'name': 'Integration in den Informationssicherheitsprozess',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.2.A10',
        'name': 'Kommunikationsabsprache',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.46']
    },
    {
        'id': 'DER.3.2.A11',
        'name': 'Durchführung eines Auftaktgesprächs für eine IS-Querschnittsrevision',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.2.A12',
        'name': 'Erstellung eines Prüfplans',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.2.A13',
        'name': 'Sichtung und Prüfung der Dokumente',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.2.A14',
        'name': 'Auswahl der Zielobjekte und der zu prüfenden Anforderungen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'DER.3.2.A15',
        'name': 'Auswahl von geeigneten Prüfmethoden',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.2.A16',
        'name': 'Erstellung eines Ablaufplans für die Vor-Ort-Prüfung',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.2.A17',
        'name': 'Durchführung der Vor-Ort-Prüfung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.46']
    },
    {
        'id': 'DER.3.2.A18',
        'name': 'Durchführung von Interviews',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.2.A19',
        'name': 'Überprüfung der gewählten Risikobehandlungsoptionen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'DER.3.2.A20',
        'name': 'Nachbereitung der Vor-Ort-Prüfung',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.2.A21',
        'name': 'Erstellung eines IS-Revisionsberichts',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.46']
    },
    {
        'id': 'DER.3.2.A22',
        'name': 'Nachbereitung einer IS-Revision',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.4.A1',
        'name': 'Erstellung eines Notfallhandbuchs',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.29']
    },
    {
        'id': 'DER.4.A2',
        'name': 'Integration von Notfallmanagement und Informationssicherheitsmanagement',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.4.A3',
        'name': 'Festlegung des Geltungsbereichs und der Notfallmanagementstrategie',
        'cia': 'CIA',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.4.A4',
        'name': 'Leitlinie zum Notfallmanagement und Übernahme der Gesamtverantwortung durch die Institutionsleitung',
        'cia': 'CIA',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.4.A5',
        'name': 'Aufbau einer geeigneten Organisationsstruktur für das Notfallmanagement',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'DER.4.A6',
        'name': 'Bereitstellung angemessener Ressourcen für das Notfallmanagement',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'DER.4.A7',
        'name': 'Erstellung eines Notfallkonzepts',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'DER.4.A8',
        'name': 'Integration der Mitarbeitenden in den Notfallmanagement-Prozess',
        'cia': 'CIA',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.4.A9',
        'name': 'Integration von Notfallmanagement in organisationsweite Abläufe und Prozesse',
        'cia': 'CIA',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.4.A10',
        'name': 'Tests und Notfallübungen',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'DER.4.A12',
        'name': 'Dokumentation im Notfallmanagement-Prozess',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'DER.4.A13',
        'name': 'Überprüfung und Steuerung des Notfallmanagement-Systems',
        'cia': 'CIA',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.4.A14',
        'name': 'Regelmäßige Überprüfung und Verbesserung der Notfallmaßnahmen',
        'cia': 'CIA',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.4.A15',
        'name': 'Bewertung der Leistungsfähigkeit des Notfallmanagementsystems',
        'cia': 'CIA',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.4.A16',
        'name': 'Notfallvorsorge- und Notfallreaktionsplanung für ausgelagerte Komponenten',
        'cia': 'CIA',
        'gefahren': ['G 0.11', 'G 0.18']
    },
    {
        'id': 'IND.1.A1',
        'name': 'Einbindung in die Sicherheitsorganisation',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.20', 'G 0.29', 'G 0.30']
    },
    {
        'id': 'IND.1.A3',
        'name': 'Schutz vor Schadprogrammen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.39', 'G 0.41']
    },
    {
        'id': 'IND.1.A4',
        'name': 'Dokumentation der OT-Infrastruktur',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.21', 'G 0.23', 'G 0.29', 'G 0.32']
    },
    {
        'id': 'IND.1.A5',
        'name': 'Entwicklung eines geeigneten Zonenkonzepts',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23']
    },
    {
        'id': 'IND.1.A6',
        'name': 'Änderungsmanagement im OT-Betrieb',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'IND.1.A7',
        'name': 'Etablieren einer übergreifenden Berechtigungsverwaltung zwischen der OT und in der Office-IT',
        'cia': None,
        'gefahren': ['G 0.30', 'G 0.32', 'G 0.37']
    },
    {
        'id': 'IND.1.A8',
        'name': 'Sichere Administration',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'IND.1.A9',
        'name': 'Restriktiver Einsatz von Wechseldatenträgern und mobilen Endgeräten in ICS-Umgebungen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.29']
    },
    {
        'id': 'IND.1.A10',
        'name': 'Monitoring, Protokollierung und Detektion',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.32', 'G 0.37', 'G 0.39', 'G 0.41']
    },
    {
        'id': 'IND.1.A11',
        'name': 'Sichere Beschaffung und Systementwicklung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.20', 'G 0.28']
    },
    {
        'id': 'IND.1.A12',
        'name': 'Etablieren eines Schwachstellen-Managements',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.28']
    },
    {
        'id': 'IND.1.A13',
        'name': 'Notfallplanung für OT',
        'cia': 'A',
        'gefahren': ['G 0.5', 'G 0.11', 'G 0.25', 'G 0.41']
    },
    {
        'id': 'IND.1.A14',
        'name': 'Starke Authentisierung an OT-Komponenten',
        'cia': 'CIA',
        'gefahren': ['G 0.30', 'G 0.32', 'G 0.36', 'G 0.37']
    },
    {
        'id': 'IND.1.A15',
        'name': 'Überwachung von weitreichenden Berechtigungen',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.32', 'G 0.37']
    },
    {
        'id': 'IND.1.A16',
        'name': 'Stärkere Abschottung der Zonen',
        'cia': 'IA',
        'gefahren': ['G 0.23', 'G 0.41']
    },
    {
        'id': 'IND.1.A17',
        'name': 'Regelmäßige Sicherheitsüberprüfung',
        'cia': 'I',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'IND.1.A18',
        'name': 'Protokollierung',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.30', 'G 0.37']
    },
    {
        'id': 'IND.1.A19',
        'name': 'Erstellung von Datensicherungen',
        'cia': None,
        'gefahren': ['G 0.17', 'G 0.45']
    },
    {
        'id': 'IND.1.A20',
        'name': 'Systemdokumentation',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'IND.1.A21',
        'name': 'Dokumentation der Kommunikationsbeziehungen',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'IND.1.A22',
        'name': 'Zentrale Systemprotokollierung und -überwachung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.21', 'G 0.22', 'G 0.30', 'G 0.37']
    },
    {
        'id': 'IND.1.A23',
        'name': 'Aussonderung von ICS-Komponenten',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'IND.1.A24',
        'name': 'Kommunikation im Störfall',
        'cia': 'A',
        'gefahren': ['G 0.9', 'G 0.25', 'G 0.27']
    },
    {
        'id': 'IND.2.1.A1',
        'name': 'Einschränkung des Zugriffs für Konfigurations- und Wartungsschnittstellen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.30', 'G 0.32', 'G 0.41', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'IND.2.1.A2',
        'name': 'Nutzung sicherer Übertragungsprotokolle für die Konfiguration und Wartung',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.39', 'G 0.41', 'G 0.46']
    },
    {
        'id': 'IND.2.1.A4',
        'name': 'Deaktivierung oder Deinstallation nicht genutzter Dienste, Funktionen und Schnittstellen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.41']
    },
    {
        'id': 'IND.2.1.A6',
        'name': 'Netzsegmentierung',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.40', 'G 0.41']
    },
    {
        'id': 'IND.2.1.A7',
        'name': 'Erstellung von Datensicherungen',
        'cia': None,
        'gefahren': ['G 0.2', 'G 0.4', 'G 0.8', 'G 0.9', 'G 0.10', 'G 0.12', 'G 0.25', 'G 0.39', 'G 0.40', 'G 0.41', 'G 0.45']
    },
    {
        'id': 'IND.2.1.A8',
        'name': 'Schutz vor Schadsoftware',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.30', 'G 0.39']
    },
    {
        'id': 'IND.2.1.A11',
        'name': 'Wartung der ICS-Komponenten',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.41']
    },
    {
        'id': 'IND.2.1.A13',
        'name': 'Geeignete Inbetriebnahme der ICS-Komponenten',
        'cia': None,
        'gefahren': ['G 0.12', 'G 0.14', 'G 0.15', 'G 0.21', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.39', 'G 0.41']
    },
    {
        'id': 'IND.2.1.A16',
        'name': 'Schutz externer Schnittstellen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.39', 'G 0.41', 'G 0.45']
    },
    {
        'id': 'IND.2.1.A17',
        'name': 'Nutzung sicherer Protokolle für die Übertragung von Mess- und Steuerdaten',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.30', 'G 0.37', 'G 0.39', 'G 0.41', 'G 0.46']
    },
    {
        'id': 'IND.2.1.A18',
        'name': 'Kommunikation im Störfall',
        'cia': 'A',
        'gefahren': ['G 0.9', 'G 0.45']
    },
    {
        'id': 'IND.2.1.A19',
        'name': 'Security-Tests',
        'cia': 'CIA',
        'gefahren': ['G 0.8', 'G 0.9', 'G 0.14', 'G 0.21', 'G 0.23', 'G 0.28', 'G 0.30', 'G 0.39', 'G 0.40', 'G 0.41', 'G 0.46']
    },
    {
        'id': 'IND.2.1.A20',
        'name': 'Vertrauenswürdiger Code',
        'cia': 'IA',
        'gefahren': ['G 0.14', 'G 0.21', 'G 0.23', 'G 0.28', 'G 0.39']
    },
    {
        'id': 'IND.2.2.A1',
        'name': 'Erweiterte Systemdokumentation für Speicherprogrammierbare Steuerungen',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.23', 'G 0.41']
    },
    {
        'id': 'IND.2.2.A3',
        'name': 'Zeitsynchronisation',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.22']
    },
    {
        'id': 'IND.2.3.A1',
        'name': 'Installation von Sensoren',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.30']
    },
    {
        'id': 'IND.2.3.A2',
        'name': 'Kalibrierung von Sensoren',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.21', 'G 0.28', 'G 0.30']
    },
    {
        'id': 'IND.2.3.A3',
        'name': 'Drahtlose Kommunikation',
        'cia': 'I',
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.21', 'G 0.23', 'G 0.28', 'G 0.30']
    },
    {
        'id': 'IND.2.4.A1',
        'name': 'Fernwartung durch Maschinen- und Anlagenbauende',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.14', 'G 0.18', 'G 0.21', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'IND.2.4.A2',
        'name': 'Betrieb nach Ende der Gewährleistung',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.39']
    },
    {
        'id': 'IND.2.7.A1',
        'name': 'Erfassung und Dokumentation',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.30', 'G 0.41', 'G 0.42', 'G 0.46']
    },
    {
        'id': 'IND.2.7.A2',
        'name': 'Zweckgebundene Nutzung der Hard- und Softwarekomponenten',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.30', 'G 0.41', 'G 0.42', 'G 0.46']
    },
    {
        'id': 'IND.2.7.A3',
        'name': 'Änderung des Anwendungsprogramms auf dem Logiksystem',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.41', 'G 0.42', 'G 0.46']
    },
    {
        'id': 'IND.2.7.A4',
        'name': 'Verankerung von Informationssicherheit im Functional Safety Management',
        'cia': None,
        'gefahren': ['G 0.5', 'G 0.6', 'G 0.9', 'G 0.11', 'G 0.14', 'G 0.15', 'G 0.19', 'G 0.20', 'G 0.21', 'G 0.23', 'G 0.28', 'G 0.29', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.39', 'G 0.41', 'G 0.42']
    },
    {
        'id': 'IND.2.7.A5',
        'name': 'Notfallmanagement von SIS',
        'cia': None,
        'gefahren': ['G 0.5', 'G 0.6', 'G 0.9', 'G 0.11', 'G 0.14', 'G 0.41']
    },
    {
        'id': 'IND.2.7.A6',
        'name': 'Sichere Planung und Spezifikation des SIS',
        'cia': None,
        'gefahren': ['G 0.5', 'G 0.6', 'G 0.9', 'G 0.11', 'G 0.14', 'G 0.15', 'G 0.18', 'G 0.19', 'G 0.20', 'G 0.21', 'G 0.23', 'G 0.41']
    },
    {
        'id': 'IND.2.7.A7',
        'name': 'Trennung und Unabhängigkeit des SIS von der Umgebung',
        'cia': None,
        'gefahren': ['G 0.6', 'G 0.9', 'G 0.14', 'G 0.15', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.41', 'G 0.42', 'G 0.46']
    },
    {
        'id': 'IND.2.7.A8',
        'name': 'Sichere Übertragung von Engineering Daten auf SIS',
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.21', 'G 0.23', 'G 0.41', 'G 0.46']
    },
    {
        'id': 'IND.2.7.A9',
        'name': 'Absicherung der Daten- und Signalverbindungen',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.14', 'G 0.15', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.41', 'G 0.46']
    },
    {
        'id': 'IND.2.7.A10',
        'name': 'Anzeige und Alarmierung von simulierten oder gebrückten Variablen',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.41', 'G 0.42']
    },
    {
        'id': 'IND.2.7.A11',
        'name': 'Umgang mit integrierten Systemen',
        'cia': None,
        'gefahren': ['G 0.6', 'G 0.14', 'G 0.15', 'G 0.19', 'G 0.20', 'G 0.21', 'G 0.23', 'G 0.41', 'G 0.42', 'G 0.46']
    },
    {
        'id': 'IND.2.7.A12',
        'name': 'Sicherstellen der Integrität und Authentizität von Anwendungsprogrammen und Konfigurationsdaten',
        'cia': 'I',
        'gefahren': ['G 0.20', 'G 0.21', 'G 0.23', 'G 0.28', 'G 0.41']
    },
    {
        'id': 'IND.3.2.A1',
        'name': 'Planung des Einsatzes der Fernwartung in der OT',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'IND.3.2.A2',
        'name': 'Konsistente Dokumentation der Fernwartung durch OT sowie Büro- und Gebäude-IT',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'IND.3.2.A3',
        'name': 'Regelmäßige Prüfungen sowie Ausnahmegenehmigungen bestehender OT-Fernwartungszugänge',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.30', 'G 0.40']
    },
    {
        'id': 'IND.3.2.A4',
        'name': 'Verbindliche Regelung der OT-Fernwartung durch Dritte',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.31', 'G 0.32']
    },
    {
        'id': 'IND.3.2.A5',
        'name': 'Interne Abstimmung für die OT-Fernwartung mit der Büro- und Gebäude-IT',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.40']
    },
    {
        'id': 'IND.3.2.A6',
        'name': 'Absicherung jedes Fernwartungszugriffs auf die OT',
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'IND.3.2.A7',
        'name': 'Technische Entkopplung von Zugriffen',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.37']
    },
    {
        'id': 'IND.3.2.A8',
        'name': 'Explizite Freigabe jeder OT-Fernwartungssitzung',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'IND.3.2.A9',
        'name': 'Sicherer Austausch von Dateien begleitend zur OT-Fernwartung',
        'cia': None,
        'gefahren': ['G 0.37', 'G 0.39', 'G 0.43']
    },
    {
        'id': 'IND.3.2.A10',
        'name': 'Beobachtung und Kontrolle von OT-Fernwartungssitzungen',
        'cia': None,
        'gefahren': ['G 0.24', 'G 0.25', 'G 0.31', 'G 0.32', 'G 0.33', 'G 0.37', 'G 0.41']
    },
    {
        'id': 'IND.3.2.A11',
        'name': 'Zentrale Verwaltung aller Konten für die OT-Fernwartung',
        'cia': None,
        'gefahren': ['G 0.30']
    },
    {
        'id': 'IND.3.2.A12',
        'name': 'Dedizierte Fernwartungslösung in der OT',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.27', 'G 0.30']
    },
    {
        'id': 'IND.3.2.A13',
        'name': 'Protokollierung der Inhalte von Fernwartungszugriffen in der OT',
        'cia': 'CI',
        'gefahren': ['G 0.37']
    },
    {
        'id': 'IND.3.2.A14',
        'name': 'Technische Kontrolle von Fernwartungssitzungen',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.31', 'G 0.32', 'G 0.37']
    },
    {
        'id': 'INF.1.A1',
        'name': 'Planung der Gebäudeabsicherung',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.18', 'G 0.44']
    },
    {
        'id': 'INF.1.A2',
        'name': 'Angepasste Aufteilung der Stromkreise',
        'cia': None,
        'gefahren': ['G 0.8']
    },
    {
        'id': 'INF.1.A3',
        'name': 'Einhaltung von Brandschutzvorschriften',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'INF.1.A4',
        'name': 'Branderkennung in Gebäuden',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.18']
    },
    {
        'id': 'INF.1.A5',
        'name': 'Handfeuerlöscher',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'INF.1.A6',
        'name': 'Geschlossene Fenster und Türen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.44']
    },
    {
        'id': 'INF.1.A7',
        'name': 'Zutrittsregelung und -kontrolle',
        'cia': None,
        'gefahren': ['G 0.44']
    },
    {
        'id': 'INF.1.A8',
        'name': 'Rauchverbot',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.4', 'G 0.18', 'G 0.44']
    },
    {
        'id': 'INF.1.A9',
        'name': 'Sicherheitskonzept für die Gebäudenutzung',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.1.A10',
        'name': 'Einhaltung einschlägiger Normen und Vorschriften',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'INF.1.A12',
        'name': 'Schlüsselverwaltung',
        'cia': None,
        'gefahren': ['G 0.16', 'G 0.18', 'G 0.44']
    },
    {
        'id': 'INF.1.A13',
        'name': 'Regelungen für Zutritt zu Verteilern',
        'cia': None,
        'gefahren': ['G 0.27', 'G 0.44']
    },
    {
        'id': 'INF.1.A14',
        'name': 'Blitzschutzeinrichtungen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'INF.1.A15',
        'name': 'Lagepläne der Versorgungsleitungen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.27']
    },
    {
        'id': 'INF.1.A16',
        'name': 'Vermeidung von Lagehinweisen auf schützenswerte Gebäudeteile',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.34']
    },
    {
        'id': 'INF.1.A17',
        'name': 'Baulicher Rauchschutz',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.18']
    },
    {
        'id': 'INF.1.A18',
        'name': 'Brandschutzbegehungen',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.18']
    },
    {
        'id': 'INF.1.A19',
        'name': 'Information des oder der Brandschutzbeauftragten',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.18']
    },
    {
        'id': 'INF.1.A20',
        'name': 'Alarmierungsplan und Brandschutzübungen',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.18']
    },
    {
        'id': 'INF.1.A22',
        'name': 'Sichere Türen und Fenster',
        'cia': 'CIA',
        'gefahren': ['G 0.1', 'G 0.18', 'G 0.34', 'G 0.44']
    },
    {
        'id': 'INF.1.A23',
        'name': 'Bildung von Sicherheitszonen',
        'cia': 'C',
        'gefahren': ['G 0.18', 'G 0.34', 'G 0.44']
    },
    {
        'id': 'INF.1.A24',
        'name': 'Selbsttätige Entwässerung',
        'cia': 'A',
        'gefahren': ['G 0.3', 'G 0.5', 'G 0.18']
    },
    {
        'id': 'INF.1.A25',
        'name': 'Geeignete Standortauswahl',
        'cia': 'A',
        'gefahren': ['G 0.5', 'G 0.6', 'G 0.7', 'G 0.18']
    },
    {
        'id': 'INF.1.A26',
        'name': 'Pforten- oder Sicherheitsdienst',
        'cia': 'CIA',
        'gefahren': ['G 0.16', 'G 0.18', 'G 0.34', 'G 0.44']
    },
    {
        'id': 'INF.1.A27',
        'name': 'Einbruchschutz',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.44']
    },
    {
        'id': 'INF.1.A30',
        'name': 'Auswahl eines geeigneten Gebäudes',
        'cia': 'CIA',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.1.A31',
        'name': 'Auszug aus Gebäuden',
        'cia': 'C',
        'gefahren': ['G 0.16', 'G 0.18']
    },
    {
        'id': 'INF.1.A32',
        'name': 'Brandschott-Kataster',
        'cia': 'A',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.1.A34',
        'name': 'Gefahrenmeldeanlage',
        'cia': 'A',
        'gefahren': ['G 0.1', 'G 0.3', 'G 0.18', 'G 0.44']
    },
    {
        'id': 'INF.1.A35',
        'name': 'Perimeterschutz',
        'cia': 'CA',
        'gefahren': ['G 0.7', 'G 0.34', 'G 0.44']
    },
    {
        'id': 'INF.1.A36',
        'name': 'Regelmäßige Aktualisierungen der Dokumentation',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.18']
    },
    {
        'id': 'INF.10.A1',
        'name': 'Sichere Nutzung von Besprechungs-, Veranstaltungs- und Schulungsräumen',
        'cia': None,
        'gefahren': ['G 0.16', 'G 0.18']
    },
    {
        'id': 'INF.10.A3',
        'name': 'Geschlossene Fenster und Türen',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.44']
    },
    {
        'id': 'INF.10.A4',
        'name': 'Planung von Besprechungs-, Veranstaltungs- und Schulungsräumen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.18', 'G 0.19', 'G 0.44']
    },
    {
        'id': 'INF.10.A5',
        'name': 'Fliegende Verkabelung',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.10.A6',
        'name': 'Einrichtung sicherer Netzzugänge',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.23', 'G 0.41']
    },
    {
        'id': 'INF.10.A7',
        'name': 'Sichere Konfiguration von Schulungs- und Präsentationsrechnern',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.23', 'G 0.41']
    },
    {
        'id': 'INF.10.A8',
        'name': 'Erstellung eines Nutzungsnachweises für Räume',
        'cia': None,
        'gefahren': ['G 0.37']
    },
    {
        'id': 'INF.10.A9',
        'name': 'Zurücksetzen von Schulungs- und Präsentationsrechnern',
        'cia': 'IA',
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.22', 'G 0.46']
    },
    {
        'id': 'INF.11.A1',
        'name': 'Planung und Beschaffung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'INF.11.A2',
        'name': 'Wartung, Inspektion und Updates',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.25']
    },
    {
        'id': 'INF.11.A3',
        'name': 'Regelungen für die Fahrzeugbenutzung',
        'cia': None,
        'gefahren': ['G 0.2', 'G 0.18', 'G 0.19', 'G 0.25']
    },
    {
        'id': 'INF.11.A4',
        'name': 'Erstellung einer Sicherheitsrichtlinie',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.11.A5',
        'name': 'Erstellung einer Inventarliste',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.11.A6',
        'name': 'Festlegung von Handlungsanweisungen',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.11.A7',
        'name': 'Sachgerechter Umgang mit Fahrzeugen und schützenswerten Informationen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'INF.11.A8',
        'name': 'Schutz vor witterungsbedingten Einflüssen',
        'cia': None,
        'gefahren': ['G 0.2']
    },
    {
        'id': 'INF.11.A9',
        'name': 'Sicherstellung der Versorgung',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.11.A10',
        'name': 'Aussonderung',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.29']
    },
    {
        'id': 'INF.11.A11',
        'name': 'Ersatzvorkehrungen bei Ausfällen',
        'cia': 'A',
        'gefahren': ['G 0.27']
    },
    {
        'id': 'INF.11.A12',
        'name': 'Diebstahlsicherung bzw. Bewachung',
        'cia': 'CA',
        'gefahren': ['G 0.16']
    },
    {
        'id': 'INF.11.A13',
        'name': 'Schädigende Fremdeinwirkung',
        'cia': 'A',
        'gefahren': ['G 0.24']
    },
    {
        'id': 'INF.11.A14',
        'name': 'Schutz sensibler Informationen vor unbefugtem Zugriff und Kenntnisnahme',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.22']
    },
    {
        'id': 'INF.11.A15',
        'name': 'Physische Absicherung der Schnittstellen',
        'cia': 'CIA',
        'gefahren': ['G 0.2', 'G 0.15', 'G 0.30']
    },
    {
        'id': 'INF.11.A16',
        'name': 'Brandlöschanlage',
        'cia': 'A',
        'gefahren': ['G 0.1']
    },
    {
        'id': 'INF.11.A17',
        'name': 'Netztrennung des In-Vehicle-Network mit einem Sonderfahrzeugnetz über Gateway',
        'cia': 'C',
        'gefahren': ['G 0.19']
    },
    {
        'id': 'INF.12.A1',
        'name': 'Auswahl geeigneter Kabeltypen',
        'cia': None,
        'gefahren': ['G 0.2', 'G 0.18', 'G 0.25', 'G 0.26', 'G 0.29']
    },
    {
        'id': 'INF.12.A2',
        'name': 'Planung der Kabelführung',
        'cia': None,
        'gefahren': ['G 0.12', 'G 0.18', 'G 0.27', 'G 0.29']
    },
    {
        'id': 'INF.12.A3',
        'name': 'Fachgerechte Installation',
        'cia': None,
        'gefahren': ['G 0.8', 'G 0.9', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'INF.12.A4',
        'name': 'EMV-taugliche Stromversorgung',
        'cia': None,
        'gefahren': ['G 0.8', 'G 0.12']
    },
    {
        'id': 'INF.12.A5',
        'name': 'Anforderungsanalyse für die Verkabelung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'INF.12.A6',
        'name': 'Abnahme der Verkabelung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.37', 'G 0.41']
    },
    {
        'id': 'INF.12.A7',
        'name': 'Überspannungsschutz',
        'cia': None,
        'gefahren': ['G 0.8', 'G 0.12', 'G 0.18']
    },
    {
        'id': 'INF.12.A8',
        'name': 'Entfernen und Deaktivieren nicht mehr benötigter Kabel',
        'cia': None,
        'gefahren': ['G 0.8', 'G 0.18']
    },
    {
        'id': 'INF.12.A9',
        'name': 'Brandaschutz in Trassen',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.27']
    },
    {
        'id': 'INF.12.A10',
        'name': 'Dokumentation und Kennzeichnung der Verkabelung',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.12.A11',
        'name': 'Neutrale Dokumentation in den Verteilern',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.19']
    },
    {
        'id': 'INF.12.A12',
        'name': 'Kontrolle elektrotechnischer Anlagen und bestehender Verbindungen',
        'cia': None,
        'gefahren': ['G 0.8', 'G 0.9', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'INF.12.A13',
        'name': 'Vermeidung elektrischer Zündquellen',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.8', 'G 0.12']
    },
    {
        'id': 'INF.12.A14',
        'name': 'A-B-Versorgung',
        'cia': 'A',
        'gefahren': ['G 0.8', 'G 0.12']
    },
    {
        'id': 'INF.12.A15',
        'name': 'Materielle Sicherung der Verkabelung',
        'cia': 'IA',
        'gefahren': ['G 0.15', 'G 0.41']
    },
    {
        'id': 'INF.12.A16',
        'name': 'Nutzung von Schranksystemen',
        'cia': 'IA',
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'INF.12.A17',
        'name': 'Redundanzen für die IT-Verkabelung',
        'cia': 'A',
        'gefahren': ['G 0.9', 'G 0.18', 'G 0.27', 'G 0.41']
    },
    {
        'id': 'INF.13.A1',
        'name': 'Beurteilung des Ist-Zustands bei der Übernahme bestehender Gebäude',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.13.A2',
        'name': 'Regelung und Dokumentation von Verantwortlichkeiten und Zuständigkeiten im Gebäude',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'INF.13.A3',
        'name': 'Dokumentation von Gebäudeeinrichtungen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'INF.13.A4',
        'name': 'Erstellung einer Sicherheitsrichtlinie für TGM',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'INF.13.A5',
        'name': 'Planung des TGM',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.13.A6',
        'name': 'Erstellung eines TGM-Konzepts',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.10', 'G 0.18', 'G 0.19', 'G 0.25', 'G 0.33']
    },
    {
        'id': 'INF.13.A7',
        'name': 'Erstellung eines Funkfrequenzkatasters',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.25', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'INF.13.A8',
        'name': 'Erstellung und Pflege eines Inventars für das TGM',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.13.A9',
        'name': 'Regelung des Einsatzes von Computer-Aided Facility Management',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'INF.13.A10',
        'name': 'Regelung des Einsatzes von Building Information Modeling',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.13.A11',
        'name': 'Angemessene Härtung von Systemen im TGM',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.24', 'G 0.25', 'G 0.28', 'G 0.39', 'G 0.41', 'G 0.43', 'G 0.47']
    },
    {
        'id': 'INF.13.A12',
        'name': 'Sichere Konfiguration der TGM-Systeme',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.24', 'G 0.25', 'G 0.26', 'G 0.28', 'G 0.39', 'G 0.41', 'G 0.43', 'G 0.47']
    },
    {
        'id': 'INF.13.A13',
        'name': 'Sichere Anbindung von eingeschränkt vertrauenswürdigen Systemen im TGM',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.24', 'G 0.25', 'G 0.28', 'G 0.39', 'G 0.41', 'G 0.43', 'G 0.47']
    },
    {
        'id': 'INF.13.A14',
        'name': 'Berücksichtigung spezieller Rollen und Berechtigungen im TGM',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'INF.13.A15',
        'name': 'Schutz vor Schadsoftware im TGM',
        'cia': None,
        'gefahren': ['G 0.39']
    },
    {
        'id': 'INF.13.A16',
        'name': 'Prozess für Änderungen im TGM',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.13.A17',
        'name': 'Regelung von Wartungs- und Reparaturarbeiten im TGM',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.10', 'G 0.18', 'G 0.24', 'G 0.25', 'G 0.30', 'G 0.32', 'G 0.44']
    },
    {
        'id': 'INF.13.A18',
        'name': 'Proaktive Instandhaltung im TGM',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.10', 'G 0.18', 'G 0.25', 'G 0.27']
    },
    {
        'id': 'INF.13.A19',
        'name': 'Konzeptionierung und Durchführung des Monitorings im TGM',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'INF.13.A20',
        'name': 'Regelung des Ereignismanagements im TGM',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.13.A21',
        'name': 'Protokollierung im TGM',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.37']
    },
    {
        'id': 'INF.13.A22',
        'name': 'Durchführung von Systemtests im TGM',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.10', 'G 0.18', 'G 0.25', 'G 0.26', 'G 0.27', 'G 0.28']
    },
    {
        'id': 'INF.13.A23',
        'name': 'Integration des TGM in das Schwachstellenmanagement',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'INF.13.A24',
        'name': 'Sicherstellung der Kontrolle über die Prozesse bei Cloud-Nutzung für das TGM',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'INF.13.A25',
        'name': 'Aufbau einer Testumgebung für das TGM',
        'cia': 'CIA',
        'gefahren': ['G 0.9', 'G 0.10', 'G 0.18', 'G 0.25', 'G 0.26', 'G 0.27', 'G 0.28']
    },
    {
        'id': 'INF.13.A26',
        'name': 'Absicherung von BIM',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.26', 'G 0.32', 'G 0.41', 'G 0.43']
    },
    {
        'id': 'INF.13.A27',
        'name': 'Einrichtung einer Private Cloud für das TGM',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.29']
    },
    {
        'id': 'INF.13.A28',
        'name': 'Sichere Nutzung von Künstlicher Intelligenz im TGM',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.29']
    },
    {
        'id': 'INF.13.A29',
        'name': 'Integration des TGM in ein SIEM',
        'cia': 'CIA',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.13.A30',
        'name': 'Durchführung von Penetrationstests im TGM',
        'cia': 'CIA',
        'gefahren': ['G 0.28']
    },
    {
        'id': 'INF.14.A1',
        'name': 'Planung der Gebäudeautomation',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.14.A2',
        'name': 'Festlegung eines Inbetriebnahme- und Schnittstellenmanagements für die GA',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.14.A3',
        'name': 'Sichere Anbindung von TGA-Anlagen und GA-Systemen',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.10', 'G 0.14', 'G 0.15', 'G 0.18', 'G 0.19', 'G 0.22', 'G 0.25', 'G 0.26', 'G 0.46']
    },
    {
        'id': 'INF.14.A4',
        'name': 'Berücksichtigung von Gefahrenmeldeanlagen in der GA',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.18', 'G 0.19', 'G 0.25', 'G 0.26', 'G 0.29', 'G 0.40', 'G 0.43']
    },
    {
        'id': 'INF.14.A5',
        'name': 'Dokumentation der GA',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'INF.14.A6',
        'name': 'Separierung von Netzen der GA',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.19', 'G 0.23', 'G 0.40', 'G 0.43']
    },
    {
        'id': 'INF.14.A7',
        'name': 'Festlegung einer Sicherheitsrichtlinie für die GA',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.14.A8',
        'name': 'Anforderungsspezifikation für GA-Systeme',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23']
    },
    {
        'id': 'INF.14.A9',
        'name': 'Entwicklung eines GA-Konzepts',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.14.A10',
        'name': 'Bildung von unabhängigen GA-Bereichen',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.10', 'G 0.18', 'G 0.25', 'G 0.26', 'G 0.40']
    },
    {
        'id': 'INF.14.A11',
        'name': 'Absicherung von frei zugänglichen Ports und Zugängen der GA',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.40', 'G 0.43']
    },
    {
        'id': 'INF.14.A12',
        'name': 'Nutzung sicherer Übertragungsprotokolle für die GA',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'INF.14.A13',
        'name': 'Netzsegmentierung in der GA',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.19', 'G 0.23', 'G 0.40', 'G 0.43']
    },
    {
        'id': 'INF.14.A14',
        'name': 'Nutzung eines GA-geeigneten Zugriffsschutzes',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'INF.14.A15',
        'name': 'Absicherung von GA-spezifischen Netzen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'INF.14.A16',
        'name': 'Absicherung von drahtloser Kommunikation in GA-Netzen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'INF.14.A17',
        'name': 'Absicherung von Mobilfunkkommunikation in GA-Netzen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'INF.14.A18',
        'name': 'Sichere Anbindung von GA-eXternen Systemen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'INF.14.A19',
        'name': 'Nutzung dedizierter Adressbereiche für GA-Netze',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'INF.14.A20',
        'name': 'Vermeidung von Broadcast-Kommunikation in GA-Netzen',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.15', 'G 0.19', 'G 0.40']
    },
    {
        'id': 'INF.14.A21',
        'name': 'Anzeigen der Gültigkeit von Informationen in GA-Systemen',
        'cia': None,
        'gefahren': ['G 0.20']
    },
    {
        'id': 'INF.14.A22',
        'name': 'Sicherstellung von autark funktionierenden GA-Systemen und TGA-Anlagen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'INF.14.A23',
        'name': 'Einsatz von physisch robusten Komponenten für die GA',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26']
    },
    {
        'id': 'INF.14.A24',
        'name': 'Zeitsynchronisation für die GA',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.46']
    },
    {
        'id': 'INF.14.A25',
        'name': 'Dediziertes Monitoring in der GA',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'INF.14.A26',
        'name': 'Protokollierung in der GA',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.37']
    },
    {
        'id': 'INF.14.A27',
        'name': 'Berücksichtigung von Wechselwirkungen zwischen Komponenten der GA in der Notfallplanung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.29']
    },
    {
        'id': 'INF.14.A28',
        'name': 'Physische Trennung der GA',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'INF.14.A29',
        'name': 'Trennung einzelner TGA-Anlagen',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'INF.14.A30',
        'name': 'Bereitstellung eines GA-eigenen Zeitservers zur Zeitsynchronisation',
        'cia': 'IA',
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.46']
    },
    {
        'id': 'INF.2.A1',
        'name': 'Festlegung von Anforderungen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'INF.2.A2',
        'name': 'Bildung von Brandabschnitten',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.24', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'INF.2.A3',
        'name': 'Einsatz einer unterbrechungsfreien Stromversorgung',
        'cia': None,
        'gefahren': ['G 0.8']
    },
    {
        'id': 'INF.2.A4',
        'name': 'Notabschaltung der Stromversorgung',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.8', 'G 0.24', 'G 0.26']
    },
    {
        'id': 'INF.2.A5',
        'name': 'Einhaltung der Lufttemperatur und -feuchtigkeit',
        'cia': None,
        'gefahren': ['G 0.2']
    },
    {
        'id': 'INF.2.A6',
        'name': 'Zutrittskontrolle',
        'cia': None,
        'gefahren': ['G 0.44']
    },
    {
        'id': 'INF.2.A7',
        'name': 'Verschließen und Sichern',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.44']
    },
    {
        'id': 'INF.2.A8',
        'name': 'Einsatz einer Brandmeldeanlage',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.18']
    },
    {
        'id': 'INF.2.A9',
        'name': 'Einsatz einer Lösch- oder Brandvermeidungsanlage',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.24', 'G 0.25']
    },
    {
        'id': 'INF.2.A10',
        'name': 'Inspektion und Wartung der Infrastruktur',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.18', 'G 0.25', 'G 0.29']
    },
    {
        'id': 'INF.2.A11',
        'name': 'Automatische Überwachung der Infrastruktur',
        'cia': None,
        'gefahren': ['G 0.10', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'INF.2.A12',
        'name': 'Perimeterschutz für das Rechenzentrum',
        'cia': None,
        'gefahren': ['G 0.7', 'G 0.34', 'G 0.44']
    },
    {
        'id': 'INF.2.A13',
        'name': 'Planung und Installation von Gefahrenmeldeanlagen',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.3', 'G 0.18', 'G 0.44']
    },
    {
        'id': 'INF.2.A14',
        'name': 'Einsatz einer Netzersatzanlage',
        'cia': None,
        'gefahren': ['G 0.8', 'G 0.18']
    },
    {
        'id': 'INF.2.A15',
        'name': 'Überspannungsschutzeinrichtung',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.18', 'G 0.25']
    },
    {
        'id': 'INF.2.A16',
        'name': 'Klimatisierung im Rechenzentrum',
        'cia': None,
        'gefahren': ['G 0.2', 'G 0.25']
    },
    {
        'id': 'INF.2.A17',
        'name': 'Einsatz einer Brandfrüherkennung',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.8', 'G 0.24']
    },
    {
        'id': 'INF.2.A19',
        'name': 'Durchführung von Funktionstests der technischen Infrastruktur',
        'cia': None,
        'gefahren': ['G 0.8', 'G 0.18', 'G 0.26', 'G 0.29']
    },
    {
        'id': 'INF.2.A21',
        'name': 'Ausweichrechenzentrum',
        'cia': 'A',
        'gefahren': ['G 0.8', 'G 0.9', 'G 0.10', 'G 0.27']
    },
    {
        'id': 'INF.2.A22',
        'name': 'Durchführung von Staubschutzmaßnahmen',
        'cia': 'IA',
        'gefahren': ['G 0.2']
    },
    {
        'id': 'INF.2.A23',
        'name': 'Zweckmäßiger Aufbau der Verkabelung im Rechenzentrum',
        'cia': 'A',
        'gefahren': ['G 0.8', 'G 0.10', 'G 0.26']
    },
    {
        'id': 'INF.2.A24',
        'name': 'Einsatz von Videoüberwachungsanlagen',
        'cia': 'IA',
        'gefahren': ['G 0.29', 'G 0.30', 'G 0.37']
    },
    {
        'id': 'INF.2.A25',
        'name': 'Redundante Auslegung von unterbrechungsfreien Stromversorgungen',
        'cia': 'A',
        'gefahren': ['G 0.8', 'G 0.27']
    },
    {
        'id': 'INF.2.A26',
        'name': 'Redundante Auslegung von Netzersatzanlagen',
        'cia': 'A',
        'gefahren': ['G 0.8', 'G 0.27']
    },
    {
        'id': 'INF.2.A28',
        'name': 'Einsatz von höherwertigen Gefahrenmeldeanlagen',
        'cia': 'IA',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.2.A29',
        'name': 'Vermeidung und Überwachung nicht erforderlicher Leitungen',
        'cia': None,
        'gefahren': ['G 0.3', 'G 0.18', 'G 0.24', 'G 0.25']
    },
    {
        'id': 'INF.2.A30',
        'name': 'Anlagen zur Erkennung',
        'cia': None,
        'gefahren': ['G 0.1']
    },
    {
        'id': 'INF.5.A1',
        'name': 'Planung der Raumabsicherung',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.5.A2',
        'name': 'Lage und Größe des Raumes für technische Infrastruktur',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.5.A3',
        'name': 'Zutrittsregelung und -kontrolle',
        'cia': None,
        'gefahren': ['G 0.44']
    },
    {
        'id': 'INF.5.A4',
        'name': 'Schutz vor Einbruch',
        'cia': None,
        'gefahren': ['G 0.44']
    },
    {
        'id': 'INF.5.A5',
        'name': 'Vermeidung sowie Schutz vor elektromagnetischen Störfeldern',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26']
    },
    {
        'id': 'INF.5.A6',
        'name': 'Minimierung von Brandlasten',
        'cia': None,
        'gefahren': ['G 0.1']
    },
    {
        'id': 'INF.5.A7',
        'name': 'Verhinderung von Zweckentfremdung',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.5.A8',
        'name': 'Vermeidung von unkontrollierter elektrostatischer Entladung',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26']
    },
    {
        'id': 'INF.5.A9',
        'name': 'Stromversorgung',
        'cia': None,
        'gefahren': ['G 0.8']
    },
    {
        'id': 'INF.5.A10',
        'name': 'Einhaltung der Lufttemperatur und -feuchtigkeit',
        'cia': None,
        'gefahren': ['G 0.2', 'G 0.18']
    },
    {
        'id': 'INF.5.A11',
        'name': 'Vermeidung von Leitungen mit gefährdenden Flüssigkeiten und Gasen',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.3', 'G 0.4']
    },
    {
        'id': 'INF.5.A12',
        'name': 'Schutz vor versehentlicher Beschädigung von Zuleitungen',
        'cia': None,
        'gefahren': ['G 0.3', 'G 0.4', 'G 0.8', 'G 0.10', 'G 0.18']
    },
    {
        'id': 'INF.5.A13',
        'name': 'Schutz vor Schädigung durch Brand und Rauchgase',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.4', 'G 0.29']
    },
    {
        'id': 'INF.5.A14',
        'name': 'Minimierung von Brandgefahren aus Nachbarbereichen',
        'cia': None,
        'gefahren': ['G 0.1']
    },
    {
        'id': 'INF.5.A15',
        'name': 'Blitz- und Überspannungsschutz',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.24', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'INF.5.A16',
        'name': 'Einsatz einer unterbrechungsfreien Stromversorgung',
        'cia': None,
        'gefahren': ['G 0.8', 'G 0.10', 'G 0.18']
    },
    {
        'id': 'INF.5.A17',
        'name': 'Inspektion und Wartung der Infrastruktur',
        'cia': None,
        'gefahren': ['G 0.5', 'G 0.8', 'G 0.10', 'G 0.18', 'G 0.24', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'INF.5.A18',
        'name': 'Lage des Raumes für technische Infrastruktur',
        'cia': 'CA',
        'gefahren': ['G 0.1', 'G 0.2', 'G 0.3', 'G 0.4', 'G 0.5', 'G 0.18']
    },
    {
        'id': 'INF.5.A19',
        'name': 'Redundanz des Raumes für technische Infrastruktur',
        'cia': 'A',
        'gefahren': ['G 0.8', 'G 0.10', 'G 0.27']
    },
    {
        'id': 'INF.5.A20',
        'name': 'Erweiterter Schutz vor Einbruch und Sabotage',
        'cia': 'CIA',
        'gefahren': ['G 0.41', 'G 0.44']
    },
    {
        'id': 'INF.5.A22',
        'name': 'Redundante Auslegung der Stromversorgung',
        'cia': 'A',
        'gefahren': ['G 0.8', 'G 0.10']
    },
    {
        'id': 'INF.5.A23',
        'name': 'Netzersatzanlage',
        'cia': 'A',
        'gefahren': ['G 0.8', 'G 0.24', 'G 0.25', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'INF.5.A24',
        'name': 'Lüftung und Kühlung',
        'cia': 'A',
        'gefahren': ['G 0.2', 'G 0.25', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'INF.5.A25',
        'name': 'Erhöhter Schutz vor Schädigung durch Brand und Rauchgase',
        'cia': 'A',
        'gefahren': ['G 0.1', 'G 0.4', 'G 0.8', 'G 0.10']
    },
    {
        'id': 'INF.5.A26',
        'name': 'Überwachung der Energieversorgung',
        'cia': 'A',
        'gefahren': ['G 0.8', 'G 0.10', 'G 0.18', 'G 0.24', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'INF.6.A1',
        'name': 'Handfeuerlöscher',
        'cia': None,
        'gefahren': ['G 0.1']
    },
    {
        'id': 'INF.6.A2',
        'name': 'Zutrittsregelung und -kontrolle',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.44']
    },
    {
        'id': 'INF.6.A3',
        'name': 'Schutz vor Staub und anderer Verschmutzung',
        'cia': None,
        'gefahren': ['G 0.4', 'G 0.18']
    },
    {
        'id': 'INF.6.A4',
        'name': 'Geschlossene Fenster und abgeschlossene Türen',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.4', 'G 0.44']
    },
    {
        'id': 'INF.6.A5',
        'name': 'Verwendung von Schutzschränken',
        'cia': None,
        'gefahren': ['G 0.3', 'G 0.16']
    },
    {
        'id': 'INF.6.A6',
        'name': 'Vermeidung von wasserführenden Leitungen',
        'cia': None,
        'gefahren': ['G 0.3', 'G 0.18']
    },
    {
        'id': 'INF.6.A7',
        'name': 'Einhaltung von klimatischen Bedingungen',
        'cia': None,
        'gefahren': ['G 0.2', 'G 0.18']
    },
    {
        'id': 'INF.6.A8',
        'name': 'Sichere Türen und Fenster',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.3', 'G 0.44']
    },
    {
        'id': 'INF.6.A9',
        'name': 'Gefahrenmeldeanlage',
        'cia': 'CIA',
        'gefahren': ['G 0.1', 'G 0.3', 'G 0.18', 'G 0.44']
    },
    {
        'id': 'INF.7.A1',
        'name': 'Geeignete Auswahl und Nutzung eines Büroraumes',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.44']
    },
    {
        'id': 'INF.7.A2',
        'name': 'Geschlossene Fenster und abgeschlossene Türen',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.14', 'G 0.16', 'G 0.18', 'G 0.30', 'G 0.44']
    },
    {
        'id': 'INF.7.A3',
        'name': 'Fliegende Verkabelung',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.7.A5',
        'name': 'Ergonomischer Arbeitsplatz',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.29', 'G 0.33']
    },
    {
        'id': 'INF.7.A6',
        'name': 'Aufgeräumter Arbeitsplatz',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.18', 'G 0.19']
    },
    {
        'id': 'INF.7.A7',
        'name': 'Geeignete Aufbewahrung dienstlicher Unterlagen und Datenträger',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.30']
    },
    {
        'id': 'INF.7.A8',
        'name': 'Einsatz von Diebstahlsicherungen',
        'cia': 'CIA',
        'gefahren': ['G 0.16']
    },
    {
        'id': 'INF.8.A1',
        'name': 'Sichern von dienstlichen Unterlagen am häuslichen Arbeitsplatz',
        'cia': None,
        'gefahren': ['G 0.16', 'G 0.19', 'G 0.30']
    },
    {
        'id': 'INF.8.A2',
        'name': 'Transport von Arbeitsmaterial zum häuslichen Arbeitsplatz',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.17', 'G 0.18', 'G 0.19', 'G 0.22']
    },
    {
        'id': 'INF.8.A3',
        'name': 'Schutz vor unbefugtem Zutritt am häuslichen Arbeitsplatz',
        'cia': None,
        'gefahren': ['G 0.16', 'G 0.18', 'G 0.19', 'G 0.30', 'G 0.44']
    },
    {
        'id': 'INF.8.A4',
        'name': 'Geeignete Einrichtung des häuslichen Arbeitsplatzes',
        'cia': None,
        'gefahren': ['G 0.16', 'G 0.19', 'G 0.33', 'G 0.44']
    },
    {
        'id': 'INF.8.A5',
        'name': 'Entsorgung von vertraulichen Informationen am häuslichen Arbeitsplatz',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19']
    },
    {
        'id': 'INF.8.A6',
        'name': 'Umgang mit dienstlichen Unterlagen bei erhöhtem Schutzbedarf am häuslichen Arbeitsplatz',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.18', 'G 0.19', 'G 0.22', 'G 0.44']
    },
    {
        'id': 'INF.9.A1',
        'name': 'Geeignete Auswahl und Nutzung eines mobilen Arbeitsplatzes',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.9.A2',
        'name': 'Regelungen für mobile Arbeitsplätze',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.37']
    },
    {
        'id': 'INF.9.A3',
        'name': 'Zutritts- und Zugriffsschutz',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.30', 'G 0.44', 'G 0.46']
    },
    {
        'id': 'INF.9.A4',
        'name': 'Arbeiten mit fremden IT-Systemen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.31']
    },
    {
        'id': 'INF.9.A5',
        'name': 'Zeitnahe Verlustmeldung',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19']
    },
    {
        'id': 'INF.9.A6',
        'name': 'Entsorgung von vertraulichen Informationen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19']
    },
    {
        'id': 'INF.9.A7',
        'name': 'Rechtliche Rahmenbedingungen für das mobile Arbeiten',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'INF.9.A8',
        'name': 'Sicherheitsrichtlinie für mobile Arbeitsplätze',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'INF.9.A9',
        'name': 'Verschlüsselung tragbarer IT-Systeme und Datenträger',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.19', 'G 0.22']
    },
    {
        'id': 'INF.9.A10',
        'name': 'Einsatz von Diebstahlsicherungen',
        'cia': 'CIA',
        'gefahren': ['G 0.16', 'G 0.18']
    },
    {
        'id': 'INF.9.A11',
        'name': 'Verbot der Nutzung unsicherer Umgebungen',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'INF.9.A12',
        'name': 'Nutzung eines Bildschirmschutzes',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19']
    },
    {
        'id': 'ISMS.1.A1',
        'name': 'Übernahme der Gesamtverantwortung für Informationssicherheit durch die Leitung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'ISMS.1.A2',
        'name': 'Festlegung der Sicherheitsziele und -strategie',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'ISMS.1.A3',
        'name': 'Erstellung einer Leitlinie zur Informationssicherheit',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'ISMS.1.A4',
        'name': 'Benennung eines oder einer Informationssicherheitsbeauftragten',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'ISMS.1.A5',
        'name': 'Vertragsgestaltung bei Bestellung eines oder einer externen Informationssicherheitsbeauftragten',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'ISMS.1.A6',
        'name': 'Aufbau einer geeigneten Organisationsstruktur für Informationssicherheit',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'ISMS.1.A7',
        'name': 'Festlegung von Sicherheitsmaßnahmen',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'ISMS.1.A8',
        'name': 'Integration der Mitarbeitenden in den Sicherheitsprozess',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'ISMS.1.A9',
        'name': 'Integration der Informationssicherheit in organisationsweite Abläufe und Prozesse',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'ISMS.1.A10',
        'name': 'Erstellung eines Sicherheitskonzepts',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'ISMS.1.A11',
        'name': 'Aufrechterhaltung der Informationssicherheit',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'ISMS.1.A12',
        'name': 'Management-Berichte zur Informationssicherheit',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'ISMS.1.A13',
        'name': 'Dokumentation des Sicherheitsprozesses',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'ISMS.1.A15',
        'name': 'Wirtschaftlicher Einsatz von Ressourcen für Informationssicherheit',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'ISMS.1.A16',
        'name': 'Erstellung von zielgruppengerechten Sicherheitsrichtlinien',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'ISMS.1.A17',
        'name': 'Abschließen von Versicherungen',
        'cia': 'A',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.1.1.A1',
        'name': 'Sicherheitsrichtlinie für das Netz',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'NET.1.1.A2',
        'name': 'Dokumentation des Netzes',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'NET.1.1.A3',
        'name': 'Anforderungsspezifikation für das Netz',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'NET.1.1.A4',
        'name': 'Netztrennung in Zonen',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.1.A5',
        'name': 'Client-Server-Segmentierung',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.1.A6',
        'name': 'Endgeräte-Segmentierung im internen Netz',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.1.A7',
        'name': 'Absicherung von schützenswerten Informationen',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'NET.1.1.A8',
        'name': 'Grundlegende Absicherung des Internetzugangs',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'NET.1.1.A9',
        'name': 'Grundlegende Absicherung der Kommunikation mit nicht vertrauenswürdigen Netzen',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.46']
    },
    {
        'id': 'NET.1.1.A10',
        'name': 'DMZ-Segmentierung für Zugriffe aus dem Internet',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.1.A11',
        'name': 'Absicherung eingehender Kommunikation vom Internet in das interne Netz',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.29', 'G 0.30', 'G 0.40', 'G 0.43']
    },
    {
        'id': 'NET.1.1.A12',
        'name': 'Absicherung ausgehender interner Kommunikation zum Internet',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'NET.1.1.A13',
        'name': 'Netzplanung',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.1.1.A14',
        'name': 'Umsetzung der Netzplanung',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.11', 'G 0.18', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.27', 'G 0.29', 'G 0.30', 'G 0.40']
    },
    {
        'id': 'NET.1.1.A15',
        'name': 'Regelmäßiger Soll-Ist-Vergleich',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'NET.1.1.A16',
        'name': 'Spezifikation der Netzarchitektur',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'NET.1.1.A17',
        'name': 'Spezifikation des Netzdesigns',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'NET.1.1.A18',
        'name': 'P-A-P-Struktur für die Internet-Anbindung',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.1.A19',
        'name': 'Separierung der Infrastrukturdienste',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.1.A20',
        'name': 'Zuweisung dedizierter Subnetze für IPv4/IPv6-Endgerätegruppen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'NET.1.1.A21',
        'name': 'Separierung des Management-Bereichs',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.22', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'NET.1.1.A22',
        'name': 'Spezifikation des Segmentierungskonzepts',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.1.A23',
        'name': 'Trennung von Netzsegmenten',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30', 'G 0.40']
    },
    {
        'id': 'NET.1.1.A24',
        'name': 'Sichere logische Trennung mittels VLAN',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.1.A25',
        'name': 'Fein- und Umsetzungsplanung von Netzarchitektur und -design',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.11', 'G 0.18', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.27', 'G 0.29', 'G 0.30', 'G 0.40']
    },
    {
        'id': 'NET.1.1.A26',
        'name': 'Spezifikation von Betriebsprozessen für das Netz',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'NET.1.1.A27',
        'name': 'Einbindung der Netzarchitektur in die Notfallplanung',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'NET.1.1.A28',
        'name': 'Hochverfügbare Netz- und Sicherheitskomponenten',
        'cia': 'A',
        'gefahren': ['G 0.25']
    },
    {
        'id': 'NET.1.1.A29',
        'name': 'Hochverfügbare Realisierung von Netzanbindungen',
        'cia': 'A',
        'gefahren': ['G 0.9', 'G 0.11', 'G 0.25', 'G 0.40']
    },
    {
        'id': 'NET.1.1.A30',
        'name': 'Schutz vor Distributed-Denial-of-Service',
        'cia': 'A',
        'gefahren': ['G 0.9', 'G 0.11', 'G 0.40']
    },
    {
        'id': 'NET.1.1.A31',
        'name': 'Physische Trennung von Netzsegmenten',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.1.A32',
        'name': 'Physische Trennung von Management-Netzsegmenten',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.1.A33',
        'name': 'Mikrosegmentierung des Netzes',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.1.A34',
        'name': 'Einsatz kryptografischer Verfahren auf Netzebene',
        'cia': 'CI',
        'gefahren': ['G 0.15', 'G 0.43']
    },
    {
        'id': 'NET.1.1.A35',
        'name': 'Einsatz von netzbasiertem DLP',
        'cia': 'CI',
        'gefahren': ['G 0.19']
    },
    {
        'id': 'NET.1.1.A36',
        'name': 'Trennung mittels VLAN bei sehr hohem Schutzbedarf',
        'cia': 'CIA',
        'gefahren': ['G 0.29']
    },
    {
        'id': 'NET.1.2.A1',
        'name': 'Planung des Netzmanagements',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.1.2.A2',
        'name': 'Anforderungsspezifikation für das Netzmanagement',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'NET.1.2.A6',
        'name': 'Regelmäßige Datensicherung',
        'cia': None,
        'gefahren': ['G 0.45']
    },
    {
        'id': 'NET.1.2.A7',
        'name': 'Grundlegende Protokollierung von Ereignissen',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.37']
    },
    {
        'id': 'NET.1.2.A8',
        'name': 'Zeit-Synchronisation',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.37']
    },
    {
        'id': 'NET.1.2.A9',
        'name': 'Absicherung der Netzmanagement-Kommunikation und des Zugriffs auf Netz-Management-Werkzeuge',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.30', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'NET.1.2.A10',
        'name': 'Beschränkung der SNMP-Kommunikation',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'NET.1.2.A11',
        'name': 'Festlegung einer Sicherheitsrichtlinie für das Netzmanagement',
        'cia': None,
        'gefahren': ['G 0.30']
    },
    {
        'id': 'NET.1.2.A12',
        'name': 'Ist-Aufnahme und Dokumentation des Netzmanagements',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'NET.1.2.A13',
        'name': 'Erstellung eines Netzmanagement-Konzepts',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'NET.1.2.A14',
        'name': 'Fein- und Umsetzungsplanung',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.19', 'G 0.23', 'G 0.25', 'G 0.27', 'G 0.29', 'G 0.30']
    },
    {
        'id': 'NET.1.2.A15',
        'name': 'Konzept für den sicheren Betrieb der Netzmanagement-Infrastruktur',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'NET.1.2.A16',
        'name': 'Einrichtung und Konfiguration von Netzmanagement-Lösungen',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.25', 'G 0.29', 'G 0.30']
    },
    {
        'id': 'NET.1.2.A17',
        'name': 'Regelmäßiger Soll-Ist-Vergleich im Rahmen des Netzmanagements',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'NET.1.2.A18',
        'name': 'Schulungen für Management-Lösungen',
        'cia': None,
        'gefahren': ['G 0.26', 'G 0.29', 'G 0.31']
    },
    {
        'id': 'NET.1.2.A21',
        'name': 'Entkopplung der Netzmanagement-Kommunikation',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'NET.1.2.A22',
        'name': 'Beschränkung der Management-Funktionen',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'NET.1.2.A24',
        'name': 'Zentrale Konfigurationsverwaltung für Netzkomponenten',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.31']
    },
    {
        'id': 'NET.1.2.A25',
        'name': 'Statusüberwachung der Netzkomponenten',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'NET.1.2.A26',
        'name': 'Alarming und Logging',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.37']
    },
    {
        'id': 'NET.1.2.A27',
        'name': 'Einbindung des Netzmanagements in die Notfallplanung',
        'cia': None,
        'gefahren': ['G 0.25']
    },
    {
        'id': 'NET.1.2.A28',
        'name': 'Platzierung der Management-Clients für das In-Band-Management',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.2.A29',
        'name': 'Einsatz von VLANs im Management-Netz',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.2.A30',
        'name': 'Hochverfügbare Realisierung der Management-Lösung',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.40']
    },
    {
        'id': 'NET.1.2.A31',
        'name': 'Grundsätzliche Nutzung von sicheren Protokollen',
        'cia': 'IA',
        'gefahren': ['G 0.15', 'G 0.22', 'G 0.30', 'G 0.46']
    },
    {
        'id': 'NET.1.2.A32',
        'name': 'Physische Trennung des Managementnetzes',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.2.A33',
        'name': 'Physische Trennung von Management-Segmenten',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.2.A35',
        'name': 'Festlegungen zur Beweissicherung',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.29', 'G 0.30', 'G 0.40', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'NET.1.2.A36',
        'name': 'Einbindung der Protokollierung des Netzmanagements in eine SIEM-Lösung',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.29', 'G 0.30', 'G 0.40', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'NET.1.2.A37',
        'name': 'Standortübergreifende Zeitsynchronisation',
        'cia': 'CI',
        'gefahren': ['G 0.29', 'G 0.35']
    },
    {
        'id': 'NET.1.2.A38',
        'name': 'Festlegung von Notbetriebsformen für die Netzmanagement-Infrastruktur',
        'cia': 'A',
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.40', 'G 0.45']
    },
    {
        'id': 'NET.2.1.A1',
        'name': 'Festlegung einer Strategie für den Einsatz von WLANs',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.2.1.A2',
        'name': 'Auswahl eines geeigneten WLAN-Standards',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.15', 'G 0.18', 'G 0.23', 'G 0.30', 'G 0.43']
    },
    {
        'id': 'NET.2.1.A3',
        'name': 'Auswahl geeigneter Kryptoverfahren für WLAN',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.23', 'G 0.30', 'G 0.43']
    },
    {
        'id': 'NET.2.1.A4',
        'name': 'Geeignete Aufstellung von Access Points',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.16', 'G 0.24', 'G 0.25']
    },
    {
        'id': 'NET.2.1.A5',
        'name': 'Sichere Basis-Konfiguration der Access Points',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.23', 'G 0.30', 'G 0.43']
    },
    {
        'id': 'NET.2.1.A6',
        'name': 'Sichere Konfiguration der WLAN-Infrastruktur',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'NET.2.1.A7',
        'name': 'Aufbau eines Distribution Systems',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23']
    },
    {
        'id': 'NET.2.1.A8',
        'name': 'Verhaltensregeln bei WLAN-Sicherheitsvorfällen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30']
    },
    {
        'id': 'NET.2.1.A9',
        'name': 'Sichere Anbindung von WLANs an ein LAN',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'NET.2.1.A10',
        'name': 'Erstellung einer Sicherheitsrichtlinie für den Betrieb von WLANs',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.2.1.A11',
        'name': 'Geeignete Auswahl von WLAN-Komponenten',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.2.1.A12',
        'name': 'Einsatz einer geeigneten WLAN-Management-Lösung',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.2.1.A13',
        'name': 'Regelmäßige Sicherheitschecks in WLANs',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.27', 'G 0.30', 'G 0.40', 'G 0.43']
    },
    {
        'id': 'NET.2.1.A14',
        'name': 'Regelmäßige Audits der WLAN-Komponenten',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23']
    },
    {
        'id': 'NET.2.1.A15',
        'name': 'Verwendung eines VPN zur Absicherung von WLANs',
        'cia': 'CI',
        'gefahren': ['G 0.15', 'G 0.43']
    },
    {
        'id': 'NET.2.1.A16',
        'name': 'Zusätzliche Absicherung bei der Anbindung von WLANs an ein LAN',
        'cia': 'CIA',
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'NET.2.1.A17',
        'name': 'Absicherung der Kommunikation zwischen Access Points',
        'cia': 'C',
        'gefahren': ['G 0.15', 'G 0.23']
    },
    {
        'id': 'NET.2.1.A18',
        'name': 'Einsatz von Wireless Intrusion Detection/Wireless Intrusion Prevention Systemen',
        'cia': 'CIA',
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.43']
    },
    {
        'id': 'NET.2.2.A1',
        'name': 'Erstellung einer Nutzungsrichtlinie für WLAN',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.31', 'G 0.43']
    },
    {
        'id': 'NET.2.2.A2',
        'name': 'Sensibilisierung und Schulung der WLAN-Benutzenden',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.2.2.A3',
        'name': 'Absicherung der WLAN-Nutzung an Hotspots',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.23', 'G 0.43']
    },
    {
        'id': 'NET.2.2.A4',
        'name': 'Verhaltensregeln bei WLAN-Sicherheitsvorfällen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23']
    },
    {
        'id': 'NET.3.1.A1',
        'name': 'Sichere Grundkonfiguration eines Routers oder Switches',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.22', 'G 0.23', 'G 0.26', 'G 0.30']
    },
    {
        'id': 'NET.3.1.A4',
        'name': 'Schutz der Administrationsschnittstellen',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'NET.3.1.A5',
        'name': 'Schutz vor Fragmentierungsangriffen',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.25', 'G 0.27', 'G 0.40']
    },
    {
        'id': 'NET.3.1.A6',
        'name': 'Notfallzugriff auf Router und Switches',
        'cia': None,
        'gefahren': ['G 0.27']
    },
    {
        'id': 'NET.3.1.A7',
        'name': 'Protokollierung bei Routern und Switches',
        'cia': None,
        'gefahren': ['G 0.37']
    },
    {
        'id': 'NET.3.1.A8',
        'name': 'Regelmäßige Datensicherung',
        'cia': None,
        'gefahren': ['G 0.27', 'G 0.45']
    },
    {
        'id': 'NET.3.1.A9',
        'name': 'Betriebsdokumentationen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19']
    },
    {
        'id': 'NET.3.1.A10',
        'name': 'Erstellung einer Sicherheitsrichtlinie',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.1.A11',
        'name': 'Beschaffung eines Routers oder Switches',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.1.A12',
        'name': 'Erstellung einer Konfigurations-Checkliste für Router und Switches',
        'cia': None,
        'gefahren': ['G 0.31']
    },
    {
        'id': 'NET.3.1.A13',
        'name': 'Administration über ein gesondertes Managementnetz',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.23', 'G 0.30', 'G 0.46']
    },
    {
        'id': 'NET.3.1.A14',
        'name': 'Schutz vor Missbrauch von ICMP-Nachrichten',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.40']
    },
    {
        'id': 'NET.3.1.A15',
        'name': 'Bogon- und Spoofing-Filterung',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'NET.3.1.A16',
        'name': 'Schutz vor "IPv6 Routing Header Type-0"-Angriffen',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.23', 'G 0.25', 'G 0.40']
    },
    {
        'id': 'NET.3.1.A17',
        'name': 'Schutz vor DoS- und DDoS-Angriffen',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.25', 'G 0.40']
    },
    {
        'id': 'NET.3.1.A18',
        'name': 'Einrichtung von Access Control Lists',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'NET.3.1.A19',
        'name': 'Sicherung von Switch-Ports',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.30']
    },
    {
        'id': 'NET.3.1.A20',
        'name': 'Sicherheitsaspekte von Routing-Protokollen',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'NET.3.1.A21',
        'name': 'Identitäts- und Berechtigungsmanagement in der Netzinfrastruktur',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'NET.3.1.A22',
        'name': 'Notfallvorsorge bei Routern und Switches',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'NET.3.1.A23',
        'name': 'Revision und Penetrationstests',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.1.A24',
        'name': 'Einsatz von Netzzugangskontrollen',
        'cia': 'IA',
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'NET.3.1.A25',
        'name': 'Erweiterter Integritätsschutz für die Konfigurationsdateien',
        'cia': 'I',
        'gefahren': ['G 0.22', 'G 0.23', 'G 0.30', 'G 0.46']
    },
    {
        'id': 'NET.3.1.A26',
        'name': 'Hochverfügbarkeit',
        'cia': 'A',
        'gefahren': ['G 0.23', 'G 0.27']
    },
    {
        'id': 'NET.3.1.A27',
        'name': 'Bandbreitenmanagement für kritische Anwendungen und Dienste',
        'cia': 'A',
        'gefahren': ['G 0.27']
    },
    {
        'id': 'NET.3.1.A28',
        'name': 'Einsatz von zertifizierten Produkten',
        'cia': 'CI',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.2.A1',
        'name': 'Erstellung einer Sicherheitsrichtlinie',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.2.A2',
        'name': 'Festlegen der Firewall-Regeln',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23']
    },
    {
        'id': 'NET.3.2.A3',
        'name': 'Einrichten geeigneter Filterregeln am Paketfilter',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.40', 'G 0.43']
    },
    {
        'id': 'NET.3.2.A4',
        'name': 'Sichere Konfiguration der Firewall',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.46']
    },
    {
        'id': 'NET.3.2.A6',
        'name': 'Schutz der Administrationsschnittstellen',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'NET.3.2.A7',
        'name': 'Notfallzugriff auf die Firewall',
        'cia': None,
        'gefahren': ['G 0.27']
    },
    {
        'id': 'NET.3.2.A8',
        'name': 'Unterbindung von dynamischem Routing',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.23', 'G 0.43']
    },
    {
        'id': 'NET.3.2.A9',
        'name': 'Protokollierung',
        'cia': None,
        'gefahren': ['G 0.37']
    },
    {
        'id': 'NET.3.2.A10',
        'name': 'Abwehr von Fragmentierungsangriffen am Paketfilter',
        'cia': None,
        'gefahren': ['G 0.41', 'G 0.43']
    },
    {
        'id': 'NET.3.2.A14',
        'name': 'Betriebsdokumentationen',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.2.A15',
        'name': 'Beschaffung einer Firewall',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.20']
    },
    {
        'id': 'NET.3.2.A16',
        'name': 'Aufbau einer "P-A-P"-Struktur',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.40']
    },
    {
        'id': 'NET.3.2.A17',
        'name': 'Deaktivierung von IPv4 oder IPv6',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'NET.3.2.A18',
        'name': 'Administration über ein gesondertes Managementnetz',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'NET.3.2.A19',
        'name': 'Schutz vor TCP SYN Flooding',
        'cia': None,
        'gefahren': ['G 0.40', 'G 0.41']
    },
    {
        'id': 'NET.3.2.A20',
        'name': 'Absicherung von grundlegenden Internetprotokollen',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'NET.3.2.A21',
        'name': 'Temporäre Entschlüsselung des Datenverkehrs',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.29', 'G 0.39']
    },
    {
        'id': 'NET.3.2.A22',
        'name': 'Sichere Zeitsynchronisation',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'NET.3.2.A23',
        'name': 'Systemüberwachung und -Auswertung',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.18', 'G 0.25', 'G 0.27']
    },
    {
        'id': 'NET.3.2.A24',
        'name': 'Revision und Penetrationstests',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.2.A25',
        'name': 'Erweiterter Integritätsschutz für die Konfigurationsdateien',
        'cia': 'I',
        'gefahren': ['G 0.22', 'G 0.23', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'NET.3.2.A26',
        'name': 'Auslagerung von funktionalen Erweiterungen auf dedizierte Hardware',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.27']
    },
    {
        'id': 'NET.3.2.A27',
        'name': 'Einsatz verschiedener Firewall-Betriebssysteme und -Produkte in einer mehrstufigen Firewall-Architektur',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.26']
    },
    {
        'id': 'NET.3.2.A28',
        'name': 'Zentrale Filterung von aktiven Inhalten',
        'cia': 'CI',
        'gefahren': ['G 0.39']
    },
    {
        'id': 'NET.3.2.A29',
        'name': 'Einsatz von Hochverfügbarkeitslösungen',
        'cia': 'A',
        'gefahren': ['G 0.9', 'G 0.18', 'G 0.25', 'G 0.27']
    },
    {
        'id': 'NET.3.2.A30',
        'name': 'Bandbreitenmanagement für kritische Anwendungen und Dienste',
        'cia': 'A',
        'gefahren': ['G 0.27']
    },
    {
        'id': 'NET.3.2.A31',
        'name': 'Einsatz von zertifizierten Produkten',
        'cia': 'CI',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.2.A32',
        'name': 'Notfallvorsorge für die Firewall',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.18', 'G 0.27']
    },
    {
        'id': 'NET.3.3.A1',
        'name': 'Planung des VPN-Einsatzes',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.32']
    },
    {
        'id': 'NET.3.3.A2',
        'name': 'Auswahl von VPN-Dienstleistenden',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18']
    },
    {
        'id': 'NET.3.3.A3',
        'name': 'Sichere Installatin vn VPN-Endgeräten',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.18']
    },
    {
        'id': 'NET.3.3.A4',
        'name': 'Sichere Knfiguratin eines VPN',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.3.A5',
        'name': 'Sperrung nicht mehr benötigter VPN-Zugänge',
        'cia': None,
        'gefahren': ['G 0.30', 'G 0.32']
    },
    {
        'id': 'NET.3.3.A6',
        'name': 'Durchführung einer VPN-Anfrderungsanalyse',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.3.A7',
        'name': 'Planung der technischen VPN-Realisierung',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.3.A8',
        'name': 'Erstellung einer Sicherheitsrichtlinie zur VPN-Nutzung',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.3.A9',
        'name': 'Geeignete Auswahl vn VPN-Prdukten',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.3.A10',
        'name': 'Sicherer Betrieb eines VPN',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.3.A11',
        'name': 'Sichere Anbindung eines externen Netzes',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'NET.3.3.A12',
        'name': 'Konten- und Zugriffsverwaltung bei Fernzugriff-VPNs',
        'cia': None,
        'gefahren': ['G 0.30', 'G 0.32']
    },
    {
        'id': 'NET.3.3.A13',
        'name': 'Integratin vn VPN-Kmpnenten in eine Firewall',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.4.A1',
        'name': 'Begründete Entscheidung für den Einsatz von NAC',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.32', 'G 0.36']
    },
    {
        'id': 'NET.3.4.A2',
        'name': 'Planung des Einsatzes von NAC',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.27', 'G 0.31', 'G 0.32', 'G 0.36', 'G 0.38', 'G 0.39']
    },
    {
        'id': 'NET.3.4.A3',
        'name': 'Erstellung eines Anforderungskatalogs für NAC',
        'cia': None,
        'gefahren': ['G 0.26', 'G 0.27', 'G 0.31', 'G 0.36', 'G 0.38', 'G 0.39']
    },
    {
        'id': 'NET.3.4.A4',
        'name': 'Erstellung eines NAC-Konzepts',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.32', 'G 0.38']
    },
    {
        'id': 'NET.3.4.A5',
        'name': 'Anpassung von Prozessen für Endgeräte bezüglich NAC',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.36']
    },
    {
        'id': 'NET.3.4.A6',
        'name': 'Festlegung von Notfallprozessen für NAC',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.27', 'G 0.31']
    },
    {
        'id': 'NET.3.4.A7',
        'name': 'Nutzung sicherer Authentisierungsverfahren',
        'cia': None,
        'gefahren': ['G 0.36']
    },
    {
        'id': 'NET.3.4.A8',
        'name': 'Festlegung der NAC-spezifischen Rollen und Berechtigungen für den RADIUS-Server',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.38']
    },
    {
        'id': 'NET.3.4.A9',
        'name': 'Festlegung eines angepassten NAC-Regelwerks',
        'cia': None,
        'gefahren': ['G 0.32', 'G 0.36', 'G 0.39']
    },
    {
        'id': 'NET.3.4.A10',
        'name': 'Sichere Nutzung von Identitäten',
        'cia': None,
        'gefahren': ['G 0.36']
    },
    {
        'id': 'NET.3.4.A11',
        'name': 'Sichere Konfiguration der NAC-Lösung',
        'cia': None,
        'gefahren': ['G 0.26', 'G 0.32', 'G 0.36', 'G 0.39']
    },
    {
        'id': 'NET.3.4.A12',
        'name': 'Monitoring der NAC-Lösung',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.28', 'G 0.31', 'G 0.32', 'G 0.39']
    },
    {
        'id': 'NET.3.4.A13',
        'name': 'Erstellung von Validierungsvorgaben für die NAC-Konfiguration',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.26', 'G 0.31', 'G 0.39']
    },
    {
        'id': 'NET.3.4.A14',
        'name': 'Umsetzung weiterer Maßnahmen bei Verwendung von MAC-Adress-Authentisierung',
        'cia': None,
        'gefahren': ['G 0.36', 'G 0.43']
    },
    {
        'id': 'NET.3.4.A15',
        'name': 'Anbindung Virenschutz an NAC-Lösung',
        'cia': None,
        'gefahren': ['G 0.39']
    },
    {
        'id': 'NET.3.4.A16',
        'name': 'Protokollierung der Ereignisse',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.27', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.36', 'G 0.38', 'G 0.39']
    },
    {
        'id': 'NET.3.4.A17',
        'name': 'Positionierung des RADIUS-Servers im Management-Bereich',
        'cia': None,
        'gefahren': ['G 0.30', 'G 0.38']
    },
    {
        'id': 'NET.3.4.A18',
        'name': 'Dokumentation der NAC-Lösung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'NET.3.4.A19',
        'name': 'Ordnungsgemäße Verwaltung von Identitäten zur Authentisierung',
        'cia': None,
        'gefahren': ['G 0.36']
    },
    {
        'id': 'NET.3.4.A20',
        'name': 'Einsatz von MACsec',
        'cia': 'CI',
        'gefahren': ['G 0.36', 'G 0.43']
    },
    {
        'id': 'NET.3.4.A21',
        'name': 'Einsatz von Endgerätekonformitätsprüfung',
        'cia': 'C',
        'gefahren': ['G 0.36', 'G 0.39']
    },
    {
        'id': 'NET.3.4.A22',
        'name': 'NAC-Autorisierung mit Mikrosegmenten',
        'cia': 'C',
        'gefahren': ['G 0.30', 'G 0.36', 'G 0.43']
    },
    {
        'id': 'NET.3.4.A23',
        'name': 'Einsatz von autarken RADIUS-Servern für unterschiedliche Netzbereiche und Funktionen',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.26']
    },
    {
        'id': 'NET.3.4.A24',
        'name': 'Nutzung sicherer Protokolle zwischen NAC-Komponenten',
        'cia': 'C',
        'gefahren': ['G 0.30', 'G 0.43']
    },
    {
        'id': 'NET.3.4.A25',
        'name': 'Einbindung der NAC-Lösung in ein Sicherheitsmonitoring',
        'cia': 'A',
        'gefahren': ['G 0.28', 'G 0.31', 'G 0.32', 'G 0.36', 'G 0.38', 'G 0.39']
    },
    {
        'id': 'NET.3.4.A26',
        'name': 'Hochverfügbarkeit der zentralen NAC-Komponenten',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.26']
    },
    {
        'id': 'NET.3.4.A27',
        'name': 'Prüfung der Notwendigkeit für MAC-Adress-Authentisierung',
        'cia': 'I',
        'gefahren': ['G 0.36', 'G 0.43']
    },
    {
        'id': 'NET.4.1.A1',
        'name': 'Anforderungsanalyse und Planung für TK-Anlagen',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18']
    },
    {
        'id': 'NET.4.1.A2',
        'name': 'Auswahl von TK-Diensteanbietenden',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18']
    },
    {
        'id': 'NET.4.1.A5',
        'name': 'Protokollierung bei TK-Anlagen',
        'cia': None,
        'gefahren': ['G 0.37']
    },
    {
        'id': 'NET.4.1.A6',
        'name': 'Erstellung einer Sicherheitsrichtlinie für TK-Anlagen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'NET.4.1.A7',
        'name': 'Geeignete Aufstellung der TK-Anlage',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.30']
    },
    {
        'id': 'NET.4.1.A8',
        'name': 'Einschränkung und Sperrung nicht benötigter oder sicherheitskritischer Leistungsmerkmale',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.31', 'G 0.42']
    },
    {
        'id': 'NET.4.1.A9',
        'name': 'Schulung zur sicheren Nutzung von TK-Anlagen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31', 'G 0.42']
    },
    {
        'id': 'NET.4.1.A10',
        'name': 'Dokumentation und Revision der TK-Anlagenkonfiguration',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.4.1.A11',
        'name': 'Außerbetriebnahme von TK-Anlagen und -geräten',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'NET.4.1.A12',
        'name': 'Datensicherung der Konfigurationsdateien',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.45']
    },
    {
        'id': 'NET.4.1.A13',
        'name': 'Beschaffung von TK-Anlagen',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.18']
    },
    {
        'id': 'NET.4.1.A14',
        'name': 'Notfallvorsorge für TK-Anlagen',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.27']
    },
    {
        'id': 'NET.4.1.A15',
        'name': 'Notrufe bei einem Ausfall der TK-Anlage',
        'cia': None,
        'gefahren': ['G 0.27']
    },
    {
        'id': 'NET.4.1.A16',
        'name': 'Sicherung von Endgeräten in frei zugänglichen Räumen',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.30']
    },
    {
        'id': 'NET.4.1.A17',
        'name': 'Wartung von TK-Anlagen',
        'cia': None,
        'gefahren': ['G 0.30']
    },
    {
        'id': 'NET.4.1.A18',
        'name': 'Erhöhter Zugangsschutz',
        'cia': 'CI',
        'gefahren': ['G 0.21', 'G 0.30']
    },
    {
        'id': 'NET.4.1.A19',
        'name': 'Redundanter Anschluss',
        'cia': 'A',
        'gefahren': ['G 0.9', 'G 0.11', 'G 0.27']
    },
    {
        'id': 'NET.4.2.A1',
        'name': 'Planung des VoIP-Einsatzes',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.4.2.A3',
        'name': 'Sichere Administration und Konfiguration von VoIP-Endgeräten',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.28', 'G 0.30']
    },
    {
        'id': 'NET.4.2.A4',
        'name': 'Einschränkung der Erreichbarkeit über VoIP',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23']
    },
    {
        'id': 'NET.4.2.A5',
        'name': 'Sichere Konfiguration der VoIP-Middleware',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'NET.4.2.A7',
        'name': 'Erstellung einer Sicherheitsrichtlinie für VoIP',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.31']
    },
    {
        'id': 'NET.4.2.A8',
        'name': 'Verschlüsselung von VoIP',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19']
    },
    {
        'id': 'NET.4.2.A9',
        'name': 'Geeignete Auswahl von VoIP-Komponenten',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.4.2.A11',
        'name': 'Sicherer Umgang mit VoIP-Endgeräten',
        'cia': None,
        'gefahren': ['G 0.30', 'G 0.31']
    },
    {
        'id': 'NET.4.2.A12',
        'name': 'Sichere Außerbetriebnahme von VoIP-Komponenten',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'NET.4.2.A13',
        'name': 'Anforderungen an eine Firewall für den Einsatz von VoIP',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.46']
    },
    {
        'id': 'NET.4.2.A14',
        'name': 'Verschlüsselung der Signalisierung',
        'cia': 'CI',
        'gefahren': ['G 0.15', 'G 0.46']
    },
    {
        'id': 'NET.4.2.A15',
        'name': 'Sicherer Medientransport mit SRTP',
        'cia': 'CI',
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.19', 'G 0.46']
    },
    {
        'id': 'NET.4.2.A16',
        'name': 'Trennung des Daten- und VoIP-Netzes',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'NET.4.3.A1',
        'name': 'Geeignete Aufstellung eines Faxgerätes',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.27']
    },
    {
        'id': 'NET.4.3.A2',
        'name': 'Informationen für Mitarbeitende über die Faxnutzung',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.31']
    },
    {
        'id': 'NET.4.3.A3',
        'name': 'Sicherer Betrieb eines Faxservers',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.26', 'G 0.27', 'G 0.31']
    },
    {
        'id': 'NET.4.3.A4',
        'name': 'Erstellung einer Sicherheitsrichtlinie für die Faxnutzung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'NET.4.3.A6',
        'name': 'Beschaffung geeigneter Faxgeräte und Faxserver',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.4.3.A7',
        'name': 'Geeignete Kennzeichnung ausgehender Faxsendungen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.37']
    },
    {
        'id': 'NET.4.3.A8',
        'name': 'Geeignete Entsorgung von Fax-Verbrauchsgütern und -Ersatzteilen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19']
    },
    {
        'id': 'NET.4.3.A9',
        'name': 'Nutzung von Sende- und Empfangsprotokollen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.37']
    },
    {
        'id': 'NET.4.3.A10',
        'name': 'Kontrolle programmierbarer Zieladressen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19']
    },
    {
        'id': 'NET.4.3.A11',
        'name': 'Schutz vor Überlastung des Faxgerätes',
        'cia': 'A',
        'gefahren': ['G 0.27']
    },
    {
        'id': 'NET.4.3.A12',
        'name': 'Sperren bestimmter Quell- und Ziel-Faxnummern',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.30']
    },
    {
        'id': 'NET.4.3.A13',
        'name': 'Festlegung berechtigter Faxbedienenden',
        'cia': 'CIA',
        'gefahren': ['G 0.30', 'G 0.31']
    },
    {
        'id': 'NET.4.3.A14',
        'name': 'Fertigung von Kopien eingehender Faxsendungen',
        'cia': 'A',
        'gefahren': ['G 0.27', 'G 0.45']
    },
    {
        'id': 'NET.4.3.A15',
        'name': 'Ankündigung und Rückversicherung im Umgang mit Faxsendungen',
        'cia': 'CIA',
        'gefahren': ['G 0.16', 'G 0.19', 'G 0.37', 'G 0.45']
    },
    {
        'id': 'OPS.1.1.1.A1',
        'name': 'Festlegung der Aufgaben und Zuständigkeiten des IT-Betriebs',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.1.A2',
        'name': 'Festlegung von Rollen und Berechtigungen für den IT-Betrieb',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'OPS.1.1.1.A3',
        'name': 'Erstellen von Betriebshandbüchern für die betriebene IT',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.1.A4',
        'name': 'Bereitstellen ausreichender Personal- und Sach-Ressourcen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.33']
    },
    {
        'id': 'OPS.1.1.1.A5',
        'name': 'Festlegen von gehärteten Standardkonfigurationen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.25', 'G 0.31']
    },
    {
        'id': 'OPS.1.1.1.A6',
        'name': 'Durchführung des IT-Asset-Managements',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.1.A7',
        'name': 'Sicherstellung eines ordnungsgemäßen IT-Betriebs',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.27', 'G 0.28']
    },
    {
        'id': 'OPS.1.1.1.A8',
        'name': 'Regelmäßiger Soll-Ist-Vergleich',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.1.A9',
        'name': 'Durchführung von IT-Monitoring',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.22', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'OPS.1.1.1.A10',
        'name': 'Führen eines Schwachstelleninventars',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.28']
    },
    {
        'id': 'OPS.1.1.1.A11',
        'name': 'Festlegung und Einhaltung von SLAs',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'OPS.1.1.1.A12',
        'name': 'Spezifikation und Umsetzung klarer Betriebsprozesse',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'OPS.1.1.1.A13',
        'name': 'Absicherung der Betriebsmittel und der Dokumentation',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22']
    },
    {
        'id': 'OPS.1.1.1.A14',
        'name': 'Berücksichtigung der Betreibbarkeit bei Konzeption und Beschaffung',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.1.A15',
        'name': 'Planung und Einsatz von Betriebsmitteln',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.22', 'G 0.23']
    },
    {
        'id': 'OPS.1.1.1.A16',
        'name': 'Schulung des Betriebspersonals',
        'cia': None,
        'gefahren': ['G 0.31']
    },
    {
        'id': 'OPS.1.1.1.A17',
        'name': 'Planung des IT-Betriebs unter besonderer Berücksichtigung von Mangel- und Notsituationen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25']
    },
    {
        'id': 'OPS.1.1.1.A18',
        'name': 'Planung des Einsatzes von Dienstleistern',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'OPS.1.1.1.A19',
        'name': 'Regelungen für Wartungs- und Reparaturarbeiten',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25']
    },
    {
        'id': 'OPS.1.1.1.A20',
        'name': 'Prüfen auf Schwachstellen',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.28']
    },
    {
        'id': 'OPS.1.1.1.A21',
        'name': 'Einbinden der Betriebsmittel in das Sicherheitsmonitoring',
        'cia': 'CIA',
        'gefahren': ['G 0.23', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'OPS.1.1.1.A22',
        'name': 'Automatisierte Tests auf Schwachstellen',
        'cia': 'CIA',
        'gefahren': ['G 0.23', 'G 0.28']
    },
    {
        'id': 'OPS.1.1.1.A23',
        'name': 'Durchführung von Penetrationstests',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.23']
    },
    {
        'id': 'OPS.1.1.1.A24',
        'name': 'Umfassendes Protokollieren der Prozessschritte im IT-Betrieb',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.37']
    },
    {
        'id': 'OPS.1.1.1.A25',
        'name': 'Sicherstellen von autark funktionierenden Betriebsmitteln',
        'cia': 'CIA',
        'gefahren': ['G 0.25']
    },
    {
        'id': 'OPS.1.1.1.A26',
        'name': 'Proaktive Instandhaltung im IT-Betrieb',
        'cia': 'IA',
        'gefahren': ['G 0.25']
    },
    {
        'id': 'OPS.1.1.2.A2',
        'name': 'Vertretungsregelungen',
        'cia': None,
        'gefahren': ['G 0.27', 'G 0.33']
    },
    {
        'id': 'OPS.1.1.2.A4',
        'name': 'Beendigung der Tätigkeit in der IT-Administration',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.32', 'G 0.42']
    },
    {
        'id': 'OPS.1.1.2.A5',
        'name': 'Nachweisbarkeit von administrativen Tätigkeiten',
        'cia': None,
        'gefahren': ['G 0.37']
    },
    {
        'id': 'OPS.1.1.2.A6',
        'name': 'Schutz administrativer Tätigkeiten',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'OPS.1.1.2.A7',
        'name': 'Regelung der IT-Administrationstätigkeit',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.31', 'G 0.32']
    },
    {
        'id': 'OPS.1.1.2.A8',
        'name': 'Administration von Fachanwendungen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'OPS.1.1.2.A11',
        'name': 'Dokumentation von IT-Administrationstätigkeiten',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.37']
    },
    {
        'id': 'OPS.1.1.2.A16',
        'name': 'Erweiterte Sicherheitsmaßnahmen für Administrationszugänge',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'OPS.1.1.2.A17',
        'name': 'IT-Administration im Vier-Augen-Prinzip',
        'cia': 'CI',
        'gefahren': ['G 0.31', 'G 0.32', 'G 0.37']
    },
    {
        'id': 'OPS.1.1.2.A18',
        'name': 'Durchgängige Protokollierung administrativer Tätigkeiten',
        'cia': 'CI',
        'gefahren': ['G 0.22', 'G 0.37']
    },
    {
        'id': 'OPS.1.1.2.A19',
        'name': 'Nutzung hochverfügbarer IT-Administrationswerkzeuge',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.27']
    },
    {
        'id': 'OPS.1.1.2.A21',
        'name': 'Regelung der IT-Administrationsrollen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.31', 'G 0.32']
    },
    {
        'id': 'OPS.1.1.2.A22',
        'name': 'Trennung von administrativen und anderen Tätigkeiten',
        'cia': None,
        'gefahren': ['G 0.31']
    },
    {
        'id': 'OPS.1.1.2.A23',
        'name': 'Rollen- und Berechtigungskonzept für administrative Zugriffe',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'OPS.1.1.2.A24',
        'name': 'Prüfen von Administrationstätigkeiten',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.31', 'G 0.42']
    },
    {
        'id': 'OPS.1.1.2.A25',
        'name': 'Zeitfenster für schwerwiegende Administrationstätigkeiten',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.45']
    },
    {
        'id': 'OPS.1.1.2.A26',
        'name': 'Backup der Konfiguration',
        'cia': None,
        'gefahren': ['G 0.27', 'G 0.45']
    },
    {
        'id': 'OPS.1.1.2.A27',
        'name': 'Ersatz für zentrale IT-Administrationswerkzeuge',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'OPS.1.1.2.A28',
        'name': 'Protokollierung administrativer Tätigkeiten',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.37']
    },
    {
        'id': 'OPS.1.1.2.A29',
        'name': 'Monitoring der IT-Administrationswerkzeuge',
        'cia': 'A',
        'gefahren': ['G 0.18', 'G 0.25']
    },
    {
        'id': 'OPS.1.1.2.A30',
        'name': 'Sicherheitsmonitoring administrativer Tätigkeiten',
        'cia': 'CI',
        'gefahren': ['G 0.18', 'G 0.23']
    },
    {
        'id': 'OPS.1.1.3.A1',
        'name': 'Konzept für das Patch- und Änderungsmanagement',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.3.A2',
        'name': 'Festlegung der Zuständigkeiten',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.3.A3',
        'name': 'Konfiguration von Autoupdate-Mechanismen',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.20', 'G 0.23', 'G 0.25', 'G 0.26', 'G 0.28', 'G 0.39']
    },
    {
        'id': 'OPS.1.1.3.A5',
        'name': 'Umgang mit Änderungsanforderungen',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.3.A6',
        'name': 'Abstimmung von Änderungsanforderungen',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.3.A7',
        'name': 'Integration des Änderungsmanagements in die Geschäftsprozesse',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.3.A8',
        'name': 'Sicherer Einsatz von Werkzeugen für das Patch- und Änderungsmanagement',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.3.A9',
        'name': 'Test- und Abnahmeverfahren für neue Hardware',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.28']
    },
    {
        'id': 'OPS.1.1.3.A10',
        'name': 'Sicherstellung der Integrität und Authentizität von Softwarepaketen',
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.23', 'G 0.28', 'G 0.39', 'G 0.46']
    },
    {
        'id': 'OPS.1.1.3.A11',
        'name': 'Kontinuierliche Dokumentation der Informationsverarbeitung',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.3.A12',
        'name': 'Einsatz von Werkzeugen beim Änderungsmanagement',
        'cia': 'A',
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'OPS.1.1.3.A13',
        'name': 'Erfolgsmessung von Änderungsanforderungen',
        'cia': 'IA',
        'gefahren': ['G 0.18', 'G 0.26']
    },
    {
        'id': 'OPS.1.1.3.A14',
        'name': 'Synchronisierung innerhalb des Änderungsmanagements',
        'cia': 'CIA',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.3.A15',
        'name': 'Regelmäßige Aktualisierung von IT-Systemen und Software',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.25', 'G 0.26', 'G 0.28']
    },
    {
        'id': 'OPS.1.1.4.A1',
        'name': 'Erstellung eines Konzepts für den Schutz vor Schadprogrammen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.39']
    },
    {
        'id': 'OPS.1.1.4.A2',
        'name': 'Nutzung systemspezifischer Schutzmechanismen',
        'cia': None,
        'gefahren': ['G 0.39']
    },
    {
        'id': 'OPS.1.1.4.A3',
        'name': 'Auswahl eines Virenschutzprogrammes',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.20', 'G 0.29', 'G 0.39']
    },
    {
        'id': 'OPS.1.1.4.A5',
        'name': 'Betrieb und Konfiguration von Virenschutzprogrammen',
        'cia': None,
        'gefahren': ['G 0.27', 'G 0.29', 'G 0.30', 'G 0.39']
    },
    {
        'id': 'OPS.1.1.4.A6',
        'name': 'Regelmäßige Aktualisierung der eingesetzten Virenschutzprogramme',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.39']
    },
    {
        'id': 'OPS.1.1.4.A7',
        'name': 'Sensibilisierung und Verpflichtung der Benutzer',
        'cia': None,
        'gefahren': ['G 0.31', 'G 0.39']
    },
    {
        'id': 'OPS.1.1.4.A9',
        'name': 'Meldung von Infektionen mit Schadprogrammen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.39']
    },
    {
        'id': 'OPS.1.1.4.A10',
        'name': 'Nutzung spezieller Analyseumgebungen',
        'cia': 'CIA',
        'gefahren': ['G 0.39']
    },
    {
        'id': 'OPS.1.1.4.A11',
        'name': 'Einsatz mehrerer Scan-Engines',
        'cia': 'CIA',
        'gefahren': ['G 0.39']
    },
    {
        'id': 'OPS.1.1.4.A12',
        'name': 'Einsatz von Datenträgerschleusen',
        'cia': 'CIA',
        'gefahren': ['G 0.39']
    },
    {
        'id': 'OPS.1.1.4.A13',
        'name': 'Umgang mit nicht vertrauenswürdigen Dateien',
        'cia': 'CIA',
        'gefahren': ['G 0.39']
    },
    {
        'id': 'OPS.1.1.4.A14',
        'name': 'Auswahl und Einsatz von Cyber-Sicherheitsprodukten gegen gezielte Angriffe',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.39']
    },
    {
        'id': 'OPS.1.1.5.A1',
        'name': 'Erstellung einer Sicherheitsrichtlinie für die Protokollierung',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.5.A3',
        'name': 'Konfiguration der Protokollierung auf System- und Netzebene',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.37']
    },
    {
        'id': 'OPS.1.1.5.A4',
        'name': 'Zeitsynchronisation der IT-Systeme',
        'cia': None,
        'gefahren': ['G 0.37']
    },
    {
        'id': 'OPS.1.1.5.A5',
        'name': 'Einhaltung rechtlicher Rahmenbedingungen',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.32', 'G 0.38', 'G 0.46']
    },
    {
        'id': 'OPS.1.1.5.A6',
        'name': 'Aufbau einer zentralen Protokollierungsinfrastruktur',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.26', 'G 0.27', 'G 0.37']
    },
    {
        'id': 'OPS.1.1.5.A8',
        'name': 'Archivierung von Protokollierungsdaten',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'OPS.1.1.5.A9',
        'name': 'Bereitstellung von Protokollierungsdaten für die Auswertung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.29', 'G 0.46']
    },
    {
        'id': 'OPS.1.1.5.A10',
        'name': 'Zugriffsschutz für Protokollierungsdaten',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.32']
    },
    {
        'id': 'OPS.1.1.5.A11',
        'name': 'Steigerung des Protokollierungsumfangs',
        'cia': 'CIA',
        'gefahren': ['G 0.29', 'G 0.37']
    },
    {
        'id': 'OPS.1.1.5.A12',
        'name': 'Verschlüsselung der Protokollierungsdaten',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.22', 'G 0.46']
    },
    {
        'id': 'OPS.1.1.5.A13',
        'name': 'Hochverfügbare Protokollierungsinfrastruktur',
        'cia': 'A',
        'gefahren': ['G 0.9', 'G 0.25', 'G 0.27']
    },
    {
        'id': 'OPS.1.1.6.A1',
        'name': 'Planung der Software-Tests',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'OPS.1.1.6.A2',
        'name': 'Durchführung von funktionalen Software-Tests',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26']
    },
    {
        'id': 'OPS.1.1.6.A3',
        'name': 'Auswertung der Testergebnisse',
        'cia': None,
        'gefahren': ['G 0.26']
    },
    {
        'id': 'OPS.1.1.6.A4',
        'name': 'Freigabe der Software',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'OPS.1.1.6.A5',
        'name': 'Durchführung von Software-Tests für nicht funktionale Anforderungen',
        'cia': None,
        'gefahren': ['G 0.27', 'G 0.28']
    },
    {
        'id': 'OPS.1.1.6.A6',
        'name': 'Geordnete Einweisung der Software-Testenden',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.6.A7',
        'name': 'Personalauswahl der Software-Testenden',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.41']
    },
    {
        'id': 'OPS.1.1.6.A10',
        'name': 'Erstellung eines Abnahmeplans',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.6.A11',
        'name': 'Verwendung von anonymisierten oder pseudonymisierten Testdaten',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.38']
    },
    {
        'id': 'OPS.1.1.6.A12',
        'name': 'Durchführung von Regressionstests',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.28']
    },
    {
        'id': 'OPS.1.1.6.A13',
        'name': 'Trennung der Testumgebung von der Produktivumgebung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.25', 'G 0.26', 'G 0.32', 'G 0.38', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'OPS.1.1.6.A14',
        'name': 'Durchführung von Penetrationstests',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'OPS.1.1.6.A15',
        'name': 'Überprüfung der Installation und zugehörigen Dokumentation',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'OPS.1.1.6.A16',
        'name': 'Sicherheitsüberprüfung der Testenden',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.18']
    },
    {
        'id': 'OPS.1.1.7.A1',
        'name': 'Anforderungsspezifikation für das Systemmanagement',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.18', 'G 0.25', 'G 0.26', 'G 0.27', 'G 0.29', 'G 0.30']
    },
    {
        'id': 'OPS.1.1.7.A2',
        'name': 'Planung des Systemmanagements',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.18', 'G 0.25', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'OPS.1.1.7.A3',
        'name': 'Zeitsynchronisation für das Systemmanagement',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'OPS.1.1.7.A4',
        'name': 'Absicherung der Systemmanagement-Kommunikation',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.43']
    },
    {
        'id': 'OPS.1.1.7.A5',
        'name': 'Gegenseitige Authentisierung von Systemmanagement-Lösung und zu verwaltenden Systemen',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.43']
    },
    {
        'id': 'OPS.1.1.7.A6',
        'name': 'Absicherung des Zugriffs auf die Systemmanagement-Lösung',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.31', 'G 0.43']
    },
    {
        'id': 'OPS.1.1.7.A7',
        'name': 'Festlegung einer Sicherheitsrichtlinie für das Systemmanagement',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.31', 'G 0.32']
    },
    {
        'id': 'OPS.1.1.7.A8',
        'name': 'Erstellung eines Systemmanagement-Konzepts',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.27', 'G 0.29', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'OPS.1.1.7.A9',
        'name': 'Fein- und Umsetzungsplanung für das Systemmanagement',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.27', 'G 0.29', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'OPS.1.1.7.A10',
        'name': 'Konzept für den sicheren Betrieb der Systemmanagement-Lösung',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.25', 'G 0.26', 'G 0.27', 'G 0.29', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'OPS.1.1.7.A11',
        'name': 'Regelmäßiger Soll-Ist-Vergleich im Rahmen des Systemmanagements',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.26']
    },
    {
        'id': 'OPS.1.1.7.A12',
        'name': 'Auslösung von Aktionen durch die zentralen Komponenten der Systemmanagement-Lösung',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'OPS.1.1.7.A13',
        'name': 'Verpflichtung zur Nutzung der vorgesehenen Schnittstellen für das Systemmanagement',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.31', 'G 0.43']
    },
    {
        'id': 'OPS.1.1.7.A14',
        'name': 'Zentrale Konfigurationsverwaltung für zu verwaltende Systeme',
        'cia': None,
        'gefahren': ['G 0.45']
    },
    {
        'id': 'OPS.1.1.7.A15',
        'name': 'Statusüberwachung, Protokollierung und Alarmierung bei relevanten Ereignissen im Systemmanagement-Lösung und den zu verwaltenden Systemen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.26', 'G 0.27', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.37']
    },
    {
        'id': 'OPS.1.1.7.A16',
        'name': 'Einbindung des Systemmanagements in die Notfallplanung',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26']
    },
    {
        'id': 'OPS.1.1.7.A17',
        'name': 'Kontrolle der Systemmanagement-Kommunikation',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.31', 'G 0.43']
    },
    {
        'id': 'OPS.1.1.7.A18',
        'name': 'Überprüfung des Systemzustands',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'OPS.1.1.7.A19',
        'name': 'Absicherung der Systemmanagement-Kommunikation zwischen der Systemmanagement-Lösung und den zu verwaltenden Systemen',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.43']
    },
    {
        'id': 'OPS.1.1.7.A20',
        'name': 'Hochverfügbare Realisierung der Systemmanagement-Lösung',
        'cia': 'A',
        'gefahren': ['G 0.9', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'OPS.1.1.7.A21',
        'name': 'Physische Trennung der zentralen Systemmanagementnetze',
        'cia': 'CI',
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.26', 'G 0.30', 'G 0.43']
    },
    {
        'id': 'OPS.1.1.7.A22',
        'name': 'Einbindung des Systemmanagements in automatisierte Detektionssysteme',
        'cia': 'CIA',
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.29', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'OPS.1.1.7.A23',
        'name': 'Standort-übergreifende Zeitsynchronisation für das Systemmanagement',
        'cia': 'CIA',
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'OPS.1.1.7.A24',
        'name': 'Automatisierte Überprüfung von sicherheitsrelevanten Konfigurationen durch geeignete Detektionssysteme',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.45']
    },
    {
        'id': 'OPS.1.1.7.A25',
        'name': 'Protokollierung und Reglementierung von Systemmanagement-Sitzungen',
        'cia': 'CI',
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.23', 'G 0.29', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.37']
    },
    {
        'id': 'OPS.1.1.7.A26',
        'name': 'Entkopplung von Zugriffen auf die Systemmanagement-Lösung',
        'cia': 'CI',
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.43']
    },
    {
        'id': 'OPS.1.2.2.A1',
        'name': 'Ermittlung von Einflussfaktoren für die elektronische Archivierung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.1.2.2.A2',
        'name': 'Entwicklung eines Archivierungskonzepts',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.1.2.2.A3',
        'name': 'Geeignete Aufstellung von Archivsystemen und Lagerung von Archivmedien',
        'cia': None,
        'gefahren': ['G 0.2', 'G 0.4', 'G 0.44']
    },
    {
        'id': 'OPS.1.2.2.A4',
        'name': 'Konsistente Indizierung von Daten bei der Archivierung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.45']
    },
    {
        'id': 'OPS.1.2.2.A5',
        'name': 'Regelmäßige Aufbereitung von archivierten Datenbeständen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.45']
    },
    {
        'id': 'OPS.1.2.2.A6',
        'name': 'Schutz der Integrität der Indexdatenbank von Archivsystemen',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.28', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'OPS.1.2.2.A7',
        'name': 'Regelmäßige Datensicherung der System- und Archivdaten',
        'cia': None,
        'gefahren': ['G 0.45', 'G 0.46']
    },
    {
        'id': 'OPS.1.2.2.A8',
        'name': 'Protokollierung der Archivzugriffe',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.37']
    },
    {
        'id': 'OPS.1.2.2.A9',
        'name': 'Auswahl geeigneter Datenformate für die Archivierung von Dokumenten',
        'cia': None,
        'gefahren': ['G 0.45', 'G 0.46']
    },
    {
        'id': 'OPS.1.2.2.A10',
        'name': 'Erstellung einer Richtlinie für die Nutzung von Archivsystemen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.31']
    },
    {
        'id': 'OPS.1.2.2.A11',
        'name': 'Einweisung in die Administration und Bedienung des Archivsystems',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'OPS.1.2.2.A12',
        'name': 'Überwachung der Speicherressourcen von Archivmedien',
        'cia': None,
        'gefahren': ['G 0.27']
    },
    {
        'id': 'OPS.1.2.2.A13',
        'name': 'Regelmäßige Revision der Archivierungsprozesse',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.2.2.A14',
        'name': 'Regelmäßige Beobachtung des Marktes für Archivsysteme',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.28']
    },
    {
        'id': 'OPS.1.2.2.A15',
        'name': 'Regelmäßige Aufbereitung von kryptografisch gesicherten Daten bei der Archivierung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.45']
    },
    {
        'id': 'OPS.1.2.2.A16',
        'name': 'Regelmäßige Erneuerung technischer Archivsystem-Komponenten',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.46']
    },
    {
        'id': 'OPS.1.2.2.A17',
        'name': 'Auswahl eines geeigneten Archivsystems',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26']
    },
    {
        'id': 'OPS.1.2.2.A18',
        'name': 'Verwendung geeigneter Archivmedien',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28', 'G 0.29', 'G 0.45']
    },
    {
        'id': 'OPS.1.2.2.A19',
        'name': 'Regelmäßige Funktions- und Recoverytests bei der Archivierung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'OPS.1.2.2.A20',
        'name': 'Geeigneter Einsatz kryptografischer Verfahren bei der Archivierung',
        'cia': 'CI',
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.1.2.2.A21',
        'name': 'Übertragung von Papierdaten in elektronische Archive',
        'cia': 'CI',
        'gefahren': ['G 0.45', 'G 0.46']
    },
    {
        'id': 'OPS.1.2.4.A1',
        'name': 'Regelungen für Telearbeit',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'OPS.1.2.4.A2',
        'name': 'Sicherheitstechnische Anforderungen an den Telearbeitsrechner',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.30']
    },
    {
        'id': 'OPS.1.2.4.A5',
        'name': 'Sensibilisierung und Schulung der Mitarbeitenden',
        'cia': None,
        'gefahren': ['G 0.31']
    },
    {
        'id': 'OPS.1.2.4.A6',
        'name': 'Erstellen eines Sicherheitskonzeptes für Telearbeit',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.2.4.A7',
        'name': 'Regelung der Nutzung von Kommunikationsmöglichkeiten bei Telearbeit',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'OPS.1.2.4.A8',
        'name': 'Informationsfluss zwischen Mitarbeitenden und Institution',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.2.4.A9',
        'name': 'Betreuungs- und Wartungskonzept für Telearbeitsplätze',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.27']
    },
    {
        'id': 'OPS.1.2.4.A10',
        'name': 'Durchführung einer Anforderungsanalyse für den Telearbeitsplatz',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.2.5.A1',
        'name': 'Planung des Einsatzes der Fernwartung',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.2.5.A2',
        'name': 'Sicherer Verbindungsaufbau bei der Fernwartung von Clients',
        'cia': None,
        'gefahren': ['G 0.31']
    },
    {
        'id': 'OPS.1.2.5.A3',
        'name': 'Absicherung der Schnittstellen zur Fernwartung',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.25', 'G 0.31']
    },
    {
        'id': 'OPS.1.2.5.A5',
        'name': 'Einsatz von Online-Diensten',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.25']
    },
    {
        'id': 'OPS.1.2.5.A6',
        'name': 'Erstellung einer Richtlinie für die Fernwartung',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.2.5.A7',
        'name': 'Dokumentation bei der Fernwartung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'OPS.1.2.5.A8',
        'name': 'Sichere Protokolle bei der Fernwartung',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22']
    },
    {
        'id': 'OPS.1.2.5.A9',
        'name': 'Auswahl und Beschaffung geeigneter Fernwartungswerkzeuge',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.20']
    },
    {
        'id': 'OPS.1.2.5.A10',
        'name': 'Umgang mit Fernwartungswerkzeugen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.20', 'G 0.37']
    },
    {
        'id': 'OPS.1.2.5.A14',
        'name': 'Dedizierte Clients und Konten bei der Fernwartung',
        'cia': 'CIA',
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.25']
    },
    {
        'id': 'OPS.1.2.5.A17',
        'name': 'Authentisierungsmechanismen bei der Fernwartung',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.21', 'G 0.25']
    },
    {
        'id': 'OPS.1.2.5.A19',
        'name': 'Fernwartung durch Dritte',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.21', 'G 0.39']
    },
    {
        'id': 'OPS.1.2.5.A20',
        'name': 'Betrieb der Fernwartung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.39', 'G 0.40']
    },
    {
        'id': 'OPS.1.2.5.A21',
        'name': 'Erstellung eines Notfallplans für den Ausfall der Fernwartung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30']
    },
    {
        'id': 'OPS.1.2.5.A22',
        'name': 'Redundante Kommunikationsverbindungen',
        'cia': 'A',
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.22', 'G 0.30', 'G 0.37']
    },
    {
        'id': 'OPS.1.2.5.A24',
        'name': 'Absicherung integrierter Fernwartungssysteme',
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.25', 'G 0.31']
    },
    {
        'id': 'OPS.1.2.5.A25',
        'name': 'Entkopplung der Kommunikation bei der Fernwartung',
        'cia': None,
        'gefahren': ['G 0.30']
    },
    {
        'id': 'OPS.1.2.6.A1',
        'name': 'Planung des NTP- Einsatzes',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.2.6.A2',
        'name': 'Sichere Nutzung fremder Zeitquellen',
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.29']
    },
    {
        'id': 'OPS.1.2.6.A3',
        'name': 'Sichere Konfiguration von NTP-Servern',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.30', 'G 0.46']
    },
    {
        'id': 'OPS.1.2.6.A4',
        'name': 'Nichtberücksichtigung unaufgeforderter Zeitinformationen',
        'cia': None,
        'gefahren': ['G 0.22']
    },
    {
        'id': 'OPS.1.2.6.A5',
        'name': 'Nutzung des Client-Server-Modus für NTP',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.27', 'G 0.46']
    },
    {
        'id': 'OPS.1.2.6.A6',
        'name': 'Überwachung von IT-Systemen mit NTP-Nutzung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.22']
    },
    {
        'id': 'OPS.1.2.6.A7',
        'name': 'Sichere Konfiguration von NTP-Clients',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.40', 'G 0.46']
    },
    {
        'id': 'OPS.1.2.6.A8',
        'name': 'Einsatz sicherer Protokolle zur Zeitsynchronisation',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.22', 'G 0.46']
    },
    {
        'id': 'OPS.1.2.6.A9',
        'name': 'Verfügbarkeit ausreichend vieler genauer Zeitquellen',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.27', 'G 0.46']
    },
    {
        'id': 'OPS.1.2.6.A10',
        'name': 'Ausschließlich interne NTP-Server',
        'cia': 'I',
        'gefahren': ['G 0.20', 'G 0.22']
    },
    {
        'id': 'OPS.1.2.6.A11',
        'name': 'Redundante NTP-Server',
        'cia': 'A',
        'gefahren': ['G 0.27']
    },
    {
        'id': 'OPS.1.2.6.A12',
        'name': 'NTP-Server mit authentifizierten Auskünften',
        'cia': 'I',
        'gefahren': ['G 0.20', 'G 0.22']
    },
    {
        'id': 'OPS.2.2.A1',
        'name': 'Erstellung einer Strategie für die Cloud-Nutzung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.2.A2',
        'name': 'Erstellung einer Sicherheitsrichtlinie für die Cloud-Nutzung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.2.A3',
        'name': 'Service-Definition für Cloud-Dienste',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.2.2.A4',
        'name': 'Festlegung von Verantwortungsbereichen und Schnittstellen',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.2.2.A5',
        'name': 'Planung der sicheren Migration zu einem Cloud-Dienst',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.31', 'G 0.36']
    },
    {
        'id': 'OPS.2.2.A6',
        'name': 'Planung der sicheren Einbindung von Cloud-Diensten',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.31']
    },
    {
        'id': 'OPS.2.2.A7',
        'name': 'Erstellung eines Sicherheitskonzeptes für die Cloud-Nutzung',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.25', 'G 0.26', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.45']
    },
    {
        'id': 'OPS.2.2.A8',
        'name': 'Sorgfältige Auswahl von Cloud-Diensteanbietenden',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.2.A9',
        'name': 'Vertragsgestaltung mit den Cloud-Diensteanbietenden',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.2.A10',
        'name': 'Sichere Migration zu einem Cloud-Dienst',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'OPS.2.2.A11',
        'name': 'Erstellung eines Notfallkonzeptes für einen Cloud-Dienst',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.11', 'G 0.25', 'G 0.26', 'G 0.45']
    },
    {
        'id': 'OPS.2.2.A12',
        'name': 'Aufrechterhaltung der Informationssicherheit im laufenden Cloud-Nutzungs-Betrieb',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.2.2.A13',
        'name': 'Nachweis einer ausreichenden Informationssicherheit bei der Cloud-Nutzung',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.19', 'G 0.25', 'G 0.26', 'G 0.29', 'G 0.30', 'G 0.31', 'G 0.32']
    },
    {
        'id': 'OPS.2.2.A14',
        'name': 'Geordnete Beendigung eines Cloud-Nutzungs-Verhältnisses',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.2.2.A15',
        'name': 'Sicherstellung der Portabilität von Cloud-Diensten',
        'cia': 'A',
        'gefahren': ['G 0.11', 'G 0.45']
    },
    {
        'id': 'OPS.2.2.A16',
        'name': 'Durchführung eigener Datensicherungen',
        'cia': 'A',
        'gefahren': ['G 0.11', 'G 0.45']
    },
    {
        'id': 'OPS.2.2.A17',
        'name': 'Einsatz von Verschlüsselung bei Cloud-Nutzung',
        'cia': 'A',
        'gefahren': ['G 0.14', 'G 0.15']
    },
    {
        'id': 'OPS.2.2.A18',
        'name': 'Einsatz von Verbunddiensten',
        'cia': 'CIA',
        'gefahren': ['G 0.30', 'G 0.32']
    },
    {
        'id': 'OPS.2.2.A19',
        'name': 'Sicherheitsüberprüfung von Mitarbeitenden',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.35', 'G 0.41']
    },
    {
        'id': 'OPS.2.3.A1',
        'name': 'Erstellung von Anforderungsprofilen für Prozesse',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A2',
        'name': 'Verfolgung eines risikoorientierten Ansatzes im Auslagerungsmanagement',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A3',
        'name': 'Festlegung von Eignungsanforderungen an Anbietende von Outsourcing',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A4',
        'name': 'Grundanforderungen an Verträge mit Anbietenden von Outsourcing',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'OPS.2.3.A5',
        'name': 'Vereinbarung der Mandantenfähigkeit',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.22', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A6',
        'name': 'Festlegung von Sicherheitsanforderungen und Erstellung eines Sicherheitskonzeptes für das Outsourcing-Vorhaben',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A7',
        'name': 'Regelungen für eine geplante oder ungeplante Beendigung eines Outsourcing-Verhältnisses',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.19']
    },
    {
        'id': 'OPS.2.3.A8',
        'name': 'Erstellung einer Strategie für Outsourcing-Vorhaben',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A9',
        'name': 'Etablierung einer Richtlinie zur Auslagerung',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A10',
        'name': 'Etablierung einer zuständigen Person für das Auslagerungsmanagement',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.29', 'G 0.42']
    },
    {
        'id': 'OPS.2.3.A11',
        'name': 'Führung eines Auslagerungsregisters',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A12',
        'name': 'Erstellung von Auslagerungsberichten',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A13',
        'name': 'Bereitstellung der erforderlichen Kompetenzen bei der Vertragsgestaltung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A14',
        'name': 'Erweiterte Anforderungen an Verträge mit Anbietenden von Outsourcing',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A15',
        'name': 'Anbindung an die Netze der Outsourcing-Partner',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.23']
    },
    {
        'id': 'OPS.2.3.A16',
        'name': 'Prüfung der Anbietenden von Outsourcing',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A17',
        'name': 'Regelungen für den Einsatz des Personals von Anbietenden von Outsourcing',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A18',
        'name': 'Überprüfung der Vereinbarungen mit Anbietenden von Outsourcing',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A19',
        'name': 'Überprüfung der Handlungsalternativen hinsichtlich einer geplanten oder ungeplanten Beendigung eines Outsourcing-Verhältnisses',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18']
    },
    {
        'id': 'OPS.2.3.A20',
        'name': 'Etablierung sowie Einbeziehung von Anbietenden von Outsourcing im Notfallkonzept',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.25', 'G 0.27', 'G 0.42']
    },
    {
        'id': 'OPS.2.3.A21',
        'name': 'Abschluss von ESCROW-Verträgen bei softwarenahen Dienstleistungen',
        'cia': 'IA',
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A22',
        'name': 'Durchführung von gemeinsamen Notfall- und Krisenübungen',
        'cia': 'A',
        'gefahren': ['G 0.11', 'G 0.25', 'G 0.27']
    },
    {
        'id': 'OPS.2.3.A23',
        'name': 'Einsatz von Verschlüsselungen',
        'cia': 'C',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A24',
        'name': 'Sicherheits- und Eignungsüberprüfung von Mitarbeitenden',
        'cia': 'CIA',
        'gefahren': ['G 0.29', 'G 0.35']
    },
    {
        'id': 'OPS.2.3.A25',
        'name': 'Errichtung und Nutzung einer Sandbox für eingehende Daten vom Anbietenden von Outsourcing',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.23', 'G 0.25']
    },
    {
        'id': 'OPS.3.2.A1',
        'name': 'Einhaltung der Schutzziele der Informationssicherheit durch ein Informationssicherheitsmanagement',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A2',
        'name': 'Grundanforderungen an Verträge mit Nutzenden von Outsourcing',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'OPS.3.2.A3',
        'name': 'Weitergabe der vertraglich geregelten Bestimmungen mit Nutzenden von Outsourcing an Sub-Dienstleistende',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A4',
        'name': 'Erstellung eines Mandantentrennungskonzepts',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.22', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A5',
        'name': 'Erstellung eines Sicherheitskonzepts für die Outsourcing-Dienstleistung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A6',
        'name': 'Regelungen für eine geplante und ungeplante Beendigung eines Outsourcing-Verhältnisses',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.19']
    },
    {
        'id': 'OPS.3.2.A7',
        'name': 'Bereitstellung der ausgelagerten Dienstleistung durch multiple Sub-Dienstleistende',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.27', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A8',
        'name': 'Erstellung einer Richtlinie für die Outsourcing-Dienstleistungen',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A9',
        'name': 'Überprüfung der Vereinbarung mit Nutzenden von Outsourcing',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A10',
        'name': 'Etablierung eines sicheren Kommunikationskanals und Festlegung der Kommunikationspartner',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A11',
        'name': 'Etablierung eines Notfallkonzepts',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.25', 'G 0.27', 'G 0.42']
    },
    {
        'id': 'OPS.3.2.A12',
        'name': 'Durchführung einer risikoorientierten Betrachtung von Prozessen, Anwendungen und IT-Systemen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A13',
        'name': 'Anbindung an die Netze der Outsourcing-Partner',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.23']
    },
    {
        'id': 'OPS.3.2.A14',
        'name': 'Überwachung der Prozesse, Anwendungen und IT-Systeme',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.25', 'G 0.27', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A15',
        'name': 'Berichterstattung gegenüber den Nutzenden von Outsourcing',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A16',
        'name': 'Transparenz über die Outsourcing-Kette der ausgelagerten Kundenprozesse',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.27', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A17',
        'name': 'Zutritts-, Zugangs- und Zugriffskontrolle',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.23', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A18',
        'name': 'Regelungen für den Einsatz von Sub-Dienstleistenden',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A19',
        'name': 'Sicherheitsüberprüfung von Beschäftigten',
        'cia': 'CIA',
        'gefahren': ['G 0.29', 'G 0.35']
    },
    {
        'id': 'OPS.3.2.A20',
        'name': 'Verschlüsselte Datenübertragung und -speicherung',
        'cia': 'C',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A21',
        'name': 'Durchführung von gemeinsamen Notfall- und Krisenübungenen',
        'cia': 'A',
        'gefahren': ['G 0.11', 'G 0.25', 'G 0.27']
    },
    {
        'id': 'ORP.1.A1',
        'name': 'Festlegung von Verantwortlichkeiten und Regelungen',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'ORP.1.A2',
        'name': 'Zuweisung der Zuständigkeiten',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'ORP.1.A3',
        'name': 'Beaufsichtigung oder Begleitung von Fremdpersonen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.19', 'G 0.21', 'G 0.30', 'G 0.44']
    },
    {
        'id': 'ORP.1.A4',
        'name': 'Funktionstrennung zwischen unvereinbaren Aufgaben',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.22', 'G 0.29', 'G 0.32']
    },
    {
        'id': 'ORP.1.A8',
        'name': 'Betriebsmittelverwaltung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.27']
    },
    {
        'id': 'ORP.1.A13',
        'name': 'Sicherheit bei Umzügen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.17', 'G 0.18', 'G 0.19', 'G 0.22']
    },
    {
        'id': 'ORP.1.A15',
        'name': 'Ansprechperson zu Informationssicherheitsfragen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'ORP.1.A16',
        'name': 'Richtlinie zur sicheren IT-Nutzung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.29']
    },
    {
        'id': 'ORP.1.A17',
        'name': 'Mitführverbot von Mobiltelefonen',
        'cia': 'C',
        'gefahren': ['G 0.14', 'G 0.15']
    },
    {
        'id': 'ORP.2.A1',
        'name': 'Geregelte Einarbeitung neuer Mitarbeitender',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.31', 'G 0.38']
    },
    {
        'id': 'ORP.2.A2',
        'name': 'Geregelte Verfahrensweise beim Weggang von Mitarbeitenden',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.29', 'G 0.30', 'G 0.33']
    },
    {
        'id': 'ORP.2.A3',
        'name': 'Festlegung von Vertretungsregelungen',
        'cia': None,
        'gefahren': ['G 0.31', 'G 0.33']
    },
    {
        'id': 'ORP.2.A4',
        'name': 'Festlegung von Regelungen für den Einsatz von Fremdpersonal',
        'cia': None,
        'gefahren': ['G 0.17', 'G 0.29', 'G 0.30', 'G 0.44', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'ORP.2.A5',
        'name': 'Vertraulichkeitsvereinbarungen für den Einsatz von Fremdpersonal',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22', 'G 0.29', 'G 0.32', 'G 0.37', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'ORP.2.A7',
        'name': 'Überprüfung der Vertrauenswürdigkeit von Mitarbeitenden',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.29', 'G 0.36', 'G 0.38']
    },
    {
        'id': 'ORP.2.A13',
        'name': 'Sicherheitsüberprüfung',
        'cia': 'C',
        'gefahren': ['G 0.14', 'G 0.29', 'G 0.36', 'G 0.38']
    },
    {
        'id': 'ORP.2.A14',
        'name': 'Aufgaben und Zuständigkeiten von Mitarbeitenden',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.29']
    },
    {
        'id': 'ORP.2.A15',
        'name': 'Qualifikation des Personals',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.29', 'G 0.32', 'G 0.38', 'G 0.42', 'G 0.46']
    },
    {
        'id': 'ORP.3.A1',
        'name': 'Sensibilisierung der Institutionsleitung für Informationssicherheit',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.31']
    },
    {
        'id': 'ORP.3.A3',
        'name': 'Einweisung des Personals in den sicheren Umgang mit IT',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'ORP.3.A4',
        'name': 'Konzeption und Planung eines Sensibilisierungs- und Schulungsprogramms zur Informationssicherheit',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'ORP.3.A6',
        'name': 'Durchführung von Sensibilisierungen und Schulungen zur Informationssicherheit',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.31']
    },
    {
        'id': 'ORP.3.A7',
        'name': 'Schulung zur Vorgehensweise nach IT-Grundschutz',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'ORP.3.A8',
        'name': 'Messung und Auswertung des Lernerfolgs',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'ORP.3.A9',
        'name': 'Spezielle Schulung von exponierten Personen und Institutionen',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.29', 'G 0.31', 'G 0.36', 'G 0.38', 'G 0.42']
    },
    {
        'id': 'ORP.4.A1',
        'name': 'Regelung für die Einrichtung und Löschung von Benutzenden und Benutzendengruppen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.37']
    },
    {
        'id': 'ORP.4.A2',
        'name': 'Einrichtung, Änderung und Entzug von Berechtigungen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30']
    },
    {
        'id': 'ORP.4.A3',
        'name': 'Dokumentation der Benutzendenkennungen und Rechteprofile',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'ORP.4.A4',
        'name': 'Aufgabenverteilung und Funktionstrennung',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.32', 'G 0.37']
    },
    {
        'id': 'ORP.4.A5',
        'name': 'Vergabe von Zutrittsberechtigungen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.44']
    },
    {
        'id': 'ORP.4.A6',
        'name': 'Vergabe von Zugangsberechtigungen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.29', 'G 0.30']
    },
    {
        'id': 'ORP.4.A7',
        'name': 'Vergabe von Zugriffsrechten',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.29', 'G 0.30']
    },
    {
        'id': 'ORP.4.A8',
        'name': 'Regelung des Passwortgebrauchs',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.29']
    },
    {
        'id': 'ORP.4.A9',
        'name': 'Identifikation und Authentisierung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.30', 'G 0.37']
    },
    {
        'id': 'ORP.4.A10',
        'name': 'Schutz von Benutzendenkennungen mit weitreichenden Berechtigungen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.30', 'G 0.36']
    },
    {
        'id': 'ORP.4.A11',
        'name': 'Zurücksetzen von Passwörtern',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.36']
    },
    {
        'id': 'ORP.4.A12',
        'name': 'Entwicklung eines Authentisierungskonzeptes für IT-Systeme und Anwendungen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.18', 'G 0.32', 'G 0.36']
    },
    {
        'id': 'ORP.4.A13',
        'name': 'Geeignete Auswahl von Authentisierungsmechanismen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.22', 'G 0.32', 'G 0.36']
    },
    {
        'id': 'ORP.4.A14',
        'name': 'Kontrolle der Wirksamkeit der Benutzendentrennung am IT-System bzw. an der Anwendung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.37']
    },
    {
        'id': 'ORP.4.A15',
        'name': 'Vorgehensweise und Konzeption der Prozesse beim Identitäts- und Berechtigungsmanagement',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'ORP.4.A16',
        'name': 'Richtlinien für die Zugriffs- und Zugangskontrolle',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'ORP.4.A17',
        'name': 'Geeignete Auswahl von Identitäts- und Berechtigungsmanagement-Systemen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'ORP.4.A18',
        'name': 'Einsatz eines zentralen Authentisierungsdienstes',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.18', 'G 0.36']
    },
    {
        'id': 'ORP.4.A19',
        'name': 'Einweisung aller Mitarbeitenden in den Umgang mit Authentisierungsverfahren und -mechanismen',
        'cia': None,
        'gefahren': ['G 0.31']
    },
    {
        'id': 'ORP.4.A20',
        'name': 'Notfallvorsorge für das Identitäts- und Berechtigungsmanagement-System',
        'cia': 'CIA',
        'gefahren': ['G 0.25']
    },
    {
        'id': 'ORP.4.A21',
        'name': 'Mehr-Faktor-Authentisierung',
        'cia': 'CI',
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.32', 'G 0.36']
    },
    {
        'id': 'ORP.4.A22',
        'name': 'Regelung zur Passwortqualität',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.29']
    },
    {
        'id': 'ORP.4.A23',
        'name': 'Regelung für passwortverarbeitende Anwendungen und IT-Systeme',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.29', 'G 0.30']
    },
    {
        'id': 'ORP.4.A24',
        'name': 'Vier-Augen-Prinzip für administrative Tätigkeiten',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.22', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.37']
    },
    {
        'id': 'ORP.5.A1',
        'name': 'Identifikation der Rahmenbedingungen',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'ORP.5.A2',
        'name': 'Beachtung der Rahmenbedingungen',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'ORP.5.A4',
        'name': 'Konzeption und Organisation des Compliance Managements',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'ORP.5.A5',
        'name': 'Ausnahmegenehmigungen',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'ORP.5.A8',
        'name': 'Regelmäßige Überprüfungen des Compliance Managements',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'SYS.1.1.A1',
        'name': 'Zugriffsschutz  und Nutzung',
        'cia': None,
        'gefahren': ['G 0.16', 'G 0.21']
    },
    {
        'id': 'SYS.1.1.A2',
        'name': 'Authentisierung an Servern',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'SYS.1.1.A5',
        'name': 'Schutz von Schnittstellen',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.23']
    },
    {
        'id': 'SYS.1.1.A6',
        'name': 'Deaktivierung nicht benötigter Dienste',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.23']
    },
    {
        'id': 'SYS.1.1.A9',
        'name': 'Einsatz von Virenschutz-Programmen auf Servern',
        'cia': None,
        'gefahren': ['G 0.39']
    },
    {
        'id': 'SYS.1.1.A10',
        'name': 'Protokollierung',
        'cia': None,
        'gefahren': ['G 0.37']
    },
    {
        'id': 'SYS.1.1.A11',
        'name': 'Festlegung einer Sicherheitsrichtlinie für Server',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'SYS.1.1.A12',
        'name': 'Planung des Server-Einsatzes',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.1.1.A13',
        'name': 'Beschaffung von Servern',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.1.1.A15',
        'name': 'Unterbrechungsfreie und stabile Stromversorgung',
        'cia': None,
        'gefahren': ['G 0.8']
    },
    {
        'id': 'SYS.1.1.A16',
        'name': 'Sichere Installation und Grundkonfiguration von Servern',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'SYS.1.1.A19',
        'name': 'Einrichtung lokaler Paketfilter',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.43']
    },
    {
        'id': 'SYS.1.1.A21',
        'name': 'Betriebsdokumentation für Server',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.22', 'G 0.37', 'G 0.45']
    },
    {
        'id': 'SYS.1.1.A22',
        'name': 'Einbindung in die Notfallplanung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'SYS.1.1.A23',
        'name': 'Systemüberwachung und Monitoring von Servern',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'SYS.1.1.A24',
        'name': 'Sicherheitsprüfungen für Server',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.1.1.A25',
        'name': 'Geregelte Außerbetriebnahme eines Servers',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.27', 'G 0.31']
    },
    {
        'id': 'SYS.1.1.A27',
        'name': 'Hostbasierte Angriffserkennung',
        'cia': 'IA',
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.32', 'G 0.40']
    },
    {
        'id': 'SYS.1.1.A28',
        'name': 'Steigerung der Verfügbarkeit durch Redundanz',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.27']
    },
    {
        'id': 'SYS.1.1.A30',
        'name': 'Ein Dienst pro Server',
        'cia': 'CIA',
        'gefahren': ['G 0.25', 'G 0.28']
    },
    {
        'id': 'SYS.1.1.A31',
        'name': 'Einsatz von Ausführungskontrolle',
        'cia': 'CI',
        'gefahren': ['G 0.23', 'G 0.39']
    },
    {
        'id': 'SYS.1.1.A33',
        'name': 'Aktive Verwaltung der Wurzelzertifikate',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.23']
    },
    {
        'id': 'SYS.1.1.A34',
        'name': 'Festplattenverschlüsselung',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22', 'G 0.46']
    },
    {
        'id': 'SYS.1.1.A35',
        'name': 'Erstellung und Pflege eines Betriebshandbuchs',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.20', 'G 0.27']
    },
    {
        'id': 'SYS.1.1.A36',
        'name': 'Absicherung des Bootvorgangs',
        'cia': 'CIA',
        'gefahren': ['G 0.21']
    },
    {
        'id': 'SYS.1.1.A37',
        'name': 'Kapselung von sicherheitskritischen Anwendungen und Betriebssystemkomponenten',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.31', 'G 0.39', 'G 0.45']
    },
    {
        'id': 'SYS.1.1.A38',
        'name': 'Härtung des Host-Systems mittels Read-Only-Dateisystem',
        'cia': 'I',
        'gefahren': ['G 0.21', 'G 0.28', 'G 0.39', 'G 0.46']
    },
    {
        'id': 'SYS.1.1.A39',
        'name': 'Zentrale Verwaltung der Sicherheitsrichtlinien von Servern',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.23', 'G 0.30', 'G 0.31', 'G 0.32']
    },
    {
        'id': 'SYS.1.2.2.A1',
        'name': 'Planung von Windows Server 2012',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.27', 'G 0.29']
    },
    {
        'id': 'SYS.1.2.2.A2',
        'name': 'Sichere Installation von Windows Server 2012',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.23', 'G 0.28']
    },
    {
        'id': 'SYS.1.2.2.A3',
        'name': 'Sichere Administration von Windows Server 2012',
        'cia': None,
        'gefahren': ['G 0.28', 'G 0.31']
    },
    {
        'id': 'SYS.1.2.2.A4',
        'name': 'Sichere Konfiguration von Windows Server 2012',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.28']
    },
    {
        'id': 'SYS.1.2.2.A5',
        'name': 'Schutz vor Schadsoftware auf Windows Server 2012',
        'cia': None,
        'gefahren': ['G 0.39']
    },
    {
        'id': 'SYS.1.2.2.A6',
        'name': 'Sichere Authentisierung und Autorisierung in Windows Server 2012',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.1.2.2.A8',
        'name': 'Schutz der Systemintegrität',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.23', 'G 0.46']
    },
    {
        'id': 'SYS.1.2.2.A11',
        'name': 'Angriffserkennung bei Windows Server 2012',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.23', 'G 0.37']
    },
    {
        'id': 'SYS.1.2.2.A12',
        'name': 'Redundanz und Hochverfügbarkeit bei Windows Server 2012',
        'cia': 'A',
        'gefahren': ['G 0.27', 'G 0.45']
    },
    {
        'id': 'SYS.1.2.2.A14',
        'name': 'Herunterfahren verschlüsselter Server und virtueller Maschinen',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.22']
    },
    {
        'id': 'SYS.1.2.3.A1',
        'name': 'Planung von Windows Server',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'SYS.1.2.3.A2',
        'name': 'Sichere Installation von Windows Server',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'SYS.1.2.3.A3',
        'name': 'Telemetrie- und Nutzungsdaten unter Windows Server',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.23', 'G 0.29']
    },
    {
        'id': 'SYS.1.2.3.A4',
        'name': 'Schutz vor Ausnutzung von Schwachstellen in Anwendungen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.21', 'G 0.23', 'G 0.28', 'G 0.39']
    },
    {
        'id': 'SYS.1.2.3.A5',
        'name': 'Sichere Authentisierung und Autorisierung in Windows Server',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'SYS.1.2.3.A6',
        'name': 'Sicherheit beim Fernzugriff über RDP',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.23', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'SYS.1.2.3.A7',
        'name': 'Verwendung der Windows PowerShell',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.22', 'G 0.30', 'G 0.31', 'G 0.32']
    },
    {
        'id': 'SYS.1.2.3.A8',
        'name': 'Nutzung des Virtual Secure Mode (VSM)',
        'cia': 'A',
        'gefahren': ['G 0.18', 'G 0.22', 'G 0.29']
    },
    {
        'id': 'SYS.1.3.A2',
        'name': 'Sorgfältige Vergabe von IDs',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.3.A3',
        'name': 'Kein automatisches Einbinden von Wechsellaufwerken',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.23']
    },
    {
        'id': 'SYS.1.3.A4',
        'name': 'Schutz vor Ausnutzung von Schwachstellen in Anwendungen',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.28']
    },
    {
        'id': 'SYS.1.3.A5',
        'name': 'Sichere Installation von Software-Paketen',
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.28']
    },
    {
        'id': 'SYS.1.3.A6',
        'name': 'Verwaltung von Benutzenden und Gruppen',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.31']
    },
    {
        'id': 'SYS.1.3.A8',
        'name': 'Verschlüsselter Zugriff über Secure Shell',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.23', 'G 0.43']
    },
    {
        'id': 'SYS.1.3.A10',
        'name': 'Verhinderung der Ausbreitung bei der Ausnutzung von Schwachstellen',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.28', 'G 0.39']
    },
    {
        'id': 'SYS.1.3.A14',
        'name': 'Verhinderung des Ausspähens von Informationen über das System und über Benutzende',
        'cia': 'C',
        'gefahren': ['G 0.14', 'G 0.30', 'G 0.46']
    },
    {
        'id': 'SYS.1.3.A16',
        'name': 'Zusätzliche Verhinderung der Ausbreitung bei der Ausnutzung von Schwachstellen',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.22', 'G 0.28', 'G 0.32']
    },
    {
        'id': 'SYS.1.3.A17',
        'name': 'Zusätzlicher Schutz des Kernels',
        'cia': 'CI',
        'gefahren': ['G 0.28']
    },
    {
        'id': 'SYS.1.5.A2',
        'name': 'Sicherer Einsatz virtueller IT-Systeme',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.26', 'G 0.27', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32']
    },
    {
        'id': 'SYS.1.5.A3',
        'name': 'Sichere Konfiguration virtueller IT-Systeme',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.21', 'G 0.23', 'G 0.31']
    },
    {
        'id': 'SYS.1.5.A4',
        'name': 'Sichere Konfiguration eines Netzes für virtuelle Infrastrukturen',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.29', 'G 0.30']
    },
    {
        'id': 'SYS.1.5.A5',
        'name': 'Schutz der Administrationsschnittstellen',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.21', 'G 0.23', 'G 0.30', 'G 0.46']
    },
    {
        'id': 'SYS.1.5.A6',
        'name': 'Protokollierung in der virtuellen Infrastruktur',
        'cia': None,
        'gefahren': ['G 0.27', 'G 0.37']
    },
    {
        'id': 'SYS.1.5.A7',
        'name': 'Zeitsynchronisation in virtuellen IT-Systemen',
        'cia': None,
        'gefahren': ['G 0.37']
    },
    {
        'id': 'SYS.1.5.A8',
        'name': 'Planung einer virtuellen Infrastruktur',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.1.5.A9',
        'name': 'Netzplanung für virtuelle Infrastrukturen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'SYS.1.5.A10',
        'name': 'Einführung von Verwaltungsprozessen für virtuelle IT-Systeme',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.1.5.A11',
        'name': 'Administration der Virtualisierungsinfrastruktur über ein gesondertes Managementnetz',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.23', 'G 0.30', 'G 0.46']
    },
    {
        'id': 'SYS.1.5.A12',
        'name': 'Rechte- und Rollenkonzept für die Administration einer virtuellen Infrastruktur',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'SYS.1.5.A13',
        'name': 'Auswahl geeigneter Hardware für Virtualisierungsumgebungen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'SYS.1.5.A14',
        'name': 'Einheitliche Konfigurationsstandards für virtuelle IT-Systeme',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.1.5.A15',
        'name': 'Betrieb von Gast-Betriebssystemen mit unterschiedlichem Schutzbedarf',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.23']
    },
    {
        'id': 'SYS.1.5.A16',
        'name': 'Kapselung der virtuellen Maschinen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.22', 'G 0.23']
    },
    {
        'id': 'SYS.1.5.A17',
        'name': 'Überwachung des Betriebszustands und der Konfiguration der virtuellen Infrastruktur',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'SYS.1.5.A19',
        'name': 'Regelmäßige Audits der Virtualisierungsinfrastruktur',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.1.5.A20',
        'name': 'Verwendung von hochverfügbaren Architekturen',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.27']
    },
    {
        'id': 'SYS.1.5.A21',
        'name': 'Sichere Konfiguration virtueller IT-Systeme bei erhöhtem Schutzbedarf',
        'cia': 'IA',
        'gefahren': ['G 0.26', 'G 0.27']
    },
    {
        'id': 'SYS.1.5.A22',
        'name': 'Härtung des Virtualisierungsservers',
        'cia': 'CI',
        'gefahren': ['G 0.23', 'G 0.28', 'G 0.30']
    },
    {
        'id': 'SYS.1.5.A23',
        'name': 'Rechte-Einschränkung der virtuellen Maschinen',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.1.5.A24',
        'name': 'Deaktivierung von Snapshots virtueller IT-Systeme',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.25', 'G 0.27', 'G 0.31']
    },
    {
        'id': 'SYS.1.5.A25',
        'name': 'Minimale Nutzung von Konsolenzugriffen auf virtuelle IT-Systeme',
        'cia': 'A',
        'gefahren': ['G 0.27', 'G 0.30']
    },
    {
        'id': 'SYS.1.5.A26',
        'name': 'Einsatz einer PKI',
        'cia': 'CIA',
        'gefahren': ['G 0.15', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'SYS.1.5.A27',
        'name': 'Einsatz zertifizierter Virtualisierungssoftware',
        'cia': 'CIA',
        'gefahren': ['G 0.15', 'G 0.20', 'G 0.21', 'G 0.22', 'G 0.23']
    },
    {
        'id': 'SYS.1.5.A28',
        'name': 'Verschlüsselung von virtuellen IT-Systemen',
        'cia': 'C',
        'gefahren': ['G 0.14']
    },
    {
        'id': 'SYS.1.6.A1',
        'name': 'Planung des Container-Einsatzes',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.20', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.24', 'G 0.25', 'G 0.27', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.40', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A2',
        'name': 'Planung der Verwaltung von Containern',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.24', 'G 0.25', 'G 0.27', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A3',
        'name': 'Sicherer Einsatz containerisierter IT-Systeme',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.20', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.24', 'G 0.25', 'G 0.27', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.37', 'G 0.39', 'G 0.40', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A4',
        'name': 'Planung der Bereitstellung und Verteilung von Images',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.20', 'G 0.21', 'G 0.22', 'G 0.25', 'G 0.27', 'G 0.30', 'G 0.31', 'G 0.39']
    },
    {
        'id': 'SYS.1.6.A5',
        'name': 'Separierung der Administrations- und Zugangsnetze bei Containern',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.27', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A6',
        'name': 'Verwendung sicherer Images',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.20', 'G 0.21', 'G 0.23', 'G 0.25', 'G 0.27', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.37', 'G 0.39', 'G 0.40', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A7',
        'name': 'Persistenz von Protokollierungsdaten der Container',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.30', 'G 0.37', 'G 0.45']
    },
    {
        'id': 'SYS.1.6.A8',
        'name': 'Sichere Speicherung von Zugangsdaten bei Containern',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.30', 'G 0.32', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A9',
        'name': 'Eignung für Container-Betrieb',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.20', 'G 0.21', 'G 0.24', 'G 0.27', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.40', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A10',
        'name': 'Richtlinie für Images und Container-Betrieb',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.20', 'G 0.21', 'G 0.23', 'G 0.25', 'G 0.27', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.37', 'G 0.39', 'G 0.40', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A11',
        'name': 'Nur ein Dienst pro Container',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.25']
    },
    {
        'id': 'SYS.1.6.A12',
        'name': 'Verteilung sicherer Images',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.20', 'G 0.21', 'G 0.22', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.37', 'G 0.39', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A13',
        'name': 'Freigabe von Images',
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.21', 'G 0.22', 'G 0.25', 'G 0.27', 'G 0.30', 'G 0.37', 'G 0.39', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A14',
        'name': 'Aktualisierung von Images',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.20', 'G 0.21', 'G 0.25', 'G 0.27', 'G 0.37', 'G 0.39', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A15',
        'name': 'Limitierung der Ressourcen pro Container',
        'cia': None,
        'gefahren': ['G 0.27', 'G 0.28', 'G 0.39', 'G 0.40']
    },
    {
        'id': 'SYS.1.6.A16',
        'name': 'Administrativer Fernzugriff auf Container',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A17',
        'name': 'Ausführung von Containern ohne Privilegien',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A18',
        'name': 'Accounts der Anwendungsdienste',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A19',
        'name': 'Einbinden von Datenspeichern in Container',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.27', 'G 0.39', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A20',
        'name': 'Absicherung von Konfigurationsdaten',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.37']
    },
    {
        'id': 'SYS.1.6.A21',
        'name': 'Erweiterte Sicherheitsrichtlinien',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.27', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.40', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A22',
        'name': 'Vorsorge für Untersuchungen',
        'cia': 'CI',
        'gefahren': ['G 0.18', 'G 0.37']
    },
    {
        'id': 'SYS.1.6.A23',
        'name': 'Unveränderlichkeit der Container',
        'cia': 'I',
        'gefahren': ['G 0.22', 'G 0.28', 'G 0.39', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A24',
        'name': 'Hostbasierte Angriffserkennung',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.40', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A25',
        'name': 'Hochverfügbarkeit von containerisierten Anwendungen',
        'cia': 'A',
        'gefahren': ['G 0.23', 'G 0.24', 'G 0.25', 'G 0.27', 'G 0.40']
    },
    {
        'id': 'SYS.1.6.A26',
        'name': 'Weitergehende Isolation und Kapselung von Containern',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.28', 'G 0.30', 'G 0.39', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A1',
        'name': 'Einsatz restriktiver z/OS-Kennungen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.40', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A2',
        'name': 'Absicherung sicherheitskritischer z/OS-Dienstprogramme',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.40', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A3',
        'name': 'Wartung von Z-Systemen',
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.26', 'G 0.28', 'G 0.30', 'G 0.40', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A4',
        'name': 'Schulung des z/OS-Bedienungspersonals',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.31', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A5',
        'name': 'Einsatz und Sicherung systemnaher z/OS-Terminals',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A6',
        'name': 'Einsatz und Sicherung der Remote Support Facility',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.20', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.36', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A7',
        'name': 'Restriktive Autorisierung unter z/OS',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A8',
        'name': 'Einsatz des z/OS-Sicherheitssystems RACF',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.39', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A9',
        'name': 'Mandantenfähigkeit unter z/OS',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.39', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A11',
        'name': 'Schutz der Session-Daten',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.43']
    },
    {
        'id': 'SYS.1.7.A14',
        'name': 'Berichtswesen zum sicheren Betrieb von z/OS',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.39', 'G 0.40', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A16',
        'name': 'Überwachung von z/OS-Systemen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.26', 'G 0.27', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.39', 'G 0.40', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A17',
        'name': 'Synchronisierung von z/OS-Passwörtern und RACF-Kommandos',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.31', 'G 0.45']
    },
    {
        'id': 'SYS.1.7.A18',
        'name': 'Rollenkonzept für z/OS-Systeme',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.31', 'G 0.33']
    },
    {
        'id': 'SYS.1.7.A19',
        'name': 'Absicherung von z/OS-Transaktionsmonitoren',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A20',
        'name': 'Stilllegung von z/OS-Systemen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.23', 'G 0.26', 'G 0.30', 'G 0.36']
    },
    {
        'id': 'SYS.1.7.A21',
        'name': 'Absicherung des Startvorgangs von z/OS-Systemen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.31', 'G 0.33']
    },
    {
        'id': 'SYS.1.7.A22',
        'name': 'Absicherung der Betriebsfunktionen von z/OS',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.26', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A23',
        'name': 'Absicherung von z/VM',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.20', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.40', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A24',
        'name': 'Datenträgerverwaltung unter z/OS-Systemen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.26', 'G 0.27', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.39', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A25',
        'name': 'Festlegung der Systemdimensionierung von z/OS',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.27', 'G 0.31', 'G 0.45']
    },
    {
        'id': 'SYS.1.7.A26',
        'name': 'WorkLoad Management für z/OS-Systeme',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.26', 'G 0.27', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A27',
        'name': 'Zeichensatzkonvertierung bei z/OS-Systemen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.28', 'G 0.31', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A28',
        'name': 'Lizenzschlüssel-Management für z/OS-Software',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'SYS.1.7.A29',
        'name': 'Absicherung von Unix System Services bei z/OS-Systemen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.26', 'G 0.27', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A30',
        'name': 'Absicherung der z/OS-Trace-Funktionen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.43']
    },
    {
        'id': 'SYS.1.7.A31',
        'name': 'Notfallvorsorge für z/OS-Systeme',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.31', 'G 0.33', 'G 0.40', 'G 0.45']
    },
    {
        'id': 'SYS.1.7.A32',
        'name': 'Festlegung von Standards für z/OS-Systemdefinitionen',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'SYS.1.7.A33',
        'name': 'Trennung von Test- und Produktionssystemen unter z/OS',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.20', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.26', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.39', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A34',
        'name': 'Batch-Job-Planung für z/OS-Systeme',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.26', 'G 0.27', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A35',
        'name': 'Einsatz von RACF-Exits',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.26', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A36',
        'name': 'Interne Kommunikation von Betriebssystemen',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.27', 'G 0.30', 'G 0.36', 'G 0.37', 'G 0.39', 'G 0.40', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A37',
        'name': 'Parallel Sysplex unter z/OS',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.27', 'G 0.40', 'G 0.45']
    },
    {
        'id': 'SYS.1.7.A38',
        'name': 'Einsatz des VTAM Session Management Exit unter z/OS',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.40', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.8.A1',
        'name': 'Geeignete Aufstellung von Speichersystemen',
        'cia': None,
        'gefahren': ['G 0.2', 'G 0.8', 'G 0.16', 'G 0.44']
    },
    {
        'id': 'SYS.1.8.A2',
        'name': 'Sichere Grundkonfiguration von Speicherlösungen',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.23', 'G 0.28', 'G 0.30']
    },
    {
        'id': 'SYS.1.8.A4',
        'name': 'Schutz der Administrationsschnittstellen',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.1.8.A6',
        'name': 'Erstellung einer Sicherheitsrichtlinie für Speicherlösungen',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'SYS.1.8.A7',
        'name': 'Planung von Speicherlösungen',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.1.8.A8',
        'name': 'Auswahl einer geeigneten Speicherlösung',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.1.8.A9',
        'name': 'Auswahl von Liefernden für eine Speicherlösung',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18']
    },
    {
        'id': 'SYS.1.8.A10',
        'name': 'Erstellung und Pflege eines Betriebshandbuchs',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'SYS.1.8.A11',
        'name': 'Sicherer Betrieb einer Speicherlösung',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'SYS.1.8.A13',
        'name': 'Überwachung und Verwaltung von Speicherlösungen',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'SYS.1.8.A14',
        'name': 'Absicherung eines SANs durch Segmentierung',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.27', 'G 0.30']
    },
    {
        'id': 'SYS.1.8.A15',
        'name': 'Sichere Trennung von Mandanten in Speicherlösungen',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.27', 'G 0.30']
    },
    {
        'id': 'SYS.1.8.A16',
        'name': 'Sicheres Löschen in SAN-Umgebungen',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.1.8.A17',
        'name': 'Dokumentation der Systemeinstellungen von Speichersystemen',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'SYS.1.8.A18',
        'name': 'Sicherheitsaudits und Berichtswesen bei Speichersystemen',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'SYS.1.8.A19',
        'name': 'Aussonderung von Speicherlösungen',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.26']
    },
    {
        'id': 'SYS.1.8.A20',
        'name': 'Notfallvorsorge und Notfallreaktion für Speicherlösungen',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.25', 'G 0.45']
    },
    {
        'id': 'SYS.1.8.A21',
        'name': 'Einsatz von Speicherpools zur Trennung von Mandanten',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'SYS.1.8.A22',
        'name': 'Einsatz einer hochverfügbaren SAN-Lösung',
        'cia': 'A',
        'gefahren': ['G 0.25']
    },
    {
        'id': 'SYS.1.8.A23',
        'name': 'Einsatz von Verschlüsselung für Speicherlösungen',
        'cia': 'CI',
        'gefahren': ['G 0.15', 'G 0.46']
    },
    {
        'id': 'SYS.1.8.A24',
        'name': 'Sicherstellung der Integrität der SAN-Fabric',
        'cia': 'I',
        'gefahren': ['G 0.23', 'G 0.46']
    },
    {
        'id': 'SYS.1.8.A25',
        'name': 'Mehrfaches Überschreiben der Daten einer LUN',
        'cia': 'C',
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.1.8.A26',
        'name': 'Absicherung eines SANs durch Hard-Zoning',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'SYS.1.9.A1',
        'name': 'Erstellung einer Sicherheitsrichtlinie für den Einsatz von Terminalservern',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.28']
    },
    {
        'id': 'SYS.1.9.A2',
        'name': 'Planung des Einsatzes von Terminalservern',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.18', 'G 0.27', 'G 0.29', 'G 0.31']
    },
    {
        'id': 'SYS.1.9.A3',
        'name': 'Festlegung der Rollen und Berechtigungen für den Terminalserver',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31', 'G 0.41', 'G 0.43']
    },
    {
        'id': 'SYS.1.9.A4',
        'name': 'Sichere Konfiguration des Terminalservers',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.41', 'G 0.43']
    },
    {
        'id': 'SYS.1.9.A5',
        'name': 'Planung der eingesetzten Clients und Terminal-Client-Software',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22']
    },
    {
        'id': 'SYS.1.9.A6',
        'name': 'Planung der verwendeten Netze',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.18', 'G 0.23', 'G 0.27', 'G 0.31', 'G 0.36', 'G 0.39']
    },
    {
        'id': 'SYS.1.9.A7',
        'name': 'Sicherer Zugriff auf den Terminalserver',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.22', 'G 0.28', 'G 0.36']
    },
    {
        'id': 'SYS.1.9.A8',
        'name': 'Sichere Zuordnung des Terminalservers zu Netzsegmenten',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.39']
    },
    {
        'id': 'SYS.1.9.A9',
        'name': 'Sensibilisierung der Benutzenden',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.27', 'G 0.31']
    },
    {
        'id': 'SYS.1.9.A10',
        'name': 'Einsatz eines zentralen Identitäts- und Berechtigungsmanagements für Terminalserver',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.28']
    },
    {
        'id': 'SYS.1.9.A11',
        'name': 'Sichere Konfiguration von Profilen',
        'cia': None,
        'gefahren': ['G 0.9']
    },
    {
        'id': 'SYS.1.9.A12',
        'name': 'Automatisches Beenden inaktiver Sitzungen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.31']
    },
    {
        'id': 'SYS.1.9.A13',
        'name': 'Protokollierung bei Terminalservern',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.39']
    },
    {
        'id': 'SYS.1.9.A14',
        'name': 'Monitoring des Terminalservers',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.31']
    },
    {
        'id': 'SYS.1.9.A15',
        'name': 'Härtung des Terminalservers',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.43']
    },
    {
        'id': 'SYS.1.9.A16',
        'name': 'Optimierung der Kompression',
        'cia': None,
        'gefahren': ['G 0.9']
    },
    {
        'id': 'SYS.1.9.A17',
        'name': 'Verschlüsselung der Übertragung',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.22', 'G 0.28']
    },
    {
        'id': 'SYS.1.9.A18',
        'name': 'Nutzung von Thin Clients',
        'cia': 'IA',
        'gefahren': ['G 0.14', 'G 0.19']
    },
    {
        'id': 'SYS.1.9.A19',
        'name': 'Erweitertes Monitoring des Terminalservers',
        'cia': 'CIA',
        'gefahren': ['G 0.23', 'G 0.36', 'G 0.39']
    },
    {
        'id': 'SYS.1.9.A20',
        'name': 'Unterschiedliche Terminalserver für unterschiedliche Gruppen von Benutzenden oder Geschäftsprozesse',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.43']
    },
    {
        'id': 'SYS.1.9.A21',
        'name': 'Nutzung hochverfügbarer IT-Systeme',
        'cia': 'A',
        'gefahren': ['G 0.9', 'G 0.41']
    },
    {
        'id': 'SYS.1.9.A22',
        'name': 'Unterbinden des Transfers von Anwendungsdaten zwischen Client und Terminalserver',
        'cia': 'IA',
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.28', 'G 0.41']
    },
    {
        'id': 'SYS.2.1.A1',
        'name': 'Sichere Benutzerauthentisierung',
        'cia': None,
        'gefahren': ['G 0.30']
    },
    {
        'id': 'SYS.2.1.A3',
        'name': 'Aktivieren von Autoupdate-Mechanismen',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'SYS.2.1.A6',
        'name': 'Einsatz von Schutzprogrammen gegen Schadsoftware',
        'cia': None,
        'gefahren': ['G 0.39']
    },
    {
        'id': 'SYS.2.1.A8',
        'name': 'Absicherung des Bootvorgangs',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.30']
    },
    {
        'id': 'SYS.2.1.A9',
        'name': 'Festlegung einer Sicherheitsrichtlinie für Clients',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.2.1.A10',
        'name': 'Planung des Einsatzes von Clients',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.2.1.A11',
        'name': 'Beschaffung von Clients',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.2.1.A13',
        'name': 'Zugriff auf Ausführungsumgebungen mit unbeobachtbarer Codeausführung',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.30']
    },
    {
        'id': 'SYS.2.1.A14',
        'name': 'ENTFALLEN',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'SYS.2.1.A15',
        'name': 'Sichere Installation und Konfiguration von Clients',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.2.1.A16',
        'name': 'Deaktivierung und Deinstallation nicht benötigter Komponenten und Kennungen',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.28', 'G 0.30']
    },
    {
        'id': 'SYS.2.1.A18',
        'name': 'Nutzung von verschlüsselten Kommunikationsverbindungen',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.46']
    },
    {
        'id': 'SYS.2.1.A20',
        'name': 'Schutz der Administrationsverfahren bei Clients',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.21', 'G 0.30']
    },
    {
        'id': 'SYS.2.1.A21',
        'name': 'Verhinderung der unautorisierten Nutzung von Rechnermikrofonen und Kameras',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15']
    },
    {
        'id': 'SYS.2.1.A23',
        'name': 'Bevorzugung von Client-Server-Diensten',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.23', 'G 0.25', 'G 0.31']
    },
    {
        'id': 'SYS.2.1.A24',
        'name': 'Umgang mit externen Medien und Wechseldatenträgern',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.21', 'G 0.23', 'G 0.31', 'G 0.39']
    },
    {
        'id': 'SYS.2.1.A26',
        'name': 'Schutz vor Ausnutzung von Schwachstellen in Anwendungen',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.28']
    },
    {
        'id': 'SYS.2.1.A27',
        'name': 'Geregelte Außerbetriebnahme eines Clients',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.45']
    },
    {
        'id': 'SYS.2.1.A28',
        'name': 'Verschlüsselung der Clients',
        'cia': 'C',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.31']
    },
    {
        'id': 'SYS.2.1.A29',
        'name': 'Systemüberwachung und Monitoring der Clients',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.26']
    },
    {
        'id': 'SYS.2.1.A30',
        'name': 'Einrichten einer Referenzumgebung für Clients',
        'cia': 'CIA',
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.31']
    },
    {
        'id': 'SYS.2.1.A31',
        'name': 'Einrichtung lokaler Paketfilter',
        'cia': 'CIA',
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.40']
    },
    {
        'id': 'SYS.2.1.A32',
        'name': 'Einsatz zusätzlicher Maßnahmen zum Schutz vor Exploits',
        'cia': 'CIA',
        'gefahren': ['G 0.23', 'G 0.28']
    },
    {
        'id': 'SYS.2.1.A33',
        'name': 'Einsatz von Ausführungskontrolle',
        'cia': 'CI',
        'gefahren': ['G 0.23', 'G 0.31', 'G 0.39']
    },
    {
        'id': 'SYS.2.1.A34',
        'name': 'Kapselung von sicherheitskritischen Anwendungen und Betriebssystemkomponenten',
        'cia': 'CIA',
        'gefahren': ['G 0.21', 'G 0.31', 'G 0.39', 'G 0.45']
    },
    {
        'id': 'SYS.2.1.A35',
        'name': 'Aktive Verwaltung der Wurzelzertifikate',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.40']
    },
    {
        'id': 'SYS.2.1.A36',
        'name': 'Selbstverwalteter Einsatz von SecureBoot und TPM',
        'cia': 'CI',
        'gefahren': ['G 0.21']
    },
    {
        'id': 'SYS.2.1.A37',
        'name': 'Verwendung von Mehr-Faktor-Authentisierung',
        'cia': 'C',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.30', 'G 0.36']
    },
    {
        'id': 'SYS.2.1.A38',
        'name': 'Einbindung in die Notfallplanung',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.26']
    },
    {
        'id': 'SYS.2.1.A39',
        'name': 'Unterbrechungsfreie und stabile Stromversorgung',
        'cia': 'A',
        'gefahren': ['G 0.8', 'G 0.26']
    },
    {
        'id': 'SYS.2.1.A40',
        'name': 'Betriebsdokumentation',
        'cia': 'A',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.2.1.A41',
        'name': 'Verwendung von Quotas für lokale Datenträger',
        'cia': 'A',
        'gefahren': ['G 0.27']
    },
    {
        'id': 'SYS.2.1.A42',
        'name': 'Nutzung von Cloud- und Online-Funktionen',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.29']
    },
    {
        'id': 'SYS.2.1.A43',
        'name': 'Lokale Sicherheitsrichtlinien für Clients',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'SYS.2.1.A44',
        'name': 'Verwaltung der Sicherheitsrichtlinien von Clients',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'SYS.2.1.A45',
        'name': 'Erweiterte Protokollierung',
        'cia': 'CIA',
        'gefahren': ['G 0.37']
    },
    {
        'id': 'SYS.2.2.3.A1',
        'name': 'Planung des Einsatzes von Cloud-Diensten unter Windows',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'SYS.2.2.3.A2',
        'name': 'Auswahl und Beschaffung einer geeigneten Windows-Version',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'SYS.2.2.3.A4',
        'name': 'Telemetrie und Datenschutzeinstellungen unter Windows 10',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.2.2.3.A5',
        'name': 'Schutz vor Schadsoftware unter Windows',
        'cia': None,
        'gefahren': ['G 0.39']
    },
    {
        'id': 'SYS.2.2.3.A6',
        'name': 'Integration von Online-Konten in das Betriebssystem',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.2.2.3.A9',
        'name': 'Sichere zentrale Authentisierung in Windows-Netzen',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.2.2.3.A12',
        'name': 'Datei- und Freigabeberechtigungen unter Windows',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.30']
    },
    {
        'id': 'SYS.2.2.3.A13',
        'name': 'Einsatz der SmartScreen-Funktion',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.2.2.3.A14',
        'name': 'Einsatz des Sprachassistenten Cortana',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19']
    },
    {
        'id': 'SYS.2.2.3.A15',
        'name': 'Einsatz der Synchronisationsmechanismen unter Windows',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.2.2.3.A16',
        'name': 'Anbindung von Windows an den Microsoft-Store',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.28', 'G 0.29']
    },
    {
        'id': 'SYS.2.2.3.A17',
        'name': 'Keine Speicherung von Daten zur automatischen Anmeldung',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.2.2.3.A18',
        'name': 'Einsatz der Windows-Remoteunterstützung',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.2.2.3.A19',
        'name': 'Sicherheit beim Fernzugriff über RDP',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.2.2.3.A20',
        'name': 'Einsatz der Benutzerkontensteuerung UAC für privilegierte Konten',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.2.2.3.A21',
        'name': 'Einsatz des Encrypting File Systems',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.19']
    },
    {
        'id': 'SYS.2.2.3.A22',
        'name': 'Verwendung der Windows PowerShell',
        'cia': 'CIA',
        'gefahren': ['G 0.22', 'G 0.30']
    },
    {
        'id': 'SYS.2.2.3.A23',
        'name': 'Erweiterter Schutz der Anmeldeinformationen unter Windows',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22']
    },
    {
        'id': 'SYS.2.2.3.A24',
        'name': 'Aktivierung des Last-Access-Zeitstempels',
        'cia': 'A',
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.37']
    },
    {
        'id': 'SYS.2.2.3.A25',
        'name': 'Umgang mit Fernzugriffsfunktionen der „Connected User Experience and Telemetry',
        'cia': 'CI',
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.36', 'G 0.37']
    },
    {
        'id': 'SYS.2.2.3.A26',
        'name': 'Nutzung des Virtual Secure Mode (VSM)',
        'cia': 'A',
        'gefahren': ['G 0.18', 'G 0.22', 'G 0.29']
    },
    {
        'id': 'SYS.2.3.A1',
        'name': 'Authentisierung von Administrierenden und Benutzenden',
        'cia': None,
        'gefahren': ['G 0.31', 'G 0.32', 'G 0.37']
    },
    {
        'id': 'SYS.2.3.A2',
        'name': 'Auswahl einer geeigneten Distribution',
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.28']
    },
    {
        'id': 'SYS.2.3.A4',
        'name': 'Kernel-Aktualisierungen auf unixartigen Systemen',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.28']
    },
    {
        'id': 'SYS.2.3.A5',
        'name': 'Sichere Installation von Software-Paketen',
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.28', 'G 0.31', 'G 0.39']
    },
    {
        'id': 'SYS.2.3.A6',
        'name': 'Kein automatisches Einbinden von Wechsellaufwerken',
        'cia': None,
        'gefahren': ['G 0.28', 'G 0.39']
    },
    {
        'id': 'SYS.2.3.A7',
        'name': 'Restriktive Rechtevergabe auf Dateien und Verzeichnisse',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.21', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'SYS.2.3.A8',
        'name': 'Einsatz von Techniken zur Rechtebeschränkung von Anwendungen',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.21', 'G 0.22', 'G 0.28', 'G 0.30']
    },
    {
        'id': 'SYS.2.3.A9',
        'name': 'Sichere Verwendung von Passwörtern auf der Kommandozeile',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.2.3.A11',
        'name': 'Verhinderung der Überlastung der lokalen Festplatte',
        'cia': None,
        'gefahren': ['G 0.27']
    },
    {
        'id': 'SYS.2.3.A12',
        'name': 'Sicherer Einsatz von Appliances',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.2.3.A14',
        'name': 'Absicherung gegen Nutzung unbefugter Peripheriegeräte',
        'cia': 'CIA',
        'gefahren': ['G 0.23', 'G 0.28', 'G 0.30']
    },
    {
        'id': 'SYS.2.3.A15',
        'name': 'Zusätzlicher Schutz vor der Ausführung unerwünschter Dateien',
        'cia': 'CI',
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.2.3.A17',
        'name': 'Zusätzliche Verhinderung der Ausbreitung bei der Ausnutzung von Schwachstellen',
        'cia': 'CI',
        'gefahren': ['G 0.28']
    },
    {
        'id': 'SYS.2.3.A18',
        'name': 'Zusätzlicher Schutz des Kernels',
        'cia': 'CI',
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.23', 'G 0.28']
    },
    {
        'id': 'SYS.2.3.A19',
        'name': 'Festplatten- oder Dateiverschlüsselung',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.19']
    },
    {
        'id': 'SYS.2.3.A20',
        'name': 'Abschaltung kritischer SysRq-Funktionen',
        'cia': 'CIA',
        'gefahren': ['G 0.30']
    },
    {
        'id': 'SYS.2.4.A1',
        'name': 'Planung des sicheren Einsatzes von macOS',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.2.4.A2',
        'name': 'Nutzung der integrierten Sicherheitsfunktionen von macOS',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.23', 'G 0.39']
    },
    {
        'id': 'SYS.2.4.A3',
        'name': 'Verwendung geeigneter Konten',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.37']
    },
    {
        'id': 'SYS.2.4.A4',
        'name': 'Verwendung einer Festplattenverschlüsselung',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19']
    },
    {
        'id': 'SYS.2.4.A5',
        'name': 'Deaktivierung sicherheitskritischer Funktionen von macOS',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.28', 'G 0.39']
    },
    {
        'id': 'SYS.2.4.A6',
        'name': 'Verwendung aktueller Mac-Hardware',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28', 'G 0.30']
    },
    {
        'id': 'SYS.2.4.A7',
        'name': 'Zwei-Faktor-Authentisierung für Apple-ID',
        'cia': None,
        'gefahren': ['G 0.36']
    },
    {
        'id': 'SYS.2.4.A8',
        'name': 'Keine Nutzung von iCloud für schützenswerte Daten',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.2.4.A9',
        'name': 'Verwendung von zusätzlichen Schutzprogrammen unter macOS',
        'cia': None,
        'gefahren': ['G 0.39']
    },
    {
        'id': 'SYS.2.4.A10',
        'name': 'Aktivierung der Personal Firewall unter macOS',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'SYS.2.4.A11',
        'name': 'Geräteaussonderung von Macs',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.29']
    },
    {
        'id': 'SYS.2.4.A12',
        'name': 'Firmware-Kennwort und Boot-Schutz auf Macs',
        'cia': 'CIA',
        'gefahren': ['G 0.21', 'G 0.30']
    },
    {
        'id': 'SYS.2.5.A1',
        'name': 'Planung des Einsatzes virtueller Clients',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'SYS.2.5.A2',
        'name': 'Planung der verwendeten Netze für virtuelle Clients',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.27', 'G 0.28', 'G 0.30', 'G 0.32', 'G 0.39']
    },
    {
        'id': 'SYS.2.5.A3',
        'name': 'Schutz vor Schadsoftware auf den virtuellen Clients',
        'cia': None,
        'gefahren': ['G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39']
    },
    {
        'id': 'SYS.2.5.A4',
        'name': 'Verwendung einer dedizierten Virtualisierungsinfrastruktur für die virtuellen Clients',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.27', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32']
    },
    {
        'id': 'SYS.2.5.A5',
        'name': 'Zusätzliche Netzsegmentierung für virtuelle Clients',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.28', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'SYS.2.5.A6',
        'name': 'Keine lokale Datenablage auf virtuellen Clients',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.31', 'G 0.45']
    },
    {
        'id': 'SYS.2.5.A7',
        'name': 'Automatische Sperrung von Sitzungen',
        'cia': None,
        'gefahren': ['G 0.27', 'G 0.30']
    },
    {
        'id': 'SYS.2.5.A8',
        'name': 'Härtung der virtuellen Clients',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.39']
    },
    {
        'id': 'SYS.2.5.A9',
        'name': 'Einbindung der virtuellen Clients in das Patch- und Änderungsmanagement',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.28', 'G 0.31', 'G 0.39', 'G 0.45']
    },
    {
        'id': 'SYS.2.5.A10',
        'name': 'Bedarfsgerechte Zuweisung von Ressourcen zu virtuellen Clients und Gruppen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32']
    },
    {
        'id': 'SYS.2.5.A11',
        'name': 'Vermeidung von verschachtelter Virtualisierung auf virtuellen Clients',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.28', 'G 0.31', 'G 0.39']
    },
    {
        'id': 'SYS.2.5.A12',
        'name': 'Sensibilisierung der Benutzenden',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.31', 'G 0.45']
    },
    {
        'id': 'SYS.2.5.A13',
        'name': 'Verhinderung der Kommunikation zwischen virtuellen Clients an einem gemeinsam genutzten virtuellen Switch',
        'cia': 'CI',
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.2.5.A14',
        'name': 'Erweiterte Sicherheitsfunktionen für den Einsatz von virtuellen Clients',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.23']
    },
    {
        'id': 'SYS.2.5.A15',
        'name': 'Monitoring der virtuellen Clients',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.27', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'SYS.2.5.A16',
        'name': 'Erweiterte Protokollierung für virtuelle Clients',
        'cia': 'CIA',
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'SYS.2.5.A17',
        'name': 'Erweitertes Monitoring der virtuellen Clients',
        'cia': 'CIA',
        'gefahren': ['G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39']
    },
    {
        'id': 'SYS.2.5.A18',
        'name': 'Hochverfügbare Bereitstellung der Virtualisierungsinfrastruktur',
        'cia': 'A',
        'gefahren': ['G 0.25']
    },
    {
        'id': 'SYS.2.6.A1',
        'name': 'Planung des Einsatzes einer VDI',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.18', 'G 0.27']
    },
    {
        'id': 'SYS.2.6.A2',
        'name': 'Sichere Installation und Konfiguration der VDI-Komponenten',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.36', 'G 0.45']
    },
    {
        'id': 'SYS.2.6.A3',
        'name': 'Sichere Installation und Konfiguration der virtuellen Clients mithilfe der VDI',
        'cia': None,
        'gefahren': ['G 0.28', 'G 0.31', 'G 0.36']
    },
    {
        'id': 'SYS.2.6.A4',
        'name': 'Netzsegmentierung der VDI-Komponenten',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'SYS.2.6.A5',
        'name': 'Standardisierter Zugriff auf virtuelle Clients',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.28', 'G 0.31']
    },
    {
        'id': 'SYS.2.6.A6',
        'name': 'Verwendung einer dedizierten Infrastruktur für virtuelle VDI-Komponenten',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.27']
    },
    {
        'id': 'SYS.2.6.A7',
        'name': 'Härtung der virtualisierten Clients durch die VDI-Lösung',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.28', 'G 0.36']
    },
    {
        'id': 'SYS.2.6.A8',
        'name': 'Härtung der VDI-Lösung',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.28', 'G 0.31', 'G 0.36']
    },
    {
        'id': 'SYS.2.6.A9',
        'name': 'Einbindung der virtuellen Clients in das Patch- und Änderungsmanagement',
        'cia': None,
        'gefahren': ['G 0.28', 'G 0.31', 'G 0.36', 'G 0.45']
    },
    {
        'id': 'SYS.2.6.A10',
        'name': 'Monitoring von Verfügbarkeit und Nutzungsgrad der VDI',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'SYS.2.6.A11',
        'name': 'Monitoring von sicherheitsrelevanten Ereignissen der VDI',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.36']
    },
    {
        'id': 'SYS.2.6.A12',
        'name': 'Verteilung von virtuellen Clients auf Virtualisierungsservern',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'SYS.2.6.A13',
        'name': 'Verwendung getrennter VDI-Lösungen für unterschiedliche Benutzendengruppen',
        'cia': 'CIA',
        'gefahren': ['G 0.23', 'G 0.36']
    },
    {
        'id': 'SYS.2.6.A14',
        'name': 'Verwendung von nicht-persistenten virtuellen Clients',
        'cia': 'A',
        'gefahren': ['G 0.28', 'G 0.36']
    },
    {
        'id': 'SYS.2.6.A15',
        'name': 'Hochverfügbare Bereitstellung der VDI-Komponenten',
        'cia': 'A',
        'gefahren': ['G 0.9', 'G 0.45']
    },
    {
        'id': 'SYS.2.6.A16',
        'name': 'Integration der VDI in ein SIEM',
        'cia': 'CIA',
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.3.1.A1',
        'name': 'Regelungen zur mobilen Nutzung von Laptops',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'SYS.3.1.A3',
        'name': 'Einsatz von Personal Firewalls',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'SYS.3.1.A6',
        'name': 'Sicherheitsrichtlinien für Laptops',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'SYS.3.1.A7',
        'name': 'Geregelte Übergabe und Rücknahme eines Laptops',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.31']
    },
    {
        'id': 'SYS.3.1.A8',
        'name': 'Sicherer Anschluss von Laptops an Datennetze',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23']
    },
    {
        'id': 'SYS.3.1.A9',
        'name': 'Sicherer Fernzugriff mit Laptops',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.22', 'G 0.43']
    },
    {
        'id': 'SYS.3.1.A10',
        'name': 'Abgleich der Datenbestände von Laptops',
        'cia': None,
        'gefahren': ['G 0.45']
    },
    {
        'id': 'SYS.3.1.A11',
        'name': 'Sicherstellung der Energieversorgung von Laptops',
        'cia': None,
        'gefahren': ['G 0.24', 'G 0.27']
    },
    {
        'id': 'SYS.3.1.A12',
        'name': 'Verlustmeldung für Laptops',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.21']
    },
    {
        'id': 'SYS.3.1.A13',
        'name': 'Verschlüsselung von Laptops',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19']
    },
    {
        'id': 'SYS.3.1.A14',
        'name': 'Geeignete Aufbewahrung von Laptops',
        'cia': None,
        'gefahren': ['G 0.16']
    },
    {
        'id': 'SYS.3.1.A15',
        'name': 'Geeignete Auswahl von Laptops',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.3.1.A16',
        'name': 'Zentrale Administration von Laptops',
        'cia': 'CI',
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'SYS.3.1.A17',
        'name': 'Sammelaufbewahrung von Laptops',
        'cia': 'A',
        'gefahren': ['G 0.4', 'G 0.16']
    },
    {
        'id': 'SYS.3.1.A18',
        'name': 'Einsatz von Diebstahl-Sicherungen',
        'cia': 'CIA',
        'gefahren': ['G 0.16']
    },
    {
        'id': 'SYS.3.2.1.A1',
        'name': 'Festlegung einer Richtlinie für den Einsatz von Smartphones und Tablets',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'SYS.3.2.1.A2',
        'name': 'Festlegung einer Strategie für die Cloud-Nutzung',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'SYS.3.2.1.A3',
        'name': 'Sichere Grundkonfiguration für mobile Geräte',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.31']
    },
    {
        'id': 'SYS.3.2.1.A4',
        'name': 'Verwendung eines Zugriffschutzes',
        'cia': None,
        'gefahren': ['G 0.30']
    },
    {
        'id': 'SYS.3.2.1.A5',
        'name': 'Updates von Betriebssystem und Apps',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'SYS.3.2.1.A6',
        'name': 'Datenschutzeinstellungen und Berechtigungen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.30']
    },
    {
        'id': 'SYS.3.2.1.A7',
        'name': 'Verhaltensregeln bei Sicherheitsvorfällen',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.3.2.1.A8',
        'name': 'Installation von Apps',
        'cia': None,
        'gefahren': ['G 0.28', 'G 0.30', 'G 0.39']
    },
    {
        'id': 'SYS.3.2.1.A9',
        'name': 'Restriktive Nutzung von funktionalen Erweiterungen',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.3.2.1.A10',
        'name': 'Richtlinie für Mitarbeiter zur Benutzung von mobilen Geräten',
        'cia': None,
        'gefahren': ['G 0.16', 'G 0.17', 'G 0.18', 'G 0.30']
    },
    {
        'id': 'SYS.3.2.1.A11',
        'name': 'Verschlüsselung des Speichers',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19']
    },
    {
        'id': 'SYS.3.2.1.A12',
        'name': 'Verwendung nicht personalisierter Gerätenamen',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.3.2.1.A13',
        'name': 'Regelungen zum Screensharing und Casting',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.30']
    },
    {
        'id': 'SYS.3.2.1.A16',
        'name': 'Deaktivierung nicht benutzter Kommunikationsschnittstellen',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.3.2.1.A18',
        'name': 'Verwendung biometrischer Authentisierung',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.36']
    },
    {
        'id': 'SYS.3.2.1.A19',
        'name': 'Verwendung von Sprachassistenten',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19']
    },
    {
        'id': 'SYS.3.2.1.A22',
        'name': 'Einbindung mobiler Geräte in die interne Infrastruktur via VPN',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.22']
    },
    {
        'id': 'SYS.3.2.1.A25',
        'name': 'Nutzung von getrennten Arbeitsumgebungen',
        'cia': 'CI',
        'gefahren': ['G 0.19', 'G 0.31']
    },
    {
        'id': 'SYS.3.2.1.A26',
        'name': 'Nutzung von PIM-Containern',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22']
    },
    {
        'id': 'SYS.3.2.1.A27',
        'name': 'Einsatz besonders abgesicherter Endgeräte',
        'cia': 'CIA',
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.3.2.1.A28',
        'name': 'Verwendung der Filteroption für Webseiten',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.31', 'G 0.39']
    },
    {
        'id': 'SYS.3.2.1.A29',
        'name': 'Verwendung eines institutionsbezogenen APN',
        'cia': 'CIA',
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.36']
    },
    {
        'id': 'SYS.3.2.1.A30',
        'name': 'Einschränkung der App-Installation mittels Allowlist',
        'cia': 'CIA',
        'gefahren': ['G 0.20', 'G 0.30', 'G 0.36']
    },
    {
        'id': 'SYS.3.2.1.A31',
        'name': 'Regelung zu Mobile Payment',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.3.2.1.A32',
        'name': 'MDM Nutzung',
        'cia': None,
        'gefahren': ['G 0.30', 'G 0.31']
    },
    {
        'id': 'SYS.3.2.1.A33',
        'name': 'Auswahl und Installation von Sicherheits-Apps',
        'cia': None,
        'gefahren': ['G 0.31', 'G 0.39']
    },
    {
        'id': 'SYS.3.2.1.A34',
        'name': 'Konfiguration des verwendeten DNS-Servers',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.22']
    },
    {
        'id': 'SYS.3.2.1.A35',
        'name': 'Verwendung einer Firewall',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.23']
    },
    {
        'id': 'SYS.3.2.2.A1',
        'name': 'Festlegung einer Strategie für das Mobile Device Management',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'SYS.3.2.2.A2',
        'name': 'Festlegung erlaubter mobiler Endgeräte',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.3.2.2.A3',
        'name': 'Auswahl eines MDM-Produkts',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.45']
    },
    {
        'id': 'SYS.3.2.2.A4',
        'name': 'Verteilung der Grundkonfiguration auf mobile Endgeräte',
        'cia': None,
        'gefahren': ['G 0.13', 'G 0.14', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.31', 'G 0.36', 'G 0.39']
    },
    {
        'id': 'SYS.3.2.2.A5',
        'name': 'Installation des MDM-Clients',
        'cia': None,
        'gefahren': ['G 0.13', 'G 0.14', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.31', 'G 0.36', 'G 0.39']
    },
    {
        'id': 'SYS.3.2.2.A6',
        'name': 'Protokollierung und Gerätestatus',
        'cia': None,
        'gefahren': ['G 0.30', 'G 0.31', 'G 0.32', 'G 0.37']
    },
    {
        'id': 'SYS.3.2.2.A7',
        'name': 'Auswahl und Freigabe von Apps',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.24', 'G 0.25', 'G 0.29', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.36', 'G 0.39']
    },
    {
        'id': 'SYS.3.2.2.A12',
        'name': 'Absicherung der MDM-Betriebsumgebung',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.32', 'G 0.38']
    },
    {
        'id': 'SYS.3.2.2.A14',
        'name': 'Benutzung externer Reputation-Services für Apps',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.28', 'G 0.30', 'G 0.36', 'G 0.39']
    },
    {
        'id': 'SYS.3.2.2.A17',
        'name': 'Kontrolle der Nutzung von mobilen Endgeräten',
        'cia': 'I',
        'gefahren': ['G 0.29', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.37']
    },
    {
        'id': 'SYS.3.2.2.A19',
        'name': 'Einsatz von Geofencing',
        'cia': 'CI',
        'gefahren': ['G 0.14']
    },
    {
        'id': 'SYS.3.2.2.A20',
        'name': 'Regelmäßige Überprüfung des MDM',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.29', 'G 0.30', 'G 0.31', 'G 0.32']
    },
    {
        'id': 'SYS.3.2.2.A21',
        'name': 'Verwaltung von Zertifikaten',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.18', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.29', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.36', 'G 0.38']
    },
    {
        'id': 'SYS.3.2.2.A22',
        'name': 'Fernlöschung und Außerbetriebnahme von Endgeräten',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.16', 'G 0.17', 'G 0.18', 'G 0.19', 'G 0.24', 'G 0.29', 'G 0.30', 'G 0.36', 'G 0.38']
    },
    {
        'id': 'SYS.3.2.2.A23',
        'name': 'Durchsetzung von Compliance-Anforderungen',
        'cia': 'CI',
        'gefahren': ['G 0.16', 'G 0.21', 'G 0.22', 'G 0.29']
    },
    {
        'id': 'SYS.3.2.3.A1',
        'name': 'Strategie für die iOS-Nutzung',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.29', 'G 0.30', 'G 0.32', 'G 0.37', 'G 0.38', 'G 0.41', 'G 0.46']
    },
    {
        'id': 'SYS.3.2.3.A2',
        'name': 'Planung des Einsatzes von Cloud-Diensten',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.14', 'G 0.19', 'G 0.29', 'G 0.36', 'G 0.38', 'G 0.46']
    },
    {
        'id': 'SYS.3.2.3.A7',
        'name': 'Verhinderung des unautorisierten Löschens von Konfigurationsprofilen',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.32', 'G 0.35', 'G 0.37', 'G 0.38', 'G 0.41', 'G 0.46']
    },
    {
        'id': 'SYS.3.2.3.A12',
        'name': 'Verwendung von Apple-IDs',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.19', 'G 0.32', 'G 0.35', 'G 0.36', 'G 0.37', 'G 0.41', 'G 0.42', 'G 0.46']
    },
    {
        'id': 'SYS.3.2.3.A13',
        'name': 'Verwendung der Konfigurationsoption "Einschränkungen unter iOS"',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.26', 'G 0.28', 'G 0.29', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.38', 'G 0.41', 'G 0.42', 'G 0.46']
    },
    {
        'id': 'SYS.3.2.3.A14',
        'name': 'Verwendung der iCloud-Infrastruktur',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.11', 'G 0.14', 'G 0.16', 'G 0.19', 'G 0.23', 'G 0.29']
    },
    {
        'id': 'SYS.3.2.3.A15',
        'name': 'Verwendung der Continuity-Funktionen',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.19', 'G 0.29', 'G 0.46']
    },
    {
        'id': 'SYS.3.2.3.A17',
        'name': 'Verwendung der Gerätecode-Historie',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.32', 'G 0.36', 'G 0.46']
    },
    {
        'id': 'SYS.3.2.3.A18',
        'name': 'Verwendung der Konfigurationsoption für den Browser Safari',
        'cia': None,
        'gefahren': ['G 0.26', 'G 0.28']
    },
    {
        'id': 'SYS.3.2.3.A21',
        'name': 'Installation von Apps und Einbindung des Apple App Stores',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.25', 'G 0.26', 'G 0.28', 'G 0.32', 'G 0.39', 'G 0.41', 'G 0.46']
    },
    {
        'id': 'SYS.3.2.3.A23',
        'name': 'Verwendung der automatischen Konfigurationsprofillöschung',
        'cia': 'CI',
        'gefahren': ['G 0.11', 'G 0.16', 'G 0.27', 'G 0.30']
    },
    {
        'id': 'SYS.3.2.3.A25',
        'name': 'Verwendung der Konfigurationsoption für AirPrint',
        'cia': 'CI',
        'gefahren': ['G 0.16', 'G 0.19', 'G 0.29', 'G 0.35', 'G 0.46']
    },
    {
        'id': 'SYS.3.2.3.A26',
        'name': 'Keine Verbindung mit Host-Systemen',
        'cia': 'CI',
        'gefahren': ['G 0.11', 'G 0.14', 'G 0.16', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.28', 'G 0.29', 'G 0.30', 'G 0.32', 'G 0.35', 'G 0.36', 'G 0.38', 'G 0.39', 'G 0.41', 'G 0.42', 'G 0.46']
    },
    {
        'id': 'SYS.3.2.4.A2',
        'name': 'Deaktivieren des Entwicklermodus',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.21', 'G 0.32', 'G 0.41', 'G 0.46']
    },
    {
        'id': 'SYS.3.2.4.A3',
        'name': 'Einsatz des Multi-User- und Gäste-Modus',
        'cia': None,
        'gefahren': ['G 0.30', 'G 0.32', 'G 0.38']
    },
    {
        'id': 'SYS.3.2.4.A5',
        'name': 'Erweiterte Sicherheitseinstellungen',
        'cia': None,
        'gefahren': ['G 0.30']
    },
    {
        'id': 'SYS.3.3.A1',
        'name': 'Sicherheitsrichtlinien und Regelungen für die Nutzung von Mobiltelefonen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.22', 'G 0.27', 'G 0.31']
    },
    {
        'id': 'SYS.3.3.A2',
        'name': 'Sperrmaßnahmen bei Verlust eins Mobiltelefons',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.23', 'G 0.29']
    },
    {
        'id': 'SYS.3.3.A3',
        'name': 'Sensibilisierung und Schulung der Mitarbeiter im Umgang mit Mobiltelefonen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.16', 'G 0.19', 'G 0.27', 'G 0.29', 'G 0.31']
    },
    {
        'id': 'SYS.3.3.A4',
        'name': 'Aussonderung und ordnungsgemäße Entsorgung von Mobiltelefonen und darin verwendeter Speicherkarten',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.16', 'G 0.17', 'G 0.19', 'G 0.29']
    },
    {
        'id': 'SYS.3.3.A5',
        'name': 'Nutzung der Sicherheitsmechanismen von Mobiltelefonen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22']
    },
    {
        'id': 'SYS.3.3.A6',
        'name': 'Updates von Mobiltelefonen',
        'cia': None,
        'gefahren': ['G 0.31']
    },
    {
        'id': 'SYS.3.3.A7',
        'name': 'Beschaffung von Mobiltelefonen',
        'cia': None,
        'gefahren': ['G 0.27']
    },
    {
        'id': 'SYS.3.3.A8',
        'name': 'Nutzung drahtloser Schnittstellen von Mobiltelefonen',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.22', 'G 0.23']
    },
    {
        'id': 'SYS.3.3.A9',
        'name': 'Sicherstellung der Energieversorgung von Mobiltelefonen',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.27']
    },
    {
        'id': 'SYS.3.3.A10',
        'name': 'Sichere Datenübertragung über Mobiltelefone',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.22', 'G 0.23']
    },
    {
        'id': 'SYS.3.3.A11',
        'name': 'Ausfallvorsorge bei Mobiltelefonen',
        'cia': None,
        'gefahren': ['G 0.25']
    },
    {
        'id': 'SYS.3.3.A12',
        'name': 'Einrichtung eines Mobiltelefon-Pools',
        'cia': None,
        'gefahren': ['G 0.27']
    },
    {
        'id': 'SYS.3.3.A13',
        'name': 'Schutz vor der Erstellung von Bewegungsprofilen bei der Nutzung von Mobilfunk',
        'cia': 'C',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.29']
    },
    {
        'id': 'SYS.3.3.A14',
        'name': 'Schutz vor Rufnummernermittlung bei der Nutzung von Mobiltelefonen',
        'cia': 'C',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.29']
    },
    {
        'id': 'SYS.3.3.A15',
        'name': 'Schutz vor Abhören der Raumgespräche über Mobiltelefone',
        'cia': 'C',
        'gefahren': ['G 0.14', 'G 0.15']
    },
    {
        'id': 'SYS.4.1.A1',
        'name': 'Planung des Einsatzes von Druckern, Kopierern und Multifunktionsgeräten',
        'cia': None,
        'gefahren': ['G 0.16', 'G 0.18']
    },
    {
        'id': 'SYS.4.1.A2',
        'name': 'Geeignete Aufstellung und Zugriff auf Drucker, Kopierer und Multifunktionsgeräte',
        'cia': None,
        'gefahren': ['G 0.16', 'G 0.19', 'G 0.21']
    },
    {
        'id': 'SYS.4.1.A4',
        'name': 'Erstellung einer Sicherheitsrichtlinie für den Einsatz von Druckern, Kopierern und Multifunktionsgeräten',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30']
    },
    {
        'id': 'SYS.4.1.A5',
        'name': 'Erstellung von Nutzungsrichtlinien für den Umgang mit Druckern, Kopierern und Multifunktionsgeräten',
        'cia': None,
        'gefahren': ['G 0.31']
    },
    {
        'id': 'SYS.4.1.A7',
        'name': 'Beschränkung der administrativen Fernzugriffe auf Drucker, Kopierer und Multifunktionsgeräte',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.4.1.A11',
        'name': 'Einschränkung der Anbindung von Druckern, Kopierern und Multifunktionsgeräten',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.4.1.A14',
        'name': 'Authentisierung und Autorisierung bei Druckern, Kopierern und Multifunktionsgeräten',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.30']
    },
    {
        'id': 'SYS.4.1.A15',
        'name': 'Verschlüsselung von Informationen bei Druckern, Kopierern und Multifunktionsgeräten',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.22']
    },
    {
        'id': 'SYS.4.1.A16',
        'name': 'Notfallvorsorge bei Druckern',
        'cia': 'A',
        'gefahren': ['G 0.25']
    },
    {
        'id': 'SYS.4.1.A17',
        'name': 'Schutz von Nutz- und Metadaten',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.4.1.A18',
        'name': 'Konfiguration von Druckern, Kopierern und Multifunktionsgeräten',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.22']
    },
    {
        'id': 'SYS.4.1.A20',
        'name': 'Erweiterter Schutz von Informationen bei Druckern, Kopierern und Multifunktionsgeräten',
        'cia': 'C',
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.4.1.A21',
        'name': 'Erweiterte Absicherung von Druckern, Kopierern und Multifunktionsgeräten',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.21']
    },
    {
        'id': 'SYS.4.1.A22',
        'name': 'Ordnungsgemäße Entsorgung ausgedruckter Dokumente',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.4.3.A1',
        'name': 'Regelungen zum Umgang mit eingebetteten Systemen',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.31']
    },
    {
        'id': 'SYS.4.3.A2',
        'name': 'Deaktivieren nicht benutzter Schnittstellen und Dienste bei eingebetteten Systemen',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.4.3.A3',
        'name': 'Protokollierung sicherheitsrelevanter Ereignisse bei eingebetteten Systemen',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.26', 'G 0.30', 'G 0.37']
    },
    {
        'id': 'SYS.4.3.A4',
        'name': 'Erstellung von Beschaffungskriterien für eingebettete Systeme',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.20']
    },
    {
        'id': 'SYS.4.3.A5',
        'name': 'Schutz vor schädigenden Umwelteinflüssen bei eingebetteten Systemen',
        'cia': None,
        'gefahren': ['G 0.4', 'G 0.25']
    },
    {
        'id': 'SYS.4.3.A6',
        'name': 'Verhindern von Debugging-Möglichkeiten bei eingebetteten Systemen',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.4.3.A7',
        'name': 'Hardware-Realisierung von Funktionen eingebetteter Systeme',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.23', 'G 0.24']
    },
    {
        'id': 'SYS.4.3.A8',
        'name': 'Einsatz eines sicheren Betriebssystems für eingebettete Systeme',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.20', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.28', 'G 0.46']
    },
    {
        'id': 'SYS.4.3.A9',
        'name': 'Einsatz kryptografischer Prozessoren bzw. Koprozessoren bei eingebetteten Systemen',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.46']
    },
    {
        'id': 'SYS.4.3.A10',
        'name': 'Wiederherstellung von eingebetteten Systemen',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.31']
    },
    {
        'id': 'SYS.4.3.A11',
        'name': 'Sichere Aussonderung eines eingebetteten Systems',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19']
    },
    {
        'id': 'SYS.4.3.A12',
        'name': 'Auswahl einer vertrauenswürdigen Lieferungs- und Logistikkette sowie qualifizierte herstellende Institutionen für eingebettete Systeme',
        'cia': 'CIA',
        'gefahren': ['G 0.4', 'G 0.18', 'G 0.20', 'G 0.21', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'SYS.4.3.A13',
        'name': 'Einsatz eines zertifizierten Betriebssystems',
        'cia': 'CIA',
        'gefahren': ['G 0.15', 'G 0.20', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.28', 'G 0.46']
    },
    {
        'id': 'SYS.4.3.A14',
        'name': 'Abgesicherter und authentisierter Bootprozess bei eingebetteten Systemen',
        'cia': 'CI',
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.30', 'G 0.39']
    },
    {
        'id': 'SYS.4.3.A15',
        'name': 'Speicherschutz bei eingebetteten Systemen',
        'cia': 'CI',
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.39']
    },
    {
        'id': 'SYS.4.3.A16',
        'name': 'Tamper-Schutz bei eingebetteten Systemen',
        'cia': 'CI',
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.24', 'G 0.31']
    },
    {
        'id': 'SYS.4.3.A17',
        'name': 'Automatische Überwachung der Baugruppenfunktion',
        'cia': 'IA',
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.25', 'G 0.26', 'G 0.46']
    },
    {
        'id': 'SYS.4.3.A18',
        'name': 'Widerstandsfähigkeit eingebetteter Systeme gegen Seitenkanalangriffe',
        'cia': 'C',
        'gefahren': ['G 0.15', 'G 0.21', 'G 0.46']
    },
    {
        'id': 'SYS.4.4.A1',
        'name': 'Einsatzkriterien für IoT-Geräte',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.30']
    },
    {
        'id': 'SYS.4.4.A2',
        'name': 'Authentisierung',
        'cia': None,
        'gefahren': ['G 0.30']
    },
    {
        'id': 'SYS.4.4.A5',
        'name': 'Einschränkung des Netzzugriffs',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23']
    },
    {
        'id': 'SYS.4.4.A6',
        'name': 'Aufnahme von IoT-Geräten in die Sicherheitsrichtlinie der Institution',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.4.4.A7',
        'name': 'Planung des Einsatzes von IoT-Geräten',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.4.4.A8',
        'name': 'Beschaffungskriterien für IoT-Geräte',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'SYS.4.4.A9',
        'name': 'Regelung des Einsatzes von IoT-Geräten',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.4.4.A10',
        'name': 'Sichere Installation und Konfiguration von IoT-Geräten',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.30', 'G 0.38', 'G 0.39', 'G 0.40']
    },
    {
        'id': 'SYS.4.4.A11',
        'name': 'Verwendung von verschlüsselter Datenübertragung',
        'cia': None,
        'gefahren': ['G 0.16']
    },
    {
        'id': 'SYS.4.4.A13',
        'name': 'Deaktivierung und Deinstallation nicht benötigter Komponenten',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.28']
    },
    {
        'id': 'SYS.4.4.A15',
        'name': 'Restriktive Rechtevergabe',
        'cia': None,
        'gefahren': ['G 0.30']
    },
    {
        'id': 'SYS.4.4.A16',
        'name': 'Beseitigung von Schadprogrammen auf IoT-Geräten',
        'cia': None,
        'gefahren': ['G 0.39']
    },
    {
        'id': 'SYS.4.4.A17',
        'name': 'Überwachung des Netzverkehrs von IoT-Geräten',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'SYS.4.4.A18',
        'name': 'Protokollierung sicherheitsrelevanter Ereignisse bei IoT-Geräten',
        'cia': None,
        'gefahren': ['G 0.37']
    },
    {
        'id': 'SYS.4.4.A19',
        'name': 'Schutz der Administrationsschnittstellen',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.28', 'G 0.30']
    },
    {
        'id': 'SYS.4.4.A20',
        'name': 'Geregelte Außerbetriebnahme von IoT-Geräten',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.45']
    },
    {
        'id': 'SYS.4.4.A21',
        'name': 'Einsatzumgebung und Stromversorgung',
        'cia': 'I',
        'gefahren': ['G 0.2', 'G 0.4', 'G 0.8', 'G 0.16', 'G 0.18']
    },
    {
        'id': 'SYS.4.4.A22',
        'name': 'Systemüberwachung',
        'cia': 'A',
        'gefahren': ['G 0.18', 'G 0.40']
    },
    {
        'id': 'SYS.4.4.A23',
        'name': 'Auditierung von IoT-Geräten',
        'cia': 'CIA',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.4.4.A24',
        'name': 'Sichere Konfiguration und Nutzung eines eingebetteten Webservers',
        'cia': 'CIA',
        'gefahren': ['G 0.23']
    },
    {
        'id': 'SYS.4.5.A1',
        'name': 'Sensibilisierung zum sicheren Umgang mit Wechseldatenträgern',
        'cia': None,
        'gefahren': ['G 0.2', 'G 0.4', 'G 0.16', 'G 0.17', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.29']
    },
    {
        'id': 'SYS.4.5.A2',
        'name': 'Verlust- und Manipulationsmeldung',
        'cia': None,
        'gefahren': ['G 0.16', 'G 0.21']
    },
    {
        'id': 'SYS.4.5.A4',
        'name': 'Erstellung einer Richtlinie zum sicheren Umgang mit Wechseldatenträgern',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.39']
    },
    {
        'id': 'SYS.4.5.A5',
        'name': 'Regelung zur Mitnahme von Wechseldatenträgern',
        'cia': None,
        'gefahren': ['G 0.16', 'G 0.17', 'G 0.19']
    },
    {
        'id': 'SYS.4.5.A6',
        'name': 'Datenträgerverwaltung',
        'cia': None,
        'gefahren': ['G 0.2', 'G 0.4', 'G 0.17']
    },
    {
        'id': 'SYS.4.5.A7',
        'name': 'Sicheres Löschen der Datenträger vor und nach der Verwendung',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.4.5.A10',
        'name': 'Datenträgerverschlüsselung',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19']
    },
    {
        'id': 'SYS.4.5.A11',
        'name': 'Integritätsschutz durch Checksummen oder digitale Signaturen',
        'cia': 'I',
        'gefahren': ['G 0.22', 'G 0.46']
    },
    {
        'id': 'SYS.4.5.A12',
        'name': 'Schutz vor Schadsoftware',
        'cia': None,
        'gefahren': ['G 0.39']
    },
    {
        'id': 'SYS.4.5.A13',
        'name': 'Kennzeichnung der Wechseldatenträger beim Versand',
        'cia': None,
        'gefahren': ['G 0.17', 'G 0.19']
    },
    {
        'id': 'SYS.4.5.A14',
        'name': 'Sichere Versandart und Verpackung',
        'cia': 'CIA',
        'gefahren': ['G 0.2', 'G 0.4', 'G 0.17']
    },
    {
        'id': 'SYS.4.5.A15',
        'name': 'Verwendung zertifizierter Wechseldatenträger',
        'cia': 'CIA',
        'gefahren': ['G 0.20']
    },
    {
        'id': 'SYS.4.5.A16',
        'name': 'Nutzung dedizierter IT-Systeme zur Datenprüfung',
        'cia': 'CI',
        'gefahren': ['G 0.39']
    },
    {
        'id': 'SYS.4.5.A17',
        'name': 'Gewährleistung der Integrität und Verfügbarkeit bei Langzeitspeichern',
        'cia': None,
        'gefahren': ['G 0.46']
    }
]
