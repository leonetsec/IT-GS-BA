# Enthält alle Mappings für Bausteinnamen, WiBA und Profile

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


profile_names = {
    '1' : 'Kleine und mittlere Flughäfen',
    '2' : 'Ressort-Forschungseinrichtungen',
    '3' : 'Nutzung der E-Akte Bund',
    '4' : 'Leitstellen',
    '5' : 'Absicherung von 5G-Campusnetzen Eigenbetrieb',
    '6' : 'Oberste Bundesbehörden',
    '7' : 'Betrieb von UAS Band 1: UAS-Betriebskategorie "Open"(Offen)',
    '8' : 'Basis-Absicherung Kommunalverwaltung',
    '9' : 'Absicherung von 5G-Campusnetzen Fremdbetrieb',
    '10' : 'i-Kfz (Platzhalter)',
    '11' : 'Einnahmeverwaltung des Ministeriums der Finanzen Sachsen-Anhalt (Platzhalter)',
    '12' : 'Bundesgerichte',
    '13' : 'Chemie',
    '14' : 'Hochschulen',
    '15' : 'Weltrauminfrastrukturen',
    '16' : 'Verkehrssteuerungs- und Leitsysteme der Bundesautobahn',
    '17' : 'Papierfabriken',
    '18' : 'Oberste Landesbehörden Deutschlands',
    '19' : 'Handwerksbetriebe (Platzhalter)',
    '20' : 'Reedereien - Landbetrieb',
    '21' : 'Reedereien - Schiffsbetrieb',
    '22' : 'Handwerkskammern',
    '23' : 'Große IT-Dienstleister (Basis)'
}

profiles_mapping = {
    '1' : 'flughafen_profil',
    '2' : 'ressort_forschungseinrichtungen_profil',
    '3' : 'e_akte_profil',
    '4' : 'leitstellen_profil',
    '5' : 'fuenfg_eigenbetrieb_profil',
    '6' : 'oberste_bundesbehoerden_profil',
    '7' : 'uas_profil',
    '8' : 'kommunalverwaltung_profil',
    '9' : 'fuenfg_fremdbetrieb_profil',
    '10' : 'ikfz_profil',
    '11' : 'finanzen_sa_profil',
    '12' : 'bundesgerichte_profil',
    '13' : 'chemie_profil',
    '14' : 'hochschulen_profil',
    '15' : 'weltrauminfrastrukturen_profil',
    '16' : 'bundesautobahn_profil',
    '17' : 'papierfabriken_profil',
    '18' : 'oberste_landesbehoerden_profil',
    '19' : 'handwerksbetriebe_profil',
    '20' : 'reedereien_land_profil',
    '21' : 'reedereien_schiff_profil',
    '22' : 'handwerkskammern_profil',
    '23' : 'grosse_dienstleister_profil'
}

sort_list = {
    '1' : 'Nicht + Teilweise umgesetzte Anforderungen',
    '2' : 'Nicht umgesetzte Anforderungen',
    '3' : 'Umgesetzte Anforderungen',
    '4' : 'Nicht umgesetzte Basis-Anforderungen',
    '5' : 'Nicht umgesetzte Standard-Anforderungen',
    '6' : 'Nicht umgesetzt Anforderungen des erhöhten Schutzbedarfs',
    '7': 'Nicht umgesetzte Basis + Standard Anforderungen',
    '8' : 'Teilweise umgesetzte Anforderungen',
    '9' : 'Prozent an umgesetzten Anforderungen',
    '10' : 'Entbehrliche Anforderungen',
    '11' : 'Explizit nicht entbehrliche Anforderungen',
    '12' : 'Summierte Kostenschätzung',
    '13' : 'Verantwortliche',
    '14' : 'Zahl der Anforderungen insgesamt',
    '15' : 'Umsetzung bis',
    '16' : '(Teilweise) abgedeckte elementare Gefährdungen',
    '17' : '(Teilweise) abgedeckte Schutzziele'
}

format_options = {
        "1": "Excel",
        "2": "CSV",
        "3": "JSON",
        "4": "Markdown",
        "5": "HTML",
        "6": "XML",
        "7": "Leerzeichengetrennt",
        "8": "Tabstoppgetrennt",
        "9": "Benutzerdefiniertes Trennzeichen"
    }

# Nicht ausreichend, da Anforderungen oft nur teilweise erfüllt werden.
wiba_old = ['APP.6.A1', 'APP.1.1.A13', 'APP.1.2.A1', 'APP.1.2.A2', 'APP.1.2.A3', 'APP.1.2.A6',
        'APP.6.A3', 'APP.6.A4', 'INF.10.A7', 'APP.5.3.A1', 'APP.1.1.A17', 'APP.1.1.A2', 'APP.1.1.A3',
        'APP.1.1.A12', 'APP.2.1.A3', 'APP.2.1.A5', 'APP.2.2.A6', 'APP.2.2.A16', 'APP.2.2.A17', 'APP.2.2.A5',
        'APP.3.1.A1', 'APP.3.1.A4', 'APP.3.1.A14', 'APP.3.2.A1', 'APP.3.2.A11', 'APP.3.2.A2', 'APP.3.2.A4',
        'APP.3.2.A5', 'APP.3.2.A3', 'APP.3.3.A15', 'APP.3.3.A8', 'APP.3.3.A3', 'APP.3.6.A9', 'APP.3.6.A8',
        'APP.3.6.A4', 'APP.3.6.A7', 'APP.3.6.A2', 'APP.3.6.A3', 'APP.3.6.A6', 'APP.5.3.A3', 'CON.1.A2',
        'APP.5.3.A2', 'APP.5.3.A4', 'APP.1.2.A13', 'CON.3.A1', 'CON.1.A4', 'NET.3.1.A8', 'NET.4.1.A12',
        'CON.3.A2', 'CON.3.A12', 'CON.3.A14', 'CON.3.A4', 'CON.6.A1', 'CON.6.A11', 'CON.6.A12', 'CON.6.A13',
        'CON.6.A2', 'CON.9.A1', 'CON.9.A2', 'DER.1.A5', 'DER.1.A9', 'DER.1.A3', 'DER.1.A10', 'DER.1.A2',
        'DER.1.A12', 'DER.2.1.A1', 'DER.2.1.A3', 'DER.2.1.A4', 'DER.2.1.A5', 'DER.2.1.A6', 'DER.2.1.A2',
        'DER.2.2.A1', 'DER.2.2.A3', 'INF.7.A1', 'INF.7.A5', 'INF.7.A6', 'INF.7.A7', 'INF.1.A6', 'INF.1.A7',
        'INF.7.A2', 'INF.10.A6', 'INF.10.A3', 'INF.10.A1', 'INF.1.A3', 'INF.11.A3', 'INF.8.A2', 'INF.9.A1',
        'INF.9.A4', 'INF.8.A1', 'INF.2.A7', 'INF.2.A3', 'INF.2.A5', 'INF.1.A4', 'INF.2.A9', 'INF.2.A6', 'INF.2.A1',
        'INF.2.A2', 'INF.2.A8', 'INF.5.A2', 'INF.5.A3', 'INF.5.A4', 'INF.5.A7', 'INF.6.A2', 'INF.6.A4', 'INF.6.A3',
        'INF.6.A1', 'INF.1.A5', 'INF.1.A9', 'INF.8.A3', 'INF.9.A3', 'INF.8.A5', 'INF.9.A6', 'INF.11.A10',
        'INF.9.A2', 'SYS.4.5.A5', 'INF.9.A5', 'ISMS.1.A1', 'ISMS.1.A2', 'ISMS.1.A8', 'NET.1.1.A21', 'NET.1.1.A7',
        'NET.1.1.A9', 'NET.1.1.A5', 'NET.1.1.A10', 'NET.1.1.A4', 'NET.1.1.A2', 'NET.1.1.A8', 'NET.1.1.A11',
        'NET.1.2.A10', 'NET.1.2.A9', 'NET.1.2.A7', 'NET.1.2.A8', 'NET.2.1.A5', 'NET.2.1.A1', 'NET.2.1.A2',
        'NET.2.1.A4', 'NET.2.1.A8', 'NET.2.1.A6', 'NET.2.1.A13', 'NET.2.1.A3', 'NET.2.2.A3', 'NET.2.2.A1',
        'NET.2.2.A2', 'NET.3.1.A4', 'NET.3.1.A7', 'NET.3.1.A1', 'NET.3.2.A18', 'NET.3.2.A6', 'NET.3.2.A9',
        'NET.3.2.A2', 'NET.3.2.A3', 'NET.3.2.A17', 'NET.3.2.A4', 'NET.3.2.A22', 'NET.3.3.A2', 'NET.3.3.A3',
        'NET.3.3.A7', 'CON.3.A15', 'NET.4.1.A18', 'NET.4.1.A7', 'NET.4.1.A5', 'NET.4.1.A8', 'NET.4.2.A3',
        'NET.4.2.A5', 'NET.4.3.A2', 'NET.4.3.A1', 'OPS.1.1.1.A4', 'OPS.1.1.1.A2', 'OPS.1.1.1.A1', 'OPS.1.1.2.A21',
        'OPS.1.1.2.A22', 'OPS.1.1.2.A2', 'OPS.1.1.2.A4', 'OPS.1.1.2.A5', 'OPS.1.1.2.A6', 'OPS.1.1.3.A3',
        'OPS.1.1.3.A15', 'OPS.1.1.3.A1', 'OPS.1.1.4.A3', 'OPS.1.1.4.A7', 'OPS.1.1.4.A5', 'OPS.1.1.4.A6',
        'OPS.1.1.4.A2', 'OPS.1.1.5.A10', 'OPS.1.1.5.A5', 'OPS.1.1.5.A3', 'OPS.1.1.5.A4', 'OPS.1.2.4.A2',
        'OPS.1.2.4.A5', 'OPS.1.2.5.A3', 'OPS.1.2.5.A5', 'OPS.1.2.5.A1', 'OPS.1.2.5.A2', 'OPS.1.2.5.A8',
        'OPS.2.2.A13', 'OPS.2.2.A9', 'OPS.2.2.A4', 'OPS.2.2.A2', 'OPS.2.2.A3', 'OPS.2.3.A14', 'OPS.2.3.A3',
        'OPS.2.3.A4', 'OPS.2.3.A5', 'OPS.2.3.A6', 'OPS.2.3.A7', 'OPS.2.3.A11', 'OPS.2.3.A1', 'OPS.2.3.A2',
        'ORP.1.A1', 'ORP.1.A4', 'ORP.1.A15', 'ORP.1.A2', 'ORP.1.A3', 'ORP.2.A5', 'ORP.2.A2', 'ORP.2.A14',
        'ORP.2.A1', 'ORP.2.A15', 'ORP.2.A3', 'ORP.2.A4', 'ORP.3.A1', 'ORP.3.A6', 'ORP.3.A3', 'ORP.4.A23',
        'ORP.4.A8', 'ORP.4.A2', 'ORP.4.A3', 'ORP.4.A4', 'ORP.4.A1', 'ORP.4.A5', 'ORP.4.A6', 'ORP.4.A7',
        'ORP.4.A9', 'SYS.1.1.A1', 'SYS.1.1.A9', 'SYS.1.1.A2', 'SYS.1.1.A10', 'SYS.1.1.A6', 'SYS.1.1.A15',
        'SYS.1.2.3.A1', 'SYS.1.2.3.A3', 'SYS.1.2.3.A2', 'SYS.1.2.3.A4', 'SYS.1.5.A5', 'SYS.1.5.A12', 'SYS.1.5.A3',
        'SYS.1.5.A7', 'SYS.1.5.A2', 'SYS.1.9.A4', 'SYS.1.9.A12', 'SYS.1.9.A13', 'SYS.1.9.A7', 'SYS.2.1.A6',
        'SYS.2.1.A28', 'SYS.2.1.A1', 'SYS.2.1.A8', 'SYS.2.1.A42', 'SYS.2.1.A24', 'SYS.2.1.A27', 'SYS.2.1.A3',
        'SYS.2.1.A16', 'SYS.2.2.3.A9', 'SYS.2.2.3.A18', 'SYS.2.2.3.A19', 'SYS.2.2.3.A13', 'SYS.2.2.3.A12',
        'SYS.2.2.3.A1', 'SYS.2.2.3.A14', 'SYS.2.2.3.A15', 'SYS.2.2.3.A16', 'SYS.2.2.3.A4', 'SYS.2.5.A2',
        'SYS.2.5.A3', 'SYS.3.1.A1', 'SYS.3.1.A12', 'SYS.3.1.A6', 'SYS.3.1.A3', 'SYS.3.1.A13', 'SYS.3.1.A9',
        'SYS.3.2.1.A5', 'SYS.3.2.1.A4', 'SYS.3.2.1.A6', 'SYS.3.2.1.A8', 'SYS.3.2.1.A7', 'SYS.3.2.1.A3',
        'SYS.3.2.1.A1', 'SYS.3.3.A2', 'SYS.3.3.A4', 'SYS.3.3.A3', 'SYS.4.1.A1', 'SYS.4.1.A14', 'SYS.4.1.A2',
        'SYS.4.1.A7', 'SYS.4.1.A18', 'SYS.4.1.A22', 'SYS.4.5.A2', 'SYS.4.5.A4', 'SYS.4.5.A7', 'INF.11.A2',
        'SYS.4.5.A10', 'SYS.4.5.A12', 'SYS.4.5.A1']

# Alle Inhalte, weil sich Anforderungsteile nur so auseinander halten lassen
wiba = ['ob sich die Institution in Abhängigkeit zu einem Hersteller oder einer Herstellerin begibt, wenn sie diese Software einsetzt.', 'Hierbei MÜSSEN bereits Sicherheitsaspekte berücksichtigt werden.', 'Wenn die Dokumente lediglich betrachtet werden sollen, SOLLTEN entsprechende Viewer-Anwendungen verwendet werden, wenn diese verfügbar sind.', 'Webseiten MÜSSEN als eigenständige Prozesse oder mindestens als eigene Threads voneinander isolierten werden.', 'Plug-ins und Erweiterungen MÜSSEN ebenfalls in isolierten Bereichen ausgeführt werden.', 'Der verwendete Webbrowser MUSS die Content Security Policy (CSP) umsetzen.', 'Der aktuell höchste Level der CSP SOLLTE erfüllt werden.', 'Der Browser MUSS Maßnahmen zur Same-Origin-Policy und Subresource Integrity unterstützen.', 'Der Webbrowser MUSS Transport Layer Security (TLS) in einer sicheren Version unterstützen.', 'Verbindungen zu Webservern MÜSSEN mit TLS verschlüsselt werden, sofern dies vom Webserver unterstützt wird.', 'Der Webbrowser MUSS den Sicherheitsmechanismus HTTP Strict Transport Security (HSTS) gemäß RFC 6797 unterstützen und einsetzen.', 'Falls dies nicht durch technische Maßnahmen möglich ist, MUSS den Benutzenden verboten werden, diese Liste zu ändern.', 'Außerdem MUSS sichergestellt werden, dass der Webbrowser Zertifikate lokal widerrufen kann.', 'Der Webbrowser MUSS die Gültigkeit der Server-Zertifikate mithilfe des öffentlichen Schlüssels und unter Berücksichtigung des Gültigkeitszeitraums vollständig prüfen.', 'Auch der Sperrstatus der Server-Zertifikate MUSS vom Webbrowser geprüft werden.', 'Die Zertifikatskette einschließlich des Wurzelzertifikats MUSS verifiziert werden.', 'Der Webbrowser MUSS den Benutzenden eindeutig und gut sichtbar darstellen, ob die Kommunikation im Klartext oder verschlüsselt erfolgt.', 'Der Webbrowser SOLLTE den Benutzenden auf Anforderung das verwendete Serverzertifikat anzeigen können.', 'Der Webbrowser MUSS den Benutzenden signalisieren, wenn Zertifikate fehlen, ungültig sind oder widerrufen wurden.', 'Der Webbrowser MUSS in diesem Fall die Verbindung abbrechen, bis die Benutzenden diese ausdrücklich bestätigt haben.', 'Wird ein Kennwortmanager im Webbrowser verwendet, MUSS er eine direkte und eindeutige Beziehung zwischen Webseite und hierfür gespeichertem Kennwort herstellen.', 'Der Kennwortspeicher MUSS die Passwörter verschlüsselt speichern.', 'Außerdem MUSS sichergestellt sein, dass die Authentisierung für den kennwortgeschützten Zugriff nur für die aktuelle Sitzung gültig ist.', 'Der IT-Betrieb MUSS sicherstellen, dass der verwendete Browser den Benutzenden die Möglichkeit bietet, gespeicherte Passwörter zu löschen.', 'Die vertrauenswürdige Quelle SOLLTE eine Möglichkeit bereitstellen, die Software auf Integrität zu überprüfen.', 'Falls zu einem Installationspaket digitale Signaturen oder Prüfsummen verfügbar sind, MÜSSEN mit diesen die Integrität überprüft werden.', 'alle relevanten Sicherheitsupdates und -patches installiert sind, bevor die Software produktiv eingesetzt wird.', 'Dedizierte Schulungs- und Präsentationsrechner SOLLTEN mit einer Minimalkonfiguration versehen werden.', 'Die Institution MUSS eine sichere Konfiguration für die E-Mail-Clients vorgeben.', 'Die E-Mail-Clients MÜSSEN den Benutzenden vorkonfiguriert zur Verfügung gestellt werden.', 'Die Standardkonfiguration SOLLTE dokumentiert werden.', 'Alle Benutzenden MÜSSEN geeignet bezüglich der Gefährdungen durch Aktive Inhalte in Office-Dateien sensibilisiert werden.', 'Die Benutzenden MÜSSEN zum Umgang mit Dokumenten aus externen Quellen geeignet sensibilisiert werden.', 'Falls es dennoch notwendig ist, Aktive Inhalte auszuführen, MUSS darauf geachtet werden, dass Aktive Inhalte nur ausgeführt werden, wenn sie aus vertrauenswürdigen Quellen stammen.', 'Durch technische Maßnahmen SOLLTE erzwungen werden, dass Dokumente aus externen Quellen geprüft werden.', 'Falls möglich, SOLLTEN sie blockiert werden.', 'Alle Cloud-Laufwerke SOLLTEN deaktiviert werden.', 'wofür die Software genutzt und welche Informationen damit verarbeitet werden sollen,', 'Daten aus potenziell unsicheren Quellen SOLLTEN automatisch in einem geschützten Modus geöffnet werden.', 'Alle administrativen Aufgabenbereiche und Berechtigungen SOLLTEN ausreichend dokumentiert werden.', 'Der Verzeichnisdienst MUSS sicher konfiguriert werden.', 'Dabei MUSS geprüft werden, ob eine bidirektionale Vertrauensbeziehung notwendig ist.', 'Die SID-(Security Identifier)-Filterung bei Vertrauensstellungen zwischen Gesamtstrukturen DARF NICHT deaktiviert werden.', 'Sie DÜRFEN NUR als Notfallkonten dienen.', 'Das Built-in „Guest“- / „Gast“-Konto MUSS deaktiviert werden.', 'Die Berechtigungen für die Gruppe „Everyone“ / „Jeder“ MUSS beschränkt werden.', 'Privilegierte Konten MÜSSEN Mitglied der Gruppe „Protected Users“ / „Geschütze Benutzer“ sein.', 'Für Dienstkonten MÜSSEN (Group) Managed Service Accounts verwendet werden.', 'Die Anmeldung von hochpriviligierten Domänen- und Gesamtstruktur-Konten und Gruppen MUSS technisch auf die minimal notwendigen IT-Systeme einschränkt werden.', 'Insbesondere die Anmeldung von Mitgliedern der Gruppen „Schema Admins“ / „Schema-Administratoren“, „Enterprise Admins“ / „Enterprise-Administratoren“ und „Domain Admins“ / „Domänen-Administratoren“ SOLLTE technisch auf den Domänencontroller beschränkt werden, eine Anmeldung an anderen IT-Systemen ist für diese Gruppen also zu unterbinden.', 'Wenn eine Domäne keine bidirektionale Vertrauensbeziehung zu anderen Domänen in der Gesamtstruktur benötigt, SOLLTE diese Domäne in eine eigene Gesamtstruktur ausgelagert werden, da innerhalb einer Gesamtstruktur produktbedingt keine Anpassung der Vertrauensbeziehungen möglich ist.', 'Aufgrund der zentralen Bedeutung des Domänencontrollers SOLLTEN auf diesem Server keine weiteren Dienste betrieben werden, sofern diese nicht zwingend auf dem gleichen Server zum Betrieb des AD DS erforderlich sind.', 'Built-in-AD-DS-Konten MÜSSEN mit komplexen Passwörtern versehen werden.', 'Dafür MUSS eine angemessene Authentisierungsmethode ausgewählt werden.', 'Insbesondere MÜSSEN die erlaubte Dateigröße, erlaubte Dateitypen und erlaubte Speicherorte festgelegt werden.', 'Zudem MUSS sichergestellt werden, dass Clients Dateien nur im vorgegebenen erlaubten Speicherort speichern können.', 'Der IT-Betrieb MUSS Webanwendungen und Webservices so konfigurieren, dass sich Clients gegenüber der Webanwendung oder dem Webservice authentisieren müssen, wenn diese auf geschützte Ressourcen zugreifen wollen.', 'Der IT-Betrieb MUSS geeignete Grenzwerte für fehlgeschlagene Anmeldeversuche festlegen.', 'Falls eine Webanwendung oder ein Webservice eine Upload-Funktion für Dateien anbietet, MUSS diese Funktion durch den IT-Betrieb so weit wie möglich eingeschränkt werden.', 'Die Dateien mit den Quelltexten der Webanwendung oder des Webservices MÜSSEN vor unerlaubten Abrufen geschützt werden.', 'Der IT-Betrieb MUSS sicherstellen, dass Zugangsdaten zur Webanwendung oder zum Webservice serverseitig mithilfe von sicheren kryptografischen Algorithmen vor unbefugtem Zugriff geschützt werden.', 'Dem Webserver-Dienst MÜSSEN alle nicht notwendige Schreibberechtigungen entzogen werden.', 'Falls es aus Kompatibilitätsgründen erforderlich ist, veraltete Verfahren zu verwenden, SOLLTEN diese auf so wenige Fälle wie möglich beschränkt werden.', 'Wenn eine HTTPS-Verbindung genutzt wird, MÜSSEN alle Inhalte über HTTPS ausgeliefert werden.', 'Ist dies nicht möglich, SOLLTE jeder Webserver auf einem eigenen physischen oder virtuellen Server ausgeführt werden.', 'Der IT-Betrieb MUSS regelmäßig überprüfen, ob vertrauliche Dateien in öffentlichen Verzeichnissen gespeichert wurden.', 'erfolgreiche Zugriffe auf Ressourcen,', 'fehlgeschlagene Zugriffe auf Ressourcen aufgrund von mangelnder Berechtigung, nicht vorhandenen Ressourcen und Server-Fehlern sowie', 'Dazu MUSS er insbesondere den Webserver-Prozess einem Konto mit minimalen Rechten zuweisen.', 'Wenn sich Clients mit Hilfe von Passwörtern am Webserver authentisieren, MÜSSEN diese kryptografisch gesichert und vor unbefugtem Zugriff geschützt gespeichert werden.', 'Der Webserver MUSS für alle Verbindungen durch nicht vertrauenswürdige Netze eine sichere Verschlüsselung über TLS anbieten (HTTPS).', 'Der Webserver MUSS in einer gekapselten Umgebung ausgeführt werden, sofern dies vom Betriebssystem unterstützt wird.', 'Nicht benötigte Module und Funktionen des Webservers MÜSSEN deaktiviert werden.', 'Es MUSS sichergestellt werden, dass Webanwendungen nur auf einen definierten Verzeichnisbaum zugreifen können (WWW-Wurzelverzeichnis).', 'Der Webserver MUSS so konfiguriert sein, dass er nur Dateien ausliefert, die sich innerhalb des WWW-Wurzelverzeichnisses befinden.', 'Der IT-Betrieb MUSS alle nicht benötigten Funktionen, die Verzeichnisse auflisten, deaktivieren.', 'Insbesondere MUSS der IT-Betrieb sicherstellen, dass vertrauliche Dateien nicht in öffentlichen Verzeichnissen des Webservers liegen.', 'Alle mithilfe des Webservers veröffentlichten Dateien MÜSSEN vorher auf Schadprogramme geprüft werden.', 'Der Webserver MUSS mindestens folgende Ereignisse protokollieren:', 'Auch ausreichende Speicherreserven SOLLTEN vorgehalten werden.', 'Es SOLLTE ausschließlich Massenspeicher verwendet werden, der für einen Dauerbetrieb ausgelegt ist.', 'Die Geschwindigkeit und die Anbindung der Massenspeicher MUSS für den Einsatzzweck angemessen sein.', 'Die Benutzenden SOLLTEN regelmäßig über die geforderte strukturierte Datenhaltung informiert werden.', 'Es SOLLTE schriftlich festgelegt werden, welche Daten lokal und welche auf dem Fileserver gespeichert werden dürfen.', 'Alle Daten MÜSSEN durch ein Viren-Schutzprogramm auf Schadsoftware untersucht werden, bevor sie auf dem Fileserver abgelegt werden.', 'Der Speicherplatz des Fileservers MUSS ausreichend dimensioniert sein.', 'Die Dateien SOLLTEN ausschließlich strukturiert auf den Fileserver abgelegt werden.', 'Arbeitsplatzrechner DÜRFEN NICHT als Fileserver eingesetzt werden.', 'Im Notfallplan für DNS-Server MUSS ein Datensicherungskonzept für die Zonen- und Konfigurationsdateien beschrieben sein.', 'Eine Person MUSS bestimmt werden, die dafür zuständig ist, die Internet-Domainnamen zu verwalten.', 'Falls Dienstleistende mit der Domainverwaltung beauftragt werden, MUSS darauf geachtet werden, dass die Institution die Kontrolle über die Domains behält.', 'Es MUSS sichergestellt werden, dass DNS-Zonentransfers zwischen Primary und Secondary DNS-Servern funktionieren.', 'Zonentransfers MÜSSEN auf bestimmte IP-Adressen beschränkt werden.', 'Ein Resolving DNS-Server MUSS so konfiguriert werden, dass er ausschließlich Anfragen aus dem internen Netz akzeptiert.', 'Anzahl der DNS-Anfragen,', 'Anzahl der Fehler bei DNS-Anfragen,', 'EDNS-Fehler (EDNS - Extension Mechanisms for DNS),', 'auslaufende Zonen sowie', 'fehlgeschlagene Zonentransfers.', 'Es MUSS sichergestellt sein, dass die Registrierungen für alle Domains, die von einer Institution benutzt werden, regelmäßig und rechtzeitig verlängert werden.', 'Advertising DNS-Server MÜSSEN redundant ausgelegt werden.', 'Für jeden Advertising DNS-Server MUSS es mindestens einen zusätzlichen Secondary DNS-Server geben.', 'Zonentransfers MÜSSEN so konfiguriert werden, dass diese nur zwischen Primary und Secondary DNS-Servern möglich sind.', 'Advertising DNS-Server und Resolving DNS-Server MÜSSEN serverseitig getrennt sein.', 'Die Resolver der internen IT-Systeme DÜRFEN NUR die internen Resolving DNS-Server verwenden.', 'Die Version des verwendeten DNS-Server-Produktes MUSS verborgen werden.', 'Es MUSS sichergestellt werden, dass nur legitimierte IT-Systeme Domain-Informationen ändern dürfen.', 'Die Institution SOLLTE ebenfalls bei der Archivierung beachten, dass E-Mails möglicherweise nur lokal auf Clients gespeichert sind.', 'In Datensicherungen MÜSSEN kryptografische Schlüssel vom IT-Betrieb derart gespeichert oder aufbewahrt werden, dass Unbefugte nicht darauf zugreifen können.', 'Die Dateianhänge MÜSSEN auf dem Client oder auf dem E-Mail-Server überprüft werden.', 'Der eingesetzte Webbrowser MUSS sicherstellen, dass jede Instanz und jeder Verarbeitungsprozess nur auf die eigenen Ressourcen zugreifen kann (Sandboxing).', 'Unsichere Versionen von TLS SOLLTEN deaktiviert werden.', 'Für den E-Mail-Empfang über nicht vertrauenswürdige Netze MÜSSEN E-Mail-Server eine sichere Transportverschlüsselung anbieten.', 'Der IT-Betrieb MUSS den E-Mail-Server so konfigurieren, dass E-Mail-Clients nur über eine sichere Transportverschlüsselung auf Postfächer zugreifen können, wenn dies über nicht vertrauenswürdige Netze passiert.', 'Der IT-Betrieb SOLLTE den E-Mail-Versand durch unsichere Netze über unverschlüsselte Verbindungen deaktivieren.', 'Versenden E-Mail-Server von sich aus E-Mails an andere E-Mail-Server, SOLLTEN sie eine sichere Transportverschlüsselung nutzen.', 'Außerdem MUSS der IT-Betrieb den E-Mail-Server so einstellen, dass er nicht als Spam-Relay missbraucht werden kann.', 'Werden Nachrichten auf einem E-Mail-Server gespeichert, MUSS der IT-Betrieb eine geeignete Größenbeschränkung für das serverseitige Postfach einrichten und dokumentieren.', 'Der IT-Betrieb MUSS sicherstellen, dass auf E-Mail-Servern eingehende und ausgehende E-Mails, insbesondere deren Anhänge, auf Spam-Merkmale und schädliche Inhalte überprüft werden.', 'Die Institution MUSS festlegen, wie mit verschlüsselten E-Mails zu verfahren ist, wenn diese nicht durch das Virenschutzprogramm entschlüsselt werden können.', 'Falls der Webbrowser eine eigene Liste von vertrauenswürdigen Wurzelzertifikaten bereitstellt, MUSS sichergestellt werden, dass nur der IT-Betrieb diese ändern kann.', 'Es MUSS sichergestellt werden, dass auf die im Kennwortmanager gespeicherten Passwörter nur nach Eingabe eines Master-Kennworts zugegriffen werden kann.', 'Die Institution MUSS entscheiden, ob die verwendeten Browser DNS-over-HTTPS (DoH) verwenden sollen.', 'E-Mail-Clients MÜSSEN so konfiguriert werden, dass sie eventuell vorhandenen HTML-Code und andere aktive Inhalte in E-Mails nicht automatisch interpretieren.', 'Bevor Dateianhänge aus E-Mails geöffnet werden, MÜSSEN sie auf Schadsoftware überprüft werden.', 'Der IT-Betrieb MUSS Schutzmechanismen gegen Denial-of-Service (DoS)-Attacken ergreifen.', 'Vorschaufunktionen für Datei-Anhänge MÜSSEN so konfiguriert werden, dass sie Dateien nicht automatisch interpretieren.', 'E-Mail-Filterregeln sowie die automatische Weiterleitung von E-Mails MÜSSEN auf notwendige Anwendungsfälle beschränkt werden.', 'Zusätzlich MUSS die Institution die Zuständigkeiten für fachliche Betreuung, Freigabe und betriebliche Administration schon im Vorfeld klären und festlegen.', 'Die Zuständigkeiten MÜSSEN dokumentiert und bei Bedarf aktualisiert werden.', 'E-Mail-Clients MÜSSEN für die Kommunikation mit E-Mail-Servern über nicht vertrauenswürdige Netze eine sichere Transportverschlüsselung einsetzen.', 'Die ausgewählte Software MUSS aus vertrauenswürdigen Quellen beschafft werden.', 'die Software nur mit dem geringsten notwendigen Funktionsumfang installiert und ausgeführt wird,', 'Der IT-Betrieb MUSS in Abstimmung mit den Fachverantwortlichen festlegen, wer die Software wie installieren darf.', 'Idealerweise SOLLTE Software immer zentral durch den IT-Betrieb installiert werden.', 'Darüber hinaus SOLLTE die Software mit einem geeigneten Wartungsvertrag oder einer vergleichbaren Zusage des herstellenden oder anbietenden Unternehmens beschafft werden.', 'die Software mit den geringsten möglichen Berechtigungen ausgeführt wird,', 'die datensparsamsten Einstellungen (in Bezug auf die Verarbeitung von personenbezogenen Daten) konfiguriert werden sowie', 'Hierbei MÜSSEN auch abhängige Komponenten (unter anderem Laufzeitumgebungen, Bibliotheken, Schnittstellen sowie weitere Programme) mitbetrachtet werden.', 'Sofern erforderlich, SOLLTE der IT-Betrieb eine sichere Standardkonfiguration der Software festlegen, mit der die Software konfiguriert wird.', 'Die Funktion, dass eingebettete Aktive Inhalte automatisch ausgeführt werden, MUSS deaktiviert werden.', 'Alle aus externen Quellen bezogenen Dokumente MÜSSEN auf Schadsoftware überprüft werden, bevor sie geöffnet werden.', 'Alle als problematisch eingestuften und alle innerhalb der Institution nicht benötigten Dateiformate MÜSSEN verboten werden.', 'Die in einigen Office-Produkten integrierten Funktionen für Cloud-Speicher SOLLTEN grundsätzlich deaktiviert werden.', 'Diese Verträge oder Zusagen SOLLTEN insbesondere garantieren, dass auftretende Sicherheitslücken und Schwachstellen der Software während des gesamten Nutzungszeitraums zeitnah behoben werden.', 'Verfügbarkeitsanforderungen,', 'Eine Vorgehensweise SOLLTE für den Fall festgelegt werden, dass ein privater Schlüssel offengelegt wird.', 'Geheime Schlüssel MÜSSEN sicher gespeichert und vor unbefugtem Zugriff geschützt werden.', 'Vertraulichkeitsanforderungen,', 'In Hard- oder Software mit kryptografischen Funktionen SOLLTEN voreingestellte Schlüssel (ausgenommen öffentliche Zertifikate) ersetzt werden.', 'Integritätsbedarf,', 'rechtliche Anforderungen,', 'Die Konfigurationsdateien von Routern und Switches MÜSSEN regelmäßig gesichert werden.', 'Die Konfigurations- und Anwendungsdaten der eingesetzten TK-Anlage SOLLTEN bei der Ersteinrichtung und anschließend regelmäßig gesichert werden, insbesondere nachdem sich diese geändert haben.', 'Der IT-Betrieb MUSS die Daten der E-Mail-Server und -Clients regelmäßig sichern.', 'In virtuellen Umgebungen sowie für Storage-Systeme SOLLTE geprüft werden, ob das IT-System ergänzend durch Snapshot-Mechanismen gesichert werden kann, um hierdurch mehrere schnell wiederherstellbare Zwischenversionen zwischen den vollständigen Datensicherungen zu erstellen.', 'Speichervolumen,', 'Änderungsvolumen,', 'Datensicherungen MÜSSEN immer auf separaten Speichermedien für die Datensicherung gespeichert werden.', 'Der IT-Betrieb MUSS Verfahren festlegen, wie die Daten gesichert werden.', 'Langlebige kryptografische Schlüssel MÜSSEN offline, außerhalb der eingesetzten IT-Systeme, aufbewahrt werden.', 'Die Speichermedien für die Datensicherung MÜSSEN räumlich getrennt von den gesicherten IT-Systemen aufbewahrt werden.', 'Sie SOLLTEN in einem anderen Brandabschnitt aufbewahrt werden.', 'Der Aufbewahrungsort SOLLTE so klimatisiert sein, dass die Datenträger entsprechend der zeitlichen Vorgaben des Datensicherungskonzepts aufbewahrt werden können.', 'Die erstellten Datensicherungen MÜSSEN in geeigneter Weise vor unbefugtem Zugriff geschützt werden.', 'Hierbei MUSS insbesondere sichergestellt werden, dass Datensicherungen nicht absichtlich oder unbeabsichtigt überschrieben werden können.', 'IT-Systeme, die für die Datensicherung eingesetzt werden, SOLLTEN einen schreibenden Zugriff auf die Speichermedien für die Datensicherung nur für autorisierte Datensicherungen oder autorisierte Administrationstätigkeiten gestatten.', 'wie die Datensicherungen vor unbefugtem Zugriff und Überschreiben gesichert werden,', 'Dazu MÜSSEN die Fachverantwortlichen für die Anwendungen ihre Anforderungen an die Datensicherung definieren.', 'zu sichernde Daten,', 'Für die Datensicherungsverfahren MÜSSEN Art, Häufigkeit und Zeitpunkte der Datensicherungen bestimmt werden.', 'Auch MUSS definiert sein, welche Speichermedien benutzt werden und wie die Transport- und Aufbewahrungsmodalitäten ausgestaltet sein müssen.', 'Anforderungen an das Löschen und Vernichten der Daten sowie', 'wie lange Datensicherungen aufbewahrt werden,', 'welche Hard- und Software eingesetzt wird.', 'Hierbei MÜSSEN die gesetzlichen Bestimmungen beachtet werden,', 'anderseits maximale Aufbewahrungszeiten und ein Anrecht auf das sichere Löschen von personenbezogenen Daten garantieren.', 'Wenn externe Dienstleistende beauftragt werden, MUSS der Prozess zum Löschen und Vernichten ausreichend sicher und nachvollziehbar sein.', 'Die von externen Dienstleistenden eingesetzten Verfahrensweisen zum sicheren Löschen und Vernichten MÜSSEN mindestens die institutionsinternen Anforderungen an die Verfahrensweisen zur Löschung und Vernichtung erfüllen.', 'Digitale wiederbeschreibbare Datenträger MÜSSEN vollständig mit einem Datenstrom aus Zufallswerten (z. Bsp. PRNG Stream) überschrieben werden, wenn sie nicht verschlüsselt eingesetzt werden.', 'Optische Datenträger MÜSSEN mindestens nach Sicherheitsstufe O-3 entsprechend der ISO/IEC 21964-2 vernichtet werden.', 'Papier MUSS mindestens nach Sicherheitsstufe P-3 entsprechend der ISO/IEC 21964-2 vernichtet werden.', 'In sonstigen Geräten integrierte Datenträger MÜSSEN über die integrierten Funktionen sicher gelöscht werden.', 'Ist das nicht möglich, MÜSSEN die Massenspeicher ausgebaut und entweder wie herkömmliche digitale Datenträger von einem separatem IT-System aus sicher gelöscht werden oder mindestens nach Sicherheitsstufe E-3 bzw. H-3 entsprechend der ISO/IEC 21964-2 vernichtet werden.', 'Können digitale Datenträger mit schützenswerten Informationen aufgrund eines Defekts nicht sicher entsprechend der Verfahren zur Löschung von Datenträgern gelöscht werden, dann SOLLTEN diese mindestens entsprechend der Sicherheitsstufe 3 nach ISO/IEC 21964-2 vernichtet werden.', 'Alternativ SOLLTE für den Fall, dass defekte Datenträger ausgetauscht oder repariert werden, vertraglich mit den hierzu beauftragten Dienstleistenden vereinbart werden, dass diese Datenträger durch die Dienstleistenden sicher vernichtet oder gelöscht werden.', 'Die Verfahrensweisen der Dienstleistenden SOLLTEN hierbei mindestens die institutionsinternen Anforderungen an die Verfahrensweisen zur Löschung und Vernichtung erfüllen.', 'Der Prozess zum Löschen und Vernichten von Datenträgern MUSS auch Datensicherungen, wenn erforderlich, berücksichtigen.', 'Dabei MUSS auch berücksichtigt werden, dass Informationen und Betriebsmittel eventuell erst gesammelt und erst später gelöscht oder vernichtet werden.', 'Eine solche zentrale Sammelstelle MUSS vor unbefugten Zugriffen abgesichert werden.', 'Die Institution MUSS das Löschen und Vernichten von Informationen regeln.', 'Dabei MÜSSEN die Fachverantwortlichen für jedes Fachverfahren bzw. Geschäftsprozess regeln, welche Informationen unter welchen Voraussetzungen gelöscht und entsorgt werden müssen.', 'Bevor schutzbedürftigen Informationen und Datenträger entsorgt werden, MÜSSEN sie sicher gelöscht oder vernichtet werden.', 'Einzelne Mitarbeitende MÜSSEN darüber informiert werden, welche Aufgaben sie zum sicheren Löschen und Vernichten erfüllen müssen.', 'Es MUSS festgelegt werden, auf welchen Wegen die jeweiligen Informationen ausgetauscht werden dürfen.', 'Die zentrale Verwaltungsstelle MUSS festlegen, wer welche Informationen erhalten und weitergeben darf.', 'Sie MUSS festlegen, wie die Informationen bei der Übertragung zu schützen sind.', 'Alle Beteiligten MÜSSEN vor dem Austausch von Informationen sicherstellen, dass die empfangende Stelle die notwendigen Berechtigungen für den Erhalt und die Weiterverarbeitung der Informationen besitzt.', 'Es MUSS geprüft werden, ob zusätzliche Schadcodescanner auf zentralen IT-Systemen installiert werden sollen.', 'Schadcodedetektionssysteme SOLLTEN eingesetzt und zentral verwaltet werden.', 'Für sicherheitsrelevante Ereignisse MÜSSEN geeignete Melde- und Alarmierungswege festgelegt und dokumentiert werden.', 'Es MUSS bestimmt werden, welche Stellen wann zu informieren sind.', 'Es MUSS aufgeführt sein, wie die jeweiligen Personen erreicht werden können.', 'Alle Personen, die für die Meldung bzw. Alarmierung relevant sind, MÜSSEN über ihre Aufgaben informiert sein.', 'Es SOLLTE eine organisatorische Regelung erstellt werden, unter welchen datenschutzrechtlichen Voraussetzungen die Logdaten manuell ausgewertet werden dürfen.', 'Wenn Detektionssysteme eingesetzt werden, dann MÜSSEN die Persönlichkeitsrechte bzw. Mitbestimmungsrechte der Mitarbeitendenvertretungen gewahrt werden.', 'Ebenso MUSS sichergestellt sein, dass alle weiteren relevanten gesetzlichen Bestimmungen beachtet werden, z. B. das Telemediengesetz (TMG), das Betriebsverfassungsgesetz und das Telekommunikationsgesetz.', 'Alle gelieferten Informationen SOLLTEN danach bewertet werden, ob sie relevant für den eigenen Informationsverbund sind.', 'Ist dies der Fall, SOLLTEN die Informationen entsprechend der Sicherheitsvorfallbehandlung eskaliert werden.', 'Um neue Erkenntnisse über sicherheitsrelevante Ereignisse für den eigenen Informationsverbund zu gewinnen, SOLLTEN externe Quellen herangezogen werden.', 'Ein Sicherheitsvorfall MUSS so weit wie möglich von Störungen im Tagesbetrieb abgegrenzt sein.', 'Alle an der Behandlung von Sicherheitsvorfällen beteiligten Mitarbeitenden MÜSSEN die Definition eines Sicherheitsvorfalls kennen.', 'Es MUSS geregelt werden, wer bei Sicherheitsvorfällen wofür verantwortlich ist.', 'Für alle Mitarbeiter MÜSSEN die Aufgaben und Kompetenzen bei Sicherheitsvorfällen festgelegt werden.', 'Insbesondere Mitarbeitende, die Sicherheitsvorfälle bearbeiten sollen, MÜSSEN über ihre Aufgaben und Kompetenzen unterrichtet werden.', 'Ebenso MÜSSEN die Meldepflichten für Behörden und regulierte Branchen berücksichtigt werden.', 'Damit ein Sicherheitsvorfall erfolgreich behoben werden kann, MÜSSEN die Zuständigen zunächst das Problem eingrenzen und die Ursache finden.', 'Von einem Sicherheitsvorfall MÜSSEN alle betroffenen internen und externen Stellen zeitnah informiert werden.', 'Dabei MUSS geprüft werden, ob der oder die Datenschutzbeauftragte, der Betriebs- und Personalrat sowie Mitarbeitende aus der Rechtsabteilung einbezogen werden müssen.', 'Außerdem MUSS gewährleistet sein, dass betroffene Stellen über die erforderlichen Maßnahmen informiert werden.', 'Anschließend MUSS die Ursache beseitigt und ein sicherer Zustand hergestellt werden.', 'Nach einem Sicherheitsvorfall MÜSSEN die betroffenen Komponenten vom Netz genommen werden.', 'Zudem MÜSSEN alle erforderlichen Daten gesichert werden, die Aufschluss über die Art und Ursache des Problems geben könnten.', 'Auf allen betroffenen Komponenten MÜSSEN das Betriebssystem und alle Applikationen auf Veränderungen untersucht werden.', 'Die Originaldaten MÜSSEN von schreibgeschützten Datenträgern wieder eingespielt werden.', 'Dabei MÜSSEN alle sicherheitsrelevanten Konfigurationen und Patches mit aufgespielt werden.', 'Wenn Daten aus Datensicherungen wieder eingespielt werden, MUSS sichergestellt sein, dass diese vom Sicherheitsvorfall nicht betroffen waren.', 'Nach einem Angriff MÜSSEN alle Zugangsdaten auf den betroffenen Komponenten geändert werden, bevor sie wieder in Betrieb genommen werden.', 'In einer Institution MUSS klar definiert sein, was ein Sicherheitsvorfall ist.', 'So MÜSSEN Verhaltensregeln für die verschiedenen Arten von Sicherheitsvorfällen beschrieben sein.', 'Die Ansprechpartner oder Ansprechpartnerinnen für alle Arten von Sicherheitsvorfällen MÜSSEN den Mitarbeitenden bekannt sein.', 'Kontaktinformationen MÜSSEN immer aktuell und leicht zugänglich sein.', 'Kontaktinformationen MÜSSEN immer aktuell und leicht zugänglich sein.', 'Eine aktuelle Liste von internen und externen Sicherheitsfachleuten MUSS vorhanden sein, die bei Sicherheitsvorfällen für Fragen aus den erforderlichen Themenbereichen hinzugezogen werden können.', 'Danach MÜSSEN die erforderlichen Maßnahmen auswählt werden, um das Problem zu beheben.', 'Dazu MÜSSEN der Betriebs- oder Personalrat sowie der oder die Datenschutzbeauftragte einbezogen werden.', 'Verfügt eine Institution nicht über ein eigenes Forensik-Team, MÜSSEN bereits in der Vorbereitungsphase mögliche geeignete Forensik-Dienstleistenden identifiziert werden.', 'Welche Forensik-Dienstleistende infrage kommen, MUSS dokumentiert werden.', 'Büroräume mit Publikumsverkehr DÜRFEN NICHT in sicherheitsrelevanten Bereichen liegen.', 'Dabei SOLLTE beachtet werden, dass Bildschirme nicht durch Unbefugte eingesehen werden können.', 'Alle Mitarbeitenden SOLLTEN dazu angehalten werden, seinen Arbeitsplatz aufgeräumt zu hinterlassen.', 'Die Mitarbeitenden SOLLTEN dafür sorgen, dass Unbefugte keine vertraulichen Informationen einsehen können.', 'Alle Mitarbeitenden SOLLTEN ihre Arbeitsplätze sorgfältig überprüfen und sicherstellen, dass keine vertraulichen Informationen frei zugänglich sind.', 'Die Mitarbeitenden SOLLTEN angewiesen werden, vertrauliche Dokumente und Datenträger verschlossen aufzubewahren, wenn sie nicht verwendet werden.', 'Dafür SOLLTEN geeignete Behältnisse in den Büroräumen oder in deren Umfeld aufgestellt werden.', 'Dafür MUSS es eine entsprechende Anweisung geben.', 'Der Zutritt zu schutzbedürftigen Gebäudeteilen und Räumen MUSS geregelt und kontrolliert werden.', 'Die Zahl der zutrittsberechtigten Personen SOLLTE für jeden Bereich auf ein Mindestmaß reduziert werden.', 'Alle erteilten Zutrittsberechtigungen SOLLTEN dokumentiert werden.', 'Alle Mitarbeitenden SOLLTEN dazu verpflichtet werden, der Anweisung nachzukommen.', 'Die entsprechenden Vorgaben SOLLTEN in einer geeigneten Anweisung festgehalten werden.', 'Alle Mitarbeitenden SOLLTEN dazu verpflichtet werden, der Anweisung nachzukommen.', 'Es MUSS regelmäßig überprüft werden, ob die Fenster und Innen- sowie Außentüren nach Verlassen des Gebäudes verschlossen sind.', 'Auf das LAN der Institution SOLLTEN ausschließlich dafür vorgesehene IT-Systeme zugreifen können.', 'Netzzugänge SOLLTEN so eingerichtet sein, dass verhindert wird, dass Dritte den internen Datenaustausch mitlesen können.', 'Netzanschlüsse in Besprechungs-, Veranstaltungs- oder Schulungsräumen SOLLTEN abgesichert werden.', 'Alle Dokumente SOLLTEN durch die Benutzenden auf zentral verwalteten Fileservern der Institution gespeichert werden.', 'Bei Räumlichkeiten, in denen sich IT-Systeme oder schützenswerte Informationen befinden, MÜSSEN die Türen beim Verlassen abgeschlossen werden.', 'Zusätzlich MUSS regelmäßig geprüft werden, ob die Fenster und Türen nach Verlassen der Räume verschlossen wurden.', 'Dies SOLLTE insbesondere in Bereichen mit Publikumsverkehr beachtet werden.', 'Zusätzlich MUSS regelmäßig geprüft werden, ob beim Verlassen des Büroraums die Fenster geschlossen und, wenn notwendig, die Türen abgeschlossen werden.', 'Weiterhin MUSS festgelegt werden, ob und auf welche Netzzugänge und TK-Schnittstellen externen Personen zugreifen dürfen.', 'Die Schulungs- und Präsentationsrechner SOLLTEN nur an ein separates, vom LAN der Institution getrenntes Datennetz angeschlossen werden.', 'Es SOLLTE sichergestellt werden, dass mitgebrachte IT-Systeme nicht über das Datennetz mit internen IT-Systemen der Institution verbunden werden können.', 'Unnötige Brandlasten MÜSSEN vermieden werden.', 'Es MUSS eine Brandschutzbeauftragte oder einen Brandschutzbeauftragten oder eine mit dem Aufgabengebiet betraute Person geben.', 'Ein Datennetz für externe Personen SOLLTE vom LAN der Institution getrennt werden.', 'Es MUSS geklärt werden, unter welchen Rahmenbedingungen Mitarbeitende auf welche Art von Informationen ihrer Institution zugreifen dürfen.', 'Diese Regelungen MÜSSEN den Mitarbeitenden in geeigneter Weise bekanntgegeben werden.', 'Für alle Tätigkeiten, die sich auf die Sicherheit der in den Fahrzeugen verarbeiteten Informationen auswirken können, MUSS vorher geregelt werden, ob sie in den Fahrzeugen durchgeführt werden dürfen.', 'Ergänzend MUSS festgelegt werden, welche Schutzvorkehrungen dabei zu treffen sind.', 'unter welchen Arbeitsplatzbedingungen schützenswerte Informationen bearbeitet werden dürfen,', 'wie sich Mitarbeitende am mobilen Arbeitsplatz vor ungewollter Einsichtnahme Dritter schützen,', 'Sie MÜSSEN zudem festlegen, wie verhindert wird, dass nicht autorisierte Personen die Informationen einsehen können.', 'Daher MÜSSEN ausreichend verschließbare Behältnisse (z. B. abschließbare Rollcontainer oder Schränke) vorhanden sein.', 'Alle Mitarbeitenden MÜSSEN ihre Arbeitsplätze aufgeräumt hinterlassen und sicherstellen, dass keine vertraulichen Informationen frei zugänglich sind.', 'Alle Türen des Rechenzentrums MÜSSEN stets verschlossen gehalten werden.', 'Falls sie doch vorhanden sind, MÜSSEN sie ebenso wie die Türen stets verschlossen gehalten werden.', 'Türen und Fenster MÜSSEN einen dem Sicherheitsniveau angemessenen Schutz gegen Angriffe und Umgebungseinflüsse bieten.', 'Im Falle eines Serverraums SOLLTE je nach Verfügbarkeitsanforderungen der IT-Systeme geprüft werden, ob der Betrieb einer USV notwendig ist.', 'Die USV MUSS ausreichend dimensioniert sein.', 'Bei relevanten Änderungen an den Verbrauchern MUSS überprüft werden, ob die vorhandenen USV-Systeme noch ausreichend dimensioniert sind.', 'Die USV MUSS regelmäßig gewartet und auf Funktionsfähigkeit getestet werden.', 'Dafür MÜSSEN die vom herstellenden Unternehmen vorgesehenen Wartungsintervalle eingehalten werden.', 'Die tatsächliche Wärmelast in den gekühlten Bereichen MUSS in regelmäßigen Abständen und nach größeren Umbauten überprüft werden.', 'Gebäude MÜSSEN entsprechend der Auflagen in der Baugenehmigung und dem Brandschutzkonzept folgend mit einer ausreichenden Anzahl von Rauchmeldern ausgestattet sein.', 'In Serverräumen ohne Lösch- oder Brandvermeidungsanlage MÜSSEN Handfeuerlöscher mit geeigneten Löschmitteln in ausreichender Zahl und Größe vorhanden sein.', 'Für im Rechenzentrum tätige Personen MUSS sichergestellt werden, dass diese keinen Zutritt zu IT-Systemen außerhalb ihres Tätigkeitsbereiches erhalten.', 'Ein Rechenzentrum MUSS insgesamt als geschlossener Sicherheitsbereich konzipiert werden.', 'Es MUSS verhindert werden, dass sich Brand und Rauch ausbreiten.', 'Für alle betriebsrelevanten Komponenten des Rechenzentrums MUSS eine unterbrechungsfreie Stromversorgung (USV) installiert werden.', 'Es MUSS sichergestellt werden, dass die Lufttemperatur und Luftfeuchtigkeit im IT-Betriebsbereich innerhalb der vorgeschriebenen Grenzwerte liegen.', 'Der Zutritt zum Rechenzentrum MUSS kontrolliert werden.', 'In einem Rechenzentrum MUSS eine Brandmeldeanlage installiert sein.', 'In einem Rechenzentrum MUSS eine Lösch- oder Brandvermeidungsanlage nach aktuellem Stand der Technik installiert sein.', 'Der Raum für technische Infrastruktur DARF KEIN Durchgangsraum sein.', 'Dabei MUSS sichergestellt sein, dass keine unnötigen oder zu weitreichenden Zutrittsrechte vergeben werden.', 'Es MUSS geregelt werden, welche Personen für welchen Zeitraum, für welche Bereiche und zu welchem Zweck den Raum betreten dürfen.', 'Der Raum MUSS vor Einbruch geschützt werden.', 'Der Raum für technische Infrastruktur MUSS gegen unberechtigten Zutritt geschützt werden.', 'Der Raum für technische Infrastruktur DARF NICHT zweckentfremdet werden, z. B. als Abstellraum oder Putzmittellager.', 'Der Zutritt MUSS auf ein Mindestmaß an Mitarbeitenden reduziert sein.', 'Gibt es dennoch Fenster, MÜSSEN diese beim Verlassen des Datenträgerarchivs geschlossen werden.', 'Ebenso MUSS beim Verlassen die Tür verschlossen werden.', 'Der Zutritt MUSS auf ein Mindestmaß an Mitarbeitenden reduziert sein.', 'Daher MUSS der Zutritt geregelt und kontrolliert werden.', 'Der Zutritt zum Datenträgerarchiv DARF NUR für befugte Personen möglich sein.', 'Es MUSS sichergestellt werden, dass die Datenträger im Datenträgerarchiv ausreichend vor Staub und Verschmutzung geschützt sind.', 'Im Brandfall MÜSSEN im Datenträgerarchiv geeignete Handfeuerlöscher leicht erreichbar sein.', 'Zur Sofortbekämpfung von Bränden MÜSSEN Handfeuerlöscher in der jeweils geeigneten Brandklasse (DIN EN 3 Tragbare Feuerlöscher) in ausreichender Zahl und Größe im Gebäude zur Verfügung stehen.', 'Brand- und Rauchschutztüren DÜRFEN NUR dann dauerhaft offen gehalten werden, wenn dies durch zugelassene Feststellanlagen erfolgt.', 'Ebenso MUSS darauf geachtet werden, dass Brand- und Rauchschutztüren tatsächlich geschlossen werden.', 'Es MUSS sichergestellt werden, dass in Räumen des Rechenzentrums keine besonderen Brandlasten vorhanden sind.', 'Ebenso MUSS darauf geachtet werden, dass Brand- und Rauchschutztüren tatsächlich geschlossen werden.', 'Es DÜRFEN NUR geeignete Räume als Büroräume genutzt werden.', 'Schützenswerte Räume oder Gebäudeteile SOLLTEN nicht in exponierten oder besonders gefährdeten Bereichen untergebracht sein.', 'In den Räumen vorhandene Gerätschaften MÜSSEN angemessen gegen Diebstahl gesichert werden.', 'Fenster und von außen zugängliche Türen, etwa von Balkonen oder Terrassen, MÜSSEN zu Zeiten, in denen ein Raum nicht besetzt ist, geschlossen werden.', 'Die Fenster der Besprechungs-, Veranstaltungs- und Schulungsräume MÜSSEN beim Verlassen verschlossen werden.', 'Wenn Mitarbeitende ihre Büroräume verlassen, SOLLTEN alle Fenster geschlossen werden.', 'Räume MÜSSEN verschlossen werden, falls dort vertrauliche Informationen zurückgelassen werden.', 'Befinden sich vertrauliche Informationen in dem Büroraum, MÜSSEN beim Verlassen die Türen abgeschlossen werden.', 'Es MUSS auch festgelegt werden, ob und unter welchen Bedingungen von externen Personen mitgebrachte IT-Systeme verwenden dürfen.', 'Die bestehenden Brandschutzvorschriften sowie die Auflagen der Bauaufsicht MÜSSEN eingehalten werden.', 'So MUSS darauf hingewiesen werden, Fenster zu schließen und Türen abzuschließen, wenn der häusliche Arbeitsplatz nicht besetzt ist.', 'Es MUSS sichergestellt werden, dass unbefugte Personen zu keiner Zeit den häuslichen Arbeitsplatz betreten und auf dienstliche IT und Unterlagen zugreifen können.', 'Wenn der mobile Arbeitsplatz nicht besetzt ist, MÜSSEN Fenster und Türen abgeschlossen werden.', 'Ist dies nicht möglich, z. B. im Zug, MÜSSEN die Mitarbeitenden alle Unterlagen und IT-Systeme an sicherer Stelle verwahren oder mitführen, wenn sie abwesend sind.', 'Es MUSS sichergestellt werden, dass unbefugte Personen zu keiner Zeit auf dienstliche IT und Unterlagen zugreifen können.', 'Es SOLLTEN die dafür benötigten Entsorgungsmöglichkeiten verfügbar sein.', 'Ist dies der Fall, MÜSSEN die Datenträger und Dokumente wieder mit zurücktransportiert werden und auf institutseigenem Wege entsorgt oder vernichtet werden.', 'Bevor Fahrzeuge endgültig ausgesondert werden, SOLLTE anhand der Inventarliste geprüft werden, ob keine inventarisierten Gegenstände und darüber hinaus relevanten Gegenstände zurückgelassen worden sind.', 'Es MUSS geregelt werden, welche Datenträger und Unterlagen am häuslichen Arbeitsplatz bearbeitet und zwischen der Institution und dem häuslichen Arbeitsplatz hin und her transportiert werden dürfen.', 'Für alle Arbeiten unterwegs MUSS geregelt werden, welche Informationen außerhalb der Institution transportiert und bearbeitet werden dürfen.', 'So MUSS festgelegt werden, welche IT-Systeme und Datenträger mitgenommen werden dürfen, wer diese mitnehmen darf und welche grundlegenden Sicherheitsanforderungen dabei beachtet werden müssen.', 'Außerdem MÜSSEN sie darüber informiert werden, welche Art von Informationen auf mobilen IT-Systemen verarbeitet werden darf.', 'Die Regelungen MÜSSEN vorgeben, ob und wie schützenswerte Informationen an fremden IT-Systemen bearbeitet werden dürfen.', 'Ist dies der Fall, MÜSSEN die Datenträger und Dokumente wieder mit zurücktransportiert werden und auf institutseigenem Wege entsorgt oder vernichtet werden.', 'Wird der Arbeitsplatz nur kurz verlassen, MÜSSEN die eingesetzten IT-Systeme gesperrt werden, sodass sie nur nach erfolgreicher Authentisierung wieder benutzt werden können.', 'Die Mitnahme von IT-Komponenten und Datenträgern MUSS klar geregelt werden.', 'Es SOLLTE klare schriftliche Regeln dazu geben, ob, wie und zu welchen Anlässen Wechseldatenträger mitgenommen werden dürfen.', 'Darin SOLLTE festgelegt sein, welche Datenträger von wem außer Haus transportiert werden dürfen und welche Sicherheitsmaßnahmen dabei zu beachten sind.', 'Die Benutzenden von mobilen Endgeräten MÜSSEN für den Wert mobiler IT-Systeme und den Wert der darauf gespeicherten Informationen sensibilisiert werden.', 'Außerdem MUSS geregelt werden, in welchem Umfang Infotainmentsysteme, Anwendungen und sonstige Services der Fahrzeuge genutzt werden dürfen.', 'Generell MÜSSEN Datenträger und andere Unterlagen sicher transportiert werden.', 'Hierbei MUSS klar geregelt werden, welche Informationen dabei transportiert und bearbeitet werden dürfen.', 'Für alle Arbeiten unterwegs MUSS geregelt werden, welche Informationen außerhalb der Institution transportiert und bearbeitet werden dürfen.', 'Es MÜSSEN aber auch Ausschlusskriterien definiert werden, die gegen einen mobilen Arbeitsplatz sprechen.', 'Dienstliche Unterlagen und Datenträger MÜSSEN am häuslichen Arbeitsplatz so aufbewahrt werden, dass keine unbefugten Personen darauf zugreifen können.', 'Dies MUSS für jede Art von Information gelten, auch für Gespräche in den Fahrzeugen.', 'Mitarbeitende SOLLTEN ihrer Institution umgehend melden, wenn Informationen, IT-Systeme oder Datenträger verlorengegangen sind oder gestohlen wurden.', 'Dafür SOLLTE es klare Meldewege und Ansprechpartner innerhalb der Institution geben.', 'Die Institution MUSS regeln, wie Mitarbeitende mit institutionsfremden IT-Systemen arbeiten dürfen.', 'Sie MÜSSEN über die spezifischen Gefährdungen und Maßnahmen der von ihnen benutzten IT-Systeme aufgeklärt werden.', 'Mitarbeitende SOLLTEN ihrer Institution umgehend melden, wenn Informationen, IT-Systeme oder Datenträger verlorengegangen sind oder gestohlen wurden.', 'Dafür SOLLTE es klare Meldewege und Ansprechpartner innerhalb der Institution geben.', 'Vertrauliche Informationen SOLLTEN sicher entsorgt werden.', 'Vertrauliche Informationen SOLLTEN auch unterwegs sicher entsorgt werden.', 'Die Institutionsleitung MUSS die Gesamtverantwortung für Informationssicherheit in der Institution übernehmen.', 'Die Institutionsleitung MUSS Informationssicherheit vorleben.', 'Die Institutionsleitung MUSS sich regelmäßig über den Status der Informationssicherheit informieren lassen.', 'Insbesondere MUSS sich die Institutionsleitung über mögliche Risiken und Konsequenzen aufgrund fehlender Sicherheitsmaßnahmen informieren lassen.', 'Die Institutionsleitung MUSS die Sicherheitsstrategie und die Sicherheitsziele tragen und verantworten.', 'Die Institutionsleitung MUSS den Sicherheitsprozess initiieren, steuern und kontrollieren.', 'Die Institutionsleitung MUSS den Sicherheitsprozess initiieren und etablieren.', 'Dafür MUSS die Institutionsleitung angemessene Sicherheitsziele sowie eine Strategie für Informationssicherheit festlegen und dokumentieren.', 'Die Institutionsleitung MUSS die Zuständigkeiten für Informationssicherheit festlegen.', 'Die zuständigen Mitarbeitenden MÜSSEN mit den erforderlichen Kompetenzen und Ressourcen ausgestattet werden.', 'Alle Mitarbeitenden MÜSSEN in den Sicherheitsprozess integriert sein.', 'Hierfür MÜSSEN sie über Hintergründe und die für sie relevanten Gefährdungen informiert sein.', 'Sie MÜSSEN Sicherheitsmaßnahmen kennen und umsetzen, die ihren Arbeitsplatz betreffen.', 'Die Mitarbeitenden MÜSSEN darüber aufgeklärt werden, welche Konsequenzen eine Verletzung der Sicherheitsvorgaben haben kann.', 'Dabei SOLLTEN alle Endgeräte, die für das Management der IT-Infrastruktur benötigt werden, in dedizierten Netzsegmenten positioniert werden.', 'Schützenswerte Informationen MÜSSEN über nach dem derzeitigen Stand der Technik sichere Protokolle übertragen werden, falls nicht über vertrauenswürdige dedizierte Netzsegmente (z. B. innerhalb des Managementnetzes) kommuniziert wird.', 'Können solche Protokolle nicht genutzt werden, MUSS nach Stand der Technik angemessen verschlüsselt und authentisiert werden (siehe NET.3.3 VPN).', 'Netze, die nicht vertrauenswürdig sind, MÜSSEN wie das Internet behandelt und entsprechend abgesichert werden.', 'Die Kommunikation zwischen diesen Netzsegmenten MUSS mindestens durch einen zustandsbehafteten Paketfilter kontrolliert werden.', 'Eine externe DMZ MUSS am äußeren Paketfilter angeschlossen werden.', 'In der zweistufigen Firewall-Architektur MUSS jeder ein- und ausgehende Datenverkehr durch den äußeren Paketfilter bzw. den internen Paketfilter kontrolliert und gefiltert werden.', 'Sie MUSS einen Netzplan beinhalten.', 'Die Kommunikation von und zu diesen Management-Netzsegmenten SOLLTE auf die notwendigen Management-Protokolle mit definierten Kommunikations-Endpunkten beschränkt werden.', 'Die Dokumentation MUSS nachhaltig gepflegt werden.', 'Die Datenflüsse MÜSSEN durch die Firewall-Struktur auf die benötigten Protokolle und Kommunikationsbeziehungen eingeschränkt werden.', 'Ein IP-basierter Zugriff auf das interne Netz MUSS über einen sicheren Kommunikationskanal erfolgen.', 'IT-Systeme DÜRFEN NICHT via Internet oder externer DMZ auf das interne Netz zugreifen.', 'Für jedes Netz MUSS festgelegt werden, inwieweit es als vertrauenswürdig einzustufen ist.', 'Nicht vertrauenswürdige Netze (z. B. Internet) und vertrauenswürdige Netze (z. B. Intranet) MÜSSEN mindestens durch eine zweistufige Firewall-Struktur, bestehend aus zustandsbehafteten Paketfiltern (Firewall), getrennt werden.', 'Der Internetverkehr MUSS über die Firewall-Struktur geführt werden (siehe NET.1.1.A4 Netztrennung in Zonen).', 'Das Gesamtnetz MUSS mindestens in folgende drei Zonen physisch separiert sein: internes Netz, demilitarisierte Zone (DMZ) und Außenanbindungen (inklusive Internetanbindung sowie Anbindung an andere nicht vertrauenswürdige Netze).', 'Die Zonenübergänge MÜSSEN durch eine Firewall abgesichert werden.', 'Clients und Server MÜSSEN in unterschiedlichen Netzsegmenten platziert werden.', 'Die Firewall-Strukur MUSS für alle Dienste bzw. Anwendungen, die aus dem Internet erreichbar sind, um eine sogenannte externe DMZ ergänzt werden.', 'Um Internet und externe DMZ netztechnisch zu trennen, MUSS mindestens ein zustandsbehafteter Paketfilter eingesetzt werden.', 'Die Datenflüsse MÜSSEN durch die Firewall-Struktur auf die benötigten Protokolle und Kommunikationsbeziehungen eingeschränkt werden.', 'Für Gastzugänge und für Netzbereiche, in denen keine ausreichende interne Kontrolle über die Endgeräte gegeben ist, MÜSSEN dedizierte Netzsegmente eingerichtet werden.', 'Grundsätzlich DÜRFEN im Netzmanagement KEINE unsicheren Versionen des Simple Network Management Protocol (SNMP) eingesetzt werden.', 'Werden dennoch unsichere Protokolle verwendet und nicht über andere sichere Netzprotokolle (z. B. VPN oder TLS) abgesichert, MUSS ein separates Managementnetz genutzt werden.', 'Ist dies nicht möglich, MUSS ein eigens dafür vorgesehenes Administrationsnetz (Out-of-Band-Management) verwendet werden (siehe NET.1.1 Netzarchitektur und -design).', 'unerlaubte Zugriffe bzw. Zugriffsversuche,', 'Leistungs- oder Verfügbarkeitsschwankungen des Netzes,', 'Fehler in automatischen Prozessen (z. B. bei der Konfigurationsverteilung) sowie', 'eingeschränkte Erreichbarkeit von Netzkomponenten.', 'Die Uhrzeit SOLLTE an jedem Standort innerhalb des lokalen Netzes mittels NTP-Service synchronisiert werden.', 'Erfolgt die Netzmanagement-Kommunikation über die produktive Infrastruktur, MÜSSEN dafür sichere Protokolle verwendet werden.', 'Mindestens folgende Ereignisse MÜSSEN protokolliert werden:', 'Alle Komponenten des Netzmanagements, inklusive der eingebundenen Netzkomponenten, MÜSSEN eine synchrone Uhrzeit nutzen.', 'Access Points DÜRFEN NUR über eine geeignet verschlüsselte Verbindung administriert werden.', 'Außerdem MÜSSEN unsichere Administrationszugänge abgeschaltet werden.', 'Ebenso MUSS der Abdeckungsbereich des WLAN festgelegt werden.', 'Geräte, die von anerkannt sicheren Verfahren auf unsichere zurückgreifen müssen, DÜRFEN NICHT mehr eingesetzt werden.', 'Außeninstallationen MÜSSEN vor Witterungseinflüssen und elektrischen Entladungen geeignet geschützt werden.', 'Es MUSS ausgeschlossen werden, dass entwendete Geräte unberechtigt verwendet werden, um auf das Netz der Institution zuzugreifen.', 'Es MUSS sichergestellt sein, dass mittels der WLAN-Kommunikation keine Sicherheitszonen gekoppelt werden und hierdurch etablierte Schutzmaßnahmen umgangen werden.', 'WLANs SOLLTEN regelmäßig daraufhin überprüft werden, ob eventuell Sicherheitslücken existieren.', 'Insbesondere MUSS geklärt und festgelegt werden, in welchen Organisationseinheiten, für welche Anwendungen und zu welchem Zweck WLANs eingesetzt und welche Informationen darüber übertragen werden dürfen.', 'Generell MUSS sichergestellt sein, dass nur als allgemein sicher anerkannte Verfahren zur Authentisierung und Verschlüsselung eingesetzt werden.', 'Die Kommunikation über die Luftschnittstelle MUSS komplett kryptografisch abgesichert werden.', 'Access Points MÜSSEN zugriffs- und diebstahlsicher montiert werden.', 'Voreingestellte SSIDs (Service Set Identifiers), Zugangskennwörter oder kryptografische Schlüssel MÜSSEN vor dem produktiven Einsatz geändert werden.', 'Über öffentlich zugängliche WLANs DÜRFEN die Benutzenden NUR über ein Virtual Private Network (VPN) auf interne Ressourcen der Institution zugreifen.', 'Die Richtlinie MUSS Angaben dazu enthalten, welche Daten im WLAN genutzt und übertragen werden dürfen und welche nicht.', 'In einer solchen Benutzerrichtlinie MÜSSEN die Besonderheiten bei der WLAN-Nutzung beschrieben sein, z. B. ob, wie und mit welchen Geräten Hotspots genutzt werden dürfen.', 'Ebenso MÜSSEN die Benutzenden für die möglichen Gefahren sensibilisiert werden, die von fremden WLANs ausgehen.', 'Die automatische Anmeldung an WLANs SOLLTE deaktiviert werden.', 'Besonders schützenswerte Speichermedien für die Datensicherung SOLLTEN nur während der Datensicherung und Datenwiederherstellung mit dem Netz der Institution oder dem Ursprungssystem verbunden werden.', 'Um Router und Switches zu administrieren bzw. zu überwachen, SOLLTEN geeignet verschlüsselte Protokolle eingesetzt werden.', 'Sollte dennoch auf unverschlüsselte Protokolle zurückgegriffen werden, MUSS für die Administration ein eigenes Administrationsnetz (Out-of-Band-Management) genutzt werden.', 'Es MUSS sichergestellt sein, dass aus nicht vertrauenswürdigen Netzen heraus nicht direkt auf die Administrationsschnittstellen zugegriffen werden kann.', 'Konfigurationsänderungen (möglichst automatisch),', 'Reboot,', 'Systemfehler,', 'Statusänderungen pro Interface, System und Netzsegment sowie', 'Login-Fehler.', 'Alle für das Management-Interface nicht benötigten Dienste MÜSSEN deaktiviert werden.', 'Verfügt eine Netzkomponente über eine dedizierte Hardwareschnittstelle, MUSS der unberechtigte Zugriff darauf in geeigneter Weise unterbunden werden.', 'Nicht benötigte Dienste, Protokolle und funktionale Erweiterungen MÜSSEN deaktiviert oder ganz deinstalliert werden.', 'Ebenfalls MÜSSEN nicht benutzte Schnittstellen auf Routern und Switches deaktiviert werden.', 'Unbenutzte Netzports MÜSSEN nach Möglichkeit deaktiviert oder zumindest einem dafür eingerichteten Unassigned-VLAN zugeordnet werden.', 'Firewalls SOLLTEN ausschließlich über ein separates Managementnetz (Out-of-Band-Management) administriert werden.', 'Alle unsicheren Managementprotokolle SOLLTEN deaktiviert werden (siehe NET.1.2 Netz-Management).', 'Um die Firewall zu administrieren bzw. zu überwachen, DÜRFEN NUR sichere Protokolle eingesetzt werden.', 'Alternativ MUSS ein eigens dafür vorgesehenes Administrationsnetz (Out-of-Band-Management) verwendet werden.', 'Die Kommunikation im Managementnetz SOLLTE über Management-Firewalls (siehe NET.1.1 Netz-Architektur und -design) auf wenige Managementprotokolle mit genau festgelegten Ursprüngen und Zielen beschränkt werden.', 'Alle Administrations- und Managementzugänge der Firewall MÜSSEN auf einzelne Quell-IP-Adressen bzw. -Adressbereiche eingeschränkt werden.', 'Es MUSS sichergestellt sein, dass aus nicht vertrauenswürdigen Netzen heraus nicht auf die Administrationsschnittstellen zugegriffen werden kann.', 'abgewiesene Netzverbindungen (Quell- und Ziel-IP-Adressen, Quell- und Zielport oder ICMP/ICMPv6-Typ, Datum, Uhrzeit),', 'fehlgeschlagene Zugriffe auf System-Ressourcen aufgrund fehlerhafter Authentisierungen, mangelnder Berechtigung oder nicht vorhandener Ressourcen,', 'Fehlermeldungen der Firewall-Dienste,', 'allgemeine Systemfehlermeldungen und', 'Konfigurationsänderungen (möglichst automatisch).', 'Es MUSS sichergestellt sein, dass von außen keine unerlaubten Verbindungen in das geschützte Netz aufgebaut werden können.', 'Für die Firewall MÜSSEN eindeutige Regeln definiert werden, die festlegen, welche Kommunikationsverbindungen und Datenströme zugelassen werden.', 'Basierend auf den Firewall-Regeln aus NET.3.2.A2 Festlegen der Firewall-Regeln MÜSSEN geeignete Filterregeln für den Paketfilter definiert und eingerichtet werden.', 'Ein Paketfilter MUSS so eingestellt sein, dass er alle ungültigen TCP-Flag-Kombinationen verwirft.', 'Grundsätzlich MUSS immer zustandsbehaftet gefiltert werden.', 'Auch für die verbindungslosen Protokolle UDP und ICMP MÜSSEN zustandsbehaftete Filterregeln konfiguriert werden.', 'Wenn das IPv4- oder IPv6-Protokoll in einem Netzsegment nicht benötigt wird, SOLLTE es am jeweiligen Firewall-Netzzugangspunkt (z. B. am entsprechenden Firewall-Interface) deaktiviert werden.', 'Falls das IPv4- oder IPv6-Protokoll nicht benötigt bzw. eingesetzt wird, SOLLTE es auf der Firewall komplett deaktiviert werden.', 'Die Firewall MUSS die Protokolle ICMP und ICMPv6 restriktiv filtern.', 'Bevor eine Firewall eingesetzt wird, MUSS sie sicher konfiguriert werden.', 'Die Uhrzeit der Firewall SOLLTE mit einem Network-Time-Protocol (NTP)-Server synchronisiert werden.', 'Falls VPN-Dienstleistende eingesetzt werden, MÜSSEN mit diesen Service Level Agreements (SLAs) ausgehandelt und schriftlich dokumentiert werden.', 'Es MUSS sichergestellt werden, dass nur qualifiziertes Personal VPN-Komponenten installiert.', 'So SOLLTEN für das VPN die Verschlüsselungsverfahren, VPN-Endpunkte, erlaubten Zugangsprotokolle, Dienste und Ressourcen festgelegt werden.', 'So SOLLTEN für das VPN die Verschlüsselungsverfahren, VPN-Endpunkte, erlaubten Zugangsprotokolle, Dienste und Ressourcen festgelegt werden.', 'Es MUSS regelmäßig getestet werden, ob die Datensicherungen wie gewünscht funktionieren, vor allem, ob gesicherte Daten einwandfrei und in angemessener Zeit zurückgespielt werden können.', 'Die TK-Anlage SOLLTE in einem separaten sowie geeignet gesicherten Raum untergebracht sein.', 'Die TK-Anlage SOLLTE in einem geeigneten Raum untergebracht sein.', 'Die Schnittstellen an der TK-Anlage, besonders nicht genutzte Schnittstellen, SOLLTEN geeignet geschützt werden.', 'Alle Administrationsarbeiten an der TK-Anlage MÜSSEN ebenfalls protokolliert werden.', 'Der Zutritt und Zugang zur TK-Anlage SOLLTE nur einem eingeschränkten Personenkreis möglich sein.', 'Der Umfang der verfügbaren Leistungsmerkmale SOLLTE auf das notwendige Minimum beschränkt werden.', 'Nur die benötigten Leistungsmerkmale SOLLTEN freigeschaltet werden.', 'Die nicht benötigten oder wegen ihres Missbrauchspotenzials als kritisch eingestuften Leistungsmerkmale SOLLTEN so weit wie möglich an der zentralen Anlage abgeschaltet werden.', 'Protokolliert werden MÜSSEN zusätzlich alle systemtechnischen Eingriffe, die Programmveränderungen beinhalten, sowie Auswertungsläufe, Datenübermittlungen und Datenzugriffe.', 'Nicht benötigte Funktionen der Endgeräte MÜSSEN deaktiviert werden.', 'Alle nicht benötigten Dienste der VoIP-Middleware MÜSSEN deaktiviert werden.', 'Eine verständliche Bedienungsanleitung MUSS am Faxgerät ausliegen.', 'Faxgeräte MÜSSEN so aufgestellt werden, dass eingegangene Faxsendungen nicht von Unberechtigten eingesehen oder entnommen werden können.', 'Außerdem MUSS eine Anweisung zur korrekten Faxnutzung ausliegen.', 'Ebenfalls SOLLTEN geeignete Sach-Ressourcen bereitstehen.', 'Administrationsaufgaben und sonstige Betriebsaufgaben MÜSSEN durch unterschiedliche Rollen getrennt werden.', 'Der IT-Betrieb SOLLTE über ausreichende Personal-Ressourcen verfügen, um einen ordnungsgemäßen IT-Betrieb gewährleisten zu können.', 'Für alle betriebenen IT-Komponenten MUSS festgelegt werden, welche Aufgaben für den IT-Betrieb anfallen und wer dafür zuständig ist.', 'Die Personal-Ressourcen SOLLTEN mit angemessenen Redundanzen und Reserven geplant werden und auch kurzfristige Personalausfälle sowie temporär erhöhte Personalbedarfe berücksichtigen.', 'Sammel-Accounts DÜRFEN NUR in begründeten Ausnahmefällen eingerichtet werden.', 'Insbesondere MÜSSEN die Berechtigungen von ausgeschiedenem Personal auf den IT-Komponenten entfernt werden.', 'Ebenso MÜSSEN die Rollen und Berechtigungen gelöscht werden, wenn IT-Komponenten außer Betrieb genommenen werden.', 'Weiterhin MÜSSEN die Schnittstellen und Meldewege sowie das Eskalationsmanagement zwischen verschiedenen Betriebseinheiten und gegenüber anderen organisatorischen Einheiten der Institution festgelegt werden.', 'Es MÜSSEN Rollen definiert werden, die ausschließlich zur IT-Administration vergeben werden.', 'Die Zugangskennungen, die zur IT-Administration genutzt werden, SOLLTEN sich von Zugangskennungen unterscheiden, die in anderem Kontext genutzt werden.', 'Die Vertretung MUSS über die notwendigen administrativen Berechtigungen (organisatorisch und technisch) verfügen, um die Tätigkeit durchführen zu können.', 'Insbesondere MÜSSEN persönliche administrative Konten gesperrt und Passwörter aller administrativer Konten geändert werden, die der Person bekannt sind.', 'Die Institution MUSS jederzeit nachweisen können, welche Person welche administrativen Tätigkeiten durchgeführt hat.', 'Dazu SOLLTEN alle Administrierenden über eine eigene Zugangskennung verfügen.', 'Auch Vertretungen von Administrierenden SOLLTEN eigene Zugangskennungen erhalten.', 'Jeder Anmeldevorgang (Login) über eine Administrationskennung MUSS protokolliert werden.', 'Alle notwendigen IT-Administrationstätigkeiten MÜSSEN durch Berechtigungen in den Administrationsrollen nach dem Minimalprinzip abgedeckt sein.', 'Eine benannte Vertretung MUSS über die im Kontext der Administrationsaufgabe notwendigen Kenntnisse verfügen.', 'Die Regelung der Vertretung MUSS Mangel- und Notfallsituationen berücksichtigen.', 'Wenn eine Anwendung zur Erfüllung einer Administrationsaufgabe benutzt wird, DARF NICHT dieselbe Instanz dieser Anwendung für andere Aufgaben verwendet werden.', 'Für jede Administrationsaufgabe MUSS eine Vertretung benannt werden.', 'Falls eine Person von Administrationsaufgaben entbunden wird, MÜSSEN ihr alle damit zusammenhängenden privilegierten Berechtigungen auf organisatorischer und technischer Ebene entzogen werden.', 'Die durchführende Person MUSS wissen, bei welchem Teil ihrer Aufgabe es sich um administrative Tätigkeiten handelt.', 'Administrative Tätigkeiten MÜSSEN nachweisbar sein.', 'Die IT-Administration unterschiedlicher Ebenen der IT-Komponenten, z. B. die Trennung von Betriebssystem- und Anwendungsadministration, MUSS bei der Konzeption der Administrationsrollen berücksichtigt werden.', 'Administrative Schnittstellen und Funktionen DÜRFEN NUR berechtigten Personen zur Verfügung stehen.', 'Für diese Schnittstellen und Funktionen MÜSSEN geeignete Verfahren zur Authentisierung festgelegt werden.', 'Es MUSS sichergestellt sein, dass IT-Administrationstätigkeiten nur durchgeführt werden können, falls vorher eine dementsprechende Authentisierung erfolgt ist.', 'Aufgaben, die keine Administrationsrechte benötigen, DÜRFEN NICHT mit Administrationsrechten ausgeführt werden.', 'Insbesondere MUSS festgelegt werden, wie diese Mechanismen abgesichert und passend konfiguriert werden.', 'Außerdem SOLLTEN neue Komponenten daraufhin überprüft werden, welche Update-Mechanismen sie haben.', 'Basierend auf dem Konzept für das Patch- und Änderungsmanagement MÜSSEN Patches zeitnah nach Veröffentlichung bewertet und entsprechend priorisiert werden.', 'Für die Bewertung SOLLTE geprüft werden, ob es zu diesem Patch bekannte Schwachstellen gibt.', 'Wenn Patches installiert und Änderungen durchgeführt werden, MÜSSEN Rückfall-Lösungen vorhanden sein.', 'Ist dies nicht der Fall, DÜRFEN diese Hardware- oder Software-Produkte NICHT mehr verwendet werden.', 'Alle Patches und Änderungen MÜSSEN geeignet geplant, genehmigt und dokumentiert werden.', 'Innerhalb der Strategie zum Patch- und Änderungsmanagement MUSS definiert werden, wie mit integrierten Update-Mechanismen (Autoupdate) der eingesetzten Software umzugehen ist.', 'IT-Systeme und Software SOLLTEN regelmäßig aktualisiert werden.', 'Grundsätzlich SOLLTEN Patches zeitnah nach Veröffentlichung eingespielt werden.', 'Patches und Änderungen SOLLTEN vorab geeignet getestet werden (siehe hierzu auch OPS.1.1.6 Software-Tests und Freigaben).', 'Insbesondere SOLLTEN auch die gewünschten Sicherheitseinstellungen erhalten bleiben.', 'Falls Hardware- oder Software-Produkte eingesetzt werden sollen, die nicht mehr von den Herstellenden unterstützt werden oder für die kein Support mehr vorhanden ist, MUSS geprüft werden, ob diese dennoch sicher betrieben werden können.', 'Für Gateways und IT-Systeme, die dem Datenaustausch dienen, MUSS ein geeignetes Virenschutzprogramm ausgewählt und installiert werden.', 'Sie MÜSSEN die grundlegenden Verhaltensregeln einhalten, um die Gefahr eines Befalls durch Schadprogramme zu reduzieren.', 'Benutzende MÜSSEN regelmäßig über die Bedrohung durch Schadprogramme aufgeklärt werden.', 'Sie MÜSSEN entsprechenden Kontaktpersonen für den Fall eines Verdacht auf eine Infektion mit einem Schadprogramm bekannt sein.', 'Sie MÜSSEN sich an die ihnen benannten Kontaktpersonen wenden, wenn der Verdacht auf eine Infektion mit einem Schadprogramm besteht.', 'Es MUSS sichergestellt werden, dass die Benutzenden keine sicherheitsrelevanten Änderungen an den Einstellungen der Antivirenprogramme vornehmen können.', 'Abhängig vom verwendeten Betriebssystem, anderen vorhandenen Schutzmechanismen sowie der Verfügbarkeit geeigneter Virenschutzprogramme MUSS für den konkreten Einsatzzweck ein entsprechendes Schutzprogramm ausgewählt und installiert werden.', 'Das Virenschutzprogramm MUSS für seine Einsatzumgebung geeignet konfiguriert werden.', 'Auf den damit ausgestatteten IT-Systemen MÜSSEN die Virenschutzprogramme nach Empfehlung der herstellenden Institution regelmäßig und zeitnah aktualisiert werden.', 'Falls Cloud-Funktionen solcher Produkte verwendet werden, MUSS sichergestellt werden, dass dies nicht im Widerspruch zum Daten- oder Geheimschutz steht.', 'Es MUSS geprüft werden, welche Schutzmechanismen die verwendeten IT-Systeme sowie die darauf genutzten Betriebssysteme und Anwendungen bieten.', 'Diese Mechanismen MÜSSEN genutzt werden, sofern es keinen mindestens gleichwertigen Ersatz gibt oder gute Gründe dagegen sprechen.', 'Es SOLLTE sichergestellt sein, dass die ausführenden Administrierenden selbst keine Berechtigung haben, die aufgezeichneten Protokollierungsdaten zu verändern oder zu löschen.', 'Protokollierungsdaten MÜSSEN nach einem festgelegten Prozess gelöscht werden.', 'In angemessenen Intervallen MUSS stichpunktartig überprüft werden, ob die Protokollierung noch korrekt funktioniert.', 'Falls betriebs- und sicherheitsrelevante Ereignisse nicht auf einem IT-System protokolliert werden können, MÜSSEN zusätzliche IT-Systeme zur Protokollierung (z. B. von Ereignissen auf Netzebene) integriert werden.', 'Darüber hinaus MÜSSEN eventuelle Persönlichkeitsrechte bzw. Mitbestimmungsrechte der Mitarbeitendenvertretungen gewahrt werden.', 'Ebenso MUSS sichergestellt sein, dass alle weiteren relevanten gesetzlichen Bestimmungen beachtet werden.', 'Es MUSS sichergestellt sein, dass das Datums- und Zeitformat der Protokolldateien einheitlich ist.', 'Es MUSS technisch unterbunden werden, dass Protokollierungsdaten unkontrolliert gelöscht oder verändert werden.', 'Alle sicherheitsrelevanten Ereignisse von IT-Systemen und Anwendungen MÜSSEN protokolliert werden.', 'Die Systemzeit aller protokollierenden IT-Systeme und Anwendungen MUSS immer synchron sein.', 'Es MUSS sichergestellt werden, dass nur autorisierte Personen Zugang zu den Telearbeitsrechnern haben.', 'Anhand eines Leitfadens MÜSSEN die Mitarbeitenden für die Gefahren sensibilisiert werden, die mit der Telearbeit verbunden sind.', 'Alle anderen Fernwartungsverbindungen SOLLTEN verschlüsselt werden.', 'Die Institution SOLLTE festlegen, unter welchen Umständen Online-Dienste zur Fernwartung genutzt werden dürfen, bei denen die Verbindung über einen externen Server hergestellt wird.', 'Die IT-Systeme SOLLTEN keine automatisierten Verbindungen zum Online-Dienst aufbauen.', 'Es SOLLTE sichergestellt werden, dass der eingesetzte Online-Dienst die übertragenen Informationen Ende-zu-Ende-verschlüsselt.', 'Dabei MUSS mindestens berücksichtigt werden, welche IT-Systeme ferngewartet werden sollen und wer dafür zuständig ist.', 'Wird per Fernwartung auf Desktop-Umgebungen von Clients zugegriffen, MUSS die Fernwartungssoftware so konfiguriert sein, dass sie eine Verbindung erst nach expliziter Zustimmung der Benutzenden aufbaut.', 'Die möglichen Zugänge und Kommunikationsverbindungen für die Fernwartung MÜSSEN auf das notwendige Maß beschränkt werden.', 'Alle Fernwartungsverbindungen MÜSSEN nach dem Fernzugriff getrennt werden.', 'Es MUSS sichergestellt werden, dass Fernwartungssoftware nur auf IT-Systemen installiert ist, auf denen sie benötigt wird.', 'Fernwartungsverbindungen über nicht vertrauenswürdige Netze MÜSSEN verschlüsselt werden.', 'Wird auf die Fernwartungszugänge von IT-Systemen im internen Netz über ein öffentliches Datennetz zugegriffen, SOLLTE ein abgesichertes Virtuelles Privates Netz (VPN) genutzt werden.', 'Der Einsatz solcher Dienste SOLLTE generell auf möglichst wenige Fälle beschränkt werden.', 'Die Institution SOLLTE sich von den Cloud-Diensteanbietenden regelmäßig nachweisen lassen, dass die vereinbarten Sicherheitsanforderungen erfüllt sind.', 'Der Nachweis SOLLTE auf einem international anerkannten Regelwerk basieren (z. B. IT-Grundschutz, ISO/IEC 27001, Anforderungskatalog Cloud Computing (C5), Cloud Controls Matrix der Cloud Security Alliance).', 'Auch SOLLTE vereinbart werden, wie die Daten der Institution sicher zu löschen sind.', 'Ebenso SOLLTEN Kündigungsregelungen schriftlich fixiert werden.', 'Es MUSS klar erkennbar sein, wie die Verantwortungsbereiche zwischen Cloud-Diensteanbietenden und der auftraggebenden Institution voneinander abgegrenzt sind.', 'Zusätzlich SOLLTEN Eskalationsstufen und Kommunikationswege zwischen der Institution und den Cloud-Diensteanbietenden definiert werden.', 'Wenn Cloud-Dienste von internationalen Anbietenden genutzt werden, MÜSSEN die speziellen länderspezifischen Anforderungen und gesetzlichen Bestimmungen berücksichtigt werden.', 'Für jeden Cloud-Dienst MUSS eine Service-Definition erarbeitet werden.', 'Zudem SOLLTEN alle geplanten und genutzten Cloud-Dienste dokumentiert werden.', 'Sie MUSS konkrete Sicherheitsvorgaben beinhalten, mit denen sich Cloud-Dienste innerhalb der Institution umsetzen lassen.', 'Basierend auf der Service-Definition für Cloud-Dienste MÜSSEN alle relevanten Schnittstellen und Verantwortlichkeiten für die Cloud-Nutzung identifiziert und dokumentiert werden.', 'Es SOLLTE geregelt werden, an welchem Standort die Cloud-Diensteanbietenden ihre Leistung erbringen.', 'Die Verträge SOLLTEN Kündigungsoptionen, um das Outsourcing-Verhältnisses aufzulösen, enthalten.', 'Interne Eignungsanforderungen an potenzielle Anbietende von Outsourcing MÜSSEN festgelegt werden.', 'Diese Eignungsanforderungen MÜSSEN die erforderlichen Kompetenzen, um den Prozess aus Sicht der Informationssicherheit abzusichern, sowie die Reputation hinsichtlich der Vertrauenswürdigkeit und Zuverlässigkeit berücksichtigen.', 'Mit den Anbietenden von Outsourcing SOLLTE eine Verschwiegenheitserklärung zum Schutz von sensiblen Daten vereinbart werden.', 'In einer Vereinbarung zur Mandantenfähigkeit mit den Anbietenden von Outsourcing MUSS sichergestellt werden, dass die Daten und Verarbeitungskontexte durch den Anbietenden von Outsourcing ausreichend sicher getrennt sind.', 'Mit den Anbietenden von Outsourcing MUSS vertraglich vereinbart werden, dass IT-Grundschutz umgesetzt oder mindestens die Anforderungen aus den relevanten Bausteinen geeignet erfüllt werden.', 'Für geplante sowie ungeplante Beendigungen des Outsourcing-Verhältnisses MÜSSEN Regelungen getroffen werden.', 'Ferner SOLLTE überprüft werden, ob die Zugangs-, Zutritts- und Zugriffsrechte für die Anbietenden von Outsourcing mit der Beendigung des Outsourcing-Verhältnisses aufgehoben wurden.', 'Die zuständige Person für das Auslagerungsmanagement SOLLTE ein Auslagerungsregister erstellen und pflegen, dass die Dokumentation der Outsourcing-Prozesse und Vorhaben in der Institution zentralisiert.', 'Diese Anforderungsprofile MÜSSEN die Funktion, verarbeite Daten, Schnittstellen sowie eine Bewertung der Informationssicherheit enthalten.', 'Für den Fall, dass die vereinbarten Leistungskennzahlen unzureichend erfüllt werden, SOLLTEN mit den Anbietenden von Outsourcing Konsequenzen, wie z. B. Vertragsstrafen, festgelegt werden.', 'Mit Anbietenden von Outsourcing SOLLTE vereinbart werden, auf welche Bereiche und Dienste die Anbietenden im Netz der Nutzenden von Outsourcing zugreifen dürfen.', 'Die Grundanforderungen MÜSSEN in Vereinbarungen und Verträgen einheitlich umgesetzt werden.', 'Wenn der Prozess ausgelagert wird, SOLLTE das Resultat im Auslagerungsregister abgelegt werden.', 'Die Nutzenden SOLLTEN Leistungskennzahlen für die Anbietenden von Outsourcing definieren und im Vertrag festlegen.', 'Innerhalb einer Institution MÜSSEN alle relevanten Aufgaben und Funktionen klar definiert und voneinander abgegrenzt sein.', 'Auch Vertreter MÜSSEN der Funktionstrennung unterliegen.', 'Diesbezügliche Informationen MÜSSEN in der Institution für alle verfügbar und leicht zugänglich sein.', 'Für alle Geschäftsprozesse, Anwendungen, IT-Systeme, Räume und Gebäude sowie Kommunikationsverbindungen MUSS festgelegt werden, wer für diese und deren Sicherheit zuständig ist.', 'Die Mitarbeitenden der Institution MÜSSEN institutionsfremde Personen in sensiblen Bereichen beaufsichtigen.', 'Für alle Geschäftsprozesse, Anwendungen, IT-Systeme, Räume und Gebäude sowie Kommunikationsverbindungen MUSS festgelegt werden, wer für diese und deren Sicherheit zuständig ist.', 'Für alle Geschäftsprozesse, Anwendungen, IT-Systeme, Räume und Gebäude sowie Kommunikationsverbindungen MUSS festgelegt werden, wer für diese und deren Sicherheit zuständig ist.', 'Alle Mitarbeitenden MÜSSEN darüber informiert sein, insbesondere wofür sie zuständig sind und welche damit verbundenen Aufgaben sie wahrnehmen.', 'Die Aufgaben und die hierfür erforderlichen Rollen und Funktionen MÜSSEN so strukturiert sein, dass unvereinbare Aufgaben wie operative und kontrollierende Funktionen auf verschiedene Personen verteilt werden.', 'In jeder Institution MUSS es Ansprechpersonen für Sicherheitsfragen geben, die sowohl scheinbar einfache wie auch komplexe oder technische Fragen beantworten können.', 'Die Ansprechpersonen MÜSSEN allen Mitarbeitenden der Institution bekannt sein.', 'Bevor externe Personen Zugang und Zugriff zu vertraulichen Informationen erhalten, MÜSSEN mit ihnen Vertraulichkeitsvereinbarungen in schriftlicher Form geschlossen werden.', 'Vor der Verabschiedung MUSS noch einmal auf Verschwiegenheitsverpflichtungen hingewiesen werden.', 'Alle betroffenen Stellen innerhalb der Institution, wie z. B. das Sicherheitspersonal oder die IT-Abteilung, MÜSSEN über das Ausscheiden des oder der Mitarbeitenden informiert werden.', 'Damit alle verbundenen Aufgaben, die beim Ausscheiden des oder der Mitarbeitenden anfallen, erledigt werden, SOLLTE hier ebenfalls eine Checkliste angelegt werden.', 'Dies SOLLTE idealerweise durch den oder die ausscheidenden Mitarbeitenden erfolgen.', 'Ist eine direkte Übergabe nicht möglich, MUSS von den ausscheidenden Mitarbeitenden eine ausführliche Dokumentation angefertigt werden.', 'Die Aufgaben und Zuständigkeiten von Mitarbeitenden MÜSSEN in geeigneter Weise dokumentiert sein.', 'Die Personalabteilung sowie die Vorgesetzten MÜSSEN dafür sorgen, dass Mitarbeitende zu Beginn ihrer Beschäftigung in ihre neuen Aufgaben eingearbeitet werden.', 'In allen Bereichen MUSS sichergestellt werden, dass kein Mitarbeitende mit veralteten Wissensstand arbeitet.', 'Weiterhin SOLLTE den Mitarbeitenden während ihrer Beschäftigung die Möglichkeit gegeben werden, sich im Rahmen ihres Tätigkeitsfeldes weiterzubilden.', 'Es MUSS sichergestellt sein, dass Stellen nur von Mitarbeitenden besetzt werden, für die sie qualifiziert sind.', 'Bei diesen Regelungen MUSS der Aufgabenumfang der Vertretung im Vorfeld klar definiert werden.', 'Es MUSS sichergestellt werden, dass die Vertretung über das dafür nötige Wissen verfügt.', 'Ist dies nicht der Fall, MUSS überprüft werden, wie der Vertretenden zu schulen ist oder ob es ausreicht, den aktuellen Verfahrens- oder Projektstand ausreichend zu dokumentieren.', 'Ist es im Ausnahmefall nicht möglich, für einzelne Mitarbeitende einen kompetenten Vertretenden zu benennen oder zu schulen, MUSS frühzeitig entschieden werden, ob externes Personal dafür hinzugezogen werden kann.', 'Auch für diese Mitarbeitende MUSS eine Vertretungsregelung eingeführt werden.', 'Die Mitarbeitenden MÜSSEN über bestehende Regelungen, Handlungsanweisungen und Verfahrensweisen informiert werden.', 'Alle Mitarbeitenden MÜSSEN dazu verpflichtet werden, geltende Gesetze, Vorschriften und interne Regelungen einzuhalten.', 'Wird externes Personal beschäftigt, MUSS dieses wie alle eigenen Mitarbeitenden dazu verpflichtet werden, geltende Gesetze, Vorschriften und interne Regelungen einzuhalten.', 'Fremdpersonal, das kurzfristig oder einmalig eingesetzt wird, MUSS in sicherheitsrelevanten Bereichen beaufsichtigt werden.', 'Außerdem MÜSSEN von ausscheidenden Mitarbeitenden alle im Rahmen ihrer Tätigkeit erhaltenen Unterlagen, Schlüssel und Geräte sowie Ausweise und Zutrittsberechtigungen eingezogen werden.', 'Verlässt das Fremdpersonal die Institution, MÜSSEN Arbeitsergebnisse wie bei eigenem Personal geregelt übergeben und eventuell ausgehändigte Zugangsberechtigungen zurückgegeben werden.', 'Verlassen Mitarbeitende die Institution, MUSS der oder die Nachfolgende rechtzeitig eingewiesen werden.', 'Den Mitarbeitenden MUSS bewusst gemacht werden, die Informationssicherheit der Institution auch außerhalb der Arbeitszeit und außerhalb des Betriebsgeländes zu schützen.', 'Mitarbeitende MÜSSEN regelmäßig geschult bzw. weitergebildet werden.', 'Dafür MUSS sichergestellt werden, dass es für alle wesentlichen Geschäftsprozesse und Aufgaben praktikable Vertretungsregelungen gibt.', 'Hierüber hinaus MÜSSEN sie ihre Mitarbeitenden auf deren Einhaltung hinweisen.', 'Alle Mitarbeitenden SOLLTEN entsprechend ihren Aufgaben und Verantwortlichkeiten zu Informationssicherheitsthemen geschult werden.', 'Die Institutionsleitung MUSS ausreichend für Sicherheitsfragen sensibilisiert werden.', 'Alle Vorgesetzten MÜSSEN die Informationssicherheit unterstützen, indem sie mit gutem Beispiel vorangehen.', 'Führungskräfte MÜSSEN die Sicherheitsvorgaben umsetzen.', 'Dafür MÜSSEN verbindliche, verständliche und aktuelle Richtlinien zur Nutzung der jaeweiligen Komponenten zur Verfügung stehen.', 'Alle Mitarbeitenden und externen Benutzenden MÜSSEN in den sicheren Umgang mit IT-, ICS- und IoT-Komponenten eingewiesen und sensibilisiert werden, soweit dies für ihre Arbeitszusammenhänge relevant ist.', 'Nach einem Passwortwechsel DÜRFEN alte Passwörter NICHT mehr genutzt werden.', 'Dabei MUSS geprüft werden, ob Passwörter als alleiniges Authentisierungsverfahren eingesetzt werden sollen, oder ob andere Authentisierungsmerkmale bzw. -verfahren zusätzlich zu oder anstelle von Passwörtern verwendet werden können.', 'Passwörter DÜRFEN NICHT mehrfach verwendet werden.', 'Für jedes IT-System bzw. jede Anwendung MUSS ein eigenständiges Passwort verwendet werden.', 'Passwörter, die leicht zu erraten sind oder in gängigen Passwortlisten geführt werden, DÜRFEN NICHT verwendet werden.', 'Passwörter MÜSSEN geheim gehalten werden.', 'Sie DÜRFEN NUR den Benutzenden persönlich bekannt sein.', 'Passwörter DÜRFEN NUR unbeobachtet eingegeben werden.', 'Passwörter DÜRFEN NICHT auf programmierbaren Funktionstasten von Tastaturen oder Mäusen gespeichert werden.', 'Ein Passwort DARF NUR für eine Hinterlegung für einen Notfall schriftlich fixiert werden.', 'Es MUSS dann sicher aufbewahrt werden.', 'Die Nutzung eines Passwort-Managers SOLLTE geprüft werden.', 'Bei Passwort-Managern mit Funktionen oder Plug-ins, mit denen Passwörter über Onlinedienste Dritter synchronisiert oder anderweitig an Dritte übertragen werden, MÜSSEN diese Funktionen und Plug-ins deaktiviert werden.', 'Ein Passwort MUSS gewechselt werden, wenn es unautorisierten Personen bekannt geworden ist oder der Verdacht dazu besteht.', 'Reine zeitgesteuerte Wechsel SOLLTEN vermieden werden.', 'Bei personellen Veränderungen MÜSSEN die nicht mehr benötigten Benutzendenkennungen und Berechtigungen entfernt werden.', 'Beantragen Mitarbeitende Berechtigungen, die über den Standard hinausgehen, DÜRFEN diese NUR nach zusätzlicher Begründung und Prüfung vergeben werden.', 'Die Dokumentation der zugelassenen Benutzendenkennungen, angelegten Benutzendengruppen und Rechteprofile MUSS regelmäßig daraufhin überprüft werden, ob sie den tatsächlichen Stand der Rechtevergabe widerspiegelt.', 'Dabei MUSS auch geprüft werden, ob die Rechtevergabe noch den Sicherheitsanforderungen und den aktuellen Aufgaben der Benutzenden entspricht.', 'Die Dokumentation MUSS vor unberechtigtem Zugriff geschützt werden.', 'Sofern sie in elektronischer Form erfolgt, SOLLTE sie in das Datensicherungsverfahren einbezogen werden.', 'Die von der Institution definierten unvereinbaren Aufgaben und Funktionen (siehe Baustein ORP.1 Organisation) MÜSSEN durch das Identitäts- und Berechtigungsmanagement getrennt werden.', 'Jede Benutzendenkennung MUSS eindeutig einer Person zugeordnet werden können.', 'Die Ausgabe bzw. der Entzug von verwendeten Zutrittsmittel wie Chipkarten MUSS dokumentiert werden.', 'Werden Zugangsmittel wie Chipkarten verwendet, so MUSS die Ausgabe bzw. der Entzug dokumentiert werden.', 'Werden im Rahmen der Zugriffskontrolle Chipkarten oder Token verwendet, so MUSS die Ausgabe bzw. der Entzug dokumentiert werden.', 'Wenn Zutrittsmittel kompromittiert wurden, MÜSSEN sie ausgewechselt werden.', 'Wenn Zugangsmittel kompromittiert wurden, MÜSSEN sie ausgewechselt werden.', 'Bei längeren Abwesenheiten SOLLTEN berechtigte Personen vorübergehend gesperrt werden.', 'Die Institution MUSS den Passwortgebrauch verbindlich regeln (siehe auch ORP.4.A22 Regelung zur Passwortqualität und ORP.4.A23 Regelung für Passwort-verarbeitende Anwendungen und IT-Systeme).', 'Der Zugriff auf alle IT-Systeme und Dienste MUSS durch eine angemessene Identifikation und Authentisierung der zugreifenden Benutzenden, Dienste oder IT-Systeme abgesichert sein.', 'Standardpasswörter MÜSSEN durch ausreichend starke Passwörter ersetzt und vordefinierte Kennungen MÜSSEN geändert werden.', 'Vordefinierte Kennungen MÜSSEN geändert werden.', 'Vorkonfigurierte Authentisierungsmittel MÜSSEN vor dem produktiven Einsatz geändert werden.', 'IT-Systeme oder Anwendungen SOLLTEN NUR mit einem validen Grund zum Wechsel des Passworts auffordern.', 'Benutzendenkennungen, die längere Zeit inaktiv sind, SOLLTEN deaktiviert werden.', 'Bei längeren Abwesenheiten SOLLTEN berechtigte Personen vorübergehend gesperrt werden.', 'Bei längeren Abwesenheiten SOLLTEN berechtigte Personen vorübergehend gesperrt werden.', 'Alle Benutzenden und Benutzendengruppen DÜRFEN NUR über separate administrative Rollen eingerichtet und gelöscht werden.', 'Alle Berechtigungen MÜSSEN über separate administrative Rollen eingerichtet werden.', 'Nicht benötigte Benutzendenkennungen, wie z. B. standardmäßig eingerichtete Gastkonten oder Standard-Administrierendenkennungen, MÜSSEN geeignet deaktiviert oder gelöscht werden.', 'Benutzendenkennungen und Berechtigungen DÜRFEN NUR aufgrund des tatsächlichen Bedarfs und der Notwendigkeit zur Aufgabenerfüllung vergeben werden (Prinzip der geringsten Berechtigungen, englisch Least Privileges und Erforderlichkeitsprinzip, englisch Need-to-know).', 'Zugriffsberechtigungen auf Systemverzeichnisse und -dateien SOLLTEN restriktiv eingeschränkt werden.', 'Es MUSS dokumentiert werden, welche Benutzendenkennungen, angelegte Benutzendengruppen und Rechteprofile zugelassen und angelegt wurden.', 'Es MUSS festgelegt werden, welche Zutrittsberechtigungen an welche Personen im Rahmen ihrer Funktion vergeben bzw. ihnen entzogen werden.', 'Es MUSS festgelegt werden, welche Zugangsberechtigungen an welche Personen im Rahmen ihrer Funktion vergeben bzw. ihnen entzogen werden.', 'Es MUSS festgelegt werden, welche Zugriffsrechte an welche Personen im Rahmen ihrer Funktion vergeben bzw. ihnen entzogen werden.', 'Physische Server MÜSSEN daher in Rechenzentren, Serverräumen oder abschließbaren Serverschränken aufgestellt beziehungsweise eingebaut werden (siehe hierzu die entsprechenden Bausteine der Schicht INF Infrastruktur).', 'Abhängig vom installierten Betriebssystem, den bereitgestellten Diensten und von anderen vorhandenen Schutzmechanismen des Servers MUSS geprüft werden, ob Viren-Schutzprogramme eingesetzt werden sollen und können.', 'Dies SOLLTE in besonderem Maße für administrative Zugänge berücksichtigt werden.', 'Server DÜRFEN NICHT zur Erledigung von Aufgaben und Tätigkeiten verwendet werden, die grundsätzlich auf einem Client-System aus- und durchgeführt werden können.', 'Insbesondere DÜRFEN vorhandene Anwendungen, wie Webbrowser, auf dem Server NICHT für das Abrufen von Informationen aus dem Internet oder das Herunterladen von Software, Treibern und Updates verwendet werden.', 'Systemstarts und Reboots,', 'erfolgreiche und erfolglose Anmeldungen am System (Betriebssystem und Anwendungssoftware),', 'fehlgeschlagene Berechtigungsprüfungen,', 'blockierte Datenströme (Verstöße gegen ACLs oder Firewallregeln),', 'Einrichtung oder Änderungen von Benutzenden, Gruppen und Berechtigungen,', 'sicherheitsrelevante Fehlermeldungen (z. B. Hardwaredefekte, Überschreitung von Kapazitätsgrenzen) sowie', 'Warnmeldungen von Sicherheitssystemen (z. B. Virenschutz).', 'Bei virtualisierten Servern MUSS der Zugriff auf die Ressourcen der Instanz und deren Konfiguration ebenfalls auf die berechtigten Personen begrenzt werden.', 'Physische Server MÜSSEN an Orten betrieben werden, zu denen nur berechtigte Personen Zutritt haben.', 'Für die Anmeldung von Benutzenden und Diensten am Server MÜSSEN Authentisierungsverfahren eingesetzt werden, die dem Schutzbedarf der Server angemessen sind.', 'Server DÜRFEN NICHT als Arbeitsplatzrechner genutzt werden.', 'Als Arbeitsplatz genutzte IT-Systeme DÜRFEN NICHT als Server genutzt werden.', 'Alle nicht benötigten Serverrollen, Features und Funktionen, sonstige Software und Dienste MÜSSEN deaktiviert oder deinstalliert werden, vor allem Netzdienste.', 'Jeder Server SOLLTE an eine unterbrechungsfreie Stromversorgung (USV) angeschlossen werden.', 'Generell MÜSSEN alle sicherheitsrelevanten Systemereignisse protokolliert werden, dazu gehören mindestens:', 'Wenn nicht benötigt, MUSS die Einrichtung von Microsoft-Konten auf dem Server blockiert werden.', 'Um die Übertragung von Diagnose- und Nutzungsdaten an Microsoft stark zu reduzieren, MUSS das Telemetrie-Level 0 (Security) auf dem Windows Server konfiguriert werden.', 'Andernfalls MUSS begründet werden, warum die Server-Core-Variante nicht genügt.', 'Die Nutzung von mitgelieferten Cloud-Diensten im Betriebssystem MUSS grundsätzlich abgewogen und gründlich geplant werden.', 'Wenn vom Funktionsumfang her ausreichend, MUSS die Server-Core-Variante installiert werden.', 'Maßnahmen zum Schutz vor Exploits SOLLTEN für alle Programme und Dienste aktiviert werden, die den Exploit-Schutz von Windows (vgl. Verweis in Kapitel 4.1 Wissenswertes) unterstützen.', 'Um die Virtualisierungsserver oder die Managementsysteme zu administrieren bzw. zu überwachen, SOLLTEN als sicher geltende Protokolle eingesetzt werden.', 'Sollte dennoch auf unsichere Protokolle zurückgegriffen werden, MUSS für die Administration ein eigenes Administrationsnetz genutzt werden.', 'Es MUSS sichergestellt sein, dass aus nicht-vertrauenswürdigen Netzen heraus nicht auf die Administrationsschnittstellen zugegriffen werden kann.', 'Anhand der in der Planung definierten Aufgaben und Rollen (siehe SYS.1.5.A8 Planung einer virtuellen Infrastruktur) SOLLTE für die Administration der virtuellen IT-Systeme und Netze sowie der Virtualisierungsserver und der Managementumgebung ein Rechte- und Rollenkonzept erstellt und umgesetzt werden.', 'Alle Komponenten der virtuellen Infrastruktur SOLLTEN in ein zentrales Identitäts- und Berechtigungsmanagement eingebunden werden.', 'Ist eine solche Verbindung jedoch notwendig, MUSS diese exklusiv zugeteilt werden.', 'Die Systemzeit aller produktiv eingesetzten virtuellen IT-Systeme MUSS immer synchron sein.', 'Die Zugriffsrechte für Administrierende auf virtuelle IT-Systeme MÜSSEN auf das tatsächlich notwendige Maß reduziert sein.', 'Jede Person, die virtuelle IT-Systeme administriert, MUSS wissen, wie sich eine Virtualisierung auf die betriebenen IT-Systeme und Anwendungen auswirkt.', 'Gast-Systeme DÜRFEN NICHT auf Geräte und Schnittstellen des Virtualisierungsservers zugreifen.', 'Sie DARF NUR für die notwendige Dauer von den Administrierenden des Host-Systems hergestellt werden.', 'Administrierende von virtuellen Maschinen und Administrierende der Virtualisierungsumgebung SOLLTEN unterschieden werden.', 'Sie SOLLTEN mit unterschiedlichen Zugriffsrechten ausgestattet werden.', 'Rollen und Berechtigungen', 'Umfang der Verschlüsselung des Terminalserver-Protokolls', 'benötigte Authentisierungsfunktionen des Terminalserver-Protokolls', 'Möglichkeit zum Anzeigen der Ausgabe fremder Sitzungen', 'Kommunikation zwischen Anwendungen in den Terminalserver-Sitzungen und Anwendungen auf anderen Servern', 'Kommunikation zwischen Terminalserver und anderen Servern', 'Wenn eine Sitzung beendet wird, SOLLTE auch der oder die Benutzende automatisch vom Betriebssystem des Terminalservers abgemeldet werden, sofern die Sitzung am Betriebssystem nicht weiterhin für laufende Anwendungen benötigt wird.', 'Für die Terminalserver SOLLTE entschieden werden, welche Ereignisse an eine zentrale Protokollierungsinfrastruktur (siehe OPS.1.1.5 Protokollierung) übermittelt werden sollen.', 'Aktionen auf dem Terminalserver durch zugreifende Clients, die erweiterte Rechte benötigen sowie', 'Konfigurationsänderungen mit Auswirkungen auf den Terminalserver-Dienst.', 'Ist dies der Fall, MÜSSEN diese für die Erstellung der Konfigurationsvorgaben angemessen berücksichtigt werden.', 'Zusätzlich MUSS festgelegt werden, wie die Kommunikation abgesichert werden soll.', 'Inaktive Sitzungen auf Terminalservern SOLLTEN nach einem vordefinierten Zeitraum beendet werden.', 'Das Schutzprogramm MUSS nach Schadsoftware suchen, wenn Dateien ausgetauscht oder übertragen werden.', 'In diesem Zusammenhang SOLLTEN die Authentisierung (z. B. Passwort, PIN, Token), die Ablage der Wiederherstellungsinformationen, die zu verschlüsselnden Laufwerke und die Schreibrechte auf unverschlüsselte Datenträger geregelt werden.', 'Die Bildschirmsperre SOLLTE automatisch aktiviert werden, wenn für eine festgelegte Zeitspanne keine Aktion durch Benutzende durchgeführt wurde.', 'Die Bildschirmsperre DARF NUR durch eine erfolgreiche Authentisierung wieder deaktiviert werden können.', 'Es MUSS festgelegt werden, von welchen Medien gebootet werden darf.', 'Es SOLLTE entschieden werden, ob und wie der Bootvorgang kryptografisch geschützt werden soll.', 'Es MUSS sichergestellt werden, dass nur Administrierende die Clients von einem anderen als den voreingestellten Laufwerken oder externen Speichermedien booten können.', 'NUR Administrierende DÜRFEN von wechselbaren oder externen Speichermedien booten können.', 'Die Konfigurationseinstellungen des Bootvorgangs DÜRFEN NUR durch Administrierende verändert werden können.', 'Die entsprechenden Einstellungen des Betriebssystems MÜSSEN auf Konformität mit den organisatorischen Datenschutz- und Sicherheitsvorgaben überprüft und restriktiv konfiguriert bzw. die Funktionen deaktiviert werden.', 'Es SOLLTE verhindert werden, dass von den Clients auf Wechseldatenträger aus nicht vertrauenswürdigen Quellen zugegriffen werden kann.', 'Um den Client zu nutzen, MÜSSEN sich die Benutzenden gegenüber dem IT-System authentisieren.', 'Die unerlaubte Ausführung von Programmen auf bzw. von externen Datenträgern SOLLTE technisch unterbunden werden.', 'Bei der Außerbetriebnahme eines Clients SOLLTE sichergestellt werden, dass keine Daten verloren gehen und dass keine schutzbedürftigen Daten zurückbleiben.', 'Automatische Update-Mechanismen (Autoupdate) MÜSSEN aktiviert werden, sofern nicht andere Mechanismen wie regelmäßige manuelle Wartung oder ein zentrales Softwareverteilungssystem für Updates eingesetzt werden.', 'Es SOLLTE eine Checkliste erstellt werden, die bei der Außerbetriebnahme eines IT-Systems abgearbeitet werden kann.', 'Wenn vertrauliche Informationen auf den Clients gespeichert werden, SOLLTEN mindestens die schutzbedürftigen Dateien sowie ausgewählte Dateisystembereiche oder besser die gesamten Datenträger verschlüsselt werden.', 'Benutzende MÜSSEN eine Bildschirmsperre verwenden, wenn sie den Client unbeaufsichtigt betreiben.', 'Benutzende SOLLTEN verpflichtet werden, sich nach Aufgabenerfüllung vom IT-System bzw. von der IT-Anwendung abzumelden.', 'Nicht benötigte Kennungen SOLLTEN deaktiviert oder gelöscht werden.', 'Abhängig vom installierten Betriebssystem und von anderen vorhandenen Schutzmechanismen des Clients MUSS geprüft werden, ob Schutzprogramme gegen Schadsoftware eingesetzt werden sollen.', 'Der Startvorgang des IT-Systems („Booten“) MUSS gegen Manipulation abgesichert werden.', 'Nicht benötigte Module, Programme, Dienste, Aufgaben und Firmwarefunktionen (wie Fernwartung) SOLLTEN deaktiviert oder ganz deinstalliert werden.', 'Alle nicht benötigten Funktionen in der Firmware des Client-Systems MÜSSEN deaktiviert werden.', 'Nicht benötigte Schnittstellen und Hardware des IT-Systems (wie z. B. Webcams) SOLLTEN deaktiviert werden.', 'Es DÜRFEN NUR zwingend notwendige Cloud- und Online-Funktionen des Betriebssystems genutzt werden.', 'Schutzprogramme auf den Clients MÜSSEN so konfiguriert sein, dass Benutzende weder sicherheitsrelevante Änderungen an den Einstellungen vornehmen noch die Schutzprogramme deaktivieren können.', 'Es SOLLTE untersagt werden, dass nicht zugelassene Geräte oder Wechseldatenträger mit den Clients verbunden werden.', 'Für die zentrale Authentisierung SOLLTE ausschließlich Kerberos eingesetzt werden.', 'Eine Gruppenrichtlinie SOLLTE die Verwendung älterer Protokolle verhindern.', 'Ist dies nicht möglich, MUSS alternativ NTLMv2 eingesetzt werden.', 'Die Authentisierung mittels LAN-Manager und NTLMv1 DARF NICHT innerhalb der Institution und in einer produktiven Betriebsumgebung erlaubt werden.', 'Sofern die Windows-Remoteunterstützung nicht verwendet wird, SOLLTE sie vollständig deaktiviert werden.', 'Die Gruppe der berechtigten Benutzenden für den Remote-Desktopzugriff (RDP) SOLLTE durch die Zuweisung entsprechender Berechtigungen festgelegt werden.', 'Sofern der Einsatz von Remote-Desktopzugriffen nicht vorgesehen ist, SOLLTEN diese vollständig deaktiviert werden.', 'Die eingesetzten kryptografischen Protokolle und Algorithmen SOLLTEN sicher sein und den internen Vorgaben der Institution entsprechen.', 'Die SmartScreen-Funktion, die aus dem Internet heruntergeladene Dateien und Webinhalte auf mögliche Schadsoftware untersucht und dazu unter Umständen personenbezogene Daten an Microsoft überträgt, SOLLTE deaktiviert werden.', 'Insbesondere SOLLTEN Benutzende keine Schreibrechte für Ordner des Betriebssystems oder installierter Anwendungen erhalten.', 'Da Windows-basierte Geräte eng mit den Cloud-Diensten des Herstellers Microsoft verzahnt sind, MUSS vor ihrer Verwendung strategisch festgelegt werden, welche enthaltenen Cloud-Dienste in welchem Umfang genutzt werden sollen bzw. dürfen.', 'Cortana SOLLTE deaktiviert werden.', 'Die Synchronisierung von Benutzendendaten mit Microsoft Cloud-Diensten und das Sharing von WLAN-Passwörtern SOLLTEN vollständig deaktiviert werden.', 'Die generelle Installation von Apps auf Windows ist nicht von der Anbindung an den Microsoft-Store abhängig, daher SOLLTE sie, sofern sie nicht benötigt wird, deaktiviert werden.', 'Um die Übertragung von Diagnose- und Nutzungsdaten an Microsoft stark zu reduzieren, MUSS das Telemetrie-Level 0 (Security) in der Enterprise-Edition von Windows konfiguriert werden.', 'Eine Remoteunterstützung SOLLTE nur nach einer expliziten Einladung erfolgen.', 'Dem Aufbau einer Sitzung SOLLTE immer explizit zugestimmt werden.', 'Die Netzsegmente für virtuelle Clients MÜSSEN von Netzsegmenten für Server getrennt sein.', 'Für die virtuellen Clients MUSS ein Schutz vor Schadsoftware gemäß den Bausteinen OPS.1.1.4 Schutz vor Schadprogrammen und SYS.2.1 Allgemeiner Client sowie unter Berücksichtigung der betriebssystemspezifischen Bausteine umgesetzt werden.', 'Es MUSS klar geregelt werden, was Mitarbeitende bei der mobilen Nutzung von Laptops berücksichtigen müssen.', 'Benutzende SOLLTEN umgehend melden, wenn ein Laptop verloren gegangen ist oder gestohlen wurde.', 'Die darauf eingesetzte Software inklusive des Betriebssystems SOLLTE komplett neu installiert werden.', 'Die Benutzenden SOLLTEN hinsichtlich des Schutzbedarfs von Laptops und der dort gespeicherten Daten sensibilisiert werden.', 'Die Filterregeln der Firewall MÜSSEN so restriktiv wie möglich sein.', 'Die Personal Firewall MUSS so konfiguriert werden, dass die Benutzenden nicht durch Warnmeldungen belästigt werden, die sie nicht interpretieren können.', 'Es MUSS insbesondere festgelegt werden, welche Laptops mobil genutzt werden dürfen, wer sie mitnehmen darf und welche grundlegenden Sicherheitsmaßnahmen dabei zu beachten sind.', 'In Laptops verbaute Datenträger wie Festplatten oder SSDs SOLLTEN verschlüsselt werden.', 'Aus öffentlich zugänglichen Netzen DARF NUR über einen sicheren Kommunikationskanal auf das interne Netz der Institution zugegriffen werden.', 'Dafür SOLLTE es in der Institution klare Meldewege geben.', 'Auch SOLLTEN sie auf die spezifischen Gefährdungen bzw. die entsprechenden Anforderungen für die Nutzung aufmerksam gemacht werden.', 'Auf Laptops MUSS eine Personal Firewall aktiv sein, wenn sie außerhalb von Netzen der Institution eingesetzt werden.', 'Ältere Geräte, für die keine Aktualisierungen mehr bereitgestellt werden, MÜSSEN ausgesondert und durch von der herstellenden Institution unterstützte Geräte ersetzt werden.', 'Es SOLLTE vermieden werden, dass die Benutzenden bei einem Passwortwechsel Kennworte nutzen, die erst vor Kurzem verwendet wurden.', 'Die Datenschutzeinstellungen MÜSSEN so restriktiv wie möglich konfiguriert werden.', 'Insbesondere der Zugriff auf Kamera, Mikrofon sowie Ortungs- und Gesundheits- bzw. Fitnessdaten MUSS auf Konformität mit den organisationsinternen Datenschutz- und Sicherheitsvorgaben überprüft werden.', 'Sie SOLLTEN nur freigegebene Apps installieren dürfen.', 'Die Institution MUSS festlegen, aus welchen Quellen Apps installiert werden dürfen.', 'Es MUSS unterbunden werden, dass sich Apps aus nicht zugelassenen Quellen installieren lassen.', 'Gehen Geräte verloren oder werden unberechtigte Änderungen an Gerät und Software festgestellt, MÜSSEN die Benutzenden sofort die Zuständigen informieren.', 'Nicht benötigte Funktionen SOLLTEN deaktiviert werden.', 'Nicht benutzte Schnittstellen SOLLTEN deaktiviert werden.', 'Alle mobilen Geräte MÜSSEN nach einer angemessen kurzen Zeitspanne selbsttätig die Bildschirmsperre aktivieren.', 'Bei jedem fehlgeschlagenen Versuch, das Gerät zu entsperren, SOLLTE sich die Wartezeit zu einem neuen Versuch verlängern.', 'Die Anzahl der Gerätesperrcodes, nach der sich ein Code wiederholen darf, SOLLTE festgelegt werden.', 'Nach mehreren fehlgeschlagenen Versuchen, den Bildschirm zu entsperren, SOLLTE sich das mobile Gerät in den Werkszustand zurücksetzen.', 'Hierbei MUSS unter anderem festgelegt werden, wer mit Smartphones auf welche Informationen der Institution zugreifen darf.', 'Smartphones und Tablets MÜSSEN mit einem angemessen komplexen Gerätesperrcode geschützt werden.', 'Die Anzeige von vertraulichen Informationen auf dem Sperrbildschirm MUSS deaktiviert sein.', 'Bereits bei der Auswahl von zu beschaffenden mobilen Geräten MUSS die Institution darauf achten, dass die herstellende Institution angibt, über welchen geplanten Nutzungszeitraum Sicherheitsaktualisierungen für die Geräte bereitgestellt werden.', 'Apps SOLLTEN ebenfalls NICHT mehr eingesetzt werden, wenn sie nicht mehr durch die herstellende Institution unterstützt werden.', 'Der Zugriff von Apps und Betriebssystem auf Daten und Schnittstellen MUSS angemessen eingeschränkt werden.', 'Sicherheitsrelevante Berechtigungseinstellungen MÜSSEN so festgelegt werden, dass sie nicht durch Benutzende oder Apps geändert werden können.', 'Die Institution MUSS regeln, ob, wie und welche Apps Benutzende selbst auf ihren Geräten installieren dürfen.', 'Dafür MUSS eine passende Grundkonfiguration der Sicherheitsmechanismen und -einstellungen zusammengestellt und dokumentiert werden.', 'Die Bildschirmsperre MUSS genutzt werden.', 'Alle notwendigen Informationen zur Sperrung von SIM-Karte und Mobiltelefon MÜSSEN unmittelbar griffbereit sein.', 'Mobiltelefone MÜSSEN vor der Entsorgung auf den Werkszustand zurückgesetzt werden.', 'Es SOLLTE zudem sichergestellt werden, dass die Mobiltelefone und eventuell darin verwendete Speicherkarten ordnungsgemäß entsorgt werden.', 'Falls die Mobiltelefone und Speicherkarten erst zu einem späteren Zeitpunkt beziehungsweise in größerer Anzahl entsorgt werden, MÜSSEN die gesammelten Mobiltelefone und Speicherkarten vor unberechtigtem Zugriff geschützt werden.', 'Falls möglich, SOLLTEN vorhandene Mechanismen zum Diebstahlschutz, wie Fernlöschung oder -sperrung, genutzt werden.', 'Den Benutzenden MUSS der Prozess bekannt sein, durch den die Mobiltelefone gesperrt werden können.', 'Bei Verlust eines Mobiltelefons MUSS die darin verwendete SIM-Karte zeitnah gesperrt werden.', 'Mitarbeitende MÜSSEN für die besonderen Gefährdungen der Informationssicherheit durch Mobiltelefone sensibilisiert werden.', 'Die Benutzenden MÜSSEN darauf hingewiesen werden, wie die Mobiltelefone sicher und korrekt aufbewahrt werden sollten.', 'Unterstützung sicherer Protokolle zur Datenübertragung und Administration,', 'Verschlüsselung der abgespeicherten Informationen,', 'Authentisierung der Benutzenden direkt am Gerät,', 'Nutzung physischer Schutzmechanismen, wie Ösen zum Diebstahlschutz oder Geräteschlösser,', 'Existenz einer Funktion zum sicheren Löschen des Speichers sowie', 'Verfügbarkeit von regelmäßigen Updates und Wartungsverträgen.', 'Es MUSS festgelegt werden, wo die Geräte aufgestellt werden dürfen.', 'Es SOLLTEN möglichst nur zentrale Drucker, Kopierer und Multifunktionsgeräte eingesetzt werden, bei denen sich die Benutzenden am Gerät authentisieren, bevor der Druckauftrag startet („Secure-Print“).', 'Nachdem sich die Benutzenden authentisiert haben, SOLLTEN ausschließlich nur die eigenen Druckaufträge sichtbar sein.', 'Mit Dienstleistenden (z. B. für die Wartung) MÜSSEN schriftliche Vertraulichkeitsvereinbarungen getroffen werden.', 'Drucker, Kopierer und Multifunktionsgeräte MÜSSEN mit Gerätepassworten versehen sein, um so den Zugriff auf Webserver und Bedienfeld für die Administration zu sperren.', 'Der IT-Betrieb SOLLTE sicherstellen, dass der administrative Fernzugriff auf Drucker, Kopierer und Multifunktionsgeräte nur einer klar definierten Gruppe des Administrations- und Servicepersonals ermöglicht wird.', 'Insbesondere SOLLTEN alle nicht benötigten Daten- und Netzschnittstellen von Druckern, Kopierern und Multifunktionsgeräten deaktiviert werden.', 'Bevor Drucker, Kopierer und Multifunktionsgeräte beschafft werden, MUSS der sichere Einsatz geplant werden.', 'Außerdem MUSS festgelegt sein, wer auf die Drucker, Kopierer und Multifunktionsgeräte zugreifen darf.', 'Der IT-Betrieb MUSS Drucker, Kopierer und Multifunktionsgeräte so aufstellen und absichern, dass nur befugte Personen die Geräte verwenden und auf verarbeitete Informationen zugreifen können.', 'Nur berechtigte Personen SOLLTEN auf die ausgedruckten oder kopierten Dokumente zugreifen können.', 'Außerdem MUSS sichergestellt sein, dass nur berechtigte Personen die Geräte administrieren, warten und reparieren können.', 'Nicht benötigte, aber ausgedruckte Dokumente mit vertraulichen Informationen MÜSSEN in geeigneter Weise vernichtet werden.', 'Nicht benötigte Gerätefunktionen SOLLTEN abgeschaltet werden.', 'Sind Heimarbeitsplätze mit Druckern, Kopierern oder Multifunktionsgeräten ausgestattet, SOLLTE gewährleistet werden, dass die ausgedruckten Informationen auch direkt vor Ort geeignet vernichtet werden können, wenn sie nicht mehr benötigt werden.', 'Wiedergefundene Wechseldatenträger DÜRFEN NICHT ohne vorherige Überprüfung auf Manipulation und Schadsoftware verwendet werden.', 'welche Wechseldatenträger genutzt werden und wer diese einsetzen darf,', 'welche Daten auf Wechseldatenträgern gespeichert werden dürfen und welche nicht,', 'wie die auf Wechseldatenträgern gespeicherten Daten vor unbefugtem Zugriff, Manipulation und Verlust geschützt werden,', 'ob Wechseldatenträger an fremde IT-Systeme angeschlossen werden dürfen und was dabei zu beachten ist,', 'mit welchen externen Institutionen Wechseldatenträger ausgetauscht werden dürfen und welche Sicherheitsregelungen dabei zu beachten sind,', 'wie Wechseldatenträger zu versenden sind sowie', 'wie der Verbreitung von Schadsoftware über Wechseldatenträger vorgebeugt wird.', 'Die Institution SOLLTE die Verwendung von privaten Wechseldatenträgern untersagen.', 'Die Benutzenden MÜSSEN bei ihrer Meldung angeben, welche Informationen auf dem Wechseldatenträger gespeichert sind.', 'wie die Daten auf den Wechseldatenträgern gelöscht werden sollen,', 'Bevor Wechseldatenträger weitergegeben, wiederverwendet oder ausgesondert werden, SOLLTEN sie in geeigneter Weise sicher gelöscht werden.', 'Werden Fahrzeuge ausgesondert, SOLLTEN keine schützenswerten Informationen in den Fahrzeugen verbleiben.', 'Werden Fahrzeuge in fremden Institutionen gewartet, SOLLTE geprüft werden, ob alle nicht benötigten, zum Fahrzeug dazugehörigen portablen IT-Systeme entfernt werden.', 'Es SOLLTE eine Richtlinie für den richtigen Umgang mit Wechseldatenträgern erstellt werden.', 'Wenn Wechseldatenträger außerhalb eines sicheren Bereiches verwendet oder transportiert werden und dabei vertrauliche Daten enthalten, MÜSSEN sie mit einem sicheren Verfahren verschlüsselt werden.', 'Die Institution MUSS sicherstellen, dass nur Daten auf Wechseldatenträger übertragen werden, die auf Schadsoftware überprüft wurden.', 'Bevor Daten von Wechseldatenträgern verarbeitet werden, MÜSSEN sie auf Schadsoftware überprüft werden.', 'Die Benutzenden MÜSSEN umgehend melden, wenn ein Wechseldatenträger gestohlen oder verloren wurde oder der Verdacht einer Manipulation besteht.', 'Hierfür MUSS es in der Institution klare Meldewege und Zuständigkeiten geben.', 'Die Institution MUSS die Benutzenden darüber informieren, dass sie keine Wechseldatenträger, die aus unbekannten Quellen stammen, an ihre IT-Systeme anschließen dürfen.']

wiba_id = ['APP.6.A1', 'APP.6.A1', 'APP.1.1.A13', 'APP.1.2.A1', 'APP.1.2.A1', 'APP.1.2.A1', 'APP.1.2.A1', 'APP.1.2.A1', 'APP.1.2.A2', 'APP.1.2.A2', 'APP.1.2.A2', 'APP.1.2.A3', 'APP.1.2.A3', 'APP.1.2.A3', 'APP.1.2.A3', 'APP.1.2.A3', 'APP.1.2.A3', 'APP.1.2.A3', 'APP.1.2.A3', 'APP.1.2.A3', 'APP.1.2.A6', 'APP.1.2.A6', 'APP.1.2.A6', 'APP.1.2.A6', 'APP.6.A3', 'APP.6.A4', 'APP.6.A4', 'INF.10.A7', 'APP.5.3.A1', 'APP.5.3.A1', 'APP.6.A4', 'APP.1.1.A17', 'APP.1.1.A17', 'APP.1.1.A2', 'APP.1.1.A3', 'APP.1.1.A3', 'APP.1.1.A12', 'APP.6.A1', 'APP.1.1.A13', 'APP.2.1.A3', 'APP.2.1.A5', 'APP.2.2.A6', 'APP.2.2.A6', 'APP.2.2.A16', 'APP.2.2.A16', 'APP.2.2.A16', 'APP.2.2.A16', 'APP.2.2.A16', 'APP.2.2.A17', 'APP.2.2.A17', 'APP.2.2.A6', 'APP.2.2.A5', 'APP.2.2.A16', 'APP.3.1.A1', 'APP.3.1.A4', 'APP.3.1.A4', 'APP.3.1.A1', 'APP.3.1.A1', 'APP.3.1.A4', 'APP.3.1.A14', 'APP.3.1.A14', 'APP.3.2.A1', 'APP.3.2.A11', 'APP.3.2.A11', 'APP.3.2.A1', 'APP.3.2.A2', 'APP.3.2.A4', 'APP.3.2.A4', 'APP.3.2.A1', 'APP.3.2.A5', 'APP.3.2.A11', 'APP.3.2.A1', 'APP.3.2.A1', 'APP.3.2.A2', 'APP.3.2.A2', 'APP.3.2.A2', 'APP.3.2.A2', 'APP.3.2.A3', 'APP.3.2.A4', 'APP.3.3.A15', 'APP.3.3.A15', 'APP.3.3.A15', 'APP.3.3.A8', 'APP.3.3.A8', 'APP.3.3.A3', 'APP.3.3.A15', 'APP.3.3.A8', 'APP.3.3.A15', 'APP.3.6.A9', 'APP.3.6.A8', 'APP.3.6.A8', 'APP.3.6.A4', 'APP.3.6.A4', 'APP.3.6.A4', 'APP.3.6.A7', 'APP.3.6.A7', 'APP.3.6.A7', 'APP.3.6.A7', 'APP.3.6.A7', 'APP.3.6.A8', 'APP.3.6.A2', 'APP.3.6.A2', 'APP.3.6.A4', 'APP.3.6.A3', 'APP.3.6.A3', 'APP.3.6.A4', 'APP.3.6.A6', 'APP.5.3.A3', 'CON.1.A2', 'APP.5.3.A1', 'APP.1.2.A1', 'APP.1.2.A2', 'APP.5.3.A2', 'APP.5.3.A2', 'APP.5.3.A2', 'APP.5.3.A2', 'APP.5.3.A2', 'APP.5.3.A2', 'APP.5.3.A4', 'APP.5.3.A4', 'APP.1.2.A3', 'APP.1.2.A6', 'APP.1.2.A13', 'APP.5.3.A1', 'APP.5.3.A1', 'APP.5.3.A2', 'APP.5.3.A1', 'APP.5.3.A1', 'APP.6.A1', 'APP.6.A1', 'APP.5.3.A1', 'APP.6.A3', 'APP.6.A4', 'APP.6.A4', 'APP.6.A4', 'APP.6.A3', 'APP.6.A4', 'APP.6.A4', 'APP.6.A4', 'APP.6.A4', 'APP.1.1.A2', 'APP.1.1.A3', 'APP.1.1.A3', 'APP.1.1.A12', 'APP.6.A3', 'CON.3.A1', 'CON.1.A4', 'CON.1.A4', 'CON.3.A1', 'CON.1.A4', 'CON.3.A1', 'CON.3.A1', 'NET.3.1.A8', 'NET.4.1.A12', 'APP.5.3.A3', 'CON.3.A2', 'CON.3.A1', 'CON.3.A1', 'CON.3.A2', 'CON.3.A2', 'CON.1.A2', 'CON.3.A12', 'CON.3.A12', 'CON.3.A12', 'CON.3.A14', 'CON.3.A14', 'CON.3.A14', 'CON.3.A4', 'CON.3.A1', 'CON.3.A1', 'CON.3.A2', 'CON.3.A2', 'CON.3.A1', 'CON.3.A4', 'CON.3.A4', 'CON.6.A1', 'CON.6.A1', 'CON.6.A11', 'CON.6.A11', 'CON.6.A12', 'CON.6.A12', 'CON.6.A12', 'CON.6.A12', 'CON.6.A12', 'CON.6.A13', 'CON.6.A13', 'CON.6.A13', 'CON.6.A2', 'CON.6.A2', 'CON.6.A2', 'CON.6.A1', 'CON.6.A1', 'CON.6.A2', 'CON.6.A2', 'CON.9.A1', 'CON.9.A1', 'CON.9.A2', 'CON.9.A1', 'DER.1.A5', 'DER.1.A9', 'DER.1.A3', 'DER.1.A3', 'DER.1.A3', 'DER.1.A3', 'DER.1.A10', 'DER.1.A2', 'DER.1.A2', 'DER.1.A12', 'DER.1.A12', 'DER.1.A12', 'DER.2.1.A1', 'DER.2.1.A1', 'DER.2.1.A3', 'DER.2.1.A3', 'DER.2.1.A3', 'DER.2.1.A4', 'DER.2.1.A5', 'DER.2.1.A4', 'DER.2.1.A4', 'DER.2.1.A4', 'DER.2.1.A5', 'DER.2.1.A6', 'DER.2.1.A6', 'DER.2.1.A6', 'DER.2.1.A6', 'DER.2.1.A6', 'DER.2.1.A6', 'DER.2.1.A6', 'DER.2.1.A1', 'DER.2.1.A2', 'DER.2.1.A3', 'DER.2.1.A3', 'DER.2.1.A3', 'DER.2.1.A5', 'DER.2.1.A5', 'DER.2.2.A1', 'DER.2.2.A3', 'DER.2.2.A3', 'INF.7.A1', 'INF.7.A5', 'INF.7.A6', 'INF.7.A6', 'INF.7.A6', 'INF.7.A7', 'INF.7.A7', 'INF.1.A6', 'INF.1.A7', 'INF.1.A7', 'INF.1.A7', 'INF.1.A6', 'INF.7.A2', 'INF.7.A2', 'INF.1.A6', 'INF.10.A6', 'INF.10.A6', 'INF.10.A6', 'APP.1.1.A12', 'INF.10.A3', 'INF.10.A3', 'INF.7.A2', 'INF.7.A2', 'INF.10.A1', 'INF.10.A7', 'INF.10.A6', 'INF.1.A3', 'INF.1.A3', 'INF.10.A6', 'INF.11.A3', 'INF.8.A2', 'INF.11.A3', 'INF.11.A3', 'INF.9.A1', 'INF.9.A1', 'INF.9.A4', 'INF.8.A1', 'INF.8.A1', 'INF.2.A7', 'INF.2.A7', 'INF.2.A7', 'INF.2.A3', 'INF.2.A3', 'INF.2.A3', 'INF.2.A3', 'INF.2.A3', 'INF.2.A5', 'INF.1.A4', 'INF.2.A9', 'INF.2.A6', 'INF.2.A1', 'INF.2.A2', 'INF.2.A3', 'INF.2.A5', 'INF.2.A6', 'INF.2.A8', 'INF.2.A9', 'INF.5.A2', 'INF.5.A3', 'INF.5.A3', 'INF.5.A4', 'INF.5.A3', 'INF.5.A7', 'INF.6.A2', 'INF.6.A4', 'INF.6.A4', 'INF.6.A2', 'INF.6.A2', 'INF.6.A2', 'INF.6.A3', 'INF.6.A1', 'INF.1.A5', 'INF.1.A6', 'INF.10.A3', 'INF.2.A8', 'INF.7.A2', 'INF.7.A1', 'INF.1.A9', 'INF.10.A1', 'INF.1.A6', 'INF.10.A3', 'INF.7.A2', 'INF.1.A6', 'INF.7.A2', 'INF.10.A1', 'INF.1.A3', 'INF.8.A3', 'INF.8.A3', 'INF.9.A3', 'INF.9.A3', 'INF.9.A3', 'INF.8.A5', 'INF.9.A6', 'INF.11.A10', 'INF.8.A2', 'INF.9.A2', 'INF.9.A2', 'INF.9.A2', 'INF.9.A4', 'INF.9.A6', 'INF.9.A3', 'INF.9.A2', 'SYS.4.5.A5', 'SYS.4.5.A5', 'INF.9.A2', 'INF.11.A3', 'INF.8.A2', 'INF.11.A3', 'INF.9.A2', 'INF.9.A1', 'INF.8.A1', 'INF.11.A3', 'INF.9.A5', 'INF.9.A5', 'INF.9.A4', 'INF.9.A2', 'INF.9.A5', 'INF.9.A5', 'INF.8.A5', 'INF.9.A6', 'ISMS.1.A1', 'ISMS.1.A1', 'ISMS.1.A1', 'ISMS.1.A1', 'ISMS.1.A2', 'ISMS.1.A1', 'ISMS.1.A2', 'ISMS.1.A2', 'ISMS.1.A1', 'ISMS.1.A1', 'ISMS.1.A8', 'ISMS.1.A8', 'ISMS.1.A8', 'ISMS.1.A8', 'NET.1.1.A21', 'NET.1.1.A7', 'NET.1.1.A7', 'NET.1.1.A9', 'NET.1.1.A5', 'NET.1.1.A10', 'NET.1.1.A4', 'NET.1.1.A2', 'NET.1.1.A21', 'NET.1.1.A2', 'NET.1.1.A8', 'NET.1.1.A11', 'NET.1.1.A11', 'NET.1.1.A9', 'NET.1.1.A4', 'NET.1.1.A8', 'NET.1.1.A4', 'NET.1.1.A4', 'NET.1.1.A5', 'NET.1.1.A10', 'NET.1.1.A4', 'NET.1.1.A8', 'NET.1.1.A5', 'NET.1.2.A10', 'NET.1.2.A10', 'NET.1.2.A9', 'NET.1.2.A7', 'NET.1.2.A7', 'NET.1.2.A7', 'NET.1.2.A7', 'NET.1.2.A8', 'NET.1.2.A9', 'NET.1.2.A7', 'NET.1.2.A8', 'NET.2.1.A5', 'NET.2.1.A5', 'NET.2.1.A1', 'NET.2.1.A2', 'NET.2.1.A4', 'NET.2.1.A8', 'NET.2.1.A6', 'NET.2.1.A13', 'NET.2.1.A1', 'NET.2.1.A2', 'NET.2.1.A3', 'NET.2.1.A4', 'NET.2.1.A5', 'NET.2.2.A3', 'NET.2.2.A1', 'NET.2.2.A1', 'NET.2.2.A2', 'NET.2.2.A3', 'CON.3.A2', 'NET.3.1.A4', 'NET.3.1.A4', 'NET.3.1.A4', 'NET.3.1.A7', 'NET.3.1.A7', 'NET.3.1.A7', 'NET.3.1.A7', 'NET.3.1.A7', 'NET.3.1.A4', 'NET.3.1.A4', 'NET.3.1.A1', 'NET.3.1.A1', 'NET.3.1.A1', 'NET.3.2.A18', 'NET.3.2.A18', 'NET.3.2.A6', 'NET.3.2.A6', 'NET.3.2.A18', 'NET.3.2.A6', 'NET.3.2.A6', 'NET.3.2.A9', 'NET.3.2.A9', 'NET.3.2.A9', 'NET.3.2.A9', 'NET.3.2.A9', 'NET.3.2.A2', 'NET.3.2.A2', 'NET.3.2.A3', 'NET.3.2.A3', 'NET.3.2.A3', 'NET.3.2.A3', 'NET.3.2.A17', 'NET.3.2.A17', 'NET.3.2.A3', 'NET.3.2.A4', 'NET.3.2.A22', 'NET.3.3.A2', 'NET.3.3.A3', 'NET.3.3.A7', 'NET.3.3.A7', 'CON.3.A15', 'NET.4.1.A18', 'NET.4.1.A7', 'NET.4.1.A7', 'NET.4.1.A5', 'NET.4.1.A18', 'NET.4.1.A8', 'NET.4.1.A8', 'NET.4.1.A8', 'NET.4.1.A5', 'NET.4.2.A3', 'NET.4.2.A5', 'NET.4.3.A2', 'NET.4.3.A1', 'NET.4.3.A2', 'OPS.1.1.1.A4', 'OPS.1.1.1.A2', 'OPS.1.1.1.A4', 'OPS.1.1.1.A1', 'OPS.1.1.1.A4', 'OPS.1.1.1.A2', 'OPS.1.1.1.A2', 'OPS.1.1.1.A2', 'OPS.1.1.1.A1', 'OPS.1.1.2.A21', 'OPS.1.1.2.A22', 'OPS.1.1.2.A2', 'OPS.1.1.2.A4', 'OPS.1.1.2.A5', 'OPS.1.1.2.A5', 'OPS.1.1.2.A5', 'OPS.1.1.2.A5', 'OPS.1.1.2.A21', 'OPS.1.1.2.A2', 'OPS.1.1.2.A2', 'OPS.1.1.2.A22', 'OPS.1.1.2.A2', 'OPS.1.1.2.A4', 'OPS.1.1.2.A22', 'OPS.1.1.2.A5', 'OPS.1.1.2.A21', 'OPS.1.1.2.A6', 'OPS.1.1.2.A6', 'OPS.1.1.2.A6', 'OPS.1.1.2.A22', 'OPS.1.1.3.A3', 'OPS.1.1.3.A3', 'OPS.1.1.3.A15', 'OPS.1.1.3.A15', 'OPS.1.1.3.A1', 'OPS.1.1.3.A15', 'OPS.1.1.3.A1', 'OPS.1.1.3.A3', 'OPS.1.1.3.A15', 'OPS.1.1.3.A15', 'OPS.1.1.3.A1', 'OPS.1.1.3.A1', 'OPS.1.1.3.A15', 'OPS.1.1.4.A3', 'OPS.1.1.4.A7', 'OPS.1.1.4.A7', 'OPS.1.1.4.A7', 'OPS.1.1.4.A7', 'OPS.1.1.4.A5', 'OPS.1.1.4.A3', 'OPS.1.1.4.A5', 'OPS.1.1.4.A6', 'OPS.1.1.4.A3', 'OPS.1.1.4.A2', 'OPS.1.1.4.A2', 'OPS.1.1.5.A10', 'OPS.1.1.5.A5', 'OPS.1.1.5.A3', 'OPS.1.1.5.A3', 'OPS.1.1.5.A5', 'OPS.1.1.5.A5', 'OPS.1.1.5.A4', 'OPS.1.1.5.A5', 'OPS.1.1.5.A3', 'OPS.1.1.5.A4', 'OPS.1.2.4.A2', 'OPS.1.2.4.A5', 'OPS.1.2.5.A3', 'OPS.1.2.5.A5', 'OPS.1.2.5.A5', 'OPS.1.2.5.A5', 'OPS.1.2.5.A1', 'OPS.1.2.5.A2', 'OPS.1.2.5.A3', 'OPS.1.2.5.A3', 'OPS.1.2.5.A3', 'OPS.1.2.5.A3', 'OPS.1.2.5.A8', 'OPS.1.2.5.A5', 'OPS.2.2.A13', 'OPS.2.2.A13', 'OPS.2.2.A9', 'OPS.2.2.A9', 'OPS.2.2.A4', 'OPS.2.2.A9', 'OPS.2.2.A2', 'OPS.2.2.A3', 'OPS.2.2.A3', 'OPS.2.2.A2', 'OPS.2.2.A4', 'OPS.2.2.A9', 'OPS.2.3.A14', 'OPS.2.3.A3', 'OPS.2.3.A3', 'OPS.2.3.A4', 'OPS.2.3.A5', 'OPS.2.3.A6', 'OPS.2.3.A7', 'OPS.2.3.A7', 'OPS.2.3.A11', 'OPS.2.3.A1', 'OPS.2.3.A14', 'OPS.2.3.A14', 'OPS.2.3.A4', 'OPS.2.3.A2', 'OPS.2.3.A14', 'ORP.1.A1', 'ORP.1.A4', 'ORP.1.A15', 'ORP.1.A2', 'ORP.1.A3', 'ORP.1.A2', 'ORP.1.A2', 'ORP.1.A2', 'ORP.1.A4', 'ORP.1.A15', 'ORP.1.A15', 'ORP.2.A5', 'ORP.2.A2', 'ORP.2.A2', 'ORP.2.A2', 'ORP.2.A2', 'ORP.2.A2', 'ORP.2.A14', 'ORP.2.A1', 'ORP.2.A15', 'ORP.2.A15', 'ORP.2.A15', 'ORP.2.A3', 'ORP.2.A3', 'ORP.2.A3', 'ORP.2.A3', 'ORP.2.A4', 'ORP.2.A1', 'ORP.2.A14', 'ORP.2.A4', 'ORP.2.A4', 'ORP.2.A2', 'ORP.2.A4', 'ORP.2.A2', 'ORP.2.A14', 'ORP.2.A15', 'ORP.2.A3', 'ORP.3.A1', 'ORP.3.A6', 'ORP.3.A1', 'ORP.3.A1', 'ORP.3.A1', 'ORP.3.A3', 'ORP.3.A3', 'ORP.4.A23', 'ORP.4.A8', 'ORP.4.A8', 'ORP.4.A8', 'ORP.4.A8', 'ORP.4.A8', 'ORP.4.A8', 'ORP.4.A8', 'ORP.4.A8', 'ORP.4.A8', 'ORP.4.A8', 'ORP.4.A8', 'ORP.4.A8', 'ORP.4.A8', 'ORP.4.A23', 'ORP.4.A2', 'ORP.4.A2', 'ORP.4.A3', 'ORP.4.A3', 'ORP.4.A3', 'ORP.4.A3', 'ORP.4.A4', 'ORP.4.A1', 'ORP.4.A5', 'ORP.4.A6', 'ORP.4.A7', 'ORP.4.A5', 'ORP.4.A6', 'ORP.4.A5', 'ORP.4.A8', 'ORP.4.A9', 'ORP.4.A23', 'ORP.4.A23', 'ORP.4.A9', 'ORP.4.A23', 'ORP.4.A1', 'ORP.4.A6', 'ORP.4.A7', 'ORP.4.A1', 'ORP.4.A2', 'ORP.4.A1', 'ORP.4.A2', 'ORP.4.A2', 'ORP.4.A3', 'ORP.4.A5', 'ORP.4.A6', 'ORP.4.A7', 'SYS.1.1.A1', 'SYS.1.1.A9', 'SYS.1.1.A2', 'SYS.1.1.A1', 'SYS.1.1.A1', 'SYS.1.1.A10', 'SYS.1.1.A10', 'SYS.1.1.A10', 'SYS.1.1.A10', 'SYS.1.1.A10', 'SYS.1.1.A10', 'SYS.1.1.A10', 'SYS.1.1.A1', 'SYS.1.1.A1', 'SYS.1.1.A2', 'SYS.1.1.A1', 'SYS.1.1.A1', 'SYS.1.1.A6', 'SYS.1.1.A15', 'SYS.1.1.A10', 'SYS.1.2.3.A1', 'SYS.1.2.3.A3', 'SYS.1.2.3.A2', 'SYS.1.2.3.A1', 'SYS.1.2.3.A2', 'SYS.1.2.3.A4', 'SYS.1.5.A5', 'SYS.1.5.A5', 'SYS.1.5.A5', 'SYS.1.5.A12', 'SYS.1.5.A12', 'SYS.1.5.A3', 'SYS.1.5.A7', 'SYS.1.5.A2', 'SYS.1.5.A2', 'SYS.1.5.A3', 'SYS.1.5.A3', 'SYS.1.5.A12', 'SYS.1.5.A12', 'SYS.1.9.A4', 'SYS.1.9.A4', 'SYS.1.9.A4', 'SYS.1.9.A4', 'SYS.1.9.A4', 'SYS.1.9.A4', 'SYS.1.9.A12', 'SYS.1.9.A13', 'SYS.1.9.A13', 'SYS.1.9.A13', 'SYS.1.9.A4', 'SYS.1.9.A7', 'SYS.1.9.A12', 'SYS.2.1.A6', 'SYS.2.1.A28', 'SYS.2.1.A1', 'SYS.2.1.A1', 'SYS.2.1.A8', 'SYS.2.1.A8', 'SYS.2.1.A8', 'SYS.2.1.A8', 'SYS.2.1.A8', 'SYS.2.1.A42', 'SYS.2.1.A24', 'SYS.2.1.A1', 'SYS.2.1.A24', 'SYS.2.1.A27', 'SYS.2.1.A3', 'SYS.2.1.A27', 'SYS.2.1.A28', 'SYS.2.1.A1', 'SYS.2.1.A1', 'SYS.2.1.A16', 'SYS.2.1.A6', 'SYS.2.1.A8', 'SYS.2.1.A16', 'SYS.2.1.A8', 'SYS.2.1.A16', 'SYS.2.1.A42', 'SYS.2.1.A6', 'SYS.2.1.A24', 'SYS.2.2.3.A9', 'SYS.2.2.3.A9', 'SYS.2.2.3.A9', 'SYS.2.2.3.A9', 'SYS.2.2.3.A18', 'SYS.2.2.3.A19', 'SYS.2.2.3.A19', 'SYS.2.2.3.A19', 'SYS.2.2.3.A13', 'SYS.2.2.3.A12', 'SYS.2.2.3.A1', 'SYS.2.2.3.A14', 'SYS.2.2.3.A15', 'SYS.2.2.3.A16', 'SYS.2.2.3.A4', 'SYS.2.2.3.A18', 'SYS.2.2.3.A18', 'SYS.2.5.A2', 'SYS.2.5.A3', 'SYS.3.1.A1', 'SYS.3.1.A12', 'SYS.3.1.A12', 'SYS.3.1.A6', 'SYS.3.1.A3', 'SYS.3.1.A3', 'SYS.3.1.A1', 'SYS.3.1.A13', 'SYS.3.1.A9', 'SYS.3.1.A12', 'SYS.3.1.A6', 'SYS.3.1.A3', 'SYS.3.2.1.A5', 'SYS.3.2.1.A4', 'SYS.3.2.1.A6', 'SYS.3.2.1.A6', 'SYS.3.2.1.A8', 'SYS.3.2.1.A8', 'SYS.3.2.1.A8', 'SYS.3.2.1.A7', 'SYS.3.2.1.A3', 'SYS.3.2.1.A3', 'SYS.3.2.1.A4', 'SYS.3.2.1.A4', 'SYS.3.2.1.A4', 'SYS.3.2.1.A4', 'SYS.3.2.1.A1', 'SYS.3.2.1.A4', 'SYS.3.2.1.A4', 'SYS.3.2.1.A5', 'SYS.3.2.1.A5', 'SYS.3.2.1.A6', 'SYS.3.2.1.A6', 'SYS.3.2.1.A8', 'SYS.3.2.1.A3', 'SYS.3.2.1.A4', 'SYS.3.3.A2', 'SYS.3.3.A4', 'SYS.3.3.A4', 'SYS.3.3.A4', 'SYS.3.3.A2', 'SYS.3.3.A3', 'SYS.3.3.A2', 'SYS.3.3.A3', 'SYS.3.3.A3', 'SYS.4.1.A1', 'SYS.4.1.A1', 'SYS.4.1.A1', 'SYS.4.1.A1', 'SYS.4.1.A1', 'SYS.4.1.A1', 'SYS.4.1.A1', 'SYS.4.1.A14', 'SYS.4.1.A14', 'SYS.4.1.A2', 'SYS.4.1.A2', 'SYS.4.1.A7', 'SYS.4.1.A18', 'SYS.4.1.A1', 'SYS.4.1.A1', 'SYS.4.1.A2', 'SYS.4.1.A14', 'SYS.4.1.A2', 'SYS.4.1.A22', 'SYS.4.1.A18', 'SYS.4.1.A22', 'SYS.4.5.A2', 'SYS.4.5.A4', 'SYS.4.5.A4', 'SYS.4.5.A4', 'SYS.4.5.A4', 'SYS.4.5.A4', 'SYS.4.5.A4', 'SYS.4.5.A4', 'SYS.4.5.A4', 'SYS.4.5.A2', 'SYS.4.5.A4', 'SYS.4.5.A7', 'INF.11.A10', 'INF.11.A2', 'SYS.4.5.A4', 'SYS.4.5.A10', 'SYS.4.5.A12', 'SYS.4.5.A12', 'SYS.4.5.A2', 'SYS.4.5.A2', 'SYS.4.5.A1']

flughafen_profil = {
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
    'INF.14': 'Gebäudeautomation',
}

ressort_forschungseinrichtungen_profil = {
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
    'CON.11.1': 'Geheimschutz',
    'OPS.1.1.1': 'Allgemeiner IT Betrieb',
    'OPS.1.1.2': 'Ordnungsgemäße IT Administration',
    'OPS.1.1.3': 'Patch und Änderungsmanagement',
    'OPS.1.1.4': 'Schutz vor Schadprogrammen',
    'OPS.1.1.5': 'Protokollierung',
    'OPS.1.1.6': 'Software, Tests und Freigaben',
    'OPS.1.2.2': 'Archivierung',
    'OPS.1.2.4': 'Telearbeit',
    'OPS.1.2.5': 'Fernwartung',
    'OPS.1.2.6': 'NTP Zeitsynchronisation',
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
    'APP.3.1': 'Webanwendungen und Webservices',
    'APP.3.2': 'Webserver',
    'APP.3.3': 'Fileserver',
    'APP.3.6': 'DNS Server',
    'APP.4.2': 'SAP ERP System',
    'APP.4.3': 'Relationale Datenbanksysteme',
    'APP.5.2': 'Microsoft Exchange und Outlook',
    'APP.5.3': 'Allgemeiner Email Client und Server',
    'APP.5.4': 'Unified Communications und Collaboration',
    'APP.6': 'Allgemeine Software',
    'SYS.1.1': 'Allgemeiner Server',
    'SYS.1.2.3': 'Windows Server',
    'SYS.2.1': 'Allgemeiner Client',
    'SYS.2.2.3': 'Clients unter Windows',
    'SYS.3.1': 'Laptops',
    'SYS.3.2.1': 'Allgemeine Smartphones und Tablets',
    'SYS.3.2.3': 'iOS for Enterprise',
    'SYS.3.2.4': 'Android',
    'SYS.3.3': 'Mobiltelefon',
    'NET.1.1': 'Netzarchitektur und -design',
    'NET.1.2': 'Netzmanagement',
    'NET.2.1': 'WLAN Betrieb',
    'NET.2.2': 'WLAN Nutzung',
    'NET.3.1': 'Router und Switches',
    'NET.3.2': 'Firewall',
    'NET.3.3': 'VPN',
    'NET.4.1': 'TK-Anlagen',
    'INF.1': 'Allgemeines Gebäude',
    'INF.2': 'Rechenzentrum und Serverraum',
    'INF.5': 'Raum sowie Schrank für technische Infrastruktur',
    'INF.7': 'Büroarbeitsplatz',
    'INF.8': 'Häuslicher Arbeitsplatz',
    'INF.9': 'Mobiler Arbeitsplatz',
    'INF.10': 'Besprechungs-, Veranstaltungs- und Schulungsräume',
    'INF.12': 'Verkabelung',
}

e_akte_profil = {
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
    'CON.9': 'Informationsaustausch',
    'CON.11.1': 'Geheimschutz',
    'OPS.1.1.1': 'Allgemeiner IT Betrieb',
    'OPS.1.1.2': 'Ordnungsgemäße IT Administration',
    'OPS.1.1.3': 'Patch und Änderungsmanagement',
    'OPS.1.1.4': 'Schutz vor Schadprogrammen',
    'OPS.1.1.5': 'Protokollierung',
    'OPS.1.1.6': 'Software, Tests und Freigaben',
    'OPS.1.1.7': 'Systemmanagement',
    'OPS.1.2.4': 'Telearbeit',
    'OPS.1.2.5': 'Fernwartung',
    'OPS.1.2.6': 'NTP Zeitsynchronisation',
    'DER.1': 'Detektion von sicherheitsrelevanten Ereignissen',
    'DER.2.1': 'Behandlung von Sicherheitsvorfällen',
    'DER.2.2': 'Vorsorge für die IT-Forensik',
    'DER.3.2': 'Revisionen auf Basis des Leitfadens IS-Revisionen',
    'DER.4': 'Notfallmanagement',
    'APP.1.1': 'Office Produkte',
    'APP.1.2': 'Webbrowser',
    'APP.2.1': 'Allgemeiner Verzeichnisdienst',
    'APP.2.2': 'Active Directory Domain Services',
    'APP.3.3': 'Fileserver',
    'APP.3.6': 'DNS Server',
    'APP.5.2': 'Microsoft Exchange und Outlook',
    'APP.5.3': 'Allgemeiner Email Client und Server',
    'APP.5.4': 'Unified Communications und Collaboration',
    'APP.6': 'Allgemeine Software',
    'SYS.1.1': 'Allgemeiner Server',
    'SYS.1.2.3': 'Windows Server',
    'SYS.1.5': 'Virtualisierung',
    'SYS.1.8': 'Speicherlösungen',
    'SYS.2.1': 'Allgemeiner Client',
    'SYS.2.2.3': 'Clients unter Windows',
    'SYS.2.3': 'Clients unter Linux und Unix',
    'SYS.3.1': 'Laptops',
    'SYS.3.2.1': 'Allgemeine Smartphones und Tablets',
    'SYS.3.2.2': 'Mobile Device Management',
    'SYS.3.2.3': 'iOS for Enterprise',
    'SYS.3.2.4': 'Android',
    'SYS.4.1': 'Drucker, Kopierer und Multifunktionsgeräte',
    'SYS.4.5': 'Wechseldatenträger',
    'NET.1.1': 'Netzarchitektur und -design',
    'NET.1.2': 'Netzmanagement',
    'NET.2.1': 'WLAN Betrieb',
    'NET.2.2': 'WLAN Nutzung',
    'NET.3.1': 'Router und Switches',
    'NET.3.2': 'Firewall',
    'NET.3.3': 'VPN',
    'INF.1': 'Allgemeines Gebäude',
    'INF.2': 'Rechenzentrum und Serverraum',
    'INF.5': 'Raum sowie Schrank für technische Infrastruktur',
    'INF.7': 'Büroarbeitsplatz',
    'INF.8': 'Häuslicher Arbeitsplatz',
    'INF.9': 'Mobiler Arbeitsplatz',
    'INF.10': 'Besprechungs-, Veranstaltungs- und Schulungsräume',
    'INF.12': 'Verkabelung',
}

leitstellen_profil = {
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
    'CON.9': 'Informationsaustausch',
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
    'OPS.2.3': 'Nutzung von Outsourcing',
    'DER.1': 'Detektion von sicherheitsrelevanten Ereignissen',
    'DER.2.1': 'Behandlung von Sicherheitsvorfällen',
    'DER.2.2': 'Vorsorge für die IT-Forensik',
    'DER.2.3': 'Bereinigung weitreichender Sicherheitsvorfälle',
    'DER.3.1': 'Audits und Revisionen',
    'DER.4': 'Notfallmanagement',
    'APP.1.1': 'Office Produkte',
    'APP.1.2': 'Webbrowser',
    'APP.2.1': 'Allgemeiner Verzeichnisdienst',
    'APP.2.2': 'Active Directory Domain Services',
    'APP.3.1': 'Webanwendungen und Webservices',
    'APP.3.2': 'Webserver',
    'APP.3.3': 'Fileserver',
    'APP.3.6': 'DNS Server',
    'APP.4.3': 'Relationale Datenbanksysteme',
    'APP.4.4': 'Kubernetes',
    'APP.5.3': 'Allgemeiner Email Client und Server',
    'APP.6': 'Allgemeine Software',
    'SYS.1.1': 'Allgemeiner Server',
    'SYS.1.2.2': 'Windows Server 2012',
    'SYS.1.2.3': 'Windows Server',
    'SYS.1.3': 'Server unter Linux und Unix',
    'SYS.1.5': 'Virtualisierung',
    'SYS.1.6': 'Containerisierung',
    'SYS.1.8': 'Speicherlösungen',
    'SYS.2.1': 'Allgemeiner Client',
    'SYS.2.2.3': 'Clients unter Windows',
    'SYS.2.3': 'Clients unter Linux und Unix',
    'SYS.2.5': 'Client Virtualisierung',
    'SYS.3.1': 'Laptops',
    'SYS.4.1': 'Drucker, Kopierer und Multifunktionsgeräte',
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
    'NET.4.1': 'TK-Anlagen',
    'NET.4.2': 'VoIP',
    'NET.4.3': 'Faxgeräte und Faxserver',
    'INF.1': 'Allgemeines Gebäude',
    'INF.2': 'Rechenzentrum und Serverraum',
    'INF.5': 'Raum sowie Schrank für technische Infrastruktur',
    'INF.6': 'Datenträgerarchiv',
    'INF.7': 'Büroarbeitsplatz',
    'INF.8': 'Häuslicher Arbeitsplatz',
    'INF.10': 'Besprechungs-, Veranstaltungs- und Schulungsräume',
    'INF.12': 'Verkabelung',
    'INF.13': 'Technisches Gebäudemanagement',
    'INF.14': 'Gebäudeautomation',
}

fuenfg_eigenbetrieb_profil = {
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
    'CON.9': 'Informationsaustausch',
    'OPS.1.1.1': 'Allgemeiner IT Betrieb',
    'OPS.1.1.2': 'Ordnungsgemäße IT Administration',
    'OPS.1.1.3': 'Patch und Änderungsmanagement',
    'OPS.1.1.4': 'Schutz vor Schadprogrammen',
    'OPS.1.1.5': 'Protokollierung',
    'OPS.1.1.6': 'Software, Tests und Freigaben',
    'OPS.1.1.7': 'Systemmanagement',
    'OPS.1.2.5': 'Fernwartung',
    'DER.1': 'Detektion von sicherheitsrelevanten Ereignissen',
    'DER.2.1': 'Behandlung von Sicherheitsvorfällen',
    'DER.2.2': 'Vorsorge für die IT-Forensik',
    'DER.2.3': 'Bereinigung weitreichender Sicherheitsvorfälle',
    'DER.3.1': 'Audits und Revisionen',
    'DER.4': 'Notfallmanagement',
    'APP.1.2': 'Webbrowser',
    'APP.6': 'Allgemeine Software',
    'SYS.1.1': 'Allgemeiner Server',
    'SYS.1.2.2': 'Windows Server 2012',
    'SYS.1.2.3': 'Windows Server',
    'SYS.1.3': 'Server unter Linux und Unix',
    'SYS.1.5': 'Virtualisierung',
    'SYS.1.6': 'Containerisierung',
    'SYS.2.1': 'Allgemeiner Client',
    'SYS.2.2.3': 'Clients unter Windows',
    'SYS.2.3': 'Clients unter Linux und Unix',
    'SYS.2.4': 'Clients unter macOS',
    'SYS.3.1': 'Laptops',
    'SYS.3.2.1': 'Allgemeine Smartphones und Tablets',
    'SYS.3.2.3': 'iOS for Enterprise',
    'SYS.3.2.4': 'Android',
    'SYS.3.3': 'Mobiltelefon',
    'SYS.4.3': 'Eingebettete Systeme',
    'SYS.4.4': 'Allgemeines IoT-Gerät',
    'IND.1': 'Prozessleit- und Automatisierungstechnik',
    'IND.2.1': 'Allgemeine ICS Komponente',
    'IND.2.2': 'Speicherprogrammierbare Steuerung',
    'IND.2.3': 'Sensoren und Aktoren',
    'IND.2.4': 'Maschine',
    'IND.2.7': 'Safety Instrumented Systems',
    'IND.3.2': 'Fernwartung im industriellen Umfeld',
    'NET.1.1': 'Netzarchitektur und -design',
    'NET.1.2': 'Netzmanagement',
    'NET.3.1': 'Router und Switches',
    'NET.3.2': 'Firewall',
    'INF.1': 'Allgemeines Gebäude',
    'INF.2': 'Rechenzentrum und Serverraum',
    'INF.5': 'Raum sowie Schrank für technische Infrastruktur',
    'INF.12': 'Verkabelung',
}

oberste_bundesbehoerden_profil = {
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
    'CON.9': 'Informationsaustausch',
    'CON.11.1': 'Geheimschutz',
    'OPS.1.1.1': 'Allgemeiner IT Betrieb',
    'OPS.1.1.2': 'Ordnungsgemäße IT Administration',
    'OPS.1.1.3': 'Patch und Änderungsmanagement',
    'OPS.1.1.4': 'Schutz vor Schadprogrammen',
    'OPS.1.1.5': 'Protokollierung',
    'OPS.1.1.6': 'Software, Tests und Freigaben',
    'OPS.1.2.2': 'Archivierung',
    'OPS.1.2.4': 'Telearbeit',
    'OPS.1.2.5': 'Fernwartung',
    'OPS.1.2.6': 'NTP Zeitsynchronisation',
    'OPS.2.2': 'Cloud Nutzung',
    'DER.1': 'Detektion von sicherheitsrelevanten Ereignissen',
    'DER.2.1': 'Behandlung von Sicherheitsvorfällen',
    'DER.2.2': 'Vorsorge für die IT-Forensik',
    'DER.2.3': 'Bereinigung weitreichender Sicherheitsvorfälle',
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
    'APP.3.6': 'DNS Server',
    'APP.4.3': 'Relationale Datenbanksysteme',
    'APP.5.2': 'Microsoft Exchange und Outlook',
    'APP.5.3': 'Allgemeiner Email Client und Server',
    'APP.5.4': 'Unified Communications und Collaboration',
    'APP.6': 'Allgemeine Software',
    'SYS.1.1': 'Allgemeiner Server',
    'SYS.1.2.3': 'Windows Server',
    'SYS.1.3': 'Server unter Linux und Unix',
    'SYS.1.5': 'Virtualisierung',
    'SYS.1.8': 'Speicherlösungen',
    'SYS.2.1': 'Allgemeiner Client',
    'SYS.2.2.3': 'Clients unter Windows',
    'SYS.2.3': 'Clients unter Linux und Unix',
    'SYS.3.1': 'Laptops',
    'SYS.3.2.1': 'Allgemeine Smartphones und Tablets',
    'SYS.3.2.2': 'Mobile Device Management',
    'SYS.3.2.3': 'iOS for Enterprise',
    'SYS.3.2.4': 'Android',
    'SYS.3.3': 'Mobiltelefon',
    'SYS.4.1': 'Drucker, Kopierer und Multifunktionsgeräte',
    'SYS.4.4': 'Allgemeines IoT-Gerät',
    'SYS.4.5': 'Wechseldatenträger',
    'NET.1.1': 'Netzarchitektur und -design',
    'NET.2.1': 'WLAN Betrieb',
    'NET.2.2': 'WLAN Nutzung',
    'NET.3.1': 'Router und Switches',
    'NET.3.2': 'Firewall',
    'NET.3.3': 'VPN',
    'NET.3.4': 'Network Access Control',
    'NET.4.1': 'TK-Anlagen',
    'NET.4.2': 'VoIP',
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

uas_profil = {
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
    'CON.9': 'Informationsaustausch',
    'CON.11.1': 'Geheimschutz',
    'OPS.1.1.1': 'Allgemeiner IT Betrieb',
    'OPS.1.1.2': 'Ordnungsgemäße IT Administration',
    'OPS.1.1.3': 'Patch und Änderungsmanagement',
    'OPS.1.1.4': 'Schutz vor Schadprogrammen',
    'OPS.1.1.5': 'Protokollierung',
    'OPS.1.1.6': 'Software, Tests und Freigaben',
    'OPS.1.1.7': 'Systemmanagement',
    'OPS.1.2.2': 'Archivierung',
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
    'DER.4': 'Notfallmanagement',
    'APP.1.2': 'Webbrowser',
    'APP.1.4': 'Mobile Anwendungen',
    'APP.2.1': 'Allgemeiner Verzeichnisdienst',
    'APP.2.2': 'Active Directory Domain Services',
    'APP.2.3': 'OpenLDAP',
    'APP.3.1': 'Webanwendungen und Webservices',
    'APP.3.2': 'Webserver',
    'APP.3.3': 'Fileserver',
    'APP.3.4': 'Samba',
    'APP.4.4': 'Kubernetes',
    'APP.5.2': 'Microsoft Exchange und Outlook',
    'APP.5.4': 'Unified Communications und Collaboration',
    'APP.6': 'Allgemeine Software',
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

kommunalverwaltung_profil = {
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
    'CON.9': 'Informationsaustausch',
    'OPS.1.1.1': 'Allgemeiner IT Betrieb',
    'OPS.1.1.2': 'Ordnungsgemäße IT Administration',
    'OPS.1.1.3': 'Patch und Änderungsmanagement',
    'OPS.1.1.4': 'Schutz vor Schadprogrammen',
    'OPS.1.1.5': 'Protokollierung',
    'OPS.1.2.4': 'Telearbeit',
    'OPS.1.2.5': 'Fernwartung',
    'OPS.2.2': 'Cloud Nutzung',
    'OPS.2.3': 'Nutzung von Outsourcing',
    'DER.1': 'Detektion von sicherheitsrelevanten Ereignissen',
    'DER.2.1': 'Behandlung von Sicherheitsvorfällen',
    'DER.2.2': 'Vorsorge für die IT-Forensik',
    'SYS.1.1': 'Allgemeiner Server',
    'SYS.1.2.3': 'Windows Server',
    'SYS.1.5': 'Virtualisierung',
    'SYS.1.9': 'Terminalserver',
    'SYS.2.1': 'Allgemeiner Client',
    'SYS.2.2.3': 'Clients unter Windows',
    'SYS.2.5': 'Client Virtualisierung',
    'SYS.2.6': 'Virtual Desktop Infrastructure',
    'SYS.3.1': 'Laptops',
    'SYS.3.2.1': 'Allgemeine Smartphones und Tablets',
    'SYS.3.3': 'Mobiltelefon',
    'SYS.4.1': 'Drucker, Kopierer und Multifunktionsgeräte',
    'SYS.4.5': 'Wechseldatenträger',
    'APP.1.1': 'Office Produkte',
    'APP.1.2': 'Webbrowser',
    'APP.2.1': 'Allgemeiner Verzeichnisdienst',
    'APP.2.2': 'Active Directory Domain Services',
    'APP.3.1': 'Webanwendungen und Webservices',
    'APP.3.2': 'Webserver',
    'APP.3.3': 'Fileserver',
    'APP.3.6': 'DNS Server',
    'APP.5.3': 'Allgemeiner Email Client und Server',
    'APP.6': 'Allgemeine Software',
    'NET.1.1': 'Netzarchitektur und -design',
    'NET.1.2': 'Netzmanagement',
    'NET.2.1': 'WLAN Betrieb',
    'NET.2.2': 'WLAN Nutzung',
    'NET.3.1': 'Router und Switches',
    'NET.3.2': 'Firewall',
    'NET.3.3': 'VPN',
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
    'INF.12': 'Verkabelung'
}

fuenfg_fremdbetrieb_profil = {
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
    'CON.9': 'Informationsaustausch',
    'CON.10': 'Entwicklung von Webanwendungen',
    'OPS.1.1.1': 'Allgemeiner IT Betrieb',
    'OPS.1.1.2': 'Ordnungsgemäße IT Administration',
    'OPS.1.1.3': 'Patch und Änderungsmanagement',
    'OPS.1.1.4': 'Schutz vor Schadprogrammen',
    'OPS.1.1.5': 'Protokollierung',
    'OPS.1.1.6': 'Software, Tests und Freigaben',
    'OPS.1.2.5': 'Fernwartung',
    'OPS.2.3': 'Nutzung von Outsourcing',
    'DER.1': 'Detektion von sicherheitsrelevanten Ereignissen',
    'DER.2.1': 'Behandlung von Sicherheitsvorfällen',
    'DER.2.2': 'Vorsorge für die IT-Forensik',
    'DER.2.3': 'Bereinigung weitreichender Sicherheitsvorfälle',
    'DER.3.1': 'Audits und Revisionen',
    'DER.4': 'Notfallmanagement',
    'APP.1.2': 'Webbrowser',
    'APP.6': 'Allgemeine Software',
    'SYS.2.1': 'Allgemeiner Client',
    'SYS.2.2.3': 'Clients unter Windows',
    'SYS.2.3': 'Clients unter Linux und Unix',
    'SYS.2.4': 'Clients unter macOS',
    'SYS.3.1': 'Laptops',
    'SYS.3.2.1': 'Allgemeine Smartphones und Tablets',
    'SYS.3.2.3': 'iOS for Enterprise',
    'SYS.3.2.4': 'Android',
    'SYS.3.3': 'Mobiltelefon',
    'SYS.4.3': 'Eingebettete Systeme',
    'SYS.4.4': 'Allgemeines IoT-Gerät',
    'IND.1': 'Prozessleit- und Automatisierungstechnik',
    'IND.2.1': 'Allgemeine ICS Komponente',
    'IND.2.2': 'Speicherprogrammierbare Steuerung',
    'IND.2.3': 'Sensoren und Aktoren',
    'IND.2.4': 'Maschine',
    'IND.2.7': 'Safety Instrumented Systems',
    'IND.3.2': 'Fernwartung im industriellen Umfeld',
    'NET.1.1': 'Netzarchitektur und -design',
    'NET.1.2': 'Netzmanagement',
    'NET.3.1': 'Router und Switches',
    'NET.3.2': 'Firewall',
    'INF.1': 'Allgemeines Gebäude',
    'INF.2': 'Rechenzentrum und Serverraum',
    'INF.5': 'Raum sowie Schrank für technische Infrastruktur',
    'INF.12': 'Verkabelung',
    'INF.13': 'Technisches Gebäudemanagement',
    'INF.14': 'Gebäudeautomation'
}

# Platzhalter, da Profil geheim. Bei Nutzung nicht benötigte Bausteine manuell entfernen
ikfz_profil = {
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

# Platzhalter, es muss erst eine Modellierung stattfinden, um nicht relevante Bausteine ausschließen zu können
finanzen_sa_profil = {
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

bundesgerichte_profil = {
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
    'CON.9': 'Informationsaustausch',
    'CON.11.1': 'Geheimschutz',
    'OPS.1.1.1': 'Allgemeiner IT Betrieb',
    'OPS.1.1.2': 'Ordnungsgemäße IT Administration',
    'OPS.1.1.3': 'Patch und Änderungsmanagement',
    'OPS.1.1.4': 'Schutz vor Schadprogrammen',
    'OPS.1.1.5': 'Protokollierung',
    'OPS.1.1.6': 'Software, Tests und Freigaben',
    'OPS.1.2.2': 'Archivierung',
    'OPS.1.2.4': 'Telearbeit',
    'OPS.1.2.5': 'Fernwartung',
    'OPS.1.2.6': 'NTP Zeitsynchronisation',
    'OPS.2.2': 'Cloud Nutzung',
    'OPS.2.3': 'Nutzung von Outsourcing',
    'DER.1': 'Detektion von sicherheitsrelevanten Ereignissen',
    'DER.2.1': 'Behandlung von Sicherheitsvorfällen',
    'DER.2.2': 'Vorsorge für die IT-Forensik',
    'DER.2.3': 'Bereinigung weitreichender Sicherheitsvorfälle',
    'DER.3.1': 'Audits und Revisionen',
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
    'APP.3.6': 'DNS Server',
    'APP.4.3': 'Relationale Datenbanksysteme',
    'APP.5.2': 'Microsoft Exchange und Outlook',
    'APP.5.3': 'Allgemeiner Email Client und Server',
    'APP.5.4': 'Unified Communications und Collaboration',
    'APP.6': 'Allgemeine Software',
    'SYS.1.1': 'Allgemeiner Server',
    'SYS.1.2.2': 'Windows Server 2012',
    'SYS.1.2.3': 'Windows Server',
    'SYS.1.3': 'Server unter Linux und Unix',
    'SYS.1.5': 'Virtualisierung',
    'SYS.1.8': 'Speicherlösungen',
    'SYS.2.1': 'Allgemeiner Client',
    'SYS.2.2.3': 'Clients unter Windows',
    'SYS.3.1': 'Laptops',
    'SYS.3.2.1': 'Allgemeine Smartphones und Tablets',
    'SYS.3.2.2': 'Mobile Device Management',
    'SYS.3.2.3': 'iOS for Enterprise',
    'SYS.3.2.4': 'Android',
    'SYS.3.3': 'Mobiltelefon',
    'SYS.4.1': 'Drucker, Kopierer und Multifunktionsgeräte',
    'SYS.4.5': 'Wechseldatenträger',
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
    'INF.1': 'Allgemeines Gebäude',
    'INF.2': 'Rechenzentrum und Serverraum',
    'INF.5': 'Raum sowie Schrank für technische Infrastruktur',
    'INF.7': 'Büroarbeitsplatz',
    'INF.8': 'Häuslicher Arbeitsplatz',
    'INF.9': 'Mobiler Arbeitsplatz',
    'INF.10': 'Besprechungs-, Veranstaltungs- und Schulungsräume',
    'INF.12': 'Verkabelung',
}

chemie_profil = {
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
    'APP.5.4': 'Unified Communications und Collaboration',
    'APP.6': 'Allgemeine Software',
    'APP.7': 'Entwicklung von Individualsoftware',
    'SYS.1.1': 'Allgemeiner Server',
    'SYS.1.2.2': 'Windows Server 2012',
    'SYS.1.2.3': 'Windows Server',
    'SYS.1.3': 'Server unter Linux und Unix',
    'SYS.1.5': 'Virtualisierung',
    'SYS.1.6': 'Containerisierung',
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
    'INF.1': 'Allgemeines Gebäude',
    'INF.2': 'Rechenzentrum und Serverraum',
    'INF.5': 'Raum sowie Schrank für technische Infrastruktur',
    'INF.7': 'Büroarbeitsplatz',
    'INF.8': 'Häuslicher Arbeitsplatz',
    'INF.9': 'Mobiler Arbeitsplatz',
    'INF.10': 'Besprechungs-, Veranstaltungs- und Schulungsräume',
    'INF.12': 'Verkabelung',
    'INF.13': 'Technisches Gebäudemanagement',
    'INF.14': 'Gebäudeautomation'
}

hochschulen_profil = {
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
    'APP.6': 'Allgemeine Software',
    'APP.7': 'Entwicklung von Individualsoftware',
    'SYS.1.1': 'Allgemeiner Server',
    'SYS.1.2.2': 'Windows Server 2012',
    'SYS.1.2.3': 'Windows Server',
    'SYS.1.3': 'Server unter Linux und Unix',
    'SYS.1.5': 'Virtualisierung',
    'SYS.1.6': 'Containerisierung',
    'SYS.1.8': 'Speicherlösungen',
    'SYS.2.1': 'Allgemeiner Client',
    'SYS.2.2.3': 'Clients unter Windows',
    'SYS.2.3': 'Clients unter Linux und Unix',
    'SYS.2.4': 'Clients unter macOS',
    'SYS.3.1': 'Laptops',
    'SYS.3.2.1': 'Allgemeine Smartphones und Tablets',
    'SYS.3.2.2': 'Mobile Device Management',
    'SYS.3.2.3': 'iOS for Enterprise',
    'SYS.3.2.4': 'Android',
    'SYS.3.3': 'Mobiltelefon',
    'SYS.4.1': 'Drucker, Kopierer und Multifunktionsgeräte',
    'SYS.4.4': 'Allgemeines IoT-Gerät',
    'SYS.4.5': 'Wechseldatenträger',
    'NET.1.1': 'Netzarchitektur und -design',
    'NET.1.2': 'Netzmanagement',
    'NET.2.1': 'WLAN Betrieb',
    'NET.2.2': 'WLAN Nutzung',
    'NET.3.1': 'Router und Switches',
    'NET.3.2': 'Firewall',
    'NET.3.3': 'VPN',
    'NET.4.1': 'TK-Anlagen',
    'NET.4.2': 'VoIP',
    'INF.1': 'Allgemeines Gebäude',
    'INF.2': 'Rechenzentrum und Serverraum',
    'INF.5': 'Raum sowie Schrank für technische Infrastruktur',
    'INF.6': 'Datenträgerarchiv',
    'INF.7': 'Büroarbeitsplatz',
    'INF.8': 'Häuslicher Arbeitsplatz',
    'INF.9': 'Mobiler Arbeitsplatz',
    'INF.10': 'Besprechungs-, Veranstaltungs- und Schulungsräume',
    'INF.12': 'Verkabelung',
    'INF.13': 'Technisches Gebäudemanagement',
    'INF.14': 'Gebäudeautomation'
}

weltrauminfrastrukturen_profil = {
    'ISMS.1': 'Sicherheitsmanagement',
    'ORP.1': 'Organisation',
    'ORP.2': 'Personal',
    'ORP.3': 'Sensibilisierung und Schulung zur Informationssicherheit',
    'ORP.4': 'Identitäts- und Berechtigungsmanagement',
    'ORP.5': 'Compliance Management',
    'CON.1': 'Kryptokonzept',
    'CON.3': 'Datensicherungskonzept',
    'CON.6': 'Löschen und Vernichten',
    'CON.7': 'Informationssicherheit auf Auslandsreisen',
    'CON.8': 'Software Entwicklung',
    'CON.9': 'Informationsaustausch',
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
    'APP.3.6': 'DNS Server',
    'APP.4.2': 'SAP ERP System',
    'APP.4.3': 'Relationale Datenbanksysteme',
    'APP.4.4': 'Kubernetes',
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
    'INF.1': 'Allgemeines Gebäude',
    'INF.2': 'Rechenzentrum und Serverraum',
    'INF.7': 'Büroarbeitsplatz',
    'INF.8': 'Häuslicher Arbeitsplatz',
    'INF.9': 'Mobiler Arbeitsplatz',
    'INF.11': 'Allgemeines Fahrzeug',
    'INF.12': 'Verkabelung'
}

bundesautobahn_profil = {
    'ORP.4': 'Identitäts- und Berechtigungsmanagement',
    'CON.1': 'Kryptokonzept',
    'CON.3': 'Datensicherungskonzept',
    'CON.8': 'Software Entwicklung',
    'CON.10': 'Entwicklung von Webanwendungen',
    'CON.11.1': 'Geheimschutz',
    'OPS.1.1.1': 'Allgemeiner IT Betrieb',
    'OPS.1.1.3': 'Patch und Änderungsmanagement',
    'OPS.1.1.4': 'Schutz vor Schadprogrammen',
    'OPS.1.1.5': 'Protokollierung',
    'OPS.1.1.6': 'Software, Tests und Freigaben',
    'OPS.1.1.7': 'Systemmanagement',
    'OPS.1.2.5': 'Fernwartung',
    'OPS.1.2.6': 'NTP Zeitsynchronisation',
    'OPS.2.3': 'Nutzung von Outsourcing',
    'OPS.3.2': 'Anbieten von Outsourcing',
    'DER.1': 'Detektion von sicherheitsrelevanten Ereignissen',
    'APP.1.1': 'Office Produkte',
    'APP.1.2': 'Webbrowser',
    'APP.2.1': 'Allgemeiner Verzeichnisdienst',
    'APP.2.2': 'Active Directory Domain Services',
    'APP.2.3': 'OpenLDAP',
    'APP.3.6': 'DNS Server',
    'APP.4.3': 'Relationale Datenbanksysteme',
    'APP.4.4': 'Kubernetes',
    'APP.6': 'Allgemeine Software',
    'APP.7': 'Entwicklung von Individualsoftware',
    'SYS.1.1': 'Allgemeiner Server',
    'SYS.1.2.2': 'Windows Server 2012',
    'SYS.1.2.3': 'Windows Server',
    'SYS.1.3': 'Server unter Linux und Unix',
    'SYS.1.5': 'Virtualisierung',
    'SYS.1.6': 'Containerisierung',
    'SYS.1.8': 'Speicherlösungen',
    'SYS.1.9': 'Terminalserver',
    'SYS.2.1': 'Allgemeiner Client',
    'SYS.2.2.3': 'Clients unter Windows',
    'SYS.2.3': 'Clients unter Linux und Unix',
    'SYS.2.5': 'Client Virtualisierung',
    'SYS.2.6': 'Virtual Desktop Infrastructure',
    'SYS.4.1': 'Drucker, Kopierer und Multifunktionsgeräte',
    'SYS.4.3': 'Eingebettete Systeme',
    'IND.1': 'Prozessleit- und Automatisierungstechnik',
    'IND.2.1': 'Allgemeine ICS Komponente',
    'IND.2.2': 'Speicherprogrammierbare Steuerung',
    'IND.2.3': 'Sensoren und Aktoren',
    'IND.2.4': 'Maschine',
    'IND.3.2': 'Fernwartung im industriellen Umfeld',
    'NET.1.1': 'Netzarchitektur und -design',
    'NET.1.2': 'Netzmanagement',
    'NET.3.1': 'Router und Switches',
    'NET.3.2': 'Firewall',
    'NET.3.4': 'Network Access Control',
    'NET.4.2': 'VoIP',
    'INF.1': 'Allgemeines Gebäude',
    'INF.2': 'Rechenzentrum und Serverraum',
    'INF.5': 'Raum sowie Schrank für technische Infrastruktur',
    'INF.7': 'Büroarbeitsplatz',
    'INF.12': 'Verkabelung',
    'INF.13': 'Technisches Gebäudemanagement',
    'INF.14': 'Gebäudeautomation'
}

papierfabriken_profil = {
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
    'OPS.1.1.2': 'Ordnungsgemäße IT Administration',
    'OPS.1.1.3': 'Patch und Änderungsmanagement',
    'OPS.1.1.4': 'Schutz vor Schadprogrammen',
    'OPS.1.1.5': 'Protokollierung',
    'OPS.1.1.6': 'Software, Tests und Freigaben',
    'OPS.1.2.2': 'Archivierung',
    'OPS.1.2.4': 'Telearbeit',
    'OPS.2.2': 'Cloud Nutzung',
    'OPS.2.3': 'Nutzung von Outsourcing',
    'OPS.3.2': 'Anbieten von Outsourcing',
    'DER.1': 'Detektion von sicherheitsrelevanten Ereignissen',
    'DER.2.1': 'Behandlung von Sicherheitsvorfällen',
    'DER.2.2': 'Vorsorge für die IT-Forensik',
    'DER.3.1': 'Audits und Revisionen',
    'DER.4': 'Notfallmanagement',
    'APP.1.1': 'Office Produkte',
    'APP.1.2': 'Webbrowser',
    'APP.1.4': 'Mobile Anwendungen',
    'APP.4.2': 'SAP ERP System',
    'APP.4.3': 'Relationale Datenbanksysteme',
    'APP.5.2': 'Microsoft Exchange und Outlook',
    'SYS.1.1': 'Allgemeiner Server',
    'SYS.1.2.2': 'Windows Server 2012',
    'SYS.1.2.3': 'Windows Server',
    'SYS.1.3': 'Server unter Linux und Unix',
    'SYS.1.5': 'Virtualisierung',
    'SYS.2.1': 'Allgemeiner Client',
    'SYS.2.2.3': 'Clients unter Windows',
    'SYS.3.1': 'Laptops',
    'SYS.3.2.1': 'Allgemeine Smartphones und Tablets',
    'SYS.3.2.2': 'Mobile Device Management',
    'SYS.3.2.3': 'iOS for Enterprise',
    'SYS.3.2.4': 'Android',
    'SYS.3.3': 'Mobiltelefon',
    'SYS.4.1': 'Drucker, Kopierer und Multifunktionsgeräte',
    'SYS.4.4': 'Allgemeines IoT-Gerät',
    'SYS.4.5': 'Wechseldatenträger',
    'IND.1': 'Prozessleit- und Automatisierungstechnik',
    'IND.2.1': 'Allgemeine ICS Komponente',
    'IND.2.2': 'Speicherprogrammierbare Steuerung',
    'IND.2.3': 'Sensoren und Aktoren',
    'IND.2.4': 'Maschine',
    'IND.2.7': 'Safety Instrumented Systems',
    'NET.1.1': 'Netzarchitektur und -design',
    'NET.1.2': 'Netzmanagement',
    'NET.2.1': 'WLAN Betrieb',
    'NET.2.2': 'WLAN Nutzung',
    'NET.3.1': 'Router und Switches',
    'NET.3.2': 'Firewall',
    'NET.3.3': 'VPN',
    'NET.4.1': 'TK-Anlagen',
    'NET.4.2': 'VoIP',
    'NET.4.3': 'Faxgeräte und Faxserver',
    'INF.1': 'Allgemeines Gebäude',
    'INF.2': 'Rechenzentrum und Serverraum',
    'INF.7': 'Büroarbeitsplatz',
    'INF.9': 'Mobiler Arbeitsplatz',
    'INF.10': 'Besprechungs-, Veranstaltungs- und Schulungsräume'
}

oberste_landesbehoerden_profil = {
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
    'CON.9': 'Informationsaustausch',
    'OPS.1.1.2': 'Ordnungsgemäße IT Administration',
    'OPS.1.1.3': 'Patch und Änderungsmanagement',
    'OPS.1.1.4': 'Schutz vor Schadprogrammen',
    'OPS.1.1.5': 'Protokollierung',
    'OPS.1.1.6': 'Software, Tests und Freigaben',
    'OPS.1.2.2': 'Archivierung',
    'OPS.1.2.4': 'Telearbeit',
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
    'APP.3.3': 'Fileserver',
    'APP.5.2': 'Microsoft Exchange und Outlook',
    'APP.5.3': 'Allgemeiner Email Client und Server',
    'APP.6': 'Allgemeine Software',
    'SYS.1.1': 'Allgemeiner Server',
    'SYS.1.2.3': 'Windows Server',
    'SYS.1.8': 'Speicherlösungen',
    'SYS.2.1': 'Allgemeiner Client',
    'SYS.2.2.3': 'Clients unter Windows',
    'SYS.3.1': 'Laptops',
    'SYS.3.2.1': 'Allgemeine Smartphones und Tablets',
    'SYS.3.2.2': 'Mobile Device Management',
    'SYS.3.2.4': 'Android',
    'SYS.3.3': 'Mobiltelefon',
    'SYS.4.1': 'Drucker, Kopierer und Multifunktionsgeräte',
    'NET.1.1': 'Netzarchitektur und -design',
    'NET.1.2': 'Netzmanagement',
    'NET.2.1': 'WLAN Betrieb',
    'NET.2.2': 'WLAN Nutzung',
    'NET.3.1': 'Router und Switches',
    'NET.3.2': 'Firewall',
    'NET.3.3': 'VPN',
    'NET.4.1': 'TK-Anlagen',
    'NET.4.2': 'VoIP',
    'NET.4.3': 'Faxgeräte und Faxserver',
    'INF.1': 'Allgemeines Gebäude',
    'INF.2': 'Rechenzentrum und Serverraum',
    'INF.7': 'Büroarbeitsplatz',
    'INF.8': 'Häuslicher Arbeitsplatz',
    'INF.10': 'Besprechungs-, Veranstaltungs- und Schulungsräume'
}

# Platzhalter, da nur für Mitglieder
handwerksbetriebe_profil = {
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

reedereien_land_profil = {
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
    'OPS.1.1.2': 'Ordnungsgemäße IT Administration',
    'OPS.1.1.3': 'Patch und Änderungsmanagement',
    'OPS.1.1.4': 'Schutz vor Schadprogrammen',
    'OPS.1.1.5': 'Protokollierung',
    'OPS.1.2.2': 'Archivierung',
    'OPS.1.2.4': 'Telearbeit',
    'OPS.1.2.5': 'Fernwartung',
    'OPS.2.2': 'Cloud Nutzung',
    'OPS.2.3': 'Nutzung von Outsourcing',
    'OPS.3.2': 'Anbieten von Outsourcing',
    'DER.1': 'Detektion von sicherheitsrelevanten Ereignissen',
    'DER.2.1': 'Behandlung von Sicherheitsvorfällen',
    'DER.2.2': 'Vorsorge für die IT-Forensik',
    'DER.3.1': 'Audits und Revisionen',
    'DER.4': 'Notfallmanagement',
    'APP.1.1': 'Office Produkte',
    'APP.1.2': 'Webbrowser',
    'APP.1.4': 'Mobile Anwendungen',
    'APP.3.1': 'Webanwendungen und Webservices',
    'APP.3.3': 'Fileserver',
    'APP.5.2': 'Microsoft Exchange und Outlook',
    'APP.5.3': 'Allgemeiner Email Client und Server',
    'APP.6': 'Allgemeine Software',
    'SYS.1.1': 'Allgemeiner Server',
    'SYS.1.2.2': 'Windows Server 2012',
    'SYS.1.2.3': 'Windows Server',
    'SYS.1.5': 'Virtualisierung',
    'SYS.1.8': 'Speicherlösungen',
    'SYS.2.1': 'Allgemeiner Client',
    'SYS.2.2.3': 'Clients unter Windows',
    'SYS.3.1': 'Laptops',
    'SYS.3.2.1': 'Allgemeine Smartphones und Tablets',
    'SYS.3.2.2': 'Mobile Device Management',
    'SYS.3.2.3': 'iOS for Enterprise',
    'SYS.3.2.4': 'Android',
    'SYS.3.3': 'Mobiltelefon',
    'SYS.4.1': 'Drucker, Kopierer und Multifunktionsgeräte',
    'SYS.4.4': 'Allgemeines IoT-Gerät',
    'NET.1.1': 'Netzarchitektur und -design',
    'NET.1.2': 'Netzmanagement',
    'NET.2.1': 'WLAN Betrieb',
    'NET.3.1': 'Router und Switches',
    'NET.3.2': 'Firewall',
    'NET.3.3': 'VPN',
    'NET.4.1': 'TK-Anlagen',
    'NET.4.2': 'VoIP',
    'NET.4.3': 'Faxgeräte und Faxserver',
    'INF.1': 'Allgemeines Gebäude',
    'INF.2': 'Rechenzentrum und Serverraum',
    'INF.7': 'Büroarbeitsplatz',
    'INF.8': 'Häuslicher Arbeitsplatz',
    'INF.9': 'Mobiler Arbeitsplatz',
    'INF.12': 'Verkabelung'
}

reedereien_schiff_profil = {
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
    'OPS.1.1.2': 'Ordnungsgemäße IT Administration',
    'OPS.1.1.3': 'Patch und Änderungsmanagement',
    'OPS.1.1.4': 'Schutz vor Schadprogrammen',
    'OPS.1.1.5': 'Protokollierung',
    'OPS.1.1.6': 'Software, Tests und Freigaben',
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
    'APP.4.3': 'Relationale Datenbanksysteme',
    'APP.5.2': 'Microsoft Exchange und Outlook',
    'APP.5.3': 'Allgemeiner Email Client und Server',
    'APP.6': 'Allgemeine Software',
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
    'SYS.3.1': 'Laptops',
    'SYS.3.2.1': 'Allgemeine Smartphones und Tablets',
    'SYS.3.2.2': 'Mobile Device Management',
    'SYS.3.2.3': 'iOS for Enterprise',
    'SYS.3.2.4': 'Android',
    'SYS.3.3': 'Mobiltelefon',
    'SYS.4.1': 'Drucker, Kopierer und Multifunktionsgeräte',
    'SYS.4.4': 'Allgemeines IoT-Gerät',
    'SYS.4.5': 'Wechseldatenträger',
    'IND.1': 'Prozessleit- und Automatisierungstechnik',
    'IND.2.1': 'Allgemeine ICS Komponente',
    'IND.2.2': 'Speicherprogrammierbare Steuerung',
    'IND.2.3': 'Sensoren und Aktoren',
    'IND.2.4': 'Maschine',
    'IND.2.7': 'Safety Instrumented Systems',
    'NET.1.1': 'Netzarchitektur und -design',
    'NET.1.2': 'Netzmanagement',
    'NET.2.1': 'WLAN Betrieb',
    'NET.2.2': 'WLAN Nutzung',
    'NET.3.1': 'Router und Switches',
    'NET.3.2': 'Firewall',
    'NET.3.3': 'VPN',
    'NET.4.1': 'TK-Anlagen',
    'NET.4.2': 'VoIP',
    'NET.4.3': 'Faxgeräte und Faxserver',
    'INF.1': 'Allgemeines Gebäude',
    'INF.2': 'Rechenzentrum und Serverraum',
    'INF.5': 'Raum sowie Schrank für technische Infrastruktur',
    'INF.6': 'Datenträgerarchiv',
    'INF.7': 'Büroarbeitsplatz',
    'INF.9': 'Mobiler Arbeitsplatz',
    'INF.10': 'Besprechungs-, Veranstaltungs- und Schulungsräume',
    'INF.12': 'Verkabelung'
}

handwerkskammern_profil = {
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
    'OPS.1.1.2': 'Ordnungsgemäße IT Administration',
    'OPS.1.1.3': 'Patch und Änderungsmanagement',
    'OPS.1.1.4': 'Schutz vor Schadprogrammen',
    'OPS.1.1.5': 'Protokollierung',
    'OPS.1.1.6': 'Software, Tests und Freigaben',
    'OPS.1.2.2': 'Archivierung',
    'OPS.1.2.4': 'Telearbeit',
    'OPS.2.3': 'Nutzung von Outsourcing',
    'OPS.3.2': 'Anbieten von Outsourcing',
    'DER.1': 'Detektion von sicherheitsrelevanten Ereignissen',
    'DER.2.1': 'Behandlung von Sicherheitsvorfällen',
    'DER.2.2': 'Vorsorge für die IT-Forensik',
    'DER.2.3': 'Bereinigung weitreichender Sicherheitsvorfälle',
    'DER.3.1': 'Audits und Revisionen',
    'DER.4': 'Notfallmanagement',
    'APP.1.1': 'Office Produkte',
    'APP.1.2': 'Webbrowser',
    'APP.2.1': 'Allgemeiner Verzeichnisdienst',
    'APP.2.2': 'Active Directory Domain Services',
    'APP.3.1': 'Webanwendungen und Webservices',
    'APP.3.2': 'Webserver',
    'APP.3.3': 'Fileserver',
    'APP.3.4': 'Samba',
    'APP.3.6': 'DNS Server',
    'APP.4.3': 'Relationale Datenbanksysteme',
    'APP.5.2': 'Microsoft Exchange und Outlook',
    'APP.5.3': 'Allgemeiner Email Client und Server',
    'APP.6': 'Allgemeine Software',
    'SYS.1.1': 'Allgemeiner Server',
    'SYS.1.2.2': 'Windows Server 2012',
    'SYS.1.2.3': 'Windows Server',
    'SYS.1.3': 'Server unter Linux und Unix',
    'SYS.1.5': 'Virtualisierung',
    'SYS.1.8': 'Speicherlösungen',
    'SYS.2.1': 'Allgemeiner Client',
    'SYS.2.2.3': 'Clients unter Windows',
    'SYS.2.3': 'Clients unter Linux und Unix',
    'SYS.3.1': 'Laptops',
    'SYS.3.2.1': 'Allgemeine Smartphones und Tablets',
    'SYS.3.2.2': 'Mobile Device Management',
    'SYS.3.2.3': 'iOS for Enterprise',
    'SYS.3.2.4': 'Android',
    'SYS.3.3': 'Mobiltelefon',
    'SYS.4.1': 'Drucker, Kopierer und Multifunktionsgeräte',
    'SYS.4.4': 'Allgemeines IoT-Gerät',
    'SYS.4.5': 'Wechseldatenträger',
    'IND.1': 'Prozessleit- und Automatisierungstechnik',
    'IND.2.1': 'Allgemeine ICS Komponente',
    'IND.2.2': 'Speicherprogrammierbare Steuerung',
    'IND.2.3': 'Sensoren und Aktoren',
    'IND.2.4': 'Maschine',
    'NET.1.1': 'Netzarchitektur und -design',
    'NET.1.2': 'Netzmanagement',
    'NET.2.1': 'WLAN Betrieb',
    'NET.2.2': 'WLAN Nutzung',
    'NET.3.1': 'Router und Switches',
    'NET.3.2': 'Firewall',
    'NET.3.3': 'VPN',
    'INF.1': 'Allgemeines Gebäude',
    'INF.2': 'Rechenzentrum und Serverraum',
    'INF.7': 'Büroarbeitsplatz',
    'INF.8': 'Häuslicher Arbeitsplatz',
    'INF.9': 'Mobiler Arbeitsplatz',
    'INF.10': 'Besprechungs-, Veranstaltungs- und Schulungsräume',
    'INF.12': 'Verkabelung',
}

grosse_dienstleister_profil = {
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
    'OPS.1.1.2': 'Ordnungsgemäße IT Administration',
    'OPS.1.1.3': 'Patch und Änderungsmanagement',
    'OPS.1.1.4': 'Schutz vor Schadprogrammen',
    'OPS.2.3': 'Nutzung von Outsourcing',
    'OPS.3.2': 'Anbieten von Outsourcing',
    'DER.1': 'Detektion von sicherheitsrelevanten Ereignissen',
    'DER.2.1': 'Behandlung von Sicherheitsvorfällen',
    'DER.4': 'Notfallmanagement',
    'NET.1.1': 'Netzarchitektur und -design',
    'NET.1.2': 'Netzmanagement',
    'NET.3.1': 'Router und Switches',
    'NET.3.2': 'Firewall',
    'NET.3.3': 'VPN',
    'NET.3.4': 'Network Access Control',
    'NET.4.1': 'TK-Anlagen',
    'NET.4.2': 'VoIP',
    'NET.4.3': 'Faxgeräte und Faxserver',
    'INF.1': 'Allgemeines Gebäude',
    'INF.2': 'Rechenzentrum und Serverraum',
    'INF.7': 'Büroarbeitsplatz',
    'INF.12': 'Verkabelung'
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
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.39']
    },
    {
        'id': 'APP.1.1.A3',
        'cia': None,
        'gefahren': ['G 0.39']
    },
    {
        'id': 'APP.1.1.A6',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.46']
    },
    {
        'id': 'APP.1.1.A10',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'APP.1.1.A11',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'APP.1.1.A12',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'APP.1.1.A13',
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.39']
    },
    {
        'id': 'APP.1.1.A14',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.46']
    },
    {
        'id': 'APP.1.1.A15',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22', 'G 0.46']
    },
    {
        'id': 'APP.1.1.A16',
        'cia': 'I',
        'gefahren': ['G 0.22', 'G 0.46']
    },
    {
        'id': 'APP.1.1.A17',
        'cia': None,
        'gefahren': ['G 0.31']
    },
    {
        'id': 'APP.1.2.A1',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.28']
    },
    {
        'id': 'APP.1.2.A2',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.22', 'G 0.46']
    },
    {
        'id': 'APP.1.2.A3',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.30', 'G 0.46']
    },
    {
        'id': 'APP.1.2.A6',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'APP.1.2.A7',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19']
    },
    {
        'id': 'APP.1.2.A9',
        'cia': 'CI',
        'gefahren': ['G 0.23']
    },
    {
        'id': 'APP.1.2.A10',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.19']
    },
    {
        'id': 'APP.1.2.A11',
        'cia': 'C',
        'gefahren': ['G 0.28', 'G 0.39']
    },
    {
        'id': 'APP.1.2.A12',
        'cia': 'A',
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.1.2.A13',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.19', 'G 0.22']
    },
    {
        'id': 'APP.1.4.A1',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.14', 'G 0.15', 'G 0.16', 'G 0.17', 'G 0.18', 'G 0.19', 'G 0.25', 'G 0.26', 'G 0.38']
    },
    {
        'id': 'APP.1.4.A3',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.20', 'G 0.21', 'G 0.23', 'G 0.32', 'G 0.39']
    },
    {
        'id': 'APP.1.4.A5',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.21', 'G 0.32', 'G 0.38', 'G 0.39', 'G 0.42']
    },
    {
        'id': 'APP.1.4.A7',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.17', 'G 0.19']
    },
    {
        'id': 'APP.1.4.A8',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.38']
    },
    {
        'id': 'APP.1.4.A12',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.38']
    },
    {
        'id': 'APP.1.4.A14',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.17', 'G 0.18', 'G 0.19', 'G 0.23', 'G 0.32', 'G 0.36']
    },
    {
        'id': 'APP.1.4.A15',
        'cia': 'CIA',
        'gefahren': ['G 0.21', 'G 0.23', 'G 0.25', 'G 0.26', 'G 0.28']
    },
    {
        'id': 'APP.1.4.A16',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'APP.2.1.A1',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.2.1.A2',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'APP.2.1.A3',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30']
    },
    {
        'id': 'APP.2.1.A5',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.45']
    },
    {
        'id': 'APP.2.1.A6',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30']
    },
    {
        'id': 'APP.2.1.A8',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.45']
    },
    {
        'id': 'APP.2.1.A9',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.2.1.A11',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'APP.2.1.A12',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'APP.2.1.A13',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'APP.2.1.A14',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.27', 'G 0.45']
    },
    {
        'id': 'APP.2.1.A15',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30']
    },
    {
        'id': 'APP.2.1.A16',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'APP.2.1.A17',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.45']
    },
    {
        'id': 'APP.2.1.A18',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'APP.2.1.A19',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.30']
    },
    {
        'id': 'APP.2.1.A20',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.23']
    },
    {
        'id': 'APP.2.1.A21',
        'cia': 'A',
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.27', 'G 0.45']
    },
    {
        'id': 'APP.2.2.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30']
    },
    {
        'id': 'APP.2.2.A3',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30']
    },
    {
        'id': 'APP.2.2.A5',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.45']
    },
    {
        'id': 'APP.2.2.A6',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.38', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.2.2.A7',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.30', 'G 0.37']
    },
    {
        'id': 'APP.2.2.A8',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.43']
    },
    {
        'id': 'APP.2.2.A9',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.23', 'G 0.30', 'G 0.46']
    },
    {
        'id': 'APP.2.2.A12',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.28', 'G 0.30', 'G 0.45']
    },
    {
        'id': 'APP.2.2.A15',
        'cia': 'CIA',
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'APP.2.2.A16',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.30', 'G 0.32', 'G 0.38', 'G 0.45']
    },
    {
        'id': 'APP.2.2.A17',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'APP.2.2.A18',
        'cia': None,
        'gefahren': ['G 0.30', 'G 0.32']
    },
    {
        'id': 'APP.2.2.A19',
        'cia': 'A',
        'gefahren': ['G 0.18', 'G 0.23']
    },
    {
        'id': 'APP.2.2.A20',
        'cia': 'CI',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.2.2.A21',
        'cia': 'CI',
        'gefahren': ['G 0.19', 'G 0.32']
    },
    {
        'id': 'APP.2.2.A22',
        'cia': 'CI',
        'gefahren': ['G 0.18', 'G 0.32']
    },
    {
        'id': 'APP.2.2.A23',
        'cia': 'CI',
        'gefahren': ['G 0.18', 'G 0.32']
    },
    {
        'id': 'APP.2.3.A1',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.2.3.A3',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.30']
    },
    {
        'id': 'APP.2.3.A4',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18']
    },
    {
        'id': 'APP.2.3.A5',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30']
    },
    {
        'id': 'APP.2.3.A6',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.30']
    },
    {
        'id': 'APP.2.3.A8',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.2.3.A9',
        'cia': None,
        'gefahren': ['G 0.27', 'G 0.45']
    },
    {
        'id': 'APP.2.3.A10',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.45']
    },
    {
        'id': 'APP.2.3.A11',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18']
    },
    {
        'id': 'APP.3.1.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'APP.3.1.A4',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.23', 'G 0.30', 'G 0.43']
    },
    {
        'id': 'APP.3.1.A7',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'APP.3.1.A8',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.3.1.A9',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'APP.3.1.A11',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.23', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'APP.3.1.A12',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'APP.3.1.A14',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'APP.3.1.A20',
        'cia': 'CIA',
        'gefahren': ['G 0.23']
    },
    {
        'id': 'APP.3.1.A21',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.23']
    },
    {
        'id': 'APP.3.1.A22',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'APP.3.2.A1',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.46']
    },
    {
        'id': 'APP.3.2.A2',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.46']
    },
    {
        'id': 'APP.3.2.A3',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.39', 'G 0.40']
    },
    {
        'id': 'APP.3.2.A4',
        'cia': None,
        'gefahren': ['G 0.26', 'G 0.30']
    },
    {
        'id': 'APP.3.2.A5',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.22', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'APP.3.2.A7',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'APP.3.2.A8',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.31']
    },
    {
        'id': 'APP.3.2.A9',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.31']
    },
    {
        'id': 'APP.3.2.A10',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'APP.3.2.A11',
        'cia': None,
        'gefahren': ['G 0.15']
    },
    {
        'id': 'APP.3.2.A12',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'APP.3.2.A13',
        'cia': None,
        'gefahren': ['G 0.30']
    },
    {
        'id': 'APP.3.2.A14',
        'cia': None,
        'gefahren': ['G 0.39', 'G 0.46']
    },
    {
        'id': 'APP.3.2.A15',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.39']
    },
    {
        'id': 'APP.3.2.A16',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.23']
    },
    {
        'id': 'APP.3.2.A18',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.40']
    },
    {
        'id': 'APP.3.2.A20',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.27']
    },
    {
        'id': 'APP.3.3.A2',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.46']
    },
    {
        'id': 'APP.3.3.A3',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.39']
    },
    {
        'id': 'APP.3.3.A6',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.27']
    },
    {
        'id': 'APP.3.3.A7',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.27', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.3.3.A8',
        'cia': None,
        'gefahren': ['G 0.45']
    },
    {
        'id': 'APP.3.3.A9',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.27', 'G 0.45']
    },
    {
        'id': 'APP.3.3.A11',
        'cia': None,
        'gefahren': ['G 0.27']
    },
    {
        'id': 'APP.3.3.A12',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.39']
    },
    {
        'id': 'APP.3.3.A13',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.45']
    },
    {
        'id': 'APP.3.3.A14',
        'cia': None,
        'gefahren': ['G 0.26', 'G 0.46']
    },
    {
        'id': 'APP.3.3.A15',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.27']
    },
    {
        'id': 'APP.3.4.A1',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.3.4.A2',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.23', 'G 0.27', 'G 0.28', 'G 0.32']
    },
    {
        'id': 'APP.3.4.A3',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.27', 'G 0.30']
    },
    {
        'id': 'APP.3.4.A4',
        'cia': None,
        'gefahren': ['G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.3.4.A5',
        'cia': None,
        'gefahren': ['G 0.32', 'G 0.46']
    },
    {
        'id': 'APP.3.4.A6',
        'cia': None,
        'gefahren': ['G 0.32']
    },
    {
        'id': 'APP.3.4.A7',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.3.4.A8',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.32']
    },
    {
        'id': 'APP.3.4.A9',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'APP.3.4.A10',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.20', 'G 0.28']
    },
    {
        'id': 'APP.3.4.A12',
        'cia': None,
        'gefahren': ['G 0.31']
    },
    {
        'id': 'APP.3.4.A13',
        'cia': None,
        'gefahren': ['G 0.45']
    },
    {
        'id': 'APP.3.4.A15',
        'cia': 'CI',
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.46']
    },
    {
        'id': 'APP.3.6.A1',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.3.6.A2',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.40']
    },
    {
        'id': 'APP.3.6.A3',
        'cia': None,
        'gefahren': ['G 0.22']
    },
    {
        'id': 'APP.3.6.A4',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30', 'G 0.31', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'APP.3.6.A6',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.30']
    },
    {
        'id': 'APP.3.6.A7',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'APP.3.6.A8',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'APP.3.6.A9',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.40', 'G 0.45']
    },
    {
        'id': 'APP.3.6.A10',
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.29']
    },
    {
        'id': 'APP.3.6.A11',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.27', 'G 0.40']
    },
    {
        'id': 'APP.3.6.A13',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'APP.3.6.A14',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'APP.3.6.A15',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.25', 'G 0.27', 'G 0.30']
    },
    {
        'id': 'APP.3.6.A16',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30', 'G 0.43']
    },
    {
        'id': 'APP.3.6.A17',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.30', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'APP.3.6.A18',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.30', 'G 0.46']
    },
    {
        'id': 'APP.3.6.A19',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'APP.3.6.A20',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.27', 'G 0.40', 'G 0.45']
    },
    {
        'id': 'APP.3.6.A21',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'APP.3.6.A22',
        'cia': 'IA',
        'gefahren': ['G 0.9']
    },
    {
        'id': 'APP.4.2.A1',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.2.A2',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.2.A3',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.43']
    },
    {
        'id': 'APP.4.2.A4',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.2.A5',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.2.A6',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.2.A7',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.2.A8',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.2.A9',
        'cia': None,
        'gefahren': ['G 0.25']
    },
    {
        'id': 'APP.4.2.A11',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.2.A12',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.22', 'G 0.32', 'G 0.46']
    },
    {
        'id': 'APP.4.2.A13',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'APP.4.2.A14',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'APP.4.2.A15',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'APP.4.2.A16',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'APP.4.2.A17',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'APP.4.2.A18',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.23']
    },
    {
        'id': 'APP.4.2.A19',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'APP.4.2.A20',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'APP.4.2.A22',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.22', 'G 0.46']
    },
    {
        'id': 'APP.4.2.A23',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.22', 'G 0.46']
    },
    {
        'id': 'APP.4.2.A24',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'APP.4.2.A25',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'APP.4.2.A26',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.30', 'G 0.39', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.2.A27',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'APP.4.2.A28',
        'cia': None,
        'gefahren': ['G 0.25']
    },
    {
        'id': 'APP.4.2.A29',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.2.A30',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.2.A31',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'APP.4.2.A32',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.3.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'APP.4.3.A3',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.22', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'APP.4.3.A4',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.4.3.A9',
        'cia': None,
        'gefahren': ['G 0.27', 'G 0.45']
    },
    {
        'id': 'APP.4.3.A11',
        'cia': None,
        'gefahren': ['G 0.27']
    },
    {
        'id': 'APP.4.3.A12',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'APP.4.3.A13',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.22', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'APP.4.3.A16',
        'cia': None,
        'gefahren': ['G 0.15']
    },
    {
        'id': 'APP.4.3.A17',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.3.A18',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'APP.4.3.A19',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.3.A20',
        'cia': None,
        'gefahren': ['G 0.28', 'G 0.31']
    },
    {
        'id': 'APP.4.3.A21',
        'cia': 'CI',
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'APP.4.3.A22',
        'cia': 'CIA',
        'gefahren': ['G 0.27']
    },
    {
        'id': 'APP.4.3.A23',
        'cia': 'IA',
        'gefahren': ['G 0.18', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.3.A24',
        'cia': 'C',
        'gefahren': ['G 0.14', 'G 0.45']
    },
    {
        'id': 'APP.4.3.A25',
        'cia': 'CIA',
        'gefahren': ['G 0.23', 'G 0.31']
    },
    {
        'id': 'APP.4.4.A1',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.28', 'G 0.46']
    },
    {
        'id': 'APP.4.4.A2',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.20', 'G 0.21', 'G 0.23', 'G 0.25', 'G 0.27', 'G 0.28', 'G 0.30', 'G 0.37', 'G 0.39', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.4.A3',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.30', 'G 0.37', 'G 0.46']
    },
    {
        'id': 'APP.4.4.A4',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.28', 'G 0.39', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.4.A5',
        'cia': None,
        'gefahren': ['G 0.45']
    },
    {
        'id': 'APP.4.4.A6',
        'cia': None,
        'gefahren': ['G 0.25']
    },
    {
        'id': 'APP.4.4.A7',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.28', 'G 0.39', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.4.A8',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.28', 'G 0.39', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.4.A9',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.21', 'G 0.30']
    },
    {
        'id': 'APP.4.4.A10',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.25', 'G 0.30']
    },
    {
        'id': 'APP.4.4.A11',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.27']
    },
    {
        'id': 'APP.4.4.A12',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.28', 'G 0.39', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.4.A13',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.30', 'G 0.39', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.4.A14',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.28', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.4.A15',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.28', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.4.A16',
        'cia': 'CIA',
        'gefahren': ['G 0.25']
    },
    {
        'id': 'APP.4.4.A17',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.28', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.4.A18',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.28', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.4.A19',
        'cia': 'A',
        'gefahren': ['G 0.25']
    },
    {
        'id': 'APP.4.4.A20',
        'cia': 'C',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.28', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.4.A21',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.28', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'APP.4.6.A1',
        'cia': None,
        'gefahren': ['G 0.30']
    },
    {
        'id': 'APP.4.6.A2',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A3',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A4',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A5',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'APP.4.6.A6',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A7',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A8',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A9',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A10',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A11',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A12',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A13',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A14',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A15',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A16',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A17',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A18',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A19',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A20',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A21',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.4.6.A22',
        'cia': 'CIA',
        'gefahren': ['G 0.28']
    },
    {
        'id': 'APP.5.2.A1',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.5.2.A2',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.5.2.A3',
        'cia': None,
        'gefahren': ['G 0.30']
    },
    {
        'id': 'APP.5.2.A5',
        'cia': None,
        'gefahren': ['G 0.45']
    },
    {
        'id': 'APP.5.2.A7',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'APP.5.2.A9',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.25', 'G 0.27', 'G 0.46']
    },
    {
        'id': 'APP.5.2.A10',
        'cia': None,
        'gefahren': ['G 0.30', 'G 0.31']
    },
    {
        'id': 'APP.5.2.A11',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'APP.5.2.A12',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.36']
    },
    {
        'id': 'APP.5.2.A17',
        'cia': 'C',
        'gefahren': ['G 0.19']
    },
    {
        'id': 'APP.5.3.A1',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.30', 'G 0.39']
    },
    {
        'id': 'APP.5.3.A2',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.40']
    },
    {
        'id': 'APP.5.3.A3',
        'cia': None,
        'gefahren': ['G 0.45']
    },
    {
        'id': 'APP.5.3.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.39']
    },
    {
        'id': 'APP.5.3.A5',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.29', 'G 0.33']
    },
    {
        'id': 'APP.5.3.A6',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.5.3.A7',
        'cia': None,
        'gefahren': ['G 0.36', 'G 0.39', 'G 0.42']
    },
    {
        'id': 'APP.5.3.A8',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.39']
    },
    {
        'id': 'APP.5.3.A9',
        'cia': None,
        'gefahren': ['G 0.36', 'G 0.42']
    },
    {
        'id': 'APP.5.3.A10',
        'cia': 'C',
        'gefahren': ['G 0.19']
    },
    {
        'id': 'APP.5.3.A11',
        'cia': 'A',
        'gefahren': ['G 0.25']
    },
    {
        'id': 'APP.5.3.A12',
        'cia': 'A',
        'gefahren': ['G 0.25']
    },
    {
        'id': 'APP.5.3.A13',
        'cia': 'CIA',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.5.4.A1',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.5.4.A2',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.5.4.A3',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'APP.5.4.A4',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.23']
    },
    {
        'id': 'APP.5.4.A5',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'APP.5.4.A6',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.30']
    },
    {
        'id': 'APP.5.4.A7',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'APP.5.4.A8',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'APP.5.4.A9',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.18', 'G 0.19', 'G 0.30', 'G 0.39']
    },
    {
        'id': 'APP.5.4.A10',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'APP.5.4.A11',
        'cia': 'A',
        'gefahren': ['G 0.9', 'G 0.25', 'G 0.27']
    },
    {
        'id': 'APP.5.4.A12',
        'cia': 'A',
        'gefahren': ['G 0.18', 'G 0.25']
    },
    {
        'id': 'APP.5.4.A13',
        'cia': 'CIA',
        'gefahren': ['G 0.31', 'G 0.32']
    },
    {
        'id': 'APP.5.4.A14',
        'cia': 'CI',
        'gefahren': ['G 0.15']
    },
    {
        'id': 'APP.5.4.A15',
        'cia': 'C',
        'gefahren': ['G 0.19']
    },
    {
        'id': 'APP.5.4.A16',
        'cia': 'CIA',
        'gefahren': ['G 0.23']
    },
    {
        'id': 'APP.5.4.A17',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'APP.5.4.A18',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.25']
    },
    {
        'id': 'APP.6.A1',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.6.A2',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.29']
    },
    {
        'id': 'APP.6.A3',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.20', 'G 0.28']
    },
    {
        'id': 'APP.6.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.20', 'G 0.28', 'G 0.31']
    },
    {
        'id': 'APP.6.A5',
        'cia': None,
        'gefahren': ['G 0.31']
    },
    {
        'id': 'APP.6.A6',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.6.A7',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.6.A8',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.45']
    },
    {
        'id': 'APP.6.A9',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'APP.6.A10',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.6.A11',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'APP.6.A12',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25']
    },
    {
        'id': 'APP.6.A13',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.6.A14',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'APP.7.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'APP.7.A2',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.22', 'G 0.29']
    },
    {
        'id': 'APP.7.A3',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'APP.7.A4',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.7.A5',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'APP.7.A6',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'APP.7.A7',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.27']
    },
    {
        'id': 'APP.7.A8',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'APP.7.A9',
        'cia': 'A',
        'gefahren': ['G 0.45']
    },
    {
        'id': 'APP.7.A10',
        'cia': 'CIA',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'CON.1.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'CON.1.A2',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'CON.1.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.20', 'G 0.45']
    },
    {
        'id': 'CON.1.A5',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'CON.1.A9',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.20', 'G 0.26', 'G 0.28', 'G 0.29', 'G 0.31']
    },
    {
        'id': 'CON.1.A10',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'CON.1.A11',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.20', 'G 0.31']
    },
    {
        'id': 'CON.1.A15',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'CON.1.A16',
        'cia': 'CIA',
        'gefahren': ['G 0.21', 'G 0.22']
    },
    {
        'id': 'CON.1.A17',
        'cia': 'C',
        'gefahren': ['G 0.13']
    },
    {
        'id': 'CON.1.A18',
        'cia': 'A',
        'gefahren': ['G 0.19', 'G 0.25', 'G 0.27']
    },
    {
        'id': 'CON.1.A19',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'CON.1.A20',
        'cia': 'CIA',
        'gefahren': ['G 0.21']
    },
    {
        'id': 'CON.10.A1',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A2',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A3',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A4',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A5',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A6',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A7',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A8',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A9',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A10',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'CON.10.A11',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A12',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A13',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A14',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A15',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A16',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A17',
        'cia': 'CIA',
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.10.A18',
        'cia': 'CIA',
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.11.1.A1',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A2',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A3',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A5',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A6',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.24', 'G 0.29', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'CON.11.1.A7',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A8',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A9',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A10',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.22', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A11',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A12',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A13',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A14',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.19', 'G 0.21', 'G 0.24', 'G 0.29', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.41', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'CON.11.1.A15',
        'cia': None,
        'gefahren': ['G 0.16', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A16',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.23', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A17',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.19', 'G 0.23', 'G 0.29']
    },
    {
        'id': 'CON.11.1.A18',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.21', 'G 0.23', 'G 0.29']
    },
    {
        'id': 'CON.2.A1',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'CON.3.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'CON.3.A2',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.39']
    },
    {
        'id': 'CON.3.A4',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'CON.3.A5',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.45']
    },
    {
        'id': 'CON.3.A6',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'CON.3.A7',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'CON.3.A9',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'CON.3.A12',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.2', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'CON.3.A13',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.22', 'G 0.46']
    },
    {
        'id': 'CON.3.A14',
        'cia': None,
        'gefahren': ['G 0.16', 'G 0.19', 'G 0.22', 'G 0.45']
    },
    {
        'id': 'CON.3.A15',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'CON.6.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.2']
    },
    {
        'id': 'CON.6.A2',
        'cia': None,
        'gefahren': ['G 0.16', 'G 0.18', 'G 0.19']
    },
    {
        'id': 'CON.6.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'CON.6.A8',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'CON.6.A11',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'CON.6.A12',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'CON.6.A13',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'CON.6.A14',
        'cia': 'C',
        'gefahren': ['G 0.19']
    },
    {
        'id': 'CON.7.A1',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'CON.7.A2',
        'cia': None,
        'gefahren': ['G 0.17', 'G 0.18', 'G 0.29', 'G 0.31']
    },
    {
        'id': 'CON.7.A3',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'CON.7.A4',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19']
    },
    {
        'id': 'CON.7.A5',
        'cia': None,
        'gefahren': ['G 0.30']
    },
    {
        'id': 'CON.7.A6',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.30']
    },
    {
        'id': 'CON.7.A7',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'CON.7.A8',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.23']
    },
    {
        'id': 'CON.7.A9',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.39']
    },
    {
        'id': 'CON.7.A10',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.29']
    },
    {
        'id': 'CON.7.A11',
        'cia': None,
        'gefahren': ['G 0.16']
    },
    {
        'id': 'CON.7.A12',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.29', 'G 0.31']
    },
    {
        'id': 'CON.7.A13',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'CON.7.A14',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.46']
    },
    {
        'id': 'CON.7.A15',
        'cia': 'C',
        'gefahren': ['G 0.13']
    },
    {
        'id': 'CON.7.A16',
        'cia': 'I',
        'gefahren': ['G 0.45', 'G 0.46']
    },
    {
        'id': 'CON.7.A17',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'CON.7.A18',
        'cia': 'CI',
        'gefahren': ['G 0.30']
    },
    {
        'id': 'CON.8.A1',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'CON.8.A2',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'CON.8.A3',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.20']
    },
    {
        'id': 'CON.8.A5',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'CON.8.A6',
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.46']
    },
    {
        'id': 'CON.8.A7',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.8.A8',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.28', 'G 0.29']
    },
    {
        'id': 'CON.8.A10',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'CON.8.A11',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.31']
    },
    {
        'id': 'CON.8.A12',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.45']
    },
    {
        'id': 'CON.8.A14',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.8.A16',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'CON.8.A17',
        'cia': 'CI',
        'gefahren': ['G 0.28']
    },
    {
        'id': 'CON.8.A18',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'CON.8.A19',
        'cia': 'I',
        'gefahren': ['G 0.22', 'G 0.31', 'G 0.46']
    },
    {
        'id': 'CON.8.A20',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.28']
    },
    {
        'id': 'CON.8.A21',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'CON.8.A22',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'CON.9.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.29']
    },
    {
        'id': 'CON.9.A2',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'CON.9.A3',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.29']
    },
    {
        'id': 'CON.9.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'CON.9.A5',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'CON.9.A6',
        'cia': None,
        'gefahren': ['G 0.25']
    },
    {
        'id': 'CON.9.A7',
        'cia': None,
        'gefahren': ['G 0.45']
    },
    {
        'id': 'CON.9.A8',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.22']
    },
    {
        'id': 'CON.9.A9',
        'cia': 'C',
        'gefahren': ['G 0.19']
    },
    {
        'id': 'DER.1.A1',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'DER.1.A2',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.38']
    },
    {
        'id': 'DER.1.A3',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.33']
    },
    {
        'id': 'DER.1.A4',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.31']
    },
    {
        'id': 'DER.1.A5',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.39']
    },
    {
        'id': 'DER.1.A6',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.22', 'G 0.25', 'G 0.26', 'G 0.27', 'G 0.29']
    },
    {
        'id': 'DER.1.A7',
        'cia': None,
        'gefahren': ['G 0.27', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'DER.1.A9',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.39']
    },
    {
        'id': 'DER.1.A10',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.29', 'G 0.30', 'G 0.39']
    },
    {
        'id': 'DER.1.A11',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.39']
    },
    {
        'id': 'DER.1.A12',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'DER.1.A13',
        'cia': None,
        'gefahren': ['G 0.27', 'G 0.29', 'G 0.39']
    },
    {
        'id': 'DER.1.A14',
        'cia': 'CI',
        'gefahren': ['G 0.27', 'G 0.31', 'G 0.33']
    },
    {
        'id': 'DER.1.A15',
        'cia': 'CIA',
        'gefahren': ['G 0.29', 'G 0.37', 'G 0.39', 'G 0.46']
    },
    {
        'id': 'DER.1.A16',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.21', 'G 0.23', 'G 0.29', 'G 0.40', 'G 0.46']
    },
    {
        'id': 'DER.1.A17',
        'cia': 'CI',
        'gefahren': ['G 0.29']
    },
    {
        'id': 'DER.1.A18',
        'cia': 'CI',
        'gefahren': ['G 0.29', 'G 0.32', 'G 0.46']
    },
    {
        'id': 'DER.2.1.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.20', 'G 0.29']
    },
    {
        'id': 'DER.2.1.A2',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.29']
    },
    {
        'id': 'DER.2.1.A3',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.29', 'G 0.33']
    },
    {
        'id': 'DER.2.1.A4',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.20', 'G 0.29']
    },
    {
        'id': 'DER.2.1.A5',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.19', 'G 0.25', 'G 0.27', 'G 0.29']
    },
    {
        'id': 'DER.2.1.A6',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.19', 'G 0.25', 'G 0.29', 'G 0.30', 'G 0.32', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.1.A7',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.29']
    },
    {
        'id': 'DER.2.1.A8',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.29', 'G 0.33']
    },
    {
        'id': 'DER.2.1.A9',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.20', 'G 0.22', 'G 0.27', 'G 0.29', 'G 0.33']
    },
    {
        'id': 'DER.2.1.A10',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.29', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.1.A11',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.29']
    },
    {
        'id': 'DER.2.1.A12',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.27', 'G 0.46']
    },
    {
        'id': 'DER.2.1.A13',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.46']
    },
    {
        'id': 'DER.2.1.A14',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.20', 'G 0.22', 'G 0.29', 'G 0.46']
    },
    {
        'id': 'DER.2.1.A15',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.20', 'G 0.29']
    },
    {
        'id': 'DER.2.1.A16',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'DER.2.1.A17',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.20', 'G 0.22', 'G 0.29', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.1.A18',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.20', 'G 0.29', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.1.A19',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.27', 'G 0.33', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.1.A20',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.20', 'G 0.22', 'G 0.27', 'G 0.29', 'G 0.32', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.1.A21',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.20', 'G 0.27', 'G 0.29', 'G 0.32', 'G 0.33', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.1.A22',
        'cia': 'CIA',
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.19', 'G 0.20', 'G 0.22', 'G 0.25', 'G 0.27', 'G 0.29', 'G 0.33', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.2.A1',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'DER.2.2.A2',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'DER.2.2.A3',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'DER.2.2.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'DER.2.2.A5',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.31']
    },
    {
        'id': 'DER.2.2.A6',
        'cia': None,
        'gefahren': ['G 0.31']
    },
    {
        'id': 'DER.2.2.A7',
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.21', 'G 0.26']
    },
    {
        'id': 'DER.2.2.A8',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31', 'G 0.45']
    },
    {
        'id': 'DER.2.2.A9',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'DER.2.2.A10',
        'cia': None,
        'gefahren': ['G 0.17', 'G 0.22', 'G 0.31', 'G 0.37', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.2.A11',
        'cia': None,
        'gefahren': ['G 0.37']
    },
    {
        'id': 'DER.2.2.A12',
        'cia': None,
        'gefahren': ['G 0.17', 'G 0.18', 'G 0.30']
    },
    {
        'id': 'DER.2.2.A13',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'DER.2.2.A14',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'DER.2.2.A15',
        'cia': 'CIA',
        'gefahren': ['G 0.31']
    },
    {
        'id': 'DER.2.3.A1',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.40', 'G 0.41', 'G 0.42', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.3.A2',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.16', 'G 0.18', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.24', 'G 0.32', 'G 0.39', 'G 0.41', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.3.A3',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.22', 'G 0.23', 'G 0.32', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.3.A4',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.16', 'G 0.18', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.24', 'G 0.32', 'G 0.39', 'G 0.40', 'G 0.41', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.3.A5',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.18', 'G 0.23', 'G 0.28', 'G 0.32', 'G 0.41', 'G 0.42']
    },
    {
        'id': 'DER.2.3.A6',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.28', 'G 0.29', 'G 0.31']
    },
    {
        'id': 'DER.2.3.A7',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.16', 'G 0.18', 'G 0.20', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.24', 'G 0.28', 'G 0.32', 'G 0.39', 'G 0.40', 'G 0.41', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.3.A8',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.16', 'G 0.18', 'G 0.22', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'DER.2.3.A9',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.16', 'G 0.18', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.39', 'G 0.41', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'DER.2.3.A10',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.16', 'G 0.18', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.24', 'G 0.28', 'G 0.32', 'G 0.39', 'G 0.41', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'DER.3.1.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.46']
    },
    {
        'id': 'DER.3.1.A2',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'DER.3.1.A3',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.1.A4',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.1.A5',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.46']
    },
    {
        'id': 'DER.3.1.A6',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.1.A7',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.46']
    },
    {
        'id': 'DER.3.1.A8',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.46']
    },
    {
        'id': 'DER.3.1.A9',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.46']
    },
    {
        'id': 'DER.3.1.A10',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.1.A11',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'DER.3.1.A12',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'DER.3.1.A13',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.1.A14',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'DER.3.1.A15',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.1.A16',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.1.A17',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'DER.3.1.A18',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'DER.3.1.A19',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'DER.3.1.A20',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.1.A21',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.1.A22',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.46']
    },
    {
        'id': 'DER.3.1.A23',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.46']
    },
    {
        'id': 'DER.3.1.A24',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.29', 'G 0.46']
    },
    {
        'id': 'DER.3.1.A25',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'DER.3.1.A26',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.29', 'G 0.46']
    },
    {
        'id': 'DER.3.1.A27',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.46']
    },
    {
        'id': 'DER.3.2.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'DER.3.2.A2',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.2.A3',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.2.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'DER.3.2.A5',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'DER.3.2.A6',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.2.A7',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.2.A8',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.46']
    },
    {
        'id': 'DER.3.2.A9',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.2.A10',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.46']
    },
    {
        'id': 'DER.3.2.A11',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.2.A12',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.2.A13',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.2.A14',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'DER.3.2.A15',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.2.A16',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.2.A17',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.46']
    },
    {
        'id': 'DER.3.2.A18',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.2.A19',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'DER.3.2.A20',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.3.2.A21',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.46']
    },
    {
        'id': 'DER.3.2.A22',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.4.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.29']
    },
    {
        'id': 'DER.4.A2',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.4.A3',
        'cia': 'CIA',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.4.A4',
        'cia': 'CIA',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.4.A5',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'DER.4.A6',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'DER.4.A7',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'DER.4.A8',
        'cia': 'CIA',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.4.A9',
        'cia': 'CIA',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.4.A10',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'DER.4.A12',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'DER.4.A13',
        'cia': 'CIA',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.4.A14',
        'cia': 'CIA',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.4.A15',
        'cia': 'CIA',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'DER.4.A16',
        'cia': 'CIA',
        'gefahren': ['G 0.11', 'G 0.18']
    },
    {
        'id': 'IND.1.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.20', 'G 0.29', 'G 0.30']
    },
    {
        'id': 'IND.1.A3',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.39', 'G 0.41']
    },
    {
        'id': 'IND.1.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.21', 'G 0.23', 'G 0.29', 'G 0.32']
    },
    {
        'id': 'IND.1.A5',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23']
    },
    {
        'id': 'IND.1.A6',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'IND.1.A7',
        'cia': None,
        'gefahren': ['G 0.30', 'G 0.32', 'G 0.37']
    },
    {
        'id': 'IND.1.A8',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'IND.1.A9',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.29']
    },
    {
        'id': 'IND.1.A10',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.32', 'G 0.37', 'G 0.39', 'G 0.41']
    },
    {
        'id': 'IND.1.A11',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.20', 'G 0.28']
    },
    {
        'id': 'IND.1.A12',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.28']
    },
    {
        'id': 'IND.1.A13',
        'cia': 'A',
        'gefahren': ['G 0.5', 'G 0.11', 'G 0.25', 'G 0.41']
    },
    {
        'id': 'IND.1.A14',
        'cia': 'CIA',
        'gefahren': ['G 0.30', 'G 0.32', 'G 0.36', 'G 0.37']
    },
    {
        'id': 'IND.1.A15',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.32', 'G 0.37']
    },
    {
        'id': 'IND.1.A16',
        'cia': 'IA',
        'gefahren': ['G 0.23', 'G 0.41']
    },
    {
        'id': 'IND.1.A17',
        'cia': 'I',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'IND.1.A18',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.30', 'G 0.37']
    },
    {
        'id': 'IND.1.A19',
        'cia': None,
        'gefahren': ['G 0.17', 'G 0.45']
    },
    {
        'id': 'IND.1.A20',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'IND.1.A21',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'IND.1.A22',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.21', 'G 0.22', 'G 0.30', 'G 0.37']
    },
    {
        'id': 'IND.1.A23',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'IND.1.A24',
        'cia': 'A',
        'gefahren': ['G 0.9', 'G 0.25', 'G 0.27']
    },
    {
        'id': 'IND.2.1.A1',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.30', 'G 0.32', 'G 0.41', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'IND.2.1.A2',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.39', 'G 0.41', 'G 0.46']
    },
    {
        'id': 'IND.2.1.A4',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.41']
    },
    {
        'id': 'IND.2.1.A6',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.40', 'G 0.41']
    },
    {
        'id': 'IND.2.1.A7',
        'cia': None,
        'gefahren': ['G 0.2', 'G 0.4', 'G 0.8', 'G 0.9', 'G 0.10', 'G 0.12', 'G 0.25', 'G 0.39', 'G 0.40', 'G 0.41', 'G 0.45']
    },
    {
        'id': 'IND.2.1.A8',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.30', 'G 0.39']
    },
    {
        'id': 'IND.2.1.A11',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.41']
    },
    {
        'id': 'IND.2.1.A13',
        'cia': None,
        'gefahren': ['G 0.12', 'G 0.14', 'G 0.15', 'G 0.21', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.39', 'G 0.41']
    },
    {
        'id': 'IND.2.1.A16',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.39', 'G 0.41', 'G 0.45']
    },
    {
        'id': 'IND.2.1.A17',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.30', 'G 0.37', 'G 0.39', 'G 0.41', 'G 0.46']
    },
    {
        'id': 'IND.2.1.A18',
        'cia': 'A',
        'gefahren': ['G 0.9', 'G 0.45']
    },
    {
        'id': 'IND.2.1.A19',
        'cia': 'CIA',
        'gefahren': ['G 0.8', 'G 0.9', 'G 0.14', 'G 0.21', 'G 0.23', 'G 0.28', 'G 0.30', 'G 0.39', 'G 0.40', 'G 0.41', 'G 0.46']
    },
    {
        'id': 'IND.2.1.A20',
        'cia': 'IA',
        'gefahren': ['G 0.14', 'G 0.21', 'G 0.23', 'G 0.28', 'G 0.39']
    },
    {
        'id': 'IND.2.2.A1',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.23', 'G 0.41']
    },
    {
        'id': 'IND.2.2.A3',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.22']
    },
    {
        'id': 'IND.2.3.A1',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.30']
    },
    {
        'id': 'IND.2.3.A2',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.21', 'G 0.28', 'G 0.30']
    },
    {
        'id': 'IND.2.3.A3',
        'cia': 'I',
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.21', 'G 0.23', 'G 0.28', 'G 0.30']
    },
    {
        'id': 'IND.2.4.A1',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.14', 'G 0.18', 'G 0.21', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'IND.2.4.A2',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.39']
    },
    {
        'id': 'IND.2.7.A1',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.30', 'G 0.41', 'G 0.42', 'G 0.46']
    },
    {
        'id': 'IND.2.7.A2',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.30', 'G 0.41', 'G 0.42', 'G 0.46']
    },
    {
        'id': 'IND.2.7.A3',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.41', 'G 0.42', 'G 0.46']
    },
    {
        'id': 'IND.2.7.A4',
        'cia': None,
        'gefahren': ['G 0.5', 'G 0.6', 'G 0.9', 'G 0.11', 'G 0.14', 'G 0.15', 'G 0.19', 'G 0.20', 'G 0.21', 'G 0.23', 'G 0.28', 'G 0.29', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.39', 'G 0.41', 'G 0.42']
    },
    {
        'id': 'IND.2.7.A5',
        'cia': None,
        'gefahren': ['G 0.5', 'G 0.6', 'G 0.9', 'G 0.11', 'G 0.14', 'G 0.41']
    },
    {
        'id': 'IND.2.7.A6',
        'cia': None,
        'gefahren': ['G 0.5', 'G 0.6', 'G 0.9', 'G 0.11', 'G 0.14', 'G 0.15', 'G 0.18', 'G 0.19', 'G 0.20', 'G 0.21', 'G 0.23', 'G 0.41']
    },
    {
        'id': 'IND.2.7.A7',
        'cia': None,
        'gefahren': ['G 0.6', 'G 0.9', 'G 0.14', 'G 0.15', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.41', 'G 0.42', 'G 0.46']
    },
    {
        'id': 'IND.2.7.A8',
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.21', 'G 0.23', 'G 0.41', 'G 0.46']
    },
    {
        'id': 'IND.2.7.A9',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.14', 'G 0.15', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.41', 'G 0.46']
    },
    {
        'id': 'IND.2.7.A10',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.41', 'G 0.42']
    },
    {
        'id': 'IND.2.7.A11',
        'cia': None,
        'gefahren': ['G 0.6', 'G 0.14', 'G 0.15', 'G 0.19', 'G 0.20', 'G 0.21', 'G 0.23', 'G 0.41', 'G 0.42', 'G 0.46']
    },
    {
        'id': 'IND.2.7.A12',
        'cia': 'I',
        'gefahren': ['G 0.20', 'G 0.21', 'G 0.23', 'G 0.28', 'G 0.41']
    },
    {
        'id': 'IND.3.2.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'IND.3.2.A2',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'IND.3.2.A3',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.30', 'G 0.40']
    },
    {
        'id': 'IND.3.2.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.31', 'G 0.32']
    },
    {
        'id': 'IND.3.2.A5',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.40']
    },
    {
        'id': 'IND.3.2.A6',
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'IND.3.2.A7',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.37']
    },
    {
        'id': 'IND.3.2.A8',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'IND.3.2.A9',
        'cia': None,
        'gefahren': ['G 0.37', 'G 0.39', 'G 0.43']
    },
    {
        'id': 'IND.3.2.A10',
        'cia': None,
        'gefahren': ['G 0.24', 'G 0.25', 'G 0.31', 'G 0.32', 'G 0.33', 'G 0.37', 'G 0.41']
    },
    {
        'id': 'IND.3.2.A11',
        'cia': None,
        'gefahren': ['G 0.30']
    },
    {
        'id': 'IND.3.2.A12',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.27', 'G 0.30']
    },
    {
        'id': 'IND.3.2.A13',
        'cia': 'CI',
        'gefahren': ['G 0.37']
    },
    {
        'id': 'IND.3.2.A14',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.31', 'G 0.32', 'G 0.37']
    },
    {
        'id': 'INF.1.A1',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.18', 'G 0.44']
    },
    {
        'id': 'INF.1.A2',
        'cia': None,
        'gefahren': ['G 0.8']
    },
    {
        'id': 'INF.1.A3',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'INF.1.A4',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.18']
    },
    {
        'id': 'INF.1.A5',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'INF.1.A6',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.44']
    },
    {
        'id': 'INF.1.A7',
        'cia': None,
        'gefahren': ['G 0.44']
    },
    {
        'id': 'INF.1.A8',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.4', 'G 0.18', 'G 0.44']
    },
    {
        'id': 'INF.1.A9',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.1.A10',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'INF.1.A12',
        'cia': None,
        'gefahren': ['G 0.16', 'G 0.18', 'G 0.44']
    },
    {
        'id': 'INF.1.A13',
        'cia': None,
        'gefahren': ['G 0.27', 'G 0.44']
    },
    {
        'id': 'INF.1.A14',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'INF.1.A15',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.27']
    },
    {
        'id': 'INF.1.A16',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.34']
    },
    {
        'id': 'INF.1.A17',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.18']
    },
    {
        'id': 'INF.1.A18',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.18']
    },
    {
        'id': 'INF.1.A19',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.18']
    },
    {
        'id': 'INF.1.A20',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.18']
    },
    {
        'id': 'INF.1.A22',
        'cia': 'CIA',
        'gefahren': ['G 0.1', 'G 0.18', 'G 0.34', 'G 0.44']
    },
    {
        'id': 'INF.1.A23',
        'cia': 'C',
        'gefahren': ['G 0.18', 'G 0.34', 'G 0.44']
    },
    {
        'id': 'INF.1.A24',
        'cia': 'A',
        'gefahren': ['G 0.3', 'G 0.5', 'G 0.18']
    },
    {
        'id': 'INF.1.A25',
        'cia': 'A',
        'gefahren': ['G 0.5', 'G 0.6', 'G 0.7', 'G 0.18']
    },
    {
        'id': 'INF.1.A26',
        'cia': 'CIA',
        'gefahren': ['G 0.16', 'G 0.18', 'G 0.34', 'G 0.44']
    },
    {
        'id': 'INF.1.A27',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.44']
    },
    {
        'id': 'INF.1.A30',
        'cia': 'CIA',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.1.A31',
        'cia': 'C',
        'gefahren': ['G 0.16', 'G 0.18']
    },
    {
        'id': 'INF.1.A32',
        'cia': 'A',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.1.A34',
        'cia': 'A',
        'gefahren': ['G 0.1', 'G 0.3', 'G 0.18', 'G 0.44']
    },
    {
        'id': 'INF.1.A35',
        'cia': 'CA',
        'gefahren': ['G 0.7', 'G 0.34', 'G 0.44']
    },
    {
        'id': 'INF.1.A36',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.18']
    },
    {
        'id': 'INF.10.A1',
        'cia': None,
        'gefahren': ['G 0.16', 'G 0.18']
    },
    {
        'id': 'INF.10.A3',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.44']
    },
    {
        'id': 'INF.10.A4',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.18', 'G 0.19', 'G 0.44']
    },
    {
        'id': 'INF.10.A5',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.10.A6',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.23', 'G 0.41']
    },
    {
        'id': 'INF.10.A7',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.23', 'G 0.41']
    },
    {
        'id': 'INF.10.A8',
        'cia': None,
        'gefahren': ['G 0.37']
    },
    {
        'id': 'INF.10.A9',
        'cia': 'IA',
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.22', 'G 0.46']
    },
    {
        'id': 'INF.11.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'INF.11.A2',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.25']
    },
    {
        'id': 'INF.11.A3',
        'cia': None,
        'gefahren': ['G 0.2', 'G 0.18', 'G 0.19', 'G 0.25']
    },
    {
        'id': 'INF.11.A4',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.11.A5',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.11.A6',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.11.A7',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'INF.11.A8',
        'cia': None,
        'gefahren': ['G 0.2']
    },
    {
        'id': 'INF.11.A9',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.11.A10',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.29']
    },
    {
        'id': 'INF.11.A11',
        'cia': 'A',
        'gefahren': ['G 0.27']
    },
    {
        'id': 'INF.11.A12',
        'cia': 'CA',
        'gefahren': ['G 0.16']
    },
    {
        'id': 'INF.11.A13',
        'cia': 'A',
        'gefahren': ['G 0.24']
    },
    {
        'id': 'INF.11.A14',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.22']
    },
    {
        'id': 'INF.11.A15',
        'cia': 'CIA',
        'gefahren': ['G 0.2', 'G 0.15', 'G 0.30']
    },
    {
        'id': 'INF.11.A16',
        'cia': 'A',
        'gefahren': ['G 0.1']
    },
    {
        'id': 'INF.11.A17',
        'cia': 'C',
        'gefahren': ['G 0.19']
    },
    {
        'id': 'INF.12.A1',
        'cia': None,
        'gefahren': ['G 0.2', 'G 0.18', 'G 0.25', 'G 0.26', 'G 0.29']
    },
    {
        'id': 'INF.12.A2',
        'cia': None,
        'gefahren': ['G 0.12', 'G 0.18', 'G 0.27', 'G 0.29']
    },
    {
        'id': 'INF.12.A3',
        'cia': None,
        'gefahren': ['G 0.8', 'G 0.9', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'INF.12.A4',
        'cia': None,
        'gefahren': ['G 0.8', 'G 0.12']
    },
    {
        'id': 'INF.12.A5',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'INF.12.A6',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.37', 'G 0.41']
    },
    {
        'id': 'INF.12.A7',
        'cia': None,
        'gefahren': ['G 0.8', 'G 0.12', 'G 0.18']
    },
    {
        'id': 'INF.12.A8',
        'cia': None,
        'gefahren': ['G 0.8', 'G 0.18']
    },
    {
        'id': 'INF.12.A9',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.27']
    },
    {
        'id': 'INF.12.A10',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.12.A11',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.19']
    },
    {
        'id': 'INF.12.A12',
        'cia': None,
        'gefahren': ['G 0.8', 'G 0.9', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'INF.12.A13',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.8', 'G 0.12']
    },
    {
        'id': 'INF.12.A14',
        'cia': 'A',
        'gefahren': ['G 0.8', 'G 0.12']
    },
    {
        'id': 'INF.12.A15',
        'cia': 'IA',
        'gefahren': ['G 0.15', 'G 0.41']
    },
    {
        'id': 'INF.12.A16',
        'cia': 'IA',
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'INF.12.A17',
        'cia': 'A',
        'gefahren': ['G 0.9', 'G 0.18', 'G 0.27', 'G 0.41']
    },
    {
        'id': 'INF.13.A1',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.13.A2',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'INF.13.A3',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'INF.13.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'INF.13.A5',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.13.A6',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.10', 'G 0.18', 'G 0.19', 'G 0.25', 'G 0.33']
    },
    {
        'id': 'INF.13.A7',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.25', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'INF.13.A8',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.13.A9',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'INF.13.A10',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.13.A11',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.24', 'G 0.25', 'G 0.28', 'G 0.39', 'G 0.41', 'G 0.43', 'G 0.47']
    },
    {
        'id': 'INF.13.A12',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.24', 'G 0.25', 'G 0.26', 'G 0.28', 'G 0.39', 'G 0.41', 'G 0.43', 'G 0.47']
    },
    {
        'id': 'INF.13.A13',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.24', 'G 0.25', 'G 0.28', 'G 0.39', 'G 0.41', 'G 0.43', 'G 0.47']
    },
    {
        'id': 'INF.13.A14',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'INF.13.A15',
        'cia': None,
        'gefahren': ['G 0.39']
    },
    {
        'id': 'INF.13.A16',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.13.A17',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.10', 'G 0.18', 'G 0.24', 'G 0.25', 'G 0.30', 'G 0.32', 'G 0.44']
    },
    {
        'id': 'INF.13.A18',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.10', 'G 0.18', 'G 0.25', 'G 0.27']
    },
    {
        'id': 'INF.13.A19',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'INF.13.A20',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.13.A21',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.37']
    },
    {
        'id': 'INF.13.A22',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.10', 'G 0.18', 'G 0.25', 'G 0.26', 'G 0.27', 'G 0.28']
    },
    {
        'id': 'INF.13.A23',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'INF.13.A24',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'INF.13.A25',
        'cia': 'CIA',
        'gefahren': ['G 0.9', 'G 0.10', 'G 0.18', 'G 0.25', 'G 0.26', 'G 0.27', 'G 0.28']
    },
    {
        'id': 'INF.13.A26',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.26', 'G 0.32', 'G 0.41', 'G 0.43']
    },
    {
        'id': 'INF.13.A27',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.29']
    },
    {
        'id': 'INF.13.A28',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.29']
    },
    {
        'id': 'INF.13.A29',
        'cia': 'CIA',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.13.A30',
        'cia': 'CIA',
        'gefahren': ['G 0.28']
    },
    {
        'id': 'INF.14.A1',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.14.A2',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.14.A3',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.10', 'G 0.14', 'G 0.15', 'G 0.18', 'G 0.19', 'G 0.22', 'G 0.25', 'G 0.26', 'G 0.46']
    },
    {
        'id': 'INF.14.A4',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.18', 'G 0.19', 'G 0.25', 'G 0.26', 'G 0.29', 'G 0.40', 'G 0.43']
    },
    {
        'id': 'INF.14.A5',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'INF.14.A6',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.19', 'G 0.23', 'G 0.40', 'G 0.43']
    },
    {
        'id': 'INF.14.A7',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.14.A8',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23']
    },
    {
        'id': 'INF.14.A9',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.14.A10',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.10', 'G 0.18', 'G 0.25', 'G 0.26', 'G 0.40']
    },
    {
        'id': 'INF.14.A11',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.40', 'G 0.43']
    },
    {
        'id': 'INF.14.A12',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'INF.14.A13',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.19', 'G 0.23', 'G 0.40', 'G 0.43']
    },
    {
        'id': 'INF.14.A14',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'INF.14.A15',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'INF.14.A16',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'INF.14.A17',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'INF.14.A18',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'INF.14.A19',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'INF.14.A20',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.15', 'G 0.19', 'G 0.40']
    },
    {
        'id': 'INF.14.A21',
        'cia': None,
        'gefahren': ['G 0.20']
    },
    {
        'id': 'INF.14.A22',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'INF.14.A23',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26']
    },
    {
        'id': 'INF.14.A24',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.46']
    },
    {
        'id': 'INF.14.A25',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'INF.14.A26',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.37']
    },
    {
        'id': 'INF.14.A27',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.29']
    },
    {
        'id': 'INF.14.A28',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'INF.14.A29',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'INF.14.A30',
        'cia': 'IA',
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.46']
    },
    {
        'id': 'INF.2.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'INF.2.A2',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.24', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'INF.2.A3',
        'cia': None,
        'gefahren': ['G 0.8']
    },
    {
        'id': 'INF.2.A4',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.8', 'G 0.24', 'G 0.26']
    },
    {
        'id': 'INF.2.A5',
        'cia': None,
        'gefahren': ['G 0.2']
    },
    {
        'id': 'INF.2.A6',
        'cia': None,
        'gefahren': ['G 0.44']
    },
    {
        'id': 'INF.2.A7',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.44']
    },
    {
        'id': 'INF.2.A8',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.18']
    },
    {
        'id': 'INF.2.A9',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.24', 'G 0.25']
    },
    {
        'id': 'INF.2.A10',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.18', 'G 0.25', 'G 0.29']
    },
    {
        'id': 'INF.2.A11',
        'cia': None,
        'gefahren': ['G 0.10', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'INF.2.A12',
        'cia': None,
        'gefahren': ['G 0.7', 'G 0.34', 'G 0.44']
    },
    {
        'id': 'INF.2.A13',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.3', 'G 0.18', 'G 0.44']
    },
    {
        'id': 'INF.2.A14',
        'cia': None,
        'gefahren': ['G 0.8', 'G 0.18']
    },
    {
        'id': 'INF.2.A15',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.18', 'G 0.25']
    },
    {
        'id': 'INF.2.A16',
        'cia': None,
        'gefahren': ['G 0.2', 'G 0.25']
    },
    {
        'id': 'INF.2.A17',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.8', 'G 0.24']
    },
    {
        'id': 'INF.2.A19',
        'cia': None,
        'gefahren': ['G 0.8', 'G 0.18', 'G 0.26', 'G 0.29']
    },
    {
        'id': 'INF.2.A21',
        'cia': 'A',
        'gefahren': ['G 0.8', 'G 0.9', 'G 0.10', 'G 0.27']
    },
    {
        'id': 'INF.2.A22',
        'cia': 'IA',
        'gefahren': ['G 0.2']
    },
    {
        'id': 'INF.2.A23',
        'cia': 'A',
        'gefahren': ['G 0.8', 'G 0.10', 'G 0.26']
    },
    {
        'id': 'INF.2.A24',
        'cia': 'IA',
        'gefahren': ['G 0.29', 'G 0.30', 'G 0.37']
    },
    {
        'id': 'INF.2.A25',
        'cia': 'A',
        'gefahren': ['G 0.8', 'G 0.27']
    },
    {
        'id': 'INF.2.A26',
        'cia': 'A',
        'gefahren': ['G 0.8', 'G 0.27']
    },
    {
        'id': 'INF.2.A28',
        'cia': 'IA',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.2.A29',
        'cia': None,
        'gefahren': ['G 0.3', 'G 0.18', 'G 0.24', 'G 0.25']
    },
    {
        'id': 'INF.2.A30',
        'cia': None,
        'gefahren': ['G 0.1']
    },
    {
        'id': 'INF.5.A1',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.5.A2',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.5.A3',
        'cia': None,
        'gefahren': ['G 0.44']
    },
    {
        'id': 'INF.5.A4',
        'cia': None,
        'gefahren': ['G 0.44']
    },
    {
        'id': 'INF.5.A5',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26']
    },
    {
        'id': 'INF.5.A6',
        'cia': None,
        'gefahren': ['G 0.1']
    },
    {
        'id': 'INF.5.A7',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.5.A8',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26']
    },
    {
        'id': 'INF.5.A9',
        'cia': None,
        'gefahren': ['G 0.8']
    },
    {
        'id': 'INF.5.A10',
        'cia': None,
        'gefahren': ['G 0.2', 'G 0.18']
    },
    {
        'id': 'INF.5.A11',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.3', 'G 0.4']
    },
    {
        'id': 'INF.5.A12',
        'cia': None,
        'gefahren': ['G 0.3', 'G 0.4', 'G 0.8', 'G 0.10', 'G 0.18']
    },
    {
        'id': 'INF.5.A13',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.4', 'G 0.29']
    },
    {
        'id': 'INF.5.A14',
        'cia': None,
        'gefahren': ['G 0.1']
    },
    {
        'id': 'INF.5.A15',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.24', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'INF.5.A16',
        'cia': None,
        'gefahren': ['G 0.8', 'G 0.10', 'G 0.18']
    },
    {
        'id': 'INF.5.A17',
        'cia': None,
        'gefahren': ['G 0.5', 'G 0.8', 'G 0.10', 'G 0.18', 'G 0.24', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'INF.5.A18',
        'cia': 'CA',
        'gefahren': ['G 0.1', 'G 0.2', 'G 0.3', 'G 0.4', 'G 0.5', 'G 0.18']
    },
    {
        'id': 'INF.5.A19',
        'cia': 'A',
        'gefahren': ['G 0.8', 'G 0.10', 'G 0.27']
    },
    {
        'id': 'INF.5.A20',
        'cia': 'CIA',
        'gefahren': ['G 0.41', 'G 0.44']
    },
    {
        'id': 'INF.5.A22',
        'cia': 'A',
        'gefahren': ['G 0.8', 'G 0.10']
    },
    {
        'id': 'INF.5.A23',
        'cia': 'A',
        'gefahren': ['G 0.8', 'G 0.24', 'G 0.25', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'INF.5.A24',
        'cia': 'A',
        'gefahren': ['G 0.2', 'G 0.25', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'INF.5.A25',
        'cia': 'A',
        'gefahren': ['G 0.1', 'G 0.4', 'G 0.8', 'G 0.10']
    },
    {
        'id': 'INF.5.A26',
        'cia': 'A',
        'gefahren': ['G 0.8', 'G 0.10', 'G 0.18', 'G 0.24', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'INF.6.A1',
        'cia': None,
        'gefahren': ['G 0.1']
    },
    {
        'id': 'INF.6.A2',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.44']
    },
    {
        'id': 'INF.6.A3',
        'cia': None,
        'gefahren': ['G 0.4', 'G 0.18']
    },
    {
        'id': 'INF.6.A4',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.4', 'G 0.44']
    },
    {
        'id': 'INF.6.A5',
        'cia': None,
        'gefahren': ['G 0.3', 'G 0.16']
    },
    {
        'id': 'INF.6.A6',
        'cia': None,
        'gefahren': ['G 0.3', 'G 0.18']
    },
    {
        'id': 'INF.6.A7',
        'cia': None,
        'gefahren': ['G 0.2', 'G 0.18']
    },
    {
        'id': 'INF.6.A8',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.3', 'G 0.44']
    },
    {
        'id': 'INF.6.A9',
        'cia': 'CIA',
        'gefahren': ['G 0.1', 'G 0.3', 'G 0.18', 'G 0.44']
    },
    {
        'id': 'INF.7.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.44']
    },
    {
        'id': 'INF.7.A2',
        'cia': None,
        'gefahren': ['G 0.1', 'G 0.14', 'G 0.16', 'G 0.18', 'G 0.30', 'G 0.44']
    },
    {
        'id': 'INF.7.A3',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.7.A5',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.29', 'G 0.33']
    },
    {
        'id': 'INF.7.A6',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.18', 'G 0.19']
    },
    {
        'id': 'INF.7.A7',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.30']
    },
    {
        'id': 'INF.7.A8',
        'cia': 'CIA',
        'gefahren': ['G 0.16']
    },
    {
        'id': 'INF.8.A1',
        'cia': None,
        'gefahren': ['G 0.16', 'G 0.19', 'G 0.30']
    },
    {
        'id': 'INF.8.A2',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.17', 'G 0.18', 'G 0.19', 'G 0.22']
    },
    {
        'id': 'INF.8.A3',
        'cia': None,
        'gefahren': ['G 0.16', 'G 0.18', 'G 0.19', 'G 0.30', 'G 0.44']
    },
    {
        'id': 'INF.8.A4',
        'cia': None,
        'gefahren': ['G 0.16', 'G 0.19', 'G 0.33', 'G 0.44']
    },
    {
        'id': 'INF.8.A5',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19']
    },
    {
        'id': 'INF.8.A6',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.18', 'G 0.19', 'G 0.22', 'G 0.44']
    },
    {
        'id': 'INF.9.A1',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'INF.9.A2',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.37']
    },
    {
        'id': 'INF.9.A3',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.30', 'G 0.44', 'G 0.46']
    },
    {
        'id': 'INF.9.A4',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.31']
    },
    {
        'id': 'INF.9.A5',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19']
    },
    {
        'id': 'INF.9.A6',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19']
    },
    {
        'id': 'INF.9.A7',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'INF.9.A8',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'INF.9.A9',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.19', 'G 0.22']
    },
    {
        'id': 'INF.9.A10',
        'cia': 'CIA',
        'gefahren': ['G 0.16', 'G 0.18']
    },
    {
        'id': 'INF.9.A11',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'INF.9.A12',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19']
    },
    {
        'id': 'ISMS.1.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'ISMS.1.A2',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'ISMS.1.A3',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'ISMS.1.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'ISMS.1.A5',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'ISMS.1.A6',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'ISMS.1.A7',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'ISMS.1.A8',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'ISMS.1.A9',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'ISMS.1.A10',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'ISMS.1.A11',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'ISMS.1.A12',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'ISMS.1.A13',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'ISMS.1.A15',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'ISMS.1.A16',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'ISMS.1.A17',
        'cia': 'A',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.1.1.A1',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'NET.1.1.A2',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'NET.1.1.A3',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'NET.1.1.A4',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.1.A5',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.1.A6',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.1.A7',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'NET.1.1.A8',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'NET.1.1.A9',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.46']
    },
    {
        'id': 'NET.1.1.A10',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.1.A11',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.29', 'G 0.30', 'G 0.40', 'G 0.43']
    },
    {
        'id': 'NET.1.1.A12',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'NET.1.1.A13',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.1.1.A14',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.11', 'G 0.18', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.27', 'G 0.29', 'G 0.30', 'G 0.40']
    },
    {
        'id': 'NET.1.1.A15',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'NET.1.1.A16',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'NET.1.1.A17',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'NET.1.1.A18',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.1.A19',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.1.A20',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'NET.1.1.A21',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.22', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'NET.1.1.A22',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.1.A23',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30', 'G 0.40']
    },
    {
        'id': 'NET.1.1.A24',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.1.A25',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.11', 'G 0.18', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.27', 'G 0.29', 'G 0.30', 'G 0.40']
    },
    {
        'id': 'NET.1.1.A26',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'NET.1.1.A27',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'NET.1.1.A28',
        'cia': 'A',
        'gefahren': ['G 0.25']
    },
    {
        'id': 'NET.1.1.A29',
        'cia': 'A',
        'gefahren': ['G 0.9', 'G 0.11', 'G 0.25', 'G 0.40']
    },
    {
        'id': 'NET.1.1.A30',
        'cia': 'A',
        'gefahren': ['G 0.9', 'G 0.11', 'G 0.40']
    },
    {
        'id': 'NET.1.1.A31',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.1.A32',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.1.A33',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.1.A34',
        'cia': 'CI',
        'gefahren': ['G 0.15', 'G 0.43']
    },
    {
        'id': 'NET.1.1.A35',
        'cia': 'CI',
        'gefahren': ['G 0.19']
    },
    {
        'id': 'NET.1.1.A36',
        'cia': 'CIA',
        'gefahren': ['G 0.29']
    },
    {
        'id': 'NET.1.2.A1',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.1.2.A2',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'NET.1.2.A6',
        'cia': None,
        'gefahren': ['G 0.45']
    },
    {
        'id': 'NET.1.2.A7',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.37']
    },
    {
        'id': 'NET.1.2.A8',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.37']
    },
    {
        'id': 'NET.1.2.A9',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.30', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'NET.1.2.A10',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'NET.1.2.A11',
        'cia': None,
        'gefahren': ['G 0.30']
    },
    {
        'id': 'NET.1.2.A12',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'NET.1.2.A13',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'NET.1.2.A14',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.19', 'G 0.23', 'G 0.25', 'G 0.27', 'G 0.29', 'G 0.30']
    },
    {
        'id': 'NET.1.2.A15',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'NET.1.2.A16',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.25', 'G 0.29', 'G 0.30']
    },
    {
        'id': 'NET.1.2.A17',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'NET.1.2.A18',
        'cia': None,
        'gefahren': ['G 0.26', 'G 0.29', 'G 0.31']
    },
    {
        'id': 'NET.1.2.A21',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'NET.1.2.A22',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'NET.1.2.A24',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.31']
    },
    {
        'id': 'NET.1.2.A25',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'NET.1.2.A26',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.37']
    },
    {
        'id': 'NET.1.2.A27',
        'cia': None,
        'gefahren': ['G 0.25']
    },
    {
        'id': 'NET.1.2.A28',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.2.A29',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.2.A30',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.40']
    },
    {
        'id': 'NET.1.2.A31',
        'cia': 'IA',
        'gefahren': ['G 0.15', 'G 0.22', 'G 0.30', 'G 0.46']
    },
    {
        'id': 'NET.1.2.A32',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.2.A33',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'NET.1.2.A35',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.29', 'G 0.30', 'G 0.40', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'NET.1.2.A36',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.29', 'G 0.30', 'G 0.40', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'NET.1.2.A37',
        'cia': 'CI',
        'gefahren': ['G 0.29', 'G 0.35']
    },
    {
        'id': 'NET.1.2.A38',
        'cia': 'A',
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.40', 'G 0.45']
    },
    {
        'id': 'NET.2.1.A1',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.2.1.A2',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.15', 'G 0.18', 'G 0.23', 'G 0.30', 'G 0.43']
    },
    {
        'id': 'NET.2.1.A3',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.23', 'G 0.30', 'G 0.43']
    },
    {
        'id': 'NET.2.1.A4',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.16', 'G 0.24', 'G 0.25']
    },
    {
        'id': 'NET.2.1.A5',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.23', 'G 0.30', 'G 0.43']
    },
    {
        'id': 'NET.2.1.A6',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'NET.2.1.A7',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23']
    },
    {
        'id': 'NET.2.1.A8',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30']
    },
    {
        'id': 'NET.2.1.A9',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'NET.2.1.A10',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.2.1.A11',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.2.1.A12',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.2.1.A13',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.27', 'G 0.30', 'G 0.40', 'G 0.43']
    },
    {
        'id': 'NET.2.1.A14',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23']
    },
    {
        'id': 'NET.2.1.A15',
        'cia': 'CI',
        'gefahren': ['G 0.15', 'G 0.43']
    },
    {
        'id': 'NET.2.1.A16',
        'cia': 'CIA',
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'NET.2.1.A17',
        'cia': 'C',
        'gefahren': ['G 0.15', 'G 0.23']
    },
    {
        'id': 'NET.2.1.A18',
        'cia': 'CIA',
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.43']
    },
    {
        'id': 'NET.2.2.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.31', 'G 0.43']
    },
    {
        'id': 'NET.2.2.A2',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.2.2.A3',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.23', 'G 0.43']
    },
    {
        'id': 'NET.2.2.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23']
    },
    {
        'id': 'NET.3.1.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.22', 'G 0.23', 'G 0.26', 'G 0.30']
    },
    {
        'id': 'NET.3.1.A4',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'NET.3.1.A5',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.25', 'G 0.27', 'G 0.40']
    },
    {
        'id': 'NET.3.1.A6',
        'cia': None,
        'gefahren': ['G 0.27']
    },
    {
        'id': 'NET.3.1.A7',
        'cia': None,
        'gefahren': ['G 0.37']
    },
    {
        'id': 'NET.3.1.A8',
        'cia': None,
        'gefahren': ['G 0.27', 'G 0.45']
    },
    {
        'id': 'NET.3.1.A9',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19']
    },
    {
        'id': 'NET.3.1.A10',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.1.A11',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.1.A12',
        'cia': None,
        'gefahren': ['G 0.31']
    },
    {
        'id': 'NET.3.1.A13',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.23', 'G 0.30', 'G 0.46']
    },
    {
        'id': 'NET.3.1.A14',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.40']
    },
    {
        'id': 'NET.3.1.A15',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'NET.3.1.A16',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.23', 'G 0.25', 'G 0.40']
    },
    {
        'id': 'NET.3.1.A17',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.25', 'G 0.40']
    },
    {
        'id': 'NET.3.1.A18',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'NET.3.1.A19',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.30']
    },
    {
        'id': 'NET.3.1.A20',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'NET.3.1.A21',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'NET.3.1.A22',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'NET.3.1.A23',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.1.A24',
        'cia': 'IA',
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'NET.3.1.A25',
        'cia': 'I',
        'gefahren': ['G 0.22', 'G 0.23', 'G 0.30', 'G 0.46']
    },
    {
        'id': 'NET.3.1.A26',
        'cia': 'A',
        'gefahren': ['G 0.23', 'G 0.27']
    },
    {
        'id': 'NET.3.1.A27',
        'cia': 'A',
        'gefahren': ['G 0.27']
    },
    {
        'id': 'NET.3.1.A28',
        'cia': 'CI',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.2.A1',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.2.A2',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23']
    },
    {
        'id': 'NET.3.2.A3',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.40', 'G 0.43']
    },
    {
        'id': 'NET.3.2.A4',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.46']
    },
    {
        'id': 'NET.3.2.A6',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'NET.3.2.A7',
        'cia': None,
        'gefahren': ['G 0.27']
    },
    {
        'id': 'NET.3.2.A8',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.23', 'G 0.43']
    },
    {
        'id': 'NET.3.2.A9',
        'cia': None,
        'gefahren': ['G 0.37']
    },
    {
        'id': 'NET.3.2.A10',
        'cia': None,
        'gefahren': ['G 0.41', 'G 0.43']
    },
    {
        'id': 'NET.3.2.A14',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.2.A15',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.20']
    },
    {
        'id': 'NET.3.2.A16',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.40']
    },
    {
        'id': 'NET.3.2.A17',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'NET.3.2.A18',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'NET.3.2.A19',
        'cia': None,
        'gefahren': ['G 0.40', 'G 0.41']
    },
    {
        'id': 'NET.3.2.A20',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'NET.3.2.A21',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.29', 'G 0.39']
    },
    {
        'id': 'NET.3.2.A22',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'NET.3.2.A23',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.18', 'G 0.25', 'G 0.27']
    },
    {
        'id': 'NET.3.2.A24',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.2.A25',
        'cia': 'I',
        'gefahren': ['G 0.22', 'G 0.23', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'NET.3.2.A26',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.27']
    },
    {
        'id': 'NET.3.2.A27',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.26']
    },
    {
        'id': 'NET.3.2.A28',
        'cia': 'CI',
        'gefahren': ['G 0.39']
    },
    {
        'id': 'NET.3.2.A29',
        'cia': 'A',
        'gefahren': ['G 0.9', 'G 0.18', 'G 0.25', 'G 0.27']
    },
    {
        'id': 'NET.3.2.A30',
        'cia': 'A',
        'gefahren': ['G 0.27']
    },
    {
        'id': 'NET.3.2.A31',
        'cia': 'CI',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.2.A32',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.18', 'G 0.27']
    },
    {
        'id': 'NET.3.3.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.32']
    },
    {
        'id': 'NET.3.3.A2',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18']
    },
    {
        'id': 'NET.3.3.A3',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.18']
    },
    {
        'id': 'NET.3.3.A4',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.3.A5',
        'cia': None,
        'gefahren': ['G 0.30', 'G 0.32']
    },
    {
        'id': 'NET.3.3.A6',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.3.A7',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.3.A8',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.3.A9',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.3.A10',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.3.A11',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'NET.3.3.A12',
        'cia': None,
        'gefahren': ['G 0.30', 'G 0.32']
    },
    {
        'id': 'NET.3.3.A13',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.3.4.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.32', 'G 0.36']
    },
    {
        'id': 'NET.3.4.A2',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.27', 'G 0.31', 'G 0.32', 'G 0.36', 'G 0.38', 'G 0.39']
    },
    {
        'id': 'NET.3.4.A3',
        'cia': None,
        'gefahren': ['G 0.26', 'G 0.27', 'G 0.31', 'G 0.36', 'G 0.38', 'G 0.39']
    },
    {
        'id': 'NET.3.4.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.32', 'G 0.38']
    },
    {
        'id': 'NET.3.4.A5',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.36']
    },
    {
        'id': 'NET.3.4.A6',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.27', 'G 0.31']
    },
    {
        'id': 'NET.3.4.A7',
        'cia': None,
        'gefahren': ['G 0.36']
    },
    {
        'id': 'NET.3.4.A8',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.38']
    },
    {
        'id': 'NET.3.4.A9',
        'cia': None,
        'gefahren': ['G 0.32', 'G 0.36', 'G 0.39']
    },
    {
        'id': 'NET.3.4.A10',
        'cia': None,
        'gefahren': ['G 0.36']
    },
    {
        'id': 'NET.3.4.A11',
        'cia': None,
        'gefahren': ['G 0.26', 'G 0.32', 'G 0.36', 'G 0.39']
    },
    {
        'id': 'NET.3.4.A12',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.28', 'G 0.31', 'G 0.32', 'G 0.39']
    },
    {
        'id': 'NET.3.4.A13',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.26', 'G 0.31', 'G 0.39']
    },
    {
        'id': 'NET.3.4.A14',
        'cia': None,
        'gefahren': ['G 0.36', 'G 0.43']
    },
    {
        'id': 'NET.3.4.A15',
        'cia': None,
        'gefahren': ['G 0.39']
    },
    {
        'id': 'NET.3.4.A16',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.27', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.36', 'G 0.38', 'G 0.39']
    },
    {
        'id': 'NET.3.4.A17',
        'cia': None,
        'gefahren': ['G 0.30', 'G 0.38']
    },
    {
        'id': 'NET.3.4.A18',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'NET.3.4.A19',
        'cia': None,
        'gefahren': ['G 0.36']
    },
    {
        'id': 'NET.3.4.A20',
        'cia': 'CI',
        'gefahren': ['G 0.36', 'G 0.43']
    },
    {
        'id': 'NET.3.4.A21',
        'cia': 'C',
        'gefahren': ['G 0.36', 'G 0.39']
    },
    {
        'id': 'NET.3.4.A22',
        'cia': 'C',
        'gefahren': ['G 0.30', 'G 0.36', 'G 0.43']
    },
    {
        'id': 'NET.3.4.A23',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.26']
    },
    {
        'id': 'NET.3.4.A24',
        'cia': 'C',
        'gefahren': ['G 0.30', 'G 0.43']
    },
    {
        'id': 'NET.3.4.A25',
        'cia': 'A',
        'gefahren': ['G 0.28', 'G 0.31', 'G 0.32', 'G 0.36', 'G 0.38', 'G 0.39']
    },
    {
        'id': 'NET.3.4.A26',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.26']
    },
    {
        'id': 'NET.3.4.A27',
        'cia': 'I',
        'gefahren': ['G 0.36', 'G 0.43']
    },
    {
        'id': 'NET.4.1.A1',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18']
    },
    {
        'id': 'NET.4.1.A2',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18']
    },
    {
        'id': 'NET.4.1.A5',
        'cia': None,
        'gefahren': ['G 0.37']
    },
    {
        'id': 'NET.4.1.A6',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'NET.4.1.A7',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.30']
    },
    {
        'id': 'NET.4.1.A8',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.31', 'G 0.42']
    },
    {
        'id': 'NET.4.1.A9',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31', 'G 0.42']
    },
    {
        'id': 'NET.4.1.A10',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.4.1.A11',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'NET.4.1.A12',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.45']
    },
    {
        'id': 'NET.4.1.A13',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.18']
    },
    {
        'id': 'NET.4.1.A14',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.27']
    },
    {
        'id': 'NET.4.1.A15',
        'cia': None,
        'gefahren': ['G 0.27']
    },
    {
        'id': 'NET.4.1.A16',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.30']
    },
    {
        'id': 'NET.4.1.A17',
        'cia': None,
        'gefahren': ['G 0.30']
    },
    {
        'id': 'NET.4.1.A18',
        'cia': 'CI',
        'gefahren': ['G 0.21', 'G 0.30']
    },
    {
        'id': 'NET.4.1.A19',
        'cia': 'A',
        'gefahren': ['G 0.9', 'G 0.11', 'G 0.27']
    },
    {
        'id': 'NET.4.2.A1',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.4.2.A3',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.28', 'G 0.30']
    },
    {
        'id': 'NET.4.2.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23']
    },
    {
        'id': 'NET.4.2.A5',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'NET.4.2.A7',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.31']
    },
    {
        'id': 'NET.4.2.A8',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19']
    },
    {
        'id': 'NET.4.2.A9',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.4.2.A11',
        'cia': None,
        'gefahren': ['G 0.30', 'G 0.31']
    },
    {
        'id': 'NET.4.2.A12',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'NET.4.2.A13',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.46']
    },
    {
        'id': 'NET.4.2.A14',
        'cia': 'CI',
        'gefahren': ['G 0.15', 'G 0.46']
    },
    {
        'id': 'NET.4.2.A15',
        'cia': 'CI',
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.19', 'G 0.46']
    },
    {
        'id': 'NET.4.2.A16',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'NET.4.3.A1',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.27']
    },
    {
        'id': 'NET.4.3.A2',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.31']
    },
    {
        'id': 'NET.4.3.A3',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.26', 'G 0.27', 'G 0.31']
    },
    {
        'id': 'NET.4.3.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'NET.4.3.A6',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'NET.4.3.A7',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.37']
    },
    {
        'id': 'NET.4.3.A8',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19']
    },
    {
        'id': 'NET.4.3.A9',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.37']
    },
    {
        'id': 'NET.4.3.A10',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19']
    },
    {
        'id': 'NET.4.3.A11',
        'cia': 'A',
        'gefahren': ['G 0.27']
    },
    {
        'id': 'NET.4.3.A12',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.30']
    },
    {
        'id': 'NET.4.3.A13',
        'cia': 'CIA',
        'gefahren': ['G 0.30', 'G 0.31']
    },
    {
        'id': 'NET.4.3.A14',
        'cia': 'A',
        'gefahren': ['G 0.27', 'G 0.45']
    },
    {
        'id': 'NET.4.3.A15',
        'cia': 'CIA',
        'gefahren': ['G 0.16', 'G 0.19', 'G 0.37', 'G 0.45']
    },
    {
        'id': 'OPS.1.1.1.A1',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.1.A2',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'OPS.1.1.1.A3',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.1.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.33']
    },
    {
        'id': 'OPS.1.1.1.A5',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.25', 'G 0.31']
    },
    {
        'id': 'OPS.1.1.1.A6',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.1.A7',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.27', 'G 0.28']
    },
    {
        'id': 'OPS.1.1.1.A8',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.1.A9',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.22', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'OPS.1.1.1.A10',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.28']
    },
    {
        'id': 'OPS.1.1.1.A11',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'OPS.1.1.1.A12',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'OPS.1.1.1.A13',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22']
    },
    {
        'id': 'OPS.1.1.1.A14',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.1.A15',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.22', 'G 0.23']
    },
    {
        'id': 'OPS.1.1.1.A16',
        'cia': None,
        'gefahren': ['G 0.31']
    },
    {
        'id': 'OPS.1.1.1.A17',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25']
    },
    {
        'id': 'OPS.1.1.1.A18',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'OPS.1.1.1.A19',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25']
    },
    {
        'id': 'OPS.1.1.1.A20',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.28']
    },
    {
        'id': 'OPS.1.1.1.A21',
        'cia': 'CIA',
        'gefahren': ['G 0.23', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'OPS.1.1.1.A22',
        'cia': 'CIA',
        'gefahren': ['G 0.23', 'G 0.28']
    },
    {
        'id': 'OPS.1.1.1.A23',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.23']
    },
    {
        'id': 'OPS.1.1.1.A24',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.37']
    },
    {
        'id': 'OPS.1.1.1.A25',
        'cia': 'CIA',
        'gefahren': ['G 0.25']
    },
    {
        'id': 'OPS.1.1.1.A26',
        'cia': 'IA',
        'gefahren': ['G 0.25']
    },
    {
        'id': 'OPS.1.1.2.A2',
        'cia': None,
        'gefahren': ['G 0.27', 'G 0.33']
    },
    {
        'id': 'OPS.1.1.2.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.32', 'G 0.42']
    },
    {
        'id': 'OPS.1.1.2.A5',
        'cia': None,
        'gefahren': ['G 0.37']
    },
    {
        'id': 'OPS.1.1.2.A6',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'OPS.1.1.2.A7',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.31', 'G 0.32']
    },
    {
        'id': 'OPS.1.1.2.A8',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'OPS.1.1.2.A11',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.37']
    },
    {
        'id': 'OPS.1.1.2.A16',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'OPS.1.1.2.A17',
        'cia': 'CI',
        'gefahren': ['G 0.31', 'G 0.32', 'G 0.37']
    },
    {
        'id': 'OPS.1.1.2.A18',
        'cia': 'CI',
        'gefahren': ['G 0.22', 'G 0.37']
    },
    {
        'id': 'OPS.1.1.2.A19',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.27']
    },
    {
        'id': 'OPS.1.1.2.A21',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.31', 'G 0.32']
    },
    {
        'id': 'OPS.1.1.2.A22',
        'cia': None,
        'gefahren': ['G 0.31']
    },
    {
        'id': 'OPS.1.1.2.A23',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'OPS.1.1.2.A24',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.31', 'G 0.42']
    },
    {
        'id': 'OPS.1.1.2.A25',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.45']
    },
    {
        'id': 'OPS.1.1.2.A26',
        'cia': None,
        'gefahren': ['G 0.27', 'G 0.45']
    },
    {
        'id': 'OPS.1.1.2.A27',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'OPS.1.1.2.A28',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.37']
    },
    {
        'id': 'OPS.1.1.2.A29',
        'cia': 'A',
        'gefahren': ['G 0.18', 'G 0.25']
    },
    {
        'id': 'OPS.1.1.2.A30',
        'cia': 'CI',
        'gefahren': ['G 0.18', 'G 0.23']
    },
    {
        'id': 'OPS.1.1.3.A1',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.3.A2',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.3.A3',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.20', 'G 0.23', 'G 0.25', 'G 0.26', 'G 0.28', 'G 0.39']
    },
    {
        'id': 'OPS.1.1.3.A5',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.3.A6',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.3.A7',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.3.A8',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.3.A9',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.28']
    },
    {
        'id': 'OPS.1.1.3.A10',
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.23', 'G 0.28', 'G 0.39', 'G 0.46']
    },
    {
        'id': 'OPS.1.1.3.A11',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.3.A12',
        'cia': 'A',
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'OPS.1.1.3.A13',
        'cia': 'IA',
        'gefahren': ['G 0.18', 'G 0.26']
    },
    {
        'id': 'OPS.1.1.3.A14',
        'cia': 'CIA',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.3.A15',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.25', 'G 0.26', 'G 0.28']
    },
    {
        'id': 'OPS.1.1.4.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.39']
    },
    {
        'id': 'OPS.1.1.4.A2',
        'cia': None,
        'gefahren': ['G 0.39']
    },
    {
        'id': 'OPS.1.1.4.A3',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.20', 'G 0.29', 'G 0.39']
    },
    {
        'id': 'OPS.1.1.4.A5',
        'cia': None,
        'gefahren': ['G 0.27', 'G 0.29', 'G 0.30', 'G 0.39']
    },
    {
        'id': 'OPS.1.1.4.A6',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.39']
    },
    {
        'id': 'OPS.1.1.4.A7',
        'cia': None,
        'gefahren': ['G 0.31', 'G 0.39']
    },
    {
        'id': 'OPS.1.1.4.A9',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.39']
    },
    {
        'id': 'OPS.1.1.4.A10',
        'cia': 'CIA',
        'gefahren': ['G 0.39']
    },
    {
        'id': 'OPS.1.1.4.A11',
        'cia': 'CIA',
        'gefahren': ['G 0.39']
    },
    {
        'id': 'OPS.1.1.4.A12',
        'cia': 'CIA',
        'gefahren': ['G 0.39']
    },
    {
        'id': 'OPS.1.1.4.A13',
        'cia': 'CIA',
        'gefahren': ['G 0.39']
    },
    {
        'id': 'OPS.1.1.4.A14',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.39']
    },
    {
        'id': 'OPS.1.1.5.A1',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.5.A3',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.37']
    },
    {
        'id': 'OPS.1.1.5.A4',
        'cia': None,
        'gefahren': ['G 0.37']
    },
    {
        'id': 'OPS.1.1.5.A5',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.32', 'G 0.38', 'G 0.46']
    },
    {
        'id': 'OPS.1.1.5.A6',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.26', 'G 0.27', 'G 0.37']
    },
    {
        'id': 'OPS.1.1.5.A8',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'OPS.1.1.5.A9',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.29', 'G 0.46']
    },
    {
        'id': 'OPS.1.1.5.A10',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.32']
    },
    {
        'id': 'OPS.1.1.5.A11',
        'cia': 'CIA',
        'gefahren': ['G 0.29', 'G 0.37']
    },
    {
        'id': 'OPS.1.1.5.A12',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.22', 'G 0.46']
    },
    {
        'id': 'OPS.1.1.5.A13',
        'cia': 'A',
        'gefahren': ['G 0.9', 'G 0.25', 'G 0.27']
    },
    {
        'id': 'OPS.1.1.6.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'OPS.1.1.6.A2',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26']
    },
    {
        'id': 'OPS.1.1.6.A3',
        'cia': None,
        'gefahren': ['G 0.26']
    },
    {
        'id': 'OPS.1.1.6.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'OPS.1.1.6.A5',
        'cia': None,
        'gefahren': ['G 0.27', 'G 0.28']
    },
    {
        'id': 'OPS.1.1.6.A6',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.6.A7',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.41']
    },
    {
        'id': 'OPS.1.1.6.A10',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.1.6.A11',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.38']
    },
    {
        'id': 'OPS.1.1.6.A12',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.28']
    },
    {
        'id': 'OPS.1.1.6.A13',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.25', 'G 0.26', 'G 0.32', 'G 0.38', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'OPS.1.1.6.A14',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'OPS.1.1.6.A15',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'OPS.1.1.6.A16',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.18']
    },
    {
        'id': 'OPS.1.1.7.A1',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.18', 'G 0.25', 'G 0.26', 'G 0.27', 'G 0.29', 'G 0.30']
    },
    {
        'id': 'OPS.1.1.7.A2',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.18', 'G 0.25', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'OPS.1.1.7.A3',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'OPS.1.1.7.A4',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.43']
    },
    {
        'id': 'OPS.1.1.7.A5',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.43']
    },
    {
        'id': 'OPS.1.1.7.A6',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.31', 'G 0.43']
    },
    {
        'id': 'OPS.1.1.7.A7',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.31', 'G 0.32']
    },
    {
        'id': 'OPS.1.1.7.A8',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.27', 'G 0.29', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'OPS.1.1.7.A9',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.27', 'G 0.29', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'OPS.1.1.7.A10',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.25', 'G 0.26', 'G 0.27', 'G 0.29', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'OPS.1.1.7.A11',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.26']
    },
    {
        'id': 'OPS.1.1.7.A12',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'OPS.1.1.7.A13',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.31', 'G 0.43']
    },
    {
        'id': 'OPS.1.1.7.A14',
        'cia': None,
        'gefahren': ['G 0.45']
    },
    {
        'id': 'OPS.1.1.7.A15',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.26', 'G 0.27', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.37']
    },
    {
        'id': 'OPS.1.1.7.A16',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26']
    },
    {
        'id': 'OPS.1.1.7.A17',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.31', 'G 0.43']
    },
    {
        'id': 'OPS.1.1.7.A18',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'OPS.1.1.7.A19',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.43']
    },
    {
        'id': 'OPS.1.1.7.A20',
        'cia': 'A',
        'gefahren': ['G 0.9', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'OPS.1.1.7.A21',
        'cia': 'CI',
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.26', 'G 0.30', 'G 0.43']
    },
    {
        'id': 'OPS.1.1.7.A22',
        'cia': 'CIA',
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.29', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'OPS.1.1.7.A23',
        'cia': 'CIA',
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'OPS.1.1.7.A24',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.45']
    },
    {
        'id': 'OPS.1.1.7.A25',
        'cia': 'CI',
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.23', 'G 0.29', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.37']
    },
    {
        'id': 'OPS.1.1.7.A26',
        'cia': 'CI',
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.43']
    },
    {
        'id': 'OPS.1.2.2.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.1.2.2.A2',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.1.2.2.A3',
        'cia': None,
        'gefahren': ['G 0.2', 'G 0.4', 'G 0.44']
    },
    {
        'id': 'OPS.1.2.2.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.45']
    },
    {
        'id': 'OPS.1.2.2.A5',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.45']
    },
    {
        'id': 'OPS.1.2.2.A6',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.28', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'OPS.1.2.2.A7',
        'cia': None,
        'gefahren': ['G 0.45', 'G 0.46']
    },
    {
        'id': 'OPS.1.2.2.A8',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.37']
    },
    {
        'id': 'OPS.1.2.2.A9',
        'cia': None,
        'gefahren': ['G 0.45', 'G 0.46']
    },
    {
        'id': 'OPS.1.2.2.A10',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.31']
    },
    {
        'id': 'OPS.1.2.2.A11',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'OPS.1.2.2.A12',
        'cia': None,
        'gefahren': ['G 0.27']
    },
    {
        'id': 'OPS.1.2.2.A13',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.2.2.A14',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.28']
    },
    {
        'id': 'OPS.1.2.2.A15',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.45']
    },
    {
        'id': 'OPS.1.2.2.A16',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.46']
    },
    {
        'id': 'OPS.1.2.2.A17',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26']
    },
    {
        'id': 'OPS.1.2.2.A18',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28', 'G 0.29', 'G 0.45']
    },
    {
        'id': 'OPS.1.2.2.A19',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'OPS.1.2.2.A20',
        'cia': 'CI',
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.1.2.2.A21',
        'cia': 'CI',
        'gefahren': ['G 0.45', 'G 0.46']
    },
    {
        'id': 'OPS.1.2.4.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'OPS.1.2.4.A2',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.30']
    },
    {
        'id': 'OPS.1.2.4.A5',
        'cia': None,
        'gefahren': ['G 0.31']
    },
    {
        'id': 'OPS.1.2.4.A6',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.2.4.A7',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'OPS.1.2.4.A8',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.2.4.A9',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.27']
    },
    {
        'id': 'OPS.1.2.4.A10',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.2.5.A1',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.2.5.A2',
        'cia': None,
        'gefahren': ['G 0.31']
    },
    {
        'id': 'OPS.1.2.5.A3',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.25', 'G 0.31']
    },
    {
        'id': 'OPS.1.2.5.A5',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.25']
    },
    {
        'id': 'OPS.1.2.5.A6',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.2.5.A7',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'OPS.1.2.5.A8',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22']
    },
    {
        'id': 'OPS.1.2.5.A9',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.20']
    },
    {
        'id': 'OPS.1.2.5.A10',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.20', 'G 0.37']
    },
    {
        'id': 'OPS.1.2.5.A14',
        'cia': 'CIA',
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.25']
    },
    {
        'id': 'OPS.1.2.5.A17',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.21', 'G 0.25']
    },
    {
        'id': 'OPS.1.2.5.A19',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.21', 'G 0.39']
    },
    {
        'id': 'OPS.1.2.5.A20',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.39', 'G 0.40']
    },
    {
        'id': 'OPS.1.2.5.A21',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30']
    },
    {
        'id': 'OPS.1.2.5.A22',
        'cia': 'A',
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.22', 'G 0.30', 'G 0.37']
    },
    {
        'id': 'OPS.1.2.5.A24',
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.25', 'G 0.31']
    },
    {
        'id': 'OPS.1.2.5.A25',
        'cia': None,
        'gefahren': ['G 0.30']
    },
    {
        'id': 'OPS.1.2.6.A1',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.1.2.6.A2',
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.29']
    },
    {
        'id': 'OPS.1.2.6.A3',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.30', 'G 0.46']
    },
    {
        'id': 'OPS.1.2.6.A4',
        'cia': None,
        'gefahren': ['G 0.22']
    },
    {
        'id': 'OPS.1.2.6.A5',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.27', 'G 0.46']
    },
    {
        'id': 'OPS.1.2.6.A6',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.22']
    },
    {
        'id': 'OPS.1.2.6.A7',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.40', 'G 0.46']
    },
    {
        'id': 'OPS.1.2.6.A8',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.22', 'G 0.46']
    },
    {
        'id': 'OPS.1.2.6.A9',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.27', 'G 0.46']
    },
    {
        'id': 'OPS.1.2.6.A10',
        'cia': 'I',
        'gefahren': ['G 0.20', 'G 0.22']
    },
    {
        'id': 'OPS.1.2.6.A11',
        'cia': 'A',
        'gefahren': ['G 0.27']
    },
    {
        'id': 'OPS.1.2.6.A12',
        'cia': 'I',
        'gefahren': ['G 0.20', 'G 0.22']
    },
    {
        'id': 'OPS.2.2.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.2.A2',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.2.A3',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.2.2.A4',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.2.2.A5',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.31', 'G 0.36']
    },
    {
        'id': 'OPS.2.2.A6',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.31']
    },
    {
        'id': 'OPS.2.2.A7',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.25', 'G 0.26', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.45']
    },
    {
        'id': 'OPS.2.2.A8',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.2.A9',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.2.A10',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.25', 'G 0.26']
    },
    {
        'id': 'OPS.2.2.A11',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.11', 'G 0.25', 'G 0.26', 'G 0.45']
    },
    {
        'id': 'OPS.2.2.A12',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.2.2.A13',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.19', 'G 0.25', 'G 0.26', 'G 0.29', 'G 0.30', 'G 0.31', 'G 0.32']
    },
    {
        'id': 'OPS.2.2.A14',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'OPS.2.2.A15',
        'cia': 'A',
        'gefahren': ['G 0.11', 'G 0.45']
    },
    {
        'id': 'OPS.2.2.A16',
        'cia': 'A',
        'gefahren': ['G 0.11', 'G 0.45']
    },
    {
        'id': 'OPS.2.2.A17',
        'cia': 'A',
        'gefahren': ['G 0.14', 'G 0.15']
    },
    {
        'id': 'OPS.2.2.A18',
        'cia': 'CIA',
        'gefahren': ['G 0.30', 'G 0.32']
    },
    {
        'id': 'OPS.2.2.A19',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.35', 'G 0.41']
    },
    {
        'id': 'OPS.2.3.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A2',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A3',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A4',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'OPS.2.3.A5',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.22', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A6',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A7',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.19']
    },
    {
        'id': 'OPS.2.3.A8',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A9',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A10',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.29', 'G 0.42']
    },
    {
        'id': 'OPS.2.3.A11',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A12',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A13',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A14',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A15',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.23']
    },
    {
        'id': 'OPS.2.3.A16',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A17',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A18',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A19',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18']
    },
    {
        'id': 'OPS.2.3.A20',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.25', 'G 0.27', 'G 0.42']
    },
    {
        'id': 'OPS.2.3.A21',
        'cia': 'IA',
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A22',
        'cia': 'A',
        'gefahren': ['G 0.11', 'G 0.25', 'G 0.27']
    },
    {
        'id': 'OPS.2.3.A23',
        'cia': 'C',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22', 'G 0.29']
    },
    {
        'id': 'OPS.2.3.A24',
        'cia': 'CIA',
        'gefahren': ['G 0.29', 'G 0.35']
    },
    {
        'id': 'OPS.2.3.A25',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.23', 'G 0.25']
    },
    {
        'id': 'OPS.3.2.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A2',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'OPS.3.2.A3',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A4',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.22', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A5',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A6',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.19']
    },
    {
        'id': 'OPS.3.2.A7',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.27', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A8',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A9',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A10',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A11',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.25', 'G 0.27', 'G 0.42']
    },
    {
        'id': 'OPS.3.2.A12',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A13',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.23']
    },
    {
        'id': 'OPS.3.2.A14',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.25', 'G 0.27', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A15',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A16',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.27', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A17',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.23', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A18',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A19',
        'cia': 'CIA',
        'gefahren': ['G 0.29', 'G 0.35']
    },
    {
        'id': 'OPS.3.2.A20',
        'cia': 'C',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22', 'G 0.29']
    },
    {
        'id': 'OPS.3.2.A21',
        'cia': 'A',
        'gefahren': ['G 0.11', 'G 0.25', 'G 0.27']
    },
    {
        'id': 'ORP.1.A1',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'ORP.1.A2',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'ORP.1.A3',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.19', 'G 0.21', 'G 0.30', 'G 0.44']
    },
    {
        'id': 'ORP.1.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.22', 'G 0.29', 'G 0.32']
    },
    {
        'id': 'ORP.1.A8',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.27']
    },
    {
        'id': 'ORP.1.A13',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.17', 'G 0.18', 'G 0.19', 'G 0.22']
    },
    {
        'id': 'ORP.1.A15',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'ORP.1.A16',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.29']
    },
    {
        'id': 'ORP.1.A17',
        'cia': 'C',
        'gefahren': ['G 0.14', 'G 0.15']
    },
    {
        'id': 'ORP.2.A1',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.31', 'G 0.38']
    },
    {
        'id': 'ORP.2.A2',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.29', 'G 0.30', 'G 0.33']
    },
    {
        'id': 'ORP.2.A3',
        'cia': None,
        'gefahren': ['G 0.31', 'G 0.33']
    },
    {
        'id': 'ORP.2.A4',
        'cia': None,
        'gefahren': ['G 0.17', 'G 0.29', 'G 0.30', 'G 0.44', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'ORP.2.A5',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22', 'G 0.29', 'G 0.32', 'G 0.37', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'ORP.2.A7',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.29', 'G 0.36', 'G 0.38']
    },
    {
        'id': 'ORP.2.A13',
        'cia': 'C',
        'gefahren': ['G 0.14', 'G 0.29', 'G 0.36', 'G 0.38']
    },
    {
        'id': 'ORP.2.A14',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.29']
    },
    {
        'id': 'ORP.2.A15',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.29', 'G 0.32', 'G 0.38', 'G 0.42', 'G 0.46']
    },
    {
        'id': 'ORP.3.A1',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.31']
    },
    {
        'id': 'ORP.3.A3',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'ORP.3.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'ORP.3.A6',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.31']
    },
    {
        'id': 'ORP.3.A7',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'ORP.3.A8',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'ORP.3.A9',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.29', 'G 0.31', 'G 0.36', 'G 0.38', 'G 0.42']
    },
    {
        'id': 'ORP.4.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.37']
    },
    {
        'id': 'ORP.4.A2',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30']
    },
    {
        'id': 'ORP.4.A3',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'ORP.4.A4',
        'cia': None,
        'gefahren': ['G 0.29', 'G 0.32', 'G 0.37']
    },
    {
        'id': 'ORP.4.A5',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.44']
    },
    {
        'id': 'ORP.4.A6',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.29', 'G 0.30']
    },
    {
        'id': 'ORP.4.A7',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.29', 'G 0.30']
    },
    {
        'id': 'ORP.4.A8',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.29']
    },
    {
        'id': 'ORP.4.A9',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.30', 'G 0.37']
    },
    {
        'id': 'ORP.4.A10',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.30', 'G 0.36']
    },
    {
        'id': 'ORP.4.A11',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.36']
    },
    {
        'id': 'ORP.4.A12',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.18', 'G 0.32', 'G 0.36']
    },
    {
        'id': 'ORP.4.A13',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.22', 'G 0.32', 'G 0.36']
    },
    {
        'id': 'ORP.4.A14',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.37']
    },
    {
        'id': 'ORP.4.A15',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'ORP.4.A16',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'ORP.4.A17',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'ORP.4.A18',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.18', 'G 0.36']
    },
    {
        'id': 'ORP.4.A19',
        'cia': None,
        'gefahren': ['G 0.31']
    },
    {
        'id': 'ORP.4.A20',
        'cia': 'CIA',
        'gefahren': ['G 0.25']
    },
    {
        'id': 'ORP.4.A21',
        'cia': 'CI',
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.32', 'G 0.36']
    },
    {
        'id': 'ORP.4.A22',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.29']
    },
    {
        'id': 'ORP.4.A23',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.29', 'G 0.30']
    },
    {
        'id': 'ORP.4.A24',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.22', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.37']
    },
    {
        'id': 'ORP.5.A1',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'ORP.5.A2',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'ORP.5.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'ORP.5.A5',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'ORP.5.A8',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'SYS.1.1.A1',
        'cia': None,
        'gefahren': ['G 0.16', 'G 0.21']
    },
    {
        'id': 'SYS.1.1.A2',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'SYS.1.1.A5',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.23']
    },
    {
        'id': 'SYS.1.1.A6',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.23']
    },
    {
        'id': 'SYS.1.1.A9',
        'cia': None,
        'gefahren': ['G 0.39']
    },
    {
        'id': 'SYS.1.1.A10',
        'cia': None,
        'gefahren': ['G 0.37']
    },
    {
        'id': 'SYS.1.1.A11',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'SYS.1.1.A12',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.1.1.A13',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.1.1.A15',
        'cia': None,
        'gefahren': ['G 0.8']
    },
    {
        'id': 'SYS.1.1.A16',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'SYS.1.1.A19',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.43']
    },
    {
        'id': 'SYS.1.1.A21',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.22', 'G 0.37', 'G 0.45']
    },
    {
        'id': 'SYS.1.1.A22',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'SYS.1.1.A23',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'SYS.1.1.A24',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.1.1.A25',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.27', 'G 0.31']
    },
    {
        'id': 'SYS.1.1.A27',
        'cia': 'IA',
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.32', 'G 0.40']
    },
    {
        'id': 'SYS.1.1.A28',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.27']
    },
    {
        'id': 'SYS.1.1.A30',
        'cia': 'CIA',
        'gefahren': ['G 0.25', 'G 0.28']
    },
    {
        'id': 'SYS.1.1.A31',
        'cia': 'CI',
        'gefahren': ['G 0.23', 'G 0.39']
    },
    {
        'id': 'SYS.1.1.A33',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.23']
    },
    {
        'id': 'SYS.1.1.A34',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22', 'G 0.46']
    },
    {
        'id': 'SYS.1.1.A35',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.20', 'G 0.27']
    },
    {
        'id': 'SYS.1.1.A36',
        'cia': 'CIA',
        'gefahren': ['G 0.21']
    },
    {
        'id': 'SYS.1.1.A37',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.31', 'G 0.39', 'G 0.45']
    },
    {
        'id': 'SYS.1.1.A38',
        'cia': 'I',
        'gefahren': ['G 0.21', 'G 0.28', 'G 0.39', 'G 0.46']
    },
    {
        'id': 'SYS.1.1.A39',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.23', 'G 0.30', 'G 0.31', 'G 0.32']
    },
    {
        'id': 'SYS.1.2.2.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.27', 'G 0.29']
    },
    {
        'id': 'SYS.1.2.2.A2',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.23', 'G 0.28']
    },
    {
        'id': 'SYS.1.2.2.A3',
        'cia': None,
        'gefahren': ['G 0.28', 'G 0.31']
    },
    {
        'id': 'SYS.1.2.2.A4',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.28']
    },
    {
        'id': 'SYS.1.2.2.A5',
        'cia': None,
        'gefahren': ['G 0.39']
    },
    {
        'id': 'SYS.1.2.2.A6',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.1.2.2.A8',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.23', 'G 0.46']
    },
    {
        'id': 'SYS.1.2.2.A11',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.23', 'G 0.37']
    },
    {
        'id': 'SYS.1.2.2.A12',
        'cia': 'A',
        'gefahren': ['G 0.27', 'G 0.45']
    },
    {
        'id': 'SYS.1.2.2.A14',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.22']
    },
    {
        'id': 'SYS.1.2.3.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'SYS.1.2.3.A2',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'SYS.1.2.3.A3',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.23', 'G 0.29']
    },
    {
        'id': 'SYS.1.2.3.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.21', 'G 0.23', 'G 0.28', 'G 0.39']
    },
    {
        'id': 'SYS.1.2.3.A5',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'SYS.1.2.3.A6',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.23', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'SYS.1.2.3.A7',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.22', 'G 0.30', 'G 0.31', 'G 0.32']
    },
    {
        'id': 'SYS.1.2.3.A8',
        'cia': 'A',
        'gefahren': ['G 0.18', 'G 0.22', 'G 0.29']
    },
    {
        'id': 'SYS.1.3.A2',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.3.A3',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.23']
    },
    {
        'id': 'SYS.1.3.A4',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.28']
    },
    {
        'id': 'SYS.1.3.A5',
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.28']
    },
    {
        'id': 'SYS.1.3.A6',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.31']
    },
    {
        'id': 'SYS.1.3.A8',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.23', 'G 0.43']
    },
    {
        'id': 'SYS.1.3.A10',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.28', 'G 0.39']
    },
    {
        'id': 'SYS.1.3.A14',
        'cia': 'C',
        'gefahren': ['G 0.14', 'G 0.30', 'G 0.46']
    },
    {
        'id': 'SYS.1.3.A16',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.22', 'G 0.28', 'G 0.32']
    },
    {
        'id': 'SYS.1.3.A17',
        'cia': 'CI',
        'gefahren': ['G 0.28']
    },
    {
        'id': 'SYS.1.5.A2',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.26', 'G 0.27', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32']
    },
    {
        'id': 'SYS.1.5.A3',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.21', 'G 0.23', 'G 0.31']
    },
    {
        'id': 'SYS.1.5.A4',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.29', 'G 0.30']
    },
    {
        'id': 'SYS.1.5.A5',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.21', 'G 0.23', 'G 0.30', 'G 0.46']
    },
    {
        'id': 'SYS.1.5.A6',
        'cia': None,
        'gefahren': ['G 0.27', 'G 0.37']
    },
    {
        'id': 'SYS.1.5.A7',
        'cia': None,
        'gefahren': ['G 0.37']
    },
    {
        'id': 'SYS.1.5.A8',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.1.5.A9',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'SYS.1.5.A10',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.1.5.A11',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.23', 'G 0.30', 'G 0.46']
    },
    {
        'id': 'SYS.1.5.A12',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'SYS.1.5.A13',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'SYS.1.5.A14',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.1.5.A15',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.23']
    },
    {
        'id': 'SYS.1.5.A16',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.22', 'G 0.23']
    },
    {
        'id': 'SYS.1.5.A17',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'SYS.1.5.A19',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.1.5.A20',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.27']
    },
    {
        'id': 'SYS.1.5.A21',
        'cia': 'IA',
        'gefahren': ['G 0.26', 'G 0.27']
    },
    {
        'id': 'SYS.1.5.A22',
        'cia': 'CI',
        'gefahren': ['G 0.23', 'G 0.28', 'G 0.30']
    },
    {
        'id': 'SYS.1.5.A23',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.1.5.A24',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.25', 'G 0.27', 'G 0.31']
    },
    {
        'id': 'SYS.1.5.A25',
        'cia': 'A',
        'gefahren': ['G 0.27', 'G 0.30']
    },
    {
        'id': 'SYS.1.5.A26',
        'cia': 'CIA',
        'gefahren': ['G 0.15', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'SYS.1.5.A27',
        'cia': 'CIA',
        'gefahren': ['G 0.15', 'G 0.20', 'G 0.21', 'G 0.22', 'G 0.23']
    },
    {
        'id': 'SYS.1.5.A28',
        'cia': 'C',
        'gefahren': ['G 0.14']
    },
    {
        'id': 'SYS.1.6.A1',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.20', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.24', 'G 0.25', 'G 0.27', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.40', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A2',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.24', 'G 0.25', 'G 0.27', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A3',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.20', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.24', 'G 0.25', 'G 0.27', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.37', 'G 0.39', 'G 0.40', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.20', 'G 0.21', 'G 0.22', 'G 0.25', 'G 0.27', 'G 0.30', 'G 0.31', 'G 0.39']
    },
    {
        'id': 'SYS.1.6.A5',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.27', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A6',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.20', 'G 0.21', 'G 0.23', 'G 0.25', 'G 0.27', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.37', 'G 0.39', 'G 0.40', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A7',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.30', 'G 0.37', 'G 0.45']
    },
    {
        'id': 'SYS.1.6.A8',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.30', 'G 0.32', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A9',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.20', 'G 0.21', 'G 0.24', 'G 0.27', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.40', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A10',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.20', 'G 0.21', 'G 0.23', 'G 0.25', 'G 0.27', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.37', 'G 0.39', 'G 0.40', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A11',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.25']
    },
    {
        'id': 'SYS.1.6.A12',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.20', 'G 0.21', 'G 0.22', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.37', 'G 0.39', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A13',
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.21', 'G 0.22', 'G 0.25', 'G 0.27', 'G 0.30', 'G 0.37', 'G 0.39', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A14',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.20', 'G 0.21', 'G 0.25', 'G 0.27', 'G 0.37', 'G 0.39', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A15',
        'cia': None,
        'gefahren': ['G 0.27', 'G 0.28', 'G 0.39', 'G 0.40']
    },
    {
        'id': 'SYS.1.6.A16',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A17',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A18',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A19',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.27', 'G 0.39', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A20',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.37']
    },
    {
        'id': 'SYS.1.6.A21',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.27', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.40', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A22',
        'cia': 'CI',
        'gefahren': ['G 0.18', 'G 0.37']
    },
    {
        'id': 'SYS.1.6.A23',
        'cia': 'I',
        'gefahren': ['G 0.22', 'G 0.28', 'G 0.39', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A24',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39', 'G 0.40', 'G 0.46']
    },
    {
        'id': 'SYS.1.6.A25',
        'cia': 'A',
        'gefahren': ['G 0.23', 'G 0.24', 'G 0.25', 'G 0.27', 'G 0.40']
    },
    {
        'id': 'SYS.1.6.A26',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.28', 'G 0.30', 'G 0.39', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A1',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.40', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A2',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.40', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A3',
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.26', 'G 0.28', 'G 0.30', 'G 0.40', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.31', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A5',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A6',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.20', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.36', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A7',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A8',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.39', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A9',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.39', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A11',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.43']
    },
    {
        'id': 'SYS.1.7.A14',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.39', 'G 0.40', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A16',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.26', 'G 0.27', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.39', 'G 0.40', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A17',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.31', 'G 0.45']
    },
    {
        'id': 'SYS.1.7.A18',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.31', 'G 0.33']
    },
    {
        'id': 'SYS.1.7.A19',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A20',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.23', 'G 0.26', 'G 0.30', 'G 0.36']
    },
    {
        'id': 'SYS.1.7.A21',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.31', 'G 0.33']
    },
    {
        'id': 'SYS.1.7.A22',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.26', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A23',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.20', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.40', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A24',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.26', 'G 0.27', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.39', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A25',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.27', 'G 0.31', 'G 0.45']
    },
    {
        'id': 'SYS.1.7.A26',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.26', 'G 0.27', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A27',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.28', 'G 0.31', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A28',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'SYS.1.7.A29',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.26', 'G 0.27', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A30',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.43']
    },
    {
        'id': 'SYS.1.7.A31',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.31', 'G 0.33', 'G 0.40', 'G 0.45']
    },
    {
        'id': 'SYS.1.7.A32',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'SYS.1.7.A33',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.20', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.26', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.39', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A34',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.26', 'G 0.27', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A35',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.26', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A36',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.27', 'G 0.30', 'G 0.36', 'G 0.37', 'G 0.39', 'G 0.40', 'G 0.43', 'G 0.46']
    },
    {
        'id': 'SYS.1.7.A37',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.25', 'G 0.26', 'G 0.27', 'G 0.40', 'G 0.45']
    },
    {
        'id': 'SYS.1.7.A38',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.40', 'G 0.43', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.1.8.A1',
        'cia': None,
        'gefahren': ['G 0.2', 'G 0.8', 'G 0.16', 'G 0.44']
    },
    {
        'id': 'SYS.1.8.A2',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.23', 'G 0.28', 'G 0.30']
    },
    {
        'id': 'SYS.1.8.A4',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.1.8.A6',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'SYS.1.8.A7',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.1.8.A8',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.1.8.A9',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18']
    },
    {
        'id': 'SYS.1.8.A10',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'SYS.1.8.A11',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'SYS.1.8.A13',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.27']
    },
    {
        'id': 'SYS.1.8.A14',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.27', 'G 0.30']
    },
    {
        'id': 'SYS.1.8.A15',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.27', 'G 0.30']
    },
    {
        'id': 'SYS.1.8.A16',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.1.8.A17',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'SYS.1.8.A18',
        'cia': None,
        'gefahren': ['G 0.29']
    },
    {
        'id': 'SYS.1.8.A19',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.26']
    },
    {
        'id': 'SYS.1.8.A20',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.25', 'G 0.45']
    },
    {
        'id': 'SYS.1.8.A21',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'SYS.1.8.A22',
        'cia': 'A',
        'gefahren': ['G 0.25']
    },
    {
        'id': 'SYS.1.8.A23',
        'cia': 'CI',
        'gefahren': ['G 0.15', 'G 0.46']
    },
    {
        'id': 'SYS.1.8.A24',
        'cia': 'I',
        'gefahren': ['G 0.23', 'G 0.46']
    },
    {
        'id': 'SYS.1.8.A25',
        'cia': 'C',
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.1.8.A26',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'SYS.1.9.A1',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.28']
    },
    {
        'id': 'SYS.1.9.A2',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.18', 'G 0.27', 'G 0.29', 'G 0.31']
    },
    {
        'id': 'SYS.1.9.A3',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31', 'G 0.41', 'G 0.43']
    },
    {
        'id': 'SYS.1.9.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.41', 'G 0.43']
    },
    {
        'id': 'SYS.1.9.A5',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22']
    },
    {
        'id': 'SYS.1.9.A6',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.18', 'G 0.23', 'G 0.27', 'G 0.31', 'G 0.36', 'G 0.39']
    },
    {
        'id': 'SYS.1.9.A7',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.22', 'G 0.28', 'G 0.36']
    },
    {
        'id': 'SYS.1.9.A8',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.39']
    },
    {
        'id': 'SYS.1.9.A9',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.27', 'G 0.31']
    },
    {
        'id': 'SYS.1.9.A10',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.28']
    },
    {
        'id': 'SYS.1.9.A11',
        'cia': None,
        'gefahren': ['G 0.9']
    },
    {
        'id': 'SYS.1.9.A12',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.31']
    },
    {
        'id': 'SYS.1.9.A13',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.39']
    },
    {
        'id': 'SYS.1.9.A14',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.31']
    },
    {
        'id': 'SYS.1.9.A15',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.43']
    },
    {
        'id': 'SYS.1.9.A16',
        'cia': None,
        'gefahren': ['G 0.9']
    },
    {
        'id': 'SYS.1.9.A17',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.22', 'G 0.28']
    },
    {
        'id': 'SYS.1.9.A18',
        'cia': 'IA',
        'gefahren': ['G 0.14', 'G 0.19']
    },
    {
        'id': 'SYS.1.9.A19',
        'cia': 'CIA',
        'gefahren': ['G 0.23', 'G 0.36', 'G 0.39']
    },
    {
        'id': 'SYS.1.9.A20',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.43']
    },
    {
        'id': 'SYS.1.9.A21',
        'cia': 'A',
        'gefahren': ['G 0.9', 'G 0.41']
    },
    {
        'id': 'SYS.1.9.A22',
        'cia': 'IA',
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.28', 'G 0.41']
    },
    {
        'id': 'SYS.2.1.A1',
        'cia': None,
        'gefahren': ['G 0.30']
    },
    {
        'id': 'SYS.2.1.A3',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'SYS.2.1.A6',
        'cia': None,
        'gefahren': ['G 0.39']
    },
    {
        'id': 'SYS.2.1.A8',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.30']
    },
    {
        'id': 'SYS.2.1.A9',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.2.1.A10',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.2.1.A11',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.2.1.A13',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.30']
    },
    {
        'id': 'SYS.2.1.A14',
        'cia': None,
        'gefahren': ['G 0.28']
    },
    {
        'id': 'SYS.2.1.A15',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.2.1.A16',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.28', 'G 0.30']
    },
    {
        'id': 'SYS.2.1.A18',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.46']
    },
    {
        'id': 'SYS.2.1.A20',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.21', 'G 0.30']
    },
    {
        'id': 'SYS.2.1.A21',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15']
    },
    {
        'id': 'SYS.2.1.A23',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.23', 'G 0.25', 'G 0.31']
    },
    {
        'id': 'SYS.2.1.A24',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.21', 'G 0.23', 'G 0.31', 'G 0.39']
    },
    {
        'id': 'SYS.2.1.A26',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.28']
    },
    {
        'id': 'SYS.2.1.A27',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.45']
    },
    {
        'id': 'SYS.2.1.A28',
        'cia': 'C',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.31']
    },
    {
        'id': 'SYS.2.1.A29',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.26']
    },
    {
        'id': 'SYS.2.1.A30',
        'cia': 'CIA',
        'gefahren': ['G 0.25', 'G 0.26', 'G 0.31']
    },
    {
        'id': 'SYS.2.1.A31',
        'cia': 'CIA',
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.40']
    },
    {
        'id': 'SYS.2.1.A32',
        'cia': 'CIA',
        'gefahren': ['G 0.23', 'G 0.28']
    },
    {
        'id': 'SYS.2.1.A33',
        'cia': 'CI',
        'gefahren': ['G 0.23', 'G 0.31', 'G 0.39']
    },
    {
        'id': 'SYS.2.1.A34',
        'cia': 'CIA',
        'gefahren': ['G 0.21', 'G 0.31', 'G 0.39', 'G 0.45']
    },
    {
        'id': 'SYS.2.1.A35',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.40']
    },
    {
        'id': 'SYS.2.1.A36',
        'cia': 'CI',
        'gefahren': ['G 0.21']
    },
    {
        'id': 'SYS.2.1.A37',
        'cia': 'C',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.30', 'G 0.36']
    },
    {
        'id': 'SYS.2.1.A38',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.26']
    },
    {
        'id': 'SYS.2.1.A39',
        'cia': 'A',
        'gefahren': ['G 0.8', 'G 0.26']
    },
    {
        'id': 'SYS.2.1.A40',
        'cia': 'A',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.2.1.A41',
        'cia': 'A',
        'gefahren': ['G 0.27']
    },
    {
        'id': 'SYS.2.1.A42',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.29']
    },
    {
        'id': 'SYS.2.1.A43',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'SYS.2.1.A44',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'SYS.2.1.A45',
        'cia': 'CIA',
        'gefahren': ['G 0.37']
    },
    {
        'id': 'SYS.2.2.3.A1',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.29']
    },
    {
        'id': 'SYS.2.2.3.A2',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'SYS.2.2.3.A4',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.2.2.3.A5',
        'cia': None,
        'gefahren': ['G 0.39']
    },
    {
        'id': 'SYS.2.2.3.A6',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.2.2.3.A9',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.2.2.3.A12',
        'cia': None,
        'gefahren': ['G 0.22', 'G 0.30']
    },
    {
        'id': 'SYS.2.2.3.A13',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.2.2.3.A14',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19']
    },
    {
        'id': 'SYS.2.2.3.A15',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.2.2.3.A16',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.28', 'G 0.29']
    },
    {
        'id': 'SYS.2.2.3.A17',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.2.2.3.A18',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.2.2.3.A19',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.2.2.3.A20',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.2.2.3.A21',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.19']
    },
    {
        'id': 'SYS.2.2.3.A22',
        'cia': 'CIA',
        'gefahren': ['G 0.22', 'G 0.30']
    },
    {
        'id': 'SYS.2.2.3.A23',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22']
    },
    {
        'id': 'SYS.2.2.3.A24',
        'cia': 'A',
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.37']
    },
    {
        'id': 'SYS.2.2.3.A25',
        'cia': 'CI',
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.36', 'G 0.37']
    },
    {
        'id': 'SYS.2.2.3.A26',
        'cia': 'A',
        'gefahren': ['G 0.18', 'G 0.22', 'G 0.29']
    },
    {
        'id': 'SYS.2.3.A1',
        'cia': None,
        'gefahren': ['G 0.31', 'G 0.32', 'G 0.37']
    },
    {
        'id': 'SYS.2.3.A2',
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.28']
    },
    {
        'id': 'SYS.2.3.A4',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.28']
    },
    {
        'id': 'SYS.2.3.A5',
        'cia': None,
        'gefahren': ['G 0.20', 'G 0.28', 'G 0.31', 'G 0.39']
    },
    {
        'id': 'SYS.2.3.A6',
        'cia': None,
        'gefahren': ['G 0.28', 'G 0.39']
    },
    {
        'id': 'SYS.2.3.A7',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.21', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'SYS.2.3.A8',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.21', 'G 0.22', 'G 0.28', 'G 0.30']
    },
    {
        'id': 'SYS.2.3.A9',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.2.3.A11',
        'cia': None,
        'gefahren': ['G 0.27']
    },
    {
        'id': 'SYS.2.3.A12',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.2.3.A14',
        'cia': 'CIA',
        'gefahren': ['G 0.23', 'G 0.28', 'G 0.30']
    },
    {
        'id': 'SYS.2.3.A15',
        'cia': 'CI',
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.2.3.A17',
        'cia': 'CI',
        'gefahren': ['G 0.28']
    },
    {
        'id': 'SYS.2.3.A18',
        'cia': 'CI',
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.23', 'G 0.28']
    },
    {
        'id': 'SYS.2.3.A19',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.19']
    },
    {
        'id': 'SYS.2.3.A20',
        'cia': 'CIA',
        'gefahren': ['G 0.30']
    },
    {
        'id': 'SYS.2.4.A1',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.2.4.A2',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.23', 'G 0.39']
    },
    {
        'id': 'SYS.2.4.A3',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.37']
    },
    {
        'id': 'SYS.2.4.A4',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19']
    },
    {
        'id': 'SYS.2.4.A5',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.28', 'G 0.39']
    },
    {
        'id': 'SYS.2.4.A6',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28', 'G 0.30']
    },
    {
        'id': 'SYS.2.4.A7',
        'cia': None,
        'gefahren': ['G 0.36']
    },
    {
        'id': 'SYS.2.4.A8',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.2.4.A9',
        'cia': None,
        'gefahren': ['G 0.39']
    },
    {
        'id': 'SYS.2.4.A10',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'SYS.2.4.A11',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.29']
    },
    {
        'id': 'SYS.2.4.A12',
        'cia': 'CIA',
        'gefahren': ['G 0.21', 'G 0.30']
    },
    {
        'id': 'SYS.2.5.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'SYS.2.5.A2',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.27', 'G 0.28', 'G 0.30', 'G 0.32', 'G 0.39']
    },
    {
        'id': 'SYS.2.5.A3',
        'cia': None,
        'gefahren': ['G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39']
    },
    {
        'id': 'SYS.2.5.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.27', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32']
    },
    {
        'id': 'SYS.2.5.A5',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.28', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'SYS.2.5.A6',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.31', 'G 0.45']
    },
    {
        'id': 'SYS.2.5.A7',
        'cia': None,
        'gefahren': ['G 0.27', 'G 0.30']
    },
    {
        'id': 'SYS.2.5.A8',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.39']
    },
    {
        'id': 'SYS.2.5.A9',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.28', 'G 0.31', 'G 0.39', 'G 0.45']
    },
    {
        'id': 'SYS.2.5.A10',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.32']
    },
    {
        'id': 'SYS.2.5.A11',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.28', 'G 0.31', 'G 0.39']
    },
    {
        'id': 'SYS.2.5.A12',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27', 'G 0.31', 'G 0.45']
    },
    {
        'id': 'SYS.2.5.A13',
        'cia': 'CI',
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.2.5.A14',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.23']
    },
    {
        'id': 'SYS.2.5.A15',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.27', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'SYS.2.5.A16',
        'cia': 'CIA',
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.32']
    },
    {
        'id': 'SYS.2.5.A17',
        'cia': 'CIA',
        'gefahren': ['G 0.28', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.39']
    },
    {
        'id': 'SYS.2.5.A18',
        'cia': 'A',
        'gefahren': ['G 0.25']
    },
    {
        'id': 'SYS.2.6.A1',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.18', 'G 0.27']
    },
    {
        'id': 'SYS.2.6.A2',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.28', 'G 0.30', 'G 0.31', 'G 0.36', 'G 0.45']
    },
    {
        'id': 'SYS.2.6.A3',
        'cia': None,
        'gefahren': ['G 0.28', 'G 0.31', 'G 0.36']
    },
    {
        'id': 'SYS.2.6.A4',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'SYS.2.6.A5',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.28', 'G 0.31']
    },
    {
        'id': 'SYS.2.6.A6',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.27']
    },
    {
        'id': 'SYS.2.6.A7',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.28', 'G 0.36']
    },
    {
        'id': 'SYS.2.6.A8',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.28', 'G 0.31', 'G 0.36']
    },
    {
        'id': 'SYS.2.6.A9',
        'cia': None,
        'gefahren': ['G 0.28', 'G 0.31', 'G 0.36', 'G 0.45']
    },
    {
        'id': 'SYS.2.6.A10',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'SYS.2.6.A11',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.36']
    },
    {
        'id': 'SYS.2.6.A12',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.27']
    },
    {
        'id': 'SYS.2.6.A13',
        'cia': 'CIA',
        'gefahren': ['G 0.23', 'G 0.36']
    },
    {
        'id': 'SYS.2.6.A14',
        'cia': 'A',
        'gefahren': ['G 0.28', 'G 0.36']
    },
    {
        'id': 'SYS.2.6.A15',
        'cia': 'A',
        'gefahren': ['G 0.9', 'G 0.45']
    },
    {
        'id': 'SYS.2.6.A16',
        'cia': 'CIA',
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.3.1.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'SYS.3.1.A3',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'SYS.3.1.A6',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'SYS.3.1.A7',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.31']
    },
    {
        'id': 'SYS.3.1.A8',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23']
    },
    {
        'id': 'SYS.3.1.A9',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.22', 'G 0.43']
    },
    {
        'id': 'SYS.3.1.A10',
        'cia': None,
        'gefahren': ['G 0.45']
    },
    {
        'id': 'SYS.3.1.A11',
        'cia': None,
        'gefahren': ['G 0.24', 'G 0.27']
    },
    {
        'id': 'SYS.3.1.A12',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.21']
    },
    {
        'id': 'SYS.3.1.A13',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19']
    },
    {
        'id': 'SYS.3.1.A14',
        'cia': None,
        'gefahren': ['G 0.16']
    },
    {
        'id': 'SYS.3.1.A15',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.3.1.A16',
        'cia': 'CI',
        'gefahren': ['G 0.18', 'G 0.31']
    },
    {
        'id': 'SYS.3.1.A17',
        'cia': 'A',
        'gefahren': ['G 0.4', 'G 0.16']
    },
    {
        'id': 'SYS.3.1.A18',
        'cia': 'CIA',
        'gefahren': ['G 0.16']
    },
    {
        'id': 'SYS.3.2.1.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.30', 'G 0.31']
    },
    {
        'id': 'SYS.3.2.1.A2',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19']
    },
    {
        'id': 'SYS.3.2.1.A3',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.23', 'G 0.31']
    },
    {
        'id': 'SYS.3.2.1.A4',
        'cia': None,
        'gefahren': ['G 0.30']
    },
    {
        'id': 'SYS.3.2.1.A5',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'SYS.3.2.1.A6',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.30']
    },
    {
        'id': 'SYS.3.2.1.A7',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.3.2.1.A8',
        'cia': None,
        'gefahren': ['G 0.28', 'G 0.30', 'G 0.39']
    },
    {
        'id': 'SYS.3.2.1.A9',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.45', 'G 0.46']
    },
    {
        'id': 'SYS.3.2.1.A10',
        'cia': None,
        'gefahren': ['G 0.16', 'G 0.17', 'G 0.18', 'G 0.30']
    },
    {
        'id': 'SYS.3.2.1.A11',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19']
    },
    {
        'id': 'SYS.3.2.1.A12',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.3.2.1.A13',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.30']
    },
    {
        'id': 'SYS.3.2.1.A16',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.3.2.1.A18',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.36']
    },
    {
        'id': 'SYS.3.2.1.A19',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19']
    },
    {
        'id': 'SYS.3.2.1.A22',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.18', 'G 0.22']
    },
    {
        'id': 'SYS.3.2.1.A25',
        'cia': 'CI',
        'gefahren': ['G 0.19', 'G 0.31']
    },
    {
        'id': 'SYS.3.2.1.A26',
        'cia': 'CIA',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22']
    },
    {
        'id': 'SYS.3.2.1.A27',
        'cia': 'CIA',
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.3.2.1.A28',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.31', 'G 0.39']
    },
    {
        'id': 'SYS.3.2.1.A29',
        'cia': 'CIA',
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.36']
    },
    {
        'id': 'SYS.3.2.1.A30',
        'cia': 'CIA',
        'gefahren': ['G 0.20', 'G 0.30', 'G 0.36']
    },
    {
        'id': 'SYS.3.2.1.A31',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.3.2.1.A32',
        'cia': None,
        'gefahren': ['G 0.30', 'G 0.31']
    },
    {
        'id': 'SYS.3.2.1.A33',
        'cia': None,
        'gefahren': ['G 0.31', 'G 0.39']
    },
    {
        'id': 'SYS.3.2.1.A34',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.22']
    },
    {
        'id': 'SYS.3.2.1.A35',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.23']
    },
    {
        'id': 'SYS.3.2.2.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29']
    },
    {
        'id': 'SYS.3.2.2.A2',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.3.2.2.A3',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.18', 'G 0.45']
    },
    {
        'id': 'SYS.3.2.2.A4',
        'cia': None,
        'gefahren': ['G 0.13', 'G 0.14', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.31', 'G 0.36', 'G 0.39']
    },
    {
        'id': 'SYS.3.2.2.A5',
        'cia': None,
        'gefahren': ['G 0.13', 'G 0.14', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.31', 'G 0.36', 'G 0.39']
    },
    {
        'id': 'SYS.3.2.2.A6',
        'cia': None,
        'gefahren': ['G 0.30', 'G 0.31', 'G 0.32', 'G 0.37']
    },
    {
        'id': 'SYS.3.2.2.A7',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.24', 'G 0.25', 'G 0.29', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.36', 'G 0.39']
    },
    {
        'id': 'SYS.3.2.2.A12',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30', 'G 0.32', 'G 0.38']
    },
    {
        'id': 'SYS.3.2.2.A14',
        'cia': 'CI',
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.28', 'G 0.30', 'G 0.36', 'G 0.39']
    },
    {
        'id': 'SYS.3.2.2.A17',
        'cia': 'I',
        'gefahren': ['G 0.29', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.37']
    },
    {
        'id': 'SYS.3.2.2.A19',
        'cia': 'CI',
        'gefahren': ['G 0.14']
    },
    {
        'id': 'SYS.3.2.2.A20',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.29', 'G 0.30', 'G 0.31', 'G 0.32']
    },
    {
        'id': 'SYS.3.2.2.A21',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.18', 'G 0.19', 'G 0.22', 'G 0.23', 'G 0.29', 'G 0.30', 'G 0.31', 'G 0.32', 'G 0.36', 'G 0.38']
    },
    {
        'id': 'SYS.3.2.2.A22',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.16', 'G 0.17', 'G 0.18', 'G 0.19', 'G 0.24', 'G 0.29', 'G 0.30', 'G 0.36', 'G 0.38']
    },
    {
        'id': 'SYS.3.2.2.A23',
        'cia': 'CI',
        'gefahren': ['G 0.16', 'G 0.21', 'G 0.22', 'G 0.29']
    },
    {
        'id': 'SYS.3.2.3.A1',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.29', 'G 0.30', 'G 0.32', 'G 0.37', 'G 0.38', 'G 0.41', 'G 0.46']
    },
    {
        'id': 'SYS.3.2.3.A2',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.14', 'G 0.19', 'G 0.29', 'G 0.36', 'G 0.38', 'G 0.46']
    },
    {
        'id': 'SYS.3.2.3.A7',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.30', 'G 0.32', 'G 0.35', 'G 0.37', 'G 0.38', 'G 0.41', 'G 0.46']
    },
    {
        'id': 'SYS.3.2.3.A12',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.19', 'G 0.32', 'G 0.35', 'G 0.36', 'G 0.37', 'G 0.41', 'G 0.42', 'G 0.46']
    },
    {
        'id': 'SYS.3.2.3.A13',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.26', 'G 0.28', 'G 0.29', 'G 0.30', 'G 0.32', 'G 0.36', 'G 0.37', 'G 0.38', 'G 0.41', 'G 0.42', 'G 0.46']
    },
    {
        'id': 'SYS.3.2.3.A14',
        'cia': None,
        'gefahren': ['G 0.9', 'G 0.11', 'G 0.14', 'G 0.16', 'G 0.19', 'G 0.23', 'G 0.29']
    },
    {
        'id': 'SYS.3.2.3.A15',
        'cia': None,
        'gefahren': ['G 0.11', 'G 0.19', 'G 0.29', 'G 0.46']
    },
    {
        'id': 'SYS.3.2.3.A17',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.16', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.32', 'G 0.36', 'G 0.46']
    },
    {
        'id': 'SYS.3.2.3.A18',
        'cia': None,
        'gefahren': ['G 0.26', 'G 0.28']
    },
    {
        'id': 'SYS.3.2.3.A21',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.21', 'G 0.25', 'G 0.26', 'G 0.28', 'G 0.32', 'G 0.39', 'G 0.41', 'G 0.46']
    },
    {
        'id': 'SYS.3.2.3.A23',
        'cia': 'CI',
        'gefahren': ['G 0.11', 'G 0.16', 'G 0.27', 'G 0.30']
    },
    {
        'id': 'SYS.3.2.3.A25',
        'cia': 'CI',
        'gefahren': ['G 0.16', 'G 0.19', 'G 0.29', 'G 0.35', 'G 0.46']
    },
    {
        'id': 'SYS.3.2.3.A26',
        'cia': 'CI',
        'gefahren': ['G 0.11', 'G 0.14', 'G 0.16', 'G 0.19', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.28', 'G 0.29', 'G 0.30', 'G 0.32', 'G 0.35', 'G 0.36', 'G 0.38', 'G 0.39', 'G 0.41', 'G 0.42', 'G 0.46']
    },
    {
        'id': 'SYS.3.2.4.A2',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.21', 'G 0.32', 'G 0.41', 'G 0.46']
    },
    {
        'id': 'SYS.3.2.4.A3',
        'cia': None,
        'gefahren': ['G 0.30', 'G 0.32', 'G 0.38']
    },
    {
        'id': 'SYS.3.2.4.A5',
        'cia': None,
        'gefahren': ['G 0.30']
    },
    {
        'id': 'SYS.3.3.A1',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.19', 'G 0.22', 'G 0.27', 'G 0.31']
    },
    {
        'id': 'SYS.3.3.A2',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.23', 'G 0.29']
    },
    {
        'id': 'SYS.3.3.A3',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.16', 'G 0.19', 'G 0.27', 'G 0.29', 'G 0.31']
    },
    {
        'id': 'SYS.3.3.A4',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.16', 'G 0.17', 'G 0.19', 'G 0.29']
    },
    {
        'id': 'SYS.3.3.A5',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.22']
    },
    {
        'id': 'SYS.3.3.A6',
        'cia': None,
        'gefahren': ['G 0.31']
    },
    {
        'id': 'SYS.3.3.A7',
        'cia': None,
        'gefahren': ['G 0.27']
    },
    {
        'id': 'SYS.3.3.A8',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.22', 'G 0.23']
    },
    {
        'id': 'SYS.3.3.A9',
        'cia': 'A',
        'gefahren': ['G 0.25', 'G 0.27']
    },
    {
        'id': 'SYS.3.3.A10',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.15', 'G 0.22', 'G 0.23']
    },
    {
        'id': 'SYS.3.3.A11',
        'cia': None,
        'gefahren': ['G 0.25']
    },
    {
        'id': 'SYS.3.3.A12',
        'cia': None,
        'gefahren': ['G 0.27']
    },
    {
        'id': 'SYS.3.3.A13',
        'cia': 'C',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.29']
    },
    {
        'id': 'SYS.3.3.A14',
        'cia': 'C',
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.29']
    },
    {
        'id': 'SYS.3.3.A15',
        'cia': 'C',
        'gefahren': ['G 0.14', 'G 0.15']
    },
    {
        'id': 'SYS.4.1.A1',
        'cia': None,
        'gefahren': ['G 0.16', 'G 0.18']
    },
    {
        'id': 'SYS.4.1.A2',
        'cia': None,
        'gefahren': ['G 0.16', 'G 0.19', 'G 0.21']
    },
    {
        'id': 'SYS.4.1.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.30']
    },
    {
        'id': 'SYS.4.1.A5',
        'cia': None,
        'gefahren': ['G 0.31']
    },
    {
        'id': 'SYS.4.1.A7',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.4.1.A11',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.4.1.A14',
        'cia': 'CIA',
        'gefahren': ['G 0.19', 'G 0.30']
    },
    {
        'id': 'SYS.4.1.A15',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19', 'G 0.22']
    },
    {
        'id': 'SYS.4.1.A16',
        'cia': 'A',
        'gefahren': ['G 0.25']
    },
    {
        'id': 'SYS.4.1.A17',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.4.1.A18',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.22']
    },
    {
        'id': 'SYS.4.1.A20',
        'cia': 'C',
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.4.1.A21',
        'cia': 'CIA',
        'gefahren': ['G 0.18', 'G 0.21']
    },
    {
        'id': 'SYS.4.1.A22',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.4.3.A1',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.29', 'G 0.31']
    },
    {
        'id': 'SYS.4.3.A2',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.4.3.A3',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.23', 'G 0.25', 'G 0.26', 'G 0.30', 'G 0.37']
    },
    {
        'id': 'SYS.4.3.A4',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.20']
    },
    {
        'id': 'SYS.4.3.A5',
        'cia': None,
        'gefahren': ['G 0.4', 'G 0.25']
    },
    {
        'id': 'SYS.4.3.A6',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.30']
    },
    {
        'id': 'SYS.4.3.A7',
        'cia': None,
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.23', 'G 0.24']
    },
    {
        'id': 'SYS.4.3.A8',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.20', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.28', 'G 0.46']
    },
    {
        'id': 'SYS.4.3.A9',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.46']
    },
    {
        'id': 'SYS.4.3.A10',
        'cia': None,
        'gefahren': ['G 0.25', 'G 0.31']
    },
    {
        'id': 'SYS.4.3.A11',
        'cia': None,
        'gefahren': ['G 0.15', 'G 0.19']
    },
    {
        'id': 'SYS.4.3.A12',
        'cia': 'CIA',
        'gefahren': ['G 0.4', 'G 0.18', 'G 0.20', 'G 0.21', 'G 0.22', 'G 0.30']
    },
    {
        'id': 'SYS.4.3.A13',
        'cia': 'CIA',
        'gefahren': ['G 0.15', 'G 0.20', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.28', 'G 0.46']
    },
    {
        'id': 'SYS.4.3.A14',
        'cia': 'CI',
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.30', 'G 0.39']
    },
    {
        'id': 'SYS.4.3.A15',
        'cia': 'CI',
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.39']
    },
    {
        'id': 'SYS.4.3.A16',
        'cia': 'CI',
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.24', 'G 0.31']
    },
    {
        'id': 'SYS.4.3.A17',
        'cia': 'IA',
        'gefahren': ['G 0.21', 'G 0.22', 'G 0.25', 'G 0.26', 'G 0.46']
    },
    {
        'id': 'SYS.4.3.A18',
        'cia': 'C',
        'gefahren': ['G 0.15', 'G 0.21', 'G 0.46']
    },
    {
        'id': 'SYS.4.4.A1',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.30']
    },
    {
        'id': 'SYS.4.4.A2',
        'cia': None,
        'gefahren': ['G 0.30']
    },
    {
        'id': 'SYS.4.4.A5',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23']
    },
    {
        'id': 'SYS.4.4.A6',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.4.4.A7',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.4.4.A8',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.28']
    },
    {
        'id': 'SYS.4.4.A9',
        'cia': None,
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.4.4.A10',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.18', 'G 0.19', 'G 0.21', 'G 0.23', 'G 0.25', 'G 0.28', 'G 0.30', 'G 0.38', 'G 0.39', 'G 0.40']
    },
    {
        'id': 'SYS.4.4.A11',
        'cia': None,
        'gefahren': ['G 0.16']
    },
    {
        'id': 'SYS.4.4.A13',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19', 'G 0.23', 'G 0.28']
    },
    {
        'id': 'SYS.4.4.A15',
        'cia': None,
        'gefahren': ['G 0.30']
    },
    {
        'id': 'SYS.4.4.A16',
        'cia': None,
        'gefahren': ['G 0.39']
    },
    {
        'id': 'SYS.4.4.A17',
        'cia': None,
        'gefahren': ['G 0.23']
    },
    {
        'id': 'SYS.4.4.A18',
        'cia': None,
        'gefahren': ['G 0.37']
    },
    {
        'id': 'SYS.4.4.A19',
        'cia': None,
        'gefahren': ['G 0.23', 'G 0.28', 'G 0.30']
    },
    {
        'id': 'SYS.4.4.A20',
        'cia': None,
        'gefahren': ['G 0.18', 'G 0.19', 'G 0.45']
    },
    {
        'id': 'SYS.4.4.A21',
        'cia': 'I',
        'gefahren': ['G 0.2', 'G 0.4', 'G 0.8', 'G 0.16', 'G 0.18']
    },
    {
        'id': 'SYS.4.4.A22',
        'cia': 'A',
        'gefahren': ['G 0.18', 'G 0.40']
    },
    {
        'id': 'SYS.4.4.A23',
        'cia': 'CIA',
        'gefahren': ['G 0.18']
    },
    {
        'id': 'SYS.4.4.A24',
        'cia': 'CIA',
        'gefahren': ['G 0.23']
    },
    {
        'id': 'SYS.4.5.A1',
        'cia': None,
        'gefahren': ['G 0.2', 'G 0.4', 'G 0.16', 'G 0.17', 'G 0.21', 'G 0.22', 'G 0.23', 'G 0.29']
    },
    {
        'id': 'SYS.4.5.A2',
        'cia': None,
        'gefahren': ['G 0.16', 'G 0.21']
    },
    {
        'id': 'SYS.4.5.A4',
        'cia': None,
        'gefahren': ['G 0.19', 'G 0.22', 'G 0.39']
    },
    {
        'id': 'SYS.4.5.A5',
        'cia': None,
        'gefahren': ['G 0.16', 'G 0.17', 'G 0.19']
    },
    {
        'id': 'SYS.4.5.A6',
        'cia': None,
        'gefahren': ['G 0.2', 'G 0.4', 'G 0.17']
    },
    {
        'id': 'SYS.4.5.A7',
        'cia': None,
        'gefahren': ['G 0.19']
    },
    {
        'id': 'SYS.4.5.A10',
        'cia': None,
        'gefahren': ['G 0.14', 'G 0.19']
    },
    {
        'id': 'SYS.4.5.A11',
        'cia': 'I',
        'gefahren': ['G 0.22', 'G 0.46']
    },
    {
        'id': 'SYS.4.5.A12',
        'cia': None,
        'gefahren': ['G 0.39']
    },
    {
        'id': 'SYS.4.5.A13',
        'cia': None,
        'gefahren': ['G 0.17', 'G 0.19']
    },
    {
        'id': 'SYS.4.5.A14',
        'cia': 'CIA',
        'gefahren': ['G 0.2', 'G 0.4', 'G 0.17']
    },
    {
        'id': 'SYS.4.5.A15',
        'cia': 'CIA',
        'gefahren': ['G 0.20']
    },
    {
        'id': 'SYS.4.5.A16',
        'cia': 'CI',
        'gefahren': ['G 0.39']
    },
    {
        'id': 'SYS.4.5.A17',
        'cia': None,
        'gefahren': ['G 0.46']
    }
]
