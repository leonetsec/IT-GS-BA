import argparse
import os
import shutil
import re
import docx2pdf
import openpyxl
import openpyxl.utils
import pandas as pd
import numpy as np
from datetime import datetime
from io import BytesIO
from openpyxl.worksheet.datavalidation import DataValidation
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import Paragraph, SimpleDocTemplate, Image, Table, TableStyle, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from collections import defaultdict
from docx import Document
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
import duckdb
import string

import mapping

FILENAME_PATTERN = re.compile(r"(?<=\bCheckliste[_\s])([A-Z]{3,4}(?:\.[0-9]+){1,3})(?:.*?)?(?=\.xlsx$)")

# Gibt zurück, ob eine Datei dem Format der Checkliste entspricht
def is_format(filename):
    if filename.endswith('.xlsx') and "Checkliste" in filename:
        return True
    else: return False

# Gibt den Namen eines Bausteins anhand des Dateinamens zurück, entweder kurz "APP.1.1" oder lang "Office Produkte"
def get_name(filename, short):
    if is_format(filename):
        match = FILENAME_PATTERN.search(filename)
        if match:
            ref = match.group(1)
            if short:
                return ref
            return mapping.bsi_ref_titles.get(ref, "Unbekanntes Kürzel")
        return None

    elif is_pdf(filename):
        ref = filename.split()[0]
        if ref.startswith("CCON"):
            ref = "CON" + ref[4:]
        if short:
            return ref
        return mapping.bsi_ref_titles.get(ref, "Unbekanntes Kürzel")
    return None

# Überprüft, ob eine PDF-Datei den Namen eines IT-Grundschutz-Bausteins hat
def is_pdf(file):
    if file.endswith(".pdf") or file.endswith(".pdf.clean"):
        split = file.split()
        if split:
            ref = split[0]
            if ref.startswith("CCON"):
                ref = "CON" + ref[4:]
            if ref in mapping.bsi_ref_titles:
                return True
    return False

# Überprüft, ob eine DOCX-Datei den Namen eines IT-Grundschutz-Bausteins hat
def is_docx(file):
    if file.endswith(".docx"):
        split = file.split()
        if split:
            ref = split[0]
            if ref.startswith("CCON"):
                ref = "CON" + ref[4:]
            if ref in mapping.bsi_ref_titles:
                return True
    return False

# Ordnet den Tabellen ihren Namen zu
def map_xlsx_files(path):
    if os.path.isfile(path):
        file_name = os.path.basename(path)
        mapped_name = get_name(file_name, False)
        print(f"{file_name} → {mapped_name if mapped_name else 'Keine Zuordnung gefunden'}")
    elif os.path.isdir(path):
        for filename in os.listdir(path):
            mapped_name = get_name(filename, False)
            print(f"{filename} → {mapped_name if mapped_name else 'Keine Zuordnung gefunden'}")
    else: print("Datei oder Ordner nicht gefunden")

# Lädt Exceldateien und überspringt Metadaten
def load_data(file_path):
    sheet_name = get_name(file_path, True)
    try:
        return pd.read_excel(file_path, sheet_name=sheet_name, skiprows=4)
    except PermissionError:
        print(f"Fehler: Die Datei {get_name(file_path, True)} ist möglicherweise geöffnet und kann nicht gelesen werden. Vorgang wird abgebrochen.")
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist beim Öffnen der Datei {file_path} aufgetreten: {e}")
    exit(1)

# Entfernt Anforderungen, bei denen eine spezifische Bedingung erfüllt ist, z.B. "Titel" ist "ENTFALLEN"
def remove_specific_requirements(df, where, is_value):
    return df[df[where] != is_value]

# Gibt Dataframe zurück, bei dem die Zeile leer oder ein bestimmter Wert ist
def get_specific_df_with_emptiness(df, column, value):
    return df[(df[column].isna() | (df[column].fillna('').str.strip().str.lower() == value))]

# Gibt Dataframe zurück, bei dem die Zeile ein bestimmter Wert ist
def get_specific_df(df, column, value):
    return df[(df[column].fillna('').str.strip().str.lower() == value)]

# Gibt Dataframe zurück, bei dem zwei Zeilen entweder leer sind oder einen bestimmten Wert haben
def get_specific_df_with_two_conditions_and_emptiness(df, column, value, column2, value2):
    return df[(df[column].isna() | (df[column].fillna('').str.strip().str.lower() == value.lower())) & (df[column2].isna() | (df[column2].fillna('').str.strip().str.lower() == value2.lower()))]

# Gibt Zahlen zurück, wie viele Anforderungen entbehrlich sowie nicht, teilweise oder ganz erfüllt sind
def implementation_count(df):
    not_implemented = get_specific_df_with_two_conditions_and_emptiness(df, "Umsetzung", "nein", "Entbehrlich", "nein")
    partly_implemented = df[df["Umsetzung"].fillna("").astype(str).str.strip().str.lower() == "teilweise"]
    fully_implemented = df[df["Umsetzung"].fillna("").astype(str).str.strip().str.lower() == "ja"]
    unnecessary = df[df["Entbehrlich"].fillna("").astype(str).str.strip().str.lower() == "ja"]
    return len(not_implemented), len(partly_implemented), len(fully_implemented), len(unnecessary)

# Summiert die Kostenspalte
def cost_count(df):
    df["Kostenschätzung_cleaned"] = df["Kostenschätzung"].astype(str).str.replace('€', '').str.replace(',', '.').str.findall(r'\d+\.?\d*').str[0]
    df["Kostenschätzung_cleaned"] = pd.to_numeric(df["Kostenschätzung_cleaned"], errors='coerce')
    return df["Kostenschätzung_cleaned"].fillna(0).sum()

# Zählt wie viele Basis, Standard und erhöhte Schutzbedarfsanforderungen vorliegen
def type_count(df):
    basis = df[df["Typ"] == "Basis"]
    standard = df[df["Typ"] == "Standard"]
    high = df[df["Typ"] == "Hoch"]
    return len(basis), len(standard), len(high)

# Gibt einzelne Dataframes für verschiedene Schutzbedarfstypen zurück
def get_type_dfs(df):
    basis = df[df["Typ"] == "Basis"]
    standard = df[df["Typ"] == "Standard"]
    high = df[df["Typ"] == "Hoch"]
    return basis, standard, high

# Gibt Verantwortliche zurück
def get_responsible(df):
    return set(df["Verantwortlich"].dropna().unique())

# Gibt eine Prozentzahl an bisher umgesetzten Anforderungen zurück
def get_percentage_missing(df):
    df = df[["Titel", "Typ", "Entbehrlich", "Umsetzung"]]
    df = remove_specific_requirements(df, "Titel", "ENTFALLEN")
    not_implemented, partly_implemented, fully_implemented, unnecessary = implementation_count(df)
    total = not_implemented + partly_implemented + fully_implemented
    return (fully_implemented / total) * 100

# Färbt Prozentzahl ein
def get_colored_percentage(percentage):
    if percentage < 50:
        color = "\033[41m"  # Roter Hintergrund
    elif percentage < 75:
        color = "\033[43m"  # Gelber Hintergrund
    else:
        color = "\033[42m"  # Grüner Hintergrund

    reset = "\033[0m"  # Reset der Farbe
    return f"{color} {percentage:.2f}% {reset}"

# Analysiert eine Tabelle nach diversen Aspekten
def analyze_single_file(file_path):
    if not is_format(file_path):
        print("Keine Datei im Format Checkliste_XXX.X.X.xlsx")
        return
    df = load_data(file_path)

    # Relevante Spalten auswählen
    df = df[["ID-Anforderung", "Titel", "Inhalt", "Typ", "Entbehrlich", "Begründung für Entbehrlichkeit", "Umsetzung", "Umsetzung bis", "Verantwortlich", "Bemerkungen / Begründung für Nicht-Umsetzung", "Kostenschätzung"]]

    # Entfallene Anforderungen entfernen
    df = remove_specific_requirements(df, "Titel", "ENTFALLEN")

    # Analyse Dataframes
    not_implemented, partly_implemented, fully_implemented, unnecessary = implementation_count(df)
    cost = cost_count(df)
    all_responsibles = f"{', '.join(get_responsible(df))}"

    # Analyse nicht umgesetzter Anforderungen nach Typ
    ni = get_specific_df_with_two_conditions_and_emptiness(df, "Umsetzung", "nein", "Entbehrlich", "nein")
    ni_basis, ni_standard, ni_high = type_count(ni)

    # Analyse elementarer Gefährdungen
    covered_risks, covered_cia = risk_analysis(file_path)

    # Statistik ausgeben
    print(f"Gesamtanzahl Anforderungen: {len(df)}")
    print(f"Umgesetzte Anforderungen: {fully_implemented}")
    print(f"Teilweise umgesetzte Anforderungen: {partly_implemented}")
    print(f"Entbehrliche Anforderungen: {unnecessary}")
    print(f"Nicht umgesetzte Anforderungen: {not_implemented}")
    print(f"(davon Basis: {ni_basis}, Standard: {ni_standard}, Erhöhter Schutzbedarf: {ni_high})")
    print(f"Summierte Kostenschätzung: {cost}€")
    print(f"Verantwortliche: {all_responsibles}")
    print(f"(Teilweise) abgedeckte elementare Gefährdungen: {len(covered_risks)}/47")
    print(f"(Teilweise) abgedeckte Schutzziele: {len(covered_cia)}/3")


# Analysiere alle Tabellen nach diversen Aspekten
def analyze_all_files(folder_path):
    total_files = 0
    total_df_count = 0
    total_fully_implemented = 0
    total_partly_implemented = 0
    total_unnecessary = 0
    total_not_implemented = 0
    total_cost = 0
    total_basis = 0
    total_standard = 0
    total_high = 0
    total_risks = set()
    total_cia = set()

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if is_format(file_path):
            total_files += 1
            df = load_data(file_path)

            # Relevante Spalten auswählen
            df = df[["Titel", "Typ", "Entbehrlich", "Umsetzung", "Kostenschätzung"]]

            # Entfallene Anforderungen entfernen
            df = remove_specific_requirements(df, "Titel", "ENTFALLEN")

            # Analyse Dataframes
            not_implemented, partly_implemented, fully_implemented, unnecessary = implementation_count(df)
            cost = cost_count(df)

            # Analyse nicht umgesetzter Anforderungen nach Typ
            ni = get_specific_df_with_two_conditions_and_emptiness(df, "Umsetzung", "nein", "Entbehrlich", "nein")
            ni_basis, ni_standard, ni_high = type_count(ni)

            # Analyse elementarer Gefährdungen
            covered_risks, covered_cia = risk_analysis(file_path)

            # Analyse den Gesamtzählern hinzufügen
            total_df_count += len(df)
            total_fully_implemented += fully_implemented
            total_partly_implemented += partly_implemented
            total_unnecessary += unnecessary
            total_not_implemented += not_implemented
            total_cost += cost
            total_basis += ni_basis
            total_standard += ni_standard
            total_high += ni_high
            total_risks.update(covered_risks)
            total_cia.update(covered_cia)
    if total_files == 0:
        print("Keine Dateien im Format Checkliste_XXX.X.X.xlsx gefunden")
        return
    total_risks_num = len(total_risks)
    total_cia_num = len(total_cia)

    print(f"Analysierte Tabellen: {total_files}")
    print(f"Gesamtanzahl Anforderungen: {total_df_count}")
    print(f"Umgesetzte Anforderungen: {total_fully_implemented}")
    print(f"Teilweise umgesetzte Anforderungen: {total_partly_implemented}")
    print(f"Entbehrliche Anforderungen: {total_unnecessary}")
    print(f"Nicht umgesetzte Anforderungen: {total_not_implemented}")
    print(f"(davon Basis: {total_basis}, Standard: {total_standard}, Erhöhter Schutzbedarf: {total_high})")
    print(f"Summierte Kostenschätzung: {total_cost}€")
    print(f"(Teilweise) abgedeckte elementare Gefährdungen: {(total_risks_num)}/47")
    print(f"(Teilweise) abgedeckte Schutzziele: {total_cia_num}/3")

# Behandelt die Prozentzahl an umgesetzten Anforderungen für eine Datei oder einen Ordner
def percentages(path):
    if os.path.isfile(path) and is_format(path):
        df = load_data(path)
        df = df[["Titel", "Typ", "Entbehrlich", "Umsetzung"]]
        df = remove_specific_requirements(df, "Titel", "ENTFALLEN")
        percentage = get_percentage_missing(df)
        print(f"Insgesamt vollständig erfüllte Anforderungen von {get_name(path, True)}: {percentage:.2f}%")

        df_basis, df_standard, df_high = get_type_dfs(df)
        basis_missing = get_percentage_missing(df_basis)
        standard_missing = get_percentage_missing(df_standard)
        high_missing = get_percentage_missing(df_high)
        print(f"Basis-Anforderungen: {basis_missing:.2f}%")
        print(f"Standard-Anforderungen: {standard_missing:.2f}%")
        print(f"Anforderungen des erhöhten Schutzbedarfs: {high_missing:.2f}%")

    # Funktioniert nicht mit altem Windows cmd
    elif os.path.isdir(path):
        print("Baustein → Prozent erfüllt")
        for file_name in os.listdir(path):
            file_path = os.path.join(path, file_name)
            if is_format(file_path):
                df = load_data(file_path)
                df = df[["Titel", "Typ", "Entbehrlich", "Umsetzung"]]
                df = remove_specific_requirements(df, "Titel", "ENTFALLEN")
                percentage = get_percentage_missing(df)
                print(f"{get_name(file_name, True)} → {get_colored_percentage(percentage)}")
    else: print("Datei oder Ordner nicht gefunden")

# Behandelt die IT-Grundschutz-Profilauswahl und führt den Verschiebungsprozess von Dateien durch
def profile_handler(file_or_dir):
    if os.path.isdir(file_or_dir):

        print("Folgende IT-Grundschutz-Profile stehen zur Verfügung (auch auf PDFs anwendbar):")
        for key, value in mapping.profile_names.items():
            print(f"{key}: {value}")
        print("Wähle mit der Zahl aus. Hinweis: Es werden nur die Bausteine, die auf jeden Fall ausgeschlossen sind, verschoben.\nManche Profile besitzen außerdem zusätzliche Bausteine, die hiermit nicht installiert werden.")
        user_input = input("Auswahl (oder exit): ").strip()
        if user_input.lower() == "exit":
            print("Abgebrochen")

        else:
            if user_input in mapping.profiles_mapping:
                profile_name = mapping.profiles_mapping[user_input]
                profile = getattr(mapping, profile_name)
            else:
                print("Ungültige Eingabe")
                return

            target_dir = os.path.join(file_or_dir, "Nach Profil nicht benötigt")
            os.makedirs(target_dir, exist_ok=True)

            for file in os.listdir(file_or_dir):
                if is_format(file) or is_pdf(file):
                    file_path = os.path.join(file_or_dir, file)
                    file_short = get_name(file, True)
                    if file_short not in profile and file_short in mapping.bsi_ref_titles:
                        shutil.move(file_path, os.path.join(target_dir, file))
                        print(f"{get_name(file, True)}: {get_name(file, False)} wurde entfernt")

    else: print("Verzeichnis nicht gefunden")

# Setzt leere Standard- oder erhöhte Schutzbedarfsanforderungen auf entbehrlich
def ignore_empty_requirements(file_path, column, value, second_empty_no_type, fully):
    df = load_data(file_path)

    if not fully:
        mask = (df[column] == value) & (df["Entbehrlich"].isna()) & (df[second_empty_no_type].isna())
    else:
        mask = (df[column] == value) & (df["Entbehrlich"].isna())

    wb = openpyxl.load_workbook(file_path)
    sheet_name = get_name(file_path, True)
    ws = wb[sheet_name]

    for idx in df[mask].index:
        excel_row = idx + 6
        col_letter = openpyxl.utils.get_column_letter(df.columns.get_loc("Entbehrlich") + 1)
        ws[f"{col_letter}{excel_row}"].value = "Ja"

        bemerkung_col = openpyxl.utils.get_column_letter(df.columns.get_loc("Begründung für Entbehrlichkeit") + 1)
        if ws[f"{bemerkung_col}{excel_row}"].value:
            ws[f"{bemerkung_col}{excel_row}"].value += f"- Alle Anforderungen des Typs {value} auf Entbehrlich gesetzt"
        else:
            ws[f"{bemerkung_col}{excel_row}"].value = f"Alle Anforderungen des Typs {value} auf Entbehrlich gesetzt"

    wb.save(file_path)

# Handler für Datei oder Ordner
def ignore_empty_requirements_handler(path, column, value, second_empty_type, fully):
    if os.path.isdir(path):
        for file in os.listdir(path):
            if is_format(file):
                file_path = os.path.join(path, file)
                ignore_empty_requirements(file_path, column, value, second_empty_type, fully)
        if not fully:
            print(f"Alle leeren {value}-Anforderungen aus {path} wurden auf entbehrlich gesetzt und gespeichert.")
        else:
            print(f"Alle {value}-Anforderungen aus {path} wurden auf entbehrlich gesetzt und gespeichert.")
    elif os.path.isfile(path) and is_format(path):
        ignore_empty_requirements(path, column, value, second_empty_type, fully)
        if not fully:
            print(f"Alle leeren {value}-Anforderungen von {get_name(path, True)} wurden auf entbehrlich gesetzt und gespeichert.")
        else:
            print(f"Alle {value}-Anforderungen von {get_name(path, True)} wurden auf entbehrlich gesetzt und gespeichert.")
    else: print("Keine Datei(en) mit passendem Format gefunden")

# Sortiert Dateien nach verschiedenen Kriterien
def sort_list(directory):
    if not os.path.isdir(directory):
        print("Ordner nicht gefunden")
        return

    print("Die Dateien können nach folgendem Kriterien absteigend sortiert werden:")
    for key, value in mapping.sort_list.items():
        print(f"{key}: {value}")
    print("Wähle mit der Zahl aus.")
    user_input = input("Auswahl (oder exit): ").strip()
    if user_input.lower() == "exit":
        print("Abgebrochen")

    if user_input not in mapping.sort_list:
        print("Ungültige Auswahl")
        return

    files_data = []

    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if is_format(file_name):
            df = load_data(file_path)
            df = df[["Titel", "Typ", "Entbehrlich", "Umsetzung", "Umsetzung bis", "Verantwortlich", "Kostenschätzung"]]
            df = remove_specific_requirements(df, "Titel", "ENTFALLEN")

            not_implemented, partly_implemented, fully_implemented, unnecessary = implementation_count(df)
            not_unnecessary = len(df[df["Entbehrlich"].fillna("").astype(str).str.strip().str.lower() == "nein"])
            cost = cost_count(df)
            percentage = get_percentage_missing(df)
            due_date = ", ".join(sorted(list(map(format_dates, df["Umsetzung bis"].dropna().unique()))))
            ni = get_specific_df_with_two_conditions_and_emptiness(df, "Umsetzung", "nein", "Entbehrlich", "nein")
            ni_basis, ni_standard, ni_high = type_count(ni)

            files_data.append({
                "file": file_name,
                "1": not_implemented + partly_implemented,
                "2": not_implemented,
                "3": fully_implemented,
                "4": ni_basis,
                "5": ni_standard,
                "6": ni_high,
                "7": ni_basis + ni_standard,
                "8": partly_implemented,
                "9": percentage,
                "10": unnecessary,
                "11": not_unnecessary,
                "12": cost,
                "13": get_responsible(df),
                "14": len(df),
                "15": due_date
            })

    if not files_data:
        print("Keine passenden Dateien gefunden")
        return

    sort_key = user_input
    files_data.sort(key=lambda x: x[sort_key], reverse=True)

    print(f"Dateien sortiert nach {mapping.sort_list[sort_key]}:\n")
    for item in files_data:
        print(f"{get_name(item['file'], True)}: {item[sort_key]}")

# Erkennt WiBA-Anforderungen anhand des Textes in einer Datei und setzt sie auf umgesetzt
def wiba_setter(file_path):
    wiba = mapping.wiba
    wiba_ids = mapping.wiba_id
    df = load_data(file_path)

    wiba_mapping = {w: i for i, w in enumerate(wiba)}

    id_status = id_check(file_path)
    if id_status == 1:
        ids = df["ID-Anforderung"]
    elif id_status == 2:
        ids = pd.Series([req_id[:-1] for req_id in df["ID-Anforderung"]])
    else:
        print(f"Sowohl eindeutige als auch nicht eindeutige IDs in {file_path} gefunden, eventuell können nicht alle WiBA-Anforderungen zugeordnet werden")
        ids = df["ID-Anforderung"]

    # Überprüfung, ob Inhalt und ID gleich sind, da der Inhalt einiger Anforderungen doppelt vorkommt
    mask = (
            df["Inhalt"].isin(wiba) &
            ids.isin(wiba_ids) &
            df["Inhalt"].map(wiba_mapping).notna() &
            (ids == df["Inhalt"].map(
                lambda x: wiba_ids[wiba_mapping[x]] if x in wiba_mapping else None)) &
            df["Umsetzung"].isna()
    )

    # Falls keine Änderungen abbrechen
    if not mask.any():
        return 0

    wb = openpyxl.load_workbook(file_path)
    sheet_name = get_name(file_path, True)
    ws = wb[sheet_name]

    for idx in df[mask].index:
        excel_row = idx + 6
        umsetzung_col = openpyxl.utils.get_column_letter(df.columns.get_loc("Umsetzung") + 1)
        bemerkung_col = openpyxl.utils.get_column_letter(df.columns.get_loc("Bemerkungen / Begründung für Nicht-Umsetzung") + 1)

        ws[f"{umsetzung_col}{excel_row}"].value = "Ja"
        if ws[f"{bemerkung_col}{excel_row}"].value:
            ws[f"{bemerkung_col}{excel_row}"].value += "- WiBA Integration"
        else:
            ws[f"{bemerkung_col}{excel_row}"].value = "WiBA Integration"
    wb.save(file_path)
    return 1

# Handler für Datei oder Ordner
def wiba_transfer(path):
    if os.path.isfile(path) and is_format(path):
        print("Starte WiBA Integration")
        wiba_setter(path)
        print(f"WiBA erfolgreich in {get_name(path, True)} integriert")
    elif os.path.isdir(path):
        print("Starte WiBA Integration")
        temp = 0
        for file_name in os.listdir(path):
            file_path = os.path.join(path, file_name)
            if is_format(file_name):
                temp += wiba_setter(file_path)
        if temp:
            print(f"WiBA erfolgreich in {temp} Dateien integriert")
        else: print("Keine Dateien im Ordner, die auch in WiBA vorkommen")
    else: print("Datei oder Ordner nicht gefunden")

# Handler für Datei oder Ordner
def scale_setter_handler(file_or_dir):
    user_choice = input("Möchten Sie eine eigene Skala angeben? (ja/Nein) Sonst wird der im Code definierte Default verwendet: ").strip().lower()
    values = None
    if user_choice == "ja":
        num_values = int(input("Wie viele Werte? ").strip())
        values_list = []

        for i in range(num_values):
            value = input(f"Geben Sie Wert {i+1} ein: ").strip()
            values_list.append(f"{value}")
        values = '"' + ", ".join(values_list) + '"'
        print("Starte Modifikation...")
    else: print("Default Skala verwendet. Starte Modifikation...")

    if os.path.isfile(file_or_dir) and is_format(file_or_dir):
        scale_setter(file_or_dir, values)
        print(f"{file_or_dir} modifiziert und gespeichert!")
    elif os.path.isdir(file_or_dir):
        for file_name in os.listdir(file_or_dir):
            file_path = os.path.join(file_or_dir, file_name)
            if is_format(file_name):
                scale_setter(file_path, values)
        print(f"Alle Dateien in {file_or_dir} modifiziert und gespeichert!")
    else: print("Keine Datei gefunden")

# Ändert die Skala der Umsetzung in einer Tabelle
def scale_setter(file_path, values):
    df = load_data(file_path)
    cell_max = len(df) + 5
    if values is None:
        values = '"Ja, Teilweise, Nein"'

    wb = openpyxl.load_workbook(file_path)
    sheet_name = get_name(file_path, True)
    sheet = wb[sheet_name]

    new_validations = []

    # Entfernt bestehende Skala
    for dv in sheet.data_validations.dataValidation:
        if any("H" in str(rng) for rng in dv.ranges):
            continue
        new_validations.append(dv)  # Behalte die anderen Validierungen

    sheet.data_validations.dataValidation = new_validations

    rule = DataValidation(type="list", formula1=values, allow_blank=True)

    sheet.add_data_validation(rule)
    rule.add(f'H6:H{cell_max}')

    original_dir = os.path.dirname(file_path)
    output_dir = os.path.join(original_dir, "Modified")

    os.makedirs(output_dir, exist_ok=True)

    filename = f"Checkliste_{get_name(file_path, True)}_modified.xlsx"
    output_path = os.path.join(output_dir, filename)
    wb.save(output_path)

# Handler für Datei oder Ordner
def export_handler(file_or_dir):
    file_format, columns, omitted, unnecessary, implemented, index_numbers, types_to_remove = get_export_settings()

    if os.path.isfile(file_or_dir) and is_format(file_or_dir):
        export(file_or_dir, file_format, columns, omitted, unnecessary, implemented, index_numbers, types_to_remove)
        print("\nDatei erfolgreich exportiert")
    elif os.path.isdir(file_or_dir):
        exported_count = 0
        for file_name in os.listdir(file_or_dir):
            file_path = os.path.join(file_or_dir, file_name)
            if os.path.isfile(file_path) and is_format(file_name):  
                export(file_path, file_format, columns, omitted, unnecessary, implemented, index_numbers, types_to_remove)
                exported_count += 1
        if exported_count > 0:
            print(f"\n{exported_count} Dateien erfolgreich exportiert")
        else:
            print("Keine passenden Excel-Dateien im Ordner gefunden.")
    else:
        print(f"'{file_or_dir}' ist weder eine passende Excel-Datei noch ein Ordner.")

# Fragt den Nutzer, welches Format und welches Spalten er exportieren möchte
def get_export_settings():

    print("Wählen Sie das Exportformat:")
    print("1. CSV\n2. JSON\n3. Markdown\n4. HTML\n5. XML\n6. Leerzeichengetrennt\n7. Tabstoppgetrennt\n8. Benutzerdefiniertes Trennzeichen")

    format_choice = input("\nAuswahl (1-8): ")

    if format_choice == "1":
        export_format = "csv"
    elif format_choice == "2":
        export_format = "json"
    elif format_choice == "3":
        export_format = "markdown"
    elif format_choice == "4":
        export_format = "html"
    elif format_choice == "5":
        export_format = "xml"
    elif format_choice == "6":
        export_format = "space"
    elif format_choice == "7":
        export_format = "tab"
    elif format_choice == "8":
        delimiter = input("Geben Sie das Trennzeichen ein: ")
        export_format = f"delimited:{delimiter}"
    else:
        print("Ungültige Auswahl. CSV wird verwendet.")
        export_format = "csv"

    print("\nWählen Sie die Spalten zum Exportieren aus:")
    columns = [
        "ID-Anforderung", "Titel", "Inhalt", "Typ", "Entbehrlich",
        "Begründung für Entbehrlichkeit", "Umsetzung", "Umsetzung bis",
        "Verantwortlich", "Bemerkungen / Begründung für Nicht-Umsetzung", "Kostenschätzung"
    ]
    for i, col in enumerate(columns):
        print(f"{i + 1}. {col}")

    selected_columns = []
    while True:
        col_choice = input("\nSpaltenauswahl (z.B. 1,3,5 oder 'Alle'): ")
        if col_choice.lower() == "alle" or col_choice == "":
            selected_columns = columns
            break
        else:
            try:
                col_indices = [int(c) - 1 for c in col_choice.split(",")]
                selected_columns = [columns[i] for i in col_indices]
                break
            except (ValueError, IndexError):
                print("Ungültige Eingabe.")

    omitted_choice = input(
        "\nMöchten Sie entfallene Anforderungen entfernen? (Ja/nein): ").strip().lower()
    if omitted_choice == "nein":
        omitted = False
    else: omitted = True

    unnecessary_choice = input(
        "\nMöchten Sie als entbehrlich markierte Anforderungen entfernen? (Ja/nein): ").strip().lower()
    if unnecessary_choice == "nein":
        unnecessary = False
    else:
        unnecessary = True

    implemented_choice = input(
        "\nMöchten Sie bereits umgesetzte Anforderungen entfernen? (ja/Nein): ").strip().lower()
    if implemented_choice == "ja":
        implemented = True
    else:
        implemented = False

    index_choice = input(
        "\nMöchten Sie nummerierte Zeilen? (Ja/nein): ").strip().lower()
    if index_choice == "nein":
        index_numbers = False
    else:
        index_numbers = True

    if export_format == "json" and index_numbers:
        print("\nNummerierte Zeilen bei JSON nicht möglich")

    types_input = input(
        "\nMöchten Sie Schutzbedarfstypen entfernen (Basis, Standard, Hoch)? \n"
        "(Auswahl z.B. 'Standard, Hoch', Default=Keine): ").strip()

    types_to_remove = []
    if types_input:
        types_to_remove = [t.strip().title() for t in types_input.split(',') if t.strip()]
        valid_types = {"Basis", "Standard", "Hoch"}
        original_input_types = set(types_to_remove)
        types_to_remove = [t for t in types_to_remove if t in valid_types]
        removed_invalid = original_input_types - set(types_to_remove)
        if removed_invalid:
            print(f"Warnung: Ungültige Typen ignoriert: {', '.join(removed_invalid)}")
    return export_format, selected_columns, omitted, unnecessary, implemented, index_numbers, types_to_remove

# Exportiert den Tabelleninhalt in ein gewünschtes Format mit diversen Anpassungsmöglichkeiten
def export(file_path, file_format, columns, omitted, unnecessary, implemented, index_numbers, types_to_remove):
    df = load_data(file_path)
    if omitted:
        df = remove_specific_requirements(df, "Titel", "ENTFALLEN")
    if unnecessary:
        df = remove_specific_requirements(df, "Entbehrlich", "Ja")
    if implemented:
        df = remove_specific_requirements(df, "Umsetzung", "Ja")
    if types_to_remove:
        for t in types_to_remove:
            df = remove_specific_requirements(df, "Typ", t)
    df = df[columns]

    export_dir = os.path.join(os.path.dirname(file_path), "Export")
    os.makedirs(export_dir, exist_ok=True)

    base_name = os.path.splitext(os.path.basename(file_path))[0]
    export_file_path = os.path.join(export_dir, base_name)

    if file_format == "csv":
        df.to_csv(export_file_path + ".csv", index=index_numbers)
    elif file_format == "json":
        df.to_json(export_file_path + ".json", orient="records")
    elif file_format == "markdown":
        df.to_markdown(export_file_path + ".md", index=index_numbers)
    elif file_format == "html":
        df.to_markdown(export_file_path + ".html", index=index_numbers)
    elif file_format == "xml":
        df.to_xml(export_file_path + ".xml", index=index_numbers)
    elif file_format == "space":
        df.to_csv(export_file_path + ".txt", sep=" ", index=index_numbers)
    elif file_format == "tab":
        df.to_csv(export_file_path + ".tsv", sep="\t", index=index_numbers)
    elif file_format.startswith("delimited:"):
        delimiter = file_format.split(":")[1]
        df.to_csv(export_file_path + ".txt", sep=delimiter, index=index_numbers)

# Überprüft, ob es nicht umgesetzte Basis-Anforderungen gibt
def risk_check(file_path):
    df = load_data(file_path)
    df = df[["ID-Anforderung", "Titel", "Inhalt", "Typ", "Entbehrlich", "Umsetzung"]]
    df = remove_specific_requirements(df, "Titel", "ENTFALLEN")

    ni = get_specific_df_with_two_conditions_and_emptiness(df, "Umsetzung", "nein", "Entbehrlich", "nein")
    ni_basis, ni_standard, ni_high = type_count(ni)
    if ni_basis != 0:
        return True
    else: return False

# Führt die erste Analyse für den Report durch
def report_analysis(file_path):
    df = load_data(file_path)
    df = df[["ID-Anforderung", "Titel", "Inhalt", "Typ", "Entbehrlich", "Begründung für Entbehrlichkeit", "Umsetzung", "Umsetzung bis", "Verantwortlich", "Bemerkungen / Begründung für Nicht-Umsetzung", "Kostenschätzung"]]
    df = remove_specific_requirements(df, "Titel", "ENTFALLEN")

    not_implemented, partly_implemented, fully_implemented, unnecessary = implementation_count(df)
    cost = cost_count(df)
    due_date = ", ".join(sorted(list(map(format_dates, df["Umsetzung bis"].dropna().unique()))))
    all_responsibles = f"{', '.join(get_responsible(df))}"
    ni = get_specific_df_with_two_conditions_and_emptiness(df, "Umsetzung", "nein", "Entbehrlich", "nein")
    ni_basis, ni_standard, ni_high = type_count(ni)

    return {
        "Gesamtanzahl Anforderungen": len(df),
        "Umgesetzte Anforderungen": fully_implemented,
        "Teilweise umgesetzte Anforderungen": partly_implemented,
        "Entbehrliche Anforderungen": unnecessary,
        "Nicht umgesetzte Anforderungen": not_implemented,
        "Nicht umgesetzte Anforderungen nach Typ": {"Basis": ni_basis, "Standard": ni_standard, "Erhöhter Schutzbedarf": ni_high},
        "Summierte Kostenschätzung": cost,
        "Verantwortliche": all_responsibles,
        "Deadlines einzelner Anforderungen": due_date,
    }

# Handler um für Dateien oder alle Dateien eines Ordners Reports zu erstellen
def report(file_or_dir):
    if os.path.isfile(file_or_dir):
        if is_format(file_or_dir):
            reports_dir = os.path.join(os.path.dirname(os.path.abspath(file_or_dir)), "Reports")
            os.makedirs(reports_dir, exist_ok=True)
            results = report_analysis(file_or_dir)
            risk = risk_check(file_or_dir)
            save_results_to_pdf(results, os.path.basename(file_or_dir), reports_dir, risk, file_or_dir)
            print("Report erstellt und gespeichert.")
        else:
            print("Keine Datei im Format Checkliste_XXX.X.X.xlsx")
    elif os.path.isdir(file_or_dir):
        reports_dir = os.path.join(os.path.abspath(file_or_dir), "Reports")
        os.makedirs(reports_dir, exist_ok=True)

        choice = input("Welche Reports sollen erstellt werden?\n\n1 - Für jede Datei einen Report\n2 - Einen Gesamtreport für alle Dateien\n3 - Beides\n\nAuswahl (1-3): ")
        if choice == "2":
            whole_report(file_or_dir, reports_dir)
            return
        if choice == "3":
            whole_report(file_or_dir, reports_dir)
        if choice not in ["1", "2", "3"]:
            print("Keine gültige Auswahl, es werden Berichte für jede Datei einzeln erstellt.")

        all_results = {}
        all_risks = {}
        print("Starte Analyse der Dateien für Einzelreports...")
        for file_name in os.listdir(file_or_dir):
            file_path = os.path.join(file_or_dir, file_name)
            if is_format(file_name):
                results = report_analysis(file_path)
                risk = risk_check(file_path)
                all_results[file_name] = results
                all_risks[file_name] = risk
        if not all_results:
            print("Keine gültigen Dateien gefunden.")
            return
        print("Analyse abgeschlossen\nErstelle Reports...")
        for file_name, results in all_results.items():
            save_results_to_pdf(results, file_name, reports_dir, all_risks[file_name], os.path.join(file_or_dir, file_name))
        print("Reports erstellt und gespeichert.")
    else:
        print(f"Ungültiger Pfad: {file_or_dir}")

# Baut die PDF zusammen, führt dabei Berechnungen durch um festzustellen, ob bestimmte Teile benötigt werden
def save_results_to_pdf(results, file_name, reports_dir, risk, file_path):
    df = load_data(file_path)
    pdf_path = os.path.join(reports_dir, f"Report_{get_name(file_name, True)}.pdf")
    doc = SimpleDocTemplate(pdf_path, pagesize=A4, title=f"Report für {get_name(file_name, True)} - {get_name(file_name, False)}")
    story = []
    image_path2 = None

    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    story.append(Paragraph(f"Analysebericht für {file_name} - {get_name(file_name, False)}", title_style))

    normal_style = styles["Normal"]
    for key, value in results.items():
        if isinstance(value, dict):
            story.append(Paragraph(f"<b>{key}:</b>", normal_style))
            for sub_key, sub_value in value.items():
                story.append(Paragraph(f"    {sub_key}: {sub_value}", normal_style))
        else:
            story.append(Paragraph(f"<b>{key}:</b> {value}", normal_style))

    if risk:
        story.append(Paragraph("<font color=red>WARNUNG: Es sind nicht alle Basis-Anforderungen umgesetzt!</font>", normal_style))
    id_status = id_check(file_path)
    if id_status == 2:
        df["ID-Anforderung"] = df["ID-Anforderung"].astype(str).apply(lambda x: x[:-1] if len(x) > 1 else x)
        story.append(Paragraph("<font color=red>Hinweis: Die IDs der Anforderungen wurden modifiziert, sodass sie für alle Teil-Anforderungen einzigartig sind</font>", normal_style))
    if id_status == 3:
        story.append(Paragraph("<font color=red>Hinweis: Die IDs der Anforderungen wurden teilweise modifiziert, möglicherweise werden sie nicht richtig gruppiert</font>", normal_style))


    image_path1 = plot_pie_chart_to_image({
        "Umgesetzt": results["Umgesetzte Anforderungen"],
        "Teilweise umgesetzt": results["Teilweise umgesetzte Anforderungen"],
        "Nicht umgesetzt": results["Nicht umgesetzte Anforderungen"],
        "Entbehrlich": results["Entbehrliche Anforderungen"]
    }, "Umsetzungsstatus")
    story.append(Image(image_path1, width=400, height=300))

    ni_df = df
    ni_df = ni_df[["ID-Anforderung", "Titel", "Inhalt", "Typ", "Umsetzung", "Entbehrlich"]]
    ni_df = remove_specific_requirements(ni_df, "Titel", "ENTFALLEN")
    ni_df = get_specific_df_with_two_conditions_and_emptiness(ni_df, "Umsetzung", "nein", "Entbehrlich", "nein")
    if not ni_df.empty:
        story.append(Paragraph(f"Nicht umgesetzte Anforderungen", title_style))
        grouped_data = defaultdict(list)
        for _, row in ni_df.iterrows():
            grouped_data[row["ID-Anforderung"]].append(row)

        table_data = [["ID-Anforderung", "Anzahl der Teil-Anforderungen", "Titel", "Typ"]]
        for id_anforderung, rows in grouped_data.items():
            first_row = rows[0]
            table_data.append([id_anforderung, len(rows), first_row["Titel"], first_row["Typ"]])

        table = get_custom_table(table_data)
        story.append(table)

        story.append(Spacer(1, 20))
        image_path2 = plot_pie_chart_to_image(results["Nicht umgesetzte Anforderungen nach Typ"],
                                          "Nicht umgesetzte Anforderungen nach Typ aufgeschlüsselt")
        story.append(Image(image_path2, width=400, height=300))

    if results["Deadlines einzelner Anforderungen"]:
        dl_df = df
        dl_df = remove_specific_requirements(dl_df, "Titel", "ENTFALLEN")
        dl_df = remove_specific_requirements(dl_df, "Umsetzung", "Ja")
        dl_df = dl_df[["ID-Anforderung", "Titel", "Typ", "Umsetzung bis"]]
        dl_df = dl_df.dropna(subset=["Umsetzung bis"])

        story.append(Paragraph(f"Offene Deadlines", title_style))
        table_data = [["ID-Anforderung", "Titel", "Typ", "Umsetzung bis"]]
        for _, row in dl_df.iterrows():
            formatted_date = format_dates(row["Umsetzung bis"])
            table_data.append([row["ID-Anforderung"], row["Titel"], row["Typ"], formatted_date])

        table = get_custom_table(table_data)
        story.append(table)

    resp_df = df
    resp_df = remove_specific_requirements(resp_df, "Verantwortlich", "ENTFALLEN")
    resp_df = resp_df[["ID-Anforderung", "Verantwortlich"]]
    resp_df = resp_df.dropna(subset=["Verantwortlich"])
    if not resp_df.empty:
        story.append(Spacer(1, 5))
        story.append(Paragraph(f"Verantwortliche für Anforderungen", title_style))
        unique_verantwortliche = resp_df["Verantwortlich"].unique()
        table_data = [["Verantwortlich", "ID-Anforderungen"]]
        for verantwortlicher in unique_verantwortliche:
                id_anforderungen = ", ".join(resp_df[resp_df["Verantwortlich"] == verantwortlicher]["ID-Anforderung"].tolist())
                table_data.append([verantwortlicher, id_anforderungen])

        table = get_custom_table(table_data)
        story.append(table)

    cost_df = df
    cost_df = remove_specific_requirements(cost_df, "ID-Anforderung", "ENTFALLEN")
    cost_df = cost_df[["ID-Anforderung", "Kostenschätzung"]]
    cost_df = cost_df.dropna(subset=["Kostenschätzung"])

    cost_df["Kostenschätzung"] = cost_df["Kostenschätzung"].astype(str) \
        .str.replace('€', '') \
        .str.replace(',', '.') \
        .str.findall(r'\d+\.?\d*').str[0]

    cost_df["Kostenschätzung"] = pd.to_numeric(cost_df["Kostenschätzung"], errors='coerce')

    cost_df = cost_df.dropna(subset=["Kostenschätzung"])

    if not cost_df.empty:
        story.append(Spacer(1, 10))
        grouped_data = cost_df.groupby("ID-Anforderung")["Kostenschätzung"].sum().reset_index()

        plt.figure(figsize=(10, 6))
        plt.bar(grouped_data["ID-Anforderung"], grouped_data["Kostenschätzung"])
        plt.xlabel("ID der Anforderung")
        plt.ylabel("Geschätzte Kosten")
        plt.title("Kostenschätzung pro Anforderung (Summe aus Teil-Anforderungen)")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()

        img_data = BytesIO()
        plt.savefig(img_data, format="png")
        img_data.seek(0)
        story.append(Image(img_data, width=400, height=300))
        plt.close()

    implemented = get_specific_df(df, "Umsetzung", "ja")
    grouped_items = {}

    ids = implemented["ID-Anforderung"].unique()

    for req_id in ids:
        for item in mapping.krt:
            if item['id'] == req_id:
                for risk_krz in item.get('gefahren', []):
                    if req_id not in grouped_items:
                        grouped_items[req_id] = []
                    grouped_items[req_id].append(risk_krz)
                break

    if grouped_items:
        story.append(Spacer(1, 15))
        story.append(Paragraph(f"(Teilweise) abgedeckte elementare Gefährdungen:", title_style))
        table_data = [["ID-Anforderung", "Elementare Gefährdungen"]]

        for req_id, risks_krz_list in grouped_items.items():
            risk_names = []
            for risk_krz in risks_krz_list:
                risk_names.append(f"{risk_krz}: {mapping.gefahren[risk_krz]}")

            risks_combined = "<br/>".join(risk_names)
            table_data.append([req_id, risks_combined])

        table = get_custom_table(table_data)
        story.append(table)

    entb_df = df
    entb_df = remove_specific_requirements(entb_df, "Titel", "ENTFALLEN")
    entb_df = entb_df[["ID-Anforderung", "Entbehrlich", "Begründung für Entbehrlichkeit"]]
    entb_df = entb_df[(entb_df["Entbehrlich"] == "Ja") & (entb_df["Begründung für Entbehrlichkeit"].isna())]
    if not entb_df.empty:
        story.append(Spacer(1, 15))
        story.append(Paragraph(f"Fehlende Begründung für entbehrliche Anforderungen:", title_style))
        bullet_list = []
        for _, row in entb_df.iterrows():
            bullet_list.append(Paragraph(f"- {row['ID-Anforderung']}", normal_style))
            story.extend(bullet_list)

    ums_df = df
    ums_df = remove_specific_requirements(ums_df, "Titel", "ENTFALLEN")
    ums_df = remove_specific_requirements(ums_df, "Entbehrlich", "Ja")
    ums_df = ums_df[["ID-Anforderung", "Umsetzung", "Bemerkungen / Begründung für Nicht-Umsetzung"]]
    ums_df = ums_df[(ums_df["Umsetzung"] == "Nein") & (ums_df["Bemerkungen / Begründung für Nicht-Umsetzung"].isna())]
    if not ums_df.empty:
        story.append(Spacer(1, 15))
        story.append(Paragraph(f"Fehlende Begründung für nicht umgesetzte Anforderungen:", title_style))
        bullet_list = []
        for _, row in ums_df.iterrows():
            bullet_list.append(Paragraph(f"- {row['ID-Anforderung']}", normal_style))
            story.extend(bullet_list)

    doc.build(story)

    os.remove(image_path1) # Temporäre Bilder entfernen, weil es früher nicht möglich ist
    if not ni_df.empty:
        os.remove(image_path2)

# Definiert wie Tabellen im Report aussehen sollen und ermöglicht Zeilenumbrüche
def get_custom_table(table_data):
    styles = getSampleStyleSheet()
    normal_style = styles["Normal"]

    paragraph_table_data = []
    for row in table_data:
        paragraph_row = []
        for cell in row:
            paragraph_row.append(Paragraph(str(cell), normal_style))
        paragraph_table_data.append(paragraph_row)

    table = Table(paragraph_table_data)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    return table

# Vereinheitlicht die Daten in der "Umsetzung bis" Spalte
def format_dates(date_value):
    if isinstance(date_value, np.datetime64):
        return pd.to_datetime(date_value).strftime('%Y-%m-%d')
    elif isinstance(date_value, datetime):
        return date_value.strftime('%Y-%m-%d')
    else:
        return date_value

# Erstellt ein Kreisdiagramm und speichert es temporär
def plot_pie_chart_to_image(data, title):
    labels = []
    values = []
    for label, value in data.items():
        if value > 0:
            labels.append(label)
            values.append(value)

    plt.figure(figsize=(8, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.axis('equal')

    temp_image_path = f"{title}.png"
    plt.savefig(temp_image_path)
    plt.close()
    return temp_image_path

# Erstellt einen Gesamtreport für alle Dateien
def whole_report(directory, output_directory):
    print("Starte Analysen für Gesamtreport...")
    total_files = 0
    total_df_count = 0
    total_fully_implemented = 0
    total_partly_implemented = 0
    total_unnecessary = 0
    total_not_implemented = 0
    total_cost = 0
    total_basis = 0
    total_standard = 0
    total_high = 0
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if is_format(file_path):
            total_files += 1
            df = load_data(file_path)
            df = df[["Titel", "Typ", "Entbehrlich", "Umsetzung", "Kostenschätzung"]]
            df = remove_specific_requirements(df, "Titel", "ENTFALLEN")

            not_implemented, partly_implemented, fully_implemented, unnecessary = implementation_count(df)
            cost = cost_count(df)

            ni = get_specific_df_with_two_conditions_and_emptiness(df, "Umsetzung", "nein", "Entbehrlich", "nein")
            ni_basis, ni_standard, ni_high = type_count(ni)
            covered_risks, covered_cia = risk_analysis(file_path)

            total_df_count += len(df)
            total_fully_implemented += fully_implemented
            total_partly_implemented += partly_implemented
            total_unnecessary += unnecessary
            total_not_implemented += not_implemented
            total_cost += cost
            total_basis += ni_basis
            total_standard += ni_standard
            total_high += ni_high
    if total_files == 0:
        print("Keine Dateien im Format Checkliste_XXX.X.X.xlsx gefunden")
        return

    results = {
    "Analysierte Tabellen": total_files,
    "Gesamtanzahl Anforderungen": total_df_count,
    "Umgesetzte Anforderungen": total_fully_implemented,
    "Teilweise umgesetzte Anforderungen": total_partly_implemented,
    "Entbehrliche Anforderungen": total_unnecessary,
    "Nicht umgesetzte Anforderungen": total_not_implemented,
    "Nicht umgesetzte Anforderungen nach Typ": {"Basis": total_basis, "Standard": total_standard, "Erhöhter Schutzbedarf": total_high},
    "Summierte Kostenschätzung": total_cost,
    }

    print("Erstelle Tabellen und Grafiken...")

    save_whole_results_to_pdf(directory, results, output_directory)

    print("Gesamtreport erstellt und gespeichert")

# Erstellt Tabellen, Grafiken und speichert den Gesamtreport
def save_whole_results_to_pdf(directory, results, reports_dir):
    pdf_path = os.path.join(reports_dir, f"Gesamtreport_{datetime.today().strftime('%d-%m-%Y')}.pdf")
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            title=f"IT-Grundschutz-Report")
    story = []

    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    story.append(Paragraph(f"Analysebericht vom {datetime.today().strftime('%d-%m-%Y')}", title_style))

    normal_style = styles["Normal"]
    for key, value in results.items():
        if isinstance(value, dict):
            story.append(Paragraph(f"<b>{key}:</b>", normal_style))
            for sub_key, sub_value in value.items():
                story.append(Paragraph(f"    {sub_key}: {sub_value}", normal_style))
        else:
            story.append(Paragraph(f"<b>{key}:</b> {value}", normal_style))

    files_in_dir = {get_name(file, True) for file in os.listdir(directory) if is_format(file)}

    matching_profiles = []
    for profile_name, profile_files in mapping.profiles_mapping.items():
        profile_set = set(getattr(mapping, profile_files))
        if files_in_dir == profile_set:
            matching_profiles.append(mapping.profile_names[profile_name])

    if matching_profiles and len(files_in_dir)<111:
        if len(matching_profiles) == 1:
            story.append(Paragraph(f"<b>IT-Grundschutz-Profil: {matching_profiles[0]}</b>", normal_style))
        else:
            story.append(Paragraph(f"<b>Passende IT-Grundschutz-Profile: {', '.join(matching_profiles)})</b>", normal_style))

    risk_files = []
    not_implemented = {}
    ni_types ={}
    deadlines = {}
    responsible = {}
    cost = {}
    missing_reason_entb = {}
    missing_reason_ni = {}
    all_covered_risks = set()
    all_covered_cia = set()
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if is_format(file_path):
            df = load_data(file_path)
            df = df[["ID-Anforderung", "Titel", "Inhalt", "Typ", "Umsetzung", "Umsetzung bis", "Bemerkungen / Begründung für Nicht-Umsetzung", "Entbehrlich", "Begründung für Entbehrlichkeit", "Verantwortlich", "Kostenschätzung"]]
            df = remove_specific_requirements(df, "Titel", "ENTFALLEN")
            if risk_check(file_path):
                risk_files.append(get_name(file_path, True))
            ni_df = get_specific_df_with_two_conditions_and_emptiness(df, "Umsetzung", "nein", "Entbehrlich", "nein")
            if not ni_df.empty:
                not_implemented[get_name(file_name, True)] = len(ni_df)
                ni_types[get_name(file_name, True)] = type_count(ni_df)
            dl_df = df.dropna(subset=["Umsetzung bis"])
            if not dl_df.empty:
                deadlines[get_name(file_name, True)] = []
                for _, row in dl_df.iterrows():
                    deadlines[get_name(file_name, True)].append(format_dates(row["Umsetzung bis"]))
            resp_df = df.dropna(subset=["Verantwortlich"])
            if not resp_df.empty:
                unique_verantwortliche = resp_df["Verantwortlich"].unique()
                responsible[get_name(file_name, True)] = unique_verantwortliche
            cost_df = df.copy()
            cost_df = cost_df.dropna(subset=["Kostenschätzung"])
            if not cost_df.empty:
                cost_sum = cost_count(cost_df)
                if cost_sum != 0:
                    cost[get_name(file_name, True)] = cost_sum
            entb_df = df[(df["Entbehrlich"] == "Ja") & (df["Begründung für Entbehrlichkeit"].isna())]
            if not entb_df.empty:
                missing_reason_entb[get_name(file_name, True)] = len(entb_df)
            ums_df = remove_specific_requirements(df, "Entbehrlich", "Ja")
            ums_df = ums_df[(ums_df["Umsetzung"] == "Nein") & (ums_df["Bemerkungen / Begründung für Nicht-Umsetzung"].isna())]
            if not ums_df.empty:
                missing_reason_ni[get_name(file_name, True)] = len(ums_df)
            covered_risks, covered_cia = risk_analysis(file_path)
            all_covered_risks.update(covered_risks)
            all_covered_cia.update(covered_cia)
        else: print(f"Datei/Ordner ausgelassen: {file_name}")

    print("Analysen abgeschlossen")

    if risk_files:
        story.append(Paragraph(f"<font color=red>WARNUNG: In den folgenden Bausteinen sind nicht alle Basis-Anforderungen umgesetzt: {', '.join(risk_files)}</font>",
                               normal_style))

    image_path1 = plot_pie_chart_to_image({
        "Umgesetzt": results["Umgesetzte Anforderungen"],
        "Teilweise umgesetzt": results["Teilweise umgesetzte Anforderungen"],
        "Nicht umgesetzt": results["Nicht umgesetzte Anforderungen"],
        "Entbehrlich": results["Entbehrliche Anforderungen"]
    }, "Umsetzungsstatus")
    story.append(Image(image_path1, width=400, height=300))


    story.append(Spacer(1, 20))
    image_path2 = plot_pie_chart_to_image(results["Nicht umgesetzte Anforderungen nach Typ"],
                                              "Insgesamt nicht umgesetzte Anforderungen nach Typ aufgeschlüsselt")
    story.append(Image(image_path2, width=400, height=300))

    if not_implemented:
        story.append(Spacer(1, 10))
        story.append(Paragraph(f"Nicht umgesetzte Anforderungen", title_style))
        table_data = [["Baustein", "Anzahl", "Basis", "Standard", "Erhöhter Schutzbedarf"]]
        for name, count in not_implemented.items():
            basis, standard, high = ni_types[name]
            table_data.append([name, count, basis, standard, high])
        table = get_custom_table(table_data)
        story.append(table)

    if deadlines:
        story.append(Spacer(1, 10))
        story.append(Paragraph(f"Deadlines", title_style))
        table_data = [["Baustein", "Deadlines"]]
        for name, deadlines in deadlines.items():
            deadline_str =  ", ".join(deadlines)
            table_data.append([name, deadline_str])
        table = get_custom_table(table_data)
        story.append(table)

    if responsible:
        story.append(Spacer(1, 10))
        story.append(Paragraph(f"Verantwortliche", title_style))
        table_data = [["Baustein", "Verantwortliche"]]
        for name, verantwortliche in responsible.items():
            verantwortliche_str = ", ".join(verantwortliche)
            table_data.append([name, verantwortliche_str])
        table = get_custom_table(table_data)
        story.append(table)

    if cost:
        story.append(Spacer(1, 10))
        story.append(Paragraph(f"Kostenschätzung", title_style))
        names = list(cost.keys())
        costs = list(cost.values())
        plt.figure(figsize=(10, 6))
        plt.bar(names, costs)
        plt.xlabel("Baustein")
        plt.ylabel("Kostenschätzung")
        plt.title("Summierte Kostenschätzung")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()

        img_data = BytesIO()
        plt.savefig(img_data, format="png")
        img_data.seek(0)
        story.append(Image(img_data, width=400, height=300))
        plt.close()

    if missing_reason_entb:
        story.append(Spacer(1, 10))
        story.append(Paragraph(f"Fehlende Begründungen für Entbehrlichkeit", title_style))
        table_data = [["Baustein", "Anzahl fehlender Begründungen"]]
        for name, count in missing_reason_entb.items():
            table_data.append([name, count])
        table = get_custom_table(table_data)
        story.append(table)

    if missing_reason_ni:
        story.append(Spacer(1, 10))
        story.append(Paragraph(f"Fehlende Begründungen für Nicht-Umsetzung", title_style))
        table_data = [["Baustein", "Anzahl fehlender Begründungen"]]
        for name, count in missing_reason_ni.items():
            table_data.append([name, count])
        table = get_custom_table(table_data)
        story.append(table)

    if all_covered_risks:
        story.append(Spacer(1, 15))
        story.append(Paragraph(f"(Teilweise) abgedeckte elementare Gefährdungen:", title_style))
        unique_risks = sorted(list(all_covered_risks))
        for risk_id in unique_risks:
            story.append(Paragraph(f"- {risk_id}: {mapping.gefahren[risk_id]}", normal_style))

    all_possible_risks = set(mapping.gefahren.keys())
    uncovered_risks = sorted(list(all_possible_risks - all_covered_risks))

    if uncovered_risks:
        story.append(Spacer(1, 15))
        story.append(Paragraph(f"Nicht abgedeckte elementare Gefährdungen:", title_style))
        for risk_id in uncovered_risks:
            story.append(Paragraph(f"- {risk_id}: {mapping.gefahren[risk_id]}", normal_style))

    if all_covered_cia:
        story.append(Spacer(1, 15))
        story.append(Paragraph(f"(Teilweise) abgedeckte Schutzziele:", title_style))
        unique_cia = sorted(list(all_covered_cia))
        for goal_id in unique_cia:
            story.append(Paragraph(f"- {mapping.cia[goal_id]} ({goal_id})", normal_style))

    all_possible_cia = set(mapping.cia.keys())
    uncovered_cia = sorted(list(all_possible_cia - all_covered_cia))
    if uncovered_cia:
        story.append(Spacer(1, 15))
        story.append(Paragraph(f"Nicht abgedeckte Schutzziele:", title_style))
        for goal_id in uncovered_cia:
            story.append(Paragraph(f"- {mapping.cia[goal_id]} ({goal_id})", normal_style))


    print("Tabellen und Grafiken erstellt")

    doc.build(story)

    os.remove(image_path1)
    if not ni_df.empty:
        os.remove(image_path2)

# Löst Konflikte für verschiedene Werte in "Entbehrlich", "Umsetzung", "Umsetzung bis"
def resolve_conflict(values, column_name, file1_path, file2_path):
    unique_values = values.unique()
    if len(unique_values) == 1:
        return unique_values[0]
    else:
        if column_name == "Umsetzung bis":
            unique_values = [format_dates(val) for val in unique_values]
        conflict_row_index = values.index[0]
        conflict_row_number = conflict_row_index + 6

        print(f"\nKonflikt in Spalte '{column_name}' in Zeile {conflict_row_number}:\n")

        wb1 = openpyxl.load_workbook(file1_path)
        ws1 = wb1.active

        af_id = ws1.cell(row=conflict_row_number, column=2).value
        titel = ws1.cell(row=conflict_row_number, column=3).value
        inhalt = ws1.cell(row=conflict_row_number, column=4).value
        typ = ws1.cell(row=conflict_row_number, column=5).value

        print(f"  ID: {af_id}")
        print(f"  Titel: {titel}")
        print(f"  Inhalt: {inhalt}")
        print(f"  Typ: {typ}")

        print(f"\n  Verschiedene Werte:")
        print(f"    {os.path.basename(file1_path)}: {unique_values[0]}")
        print(f"    {os.path.basename(file2_path)}: {unique_values[1]}")

        while True:
            if column_name == "Umsetzung":
                unique_values = "Ja", "Nein", "Teilweise"
            choice = input(f"\nWählen Sie einen Wert für '{column_name}' ({'/'.join(map(str, unique_values))}): ")
            if choice in map(str, unique_values):
                return choice
            else:
                print("Ungültige Eingabe.")

# Vereint zwei gleichartige Tabellen
def merge_tables(file1_path, file2_path):
    try:
        df1 = pd.read_excel(file1_path, sheet_name=0, skiprows=4)
        df2 = pd.read_excel(file2_path, sheet_name=0, skiprows=4)
        if len(df1) != len(df2):
            print("Verschiedene Tabellen. Vorgang wird abgebrochen.")
            exit(1)
    except PermissionError:
        print(f"Fehler: Eine der Dateien ist möglicherweise geöffnet und kann nicht gelesen werden. Vorgang wird abgebrochen.")
        exit(1)
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist beim Öffnen der Datei aufgetreten: {e}")
        exit(1)

    columns_to_sum = ["Begründung für Entbehrlichkeit", "Verantwortlich", "Bemerkungen / Begründung für Nicht-Umsetzung", "Kostenschätzung"]

    # Hilfsfunktion zum Zusammenfassen von Feldern
    def concatenate_values(series):
        return " / ".join(map(str, series.dropna().unique()))

    agg_dict = {
        **{col: "first" for col in ["ID-Anforderung", "Titel", "Inhalt", "Typ"]},
        **{col: concatenate_values for col in columns_to_sum},
        "Umsetzung": lambda x: resolve_conflict(x, "Umsetzung", file1_path, file2_path),
        "Entbehrlich": lambda x: resolve_conflict(x, "Entbehrlich", file1_path, file2_path),
        "Umsetzung bis": lambda x: resolve_conflict(x, "Umsetzung bis", file1_path, file2_path)
    }
    merged_df = pd.concat([df1, df2]).groupby(["ID-Anforderung", "Titel", "Inhalt", "Typ"], sort=False, as_index=False).agg(agg_dict)

    merged_df = merged_df[
        ["ID-Anforderung", "Titel", "Inhalt", "Typ", "Entbehrlich", "Begründung für Entbehrlichkeit", "Umsetzung",
         "Umsetzung bis", "Verantwortlich", "Bemerkungen / Begründung für Nicht-Umsetzung", "Kostenschätzung"]]

    output_file_name = os.path.basename(file1_path)
    output_dir = os.path.join(os.path.dirname(file1_path), "Merged")
    os.makedirs(output_dir, exist_ok=True)
    output_file_path = os.path.join(output_dir, output_file_name)

    wb = openpyxl.load_workbook(file1_path)

    ws = wb.active
    for idx, row in merged_df.iterrows():
        excel_row = 6 + idx
        for col_name, value in row.items():
            col_letter = openpyxl.utils.get_column_letter(merged_df.columns.get_loc(col_name)+2)
            ws[f"{col_letter}{excel_row}"].value = value

    wb.save(output_file_path)

    print(f"\n{os.path.basename(file1_path)} und {os.path.basename(file2_path)} erfolgreich zusammengeführt und gespeichert unter: {output_file_path}")

# Behandelt die Modifizierung von allen Word-Dokumenten eines Ordners
def modify(directory):
    if not os.path.isdir(directory):
        print(f"Fehler: '{directory}' ist kein gültiges Verzeichnis.")
        return

    output_directory = os.path.join(directory, "Modified")
    os.makedirs(output_directory, exist_ok=True)

    section_titles = [
        "Beschreibung",
        "Gefährdungslage",
        "Anforderungen",
        "Basis-Anforderungen",
        "Standard-Anforderungen",
        "Anforderungen bei erhöhtem Schutzbedarf",
        "Weiterführende Informationen",
    ]

    anforderungen_subsections = [
        "Basis-Anforderungen",
        "Standard-Anforderungen",
        "Anforderungen bei erhöhtem Schutzbedarf",
    ]

    sections_to_remove_flags = {}
    anforderungen_selected = False

    print("Wählen Sie die Abschnitte aus, die entfernt werden sollen:")
    for title in section_titles:
        if title in anforderungen_subsections and anforderungen_selected:
            sections_to_remove_flags[title] = True
            continue

        sections_to_remove_flags[title] = False

        eingabe = input(f"- '{title}' entfernen? (ja/Nein): ")
        if eingabe.lower() in ["j", "ja"]:
            sections_to_remove_flags[title] = True
            if title == "Anforderungen":
                anforderungen_selected = True

    delete_entfallen = True
    integrate_checklists = False
    implemented = True
    partly_implemented = False
    not_implemented = False
    unnecessary = True
    if not anforderungen_selected:
        remove_entfallen = input("\n- Entfallene Anforderungen entfernen? (Ja/nein): ")
        if remove_entfallen.strip().lower() in ["nein", "n"]:
            delete_entfallen = False
        checklisten_choice = input("\n- Excel Checklisten integrieren? (ja/Nein): ")
        if checklisten_choice.strip().lower() in ["j", "ja"]:
            integrate_checklists = True
            while True:
                checklist_path = input("\nPfad zum Ordner mit den Checklisten: ").strip().strip('"')
                if os.path.isdir(checklist_path):
                    break
                else:
                    print("Kein gültiger Pfad zu einem Ordner")
            print("Hinweis: Es werden nur Anforderungen entfernt, die vollständig die nachfolgenden Auswahlmöglichkeiten erfüllen.\n")
            implemented_choice = input("- In Tabellen bereits umgesetzte Anforderungen entfernen? (Ja/nein): ")
            if implemented_choice.strip().lower() in ["nein", "n"]:
                implemented = False
            partly_implemented_choice = input("- In Tabellen teilweise umgesetzte Anforderungen entfernen? (ja/Nein): ")
            if partly_implemented_choice.strip().lower() in ["ja", "j"]:
                partly_implemented = True
            not_implemented_choice = input("- In Tabellen nicht umgesetzte Anforderungen entfernen? (ja/Nein): ")
            if not_implemented_choice.strip().lower() in ["ja", "j"]:
                not_implemented = True
            unnecessary_choice = input("- In Tabellen entbehrliche Anforderungen entfernen? (Ja/nein): ")
            if unnecessary_choice.strip().lower() in ["nein", "n"]:
                unnecessary = False


    save_as_pdf = input("\n- Dokumente auch als PDF speichern? Hinweis: Diese Operation ist sehr rechenaufwendig.\n  Antwort (ja/Nein): ")
    save_as_pdf = save_as_pdf.strip().lower() in ["ja", "j"]

    sections_for_removal = [title for title, remove in sections_to_remove_flags.items() if remove]

    if not sections_for_removal and not delete_entfallen and not save_as_pdf and not integrate_checklists:
        print("Keine Aktion ausgewählt.")
        return


    for filename in os.listdir(directory):
        if is_docx(filename):
            original_file_path = os.path.join(directory, filename)
            output_file_path = os.path.join(output_directory, filename)

            dokument = Document(original_file_path)
            if sections_for_removal:
                remove_sections(dokument, sections_for_removal, section_titles)
            if delete_entfallen:
                remove_entfallene_anforderungen(dokument)
            if integrate_checklists:
                checklist_integration(checklist_path, filename, dokument, implemented, partly_implemented, not_implemented, unnecessary)
            try:
                dokument.save(output_file_path)
                if save_as_pdf:
                    pdf_directory = os.path.join(output_directory, "PDFs")
                    os.makedirs(pdf_directory, exist_ok=True)
                    pdf_filename = os.path.splitext(filename)[0] + ".pdf"
                    pdf_path = os.path.join(pdf_directory, pdf_filename)
                    docx2pdf.convert(output_file_path, pdf_path)
            except Exception as e:
                print(f" Fehler beim Speichern von {filename}: {e}")

    if not any(is_docx(f) for f in os.listdir(directory)):
        print("\nKeine .docx-Dateien im Verzeichnis gefunden.")
    else:
        print(f"\nDateien erfolgreich gespeichert.")

# Entfernt gewünschte Abschnitte eines Word-Dokuments
def remove_sections(dokument, sections_to_remove, section_titles):
    paragraphs = dokument.paragraphs
    num_paragraphs = len(paragraphs)

    found_sections_indices = {}
    for i, p in enumerate(paragraphs):
        p_text = p.text.strip()
        for title in sorted(section_titles, key=len, reverse=True): # Wichtig, damit 'Anforderungen' und 'Anforderungen des erhöhten Schutzbedarfs' nicht vertauscht werden
            if p_text.startswith(title) and title not in found_sections_indices:
                found_sections_indices[title] = i
                break

    section_ranges = {}
    sorted_found_keys = sorted(
        found_sections_indices.items(),
        key=lambda item: section_titles.index(item[0]) if item[0] in section_titles else float('inf')
    )
    sorted_found_keys.sort(key=lambda item: item[1])

    for i, (title, start_index) in enumerate(sorted_found_keys):
        end_index = num_paragraphs
        if i + 1 < len(sorted_found_keys):
            _, next_start_index = sorted_found_keys[i + 1]
            end_index = next_start_index
        if start_index < end_index:
            section_ranges[title] = {"start": start_index, "end": end_index}

    elements_to_delete = []
    paragraph_ranges_to_delete = [section_ranges[title] for title in sections_to_remove if title in section_ranges]
    paragraph_ranges_to_delete.sort(key=lambda r: r["start"], reverse=True)

    body_elements = list(dokument.element.body.iterchildren())
    for range_info in paragraph_ranges_to_delete:
        start_idx = range_info["start"]
        end_idx = range_info["end"]

        try:
            start_paragraph = paragraphs[start_idx]
            start_element = start_paragraph._element
            end_element = paragraphs[end_idx]._element if end_idx < num_paragraphs else None
        except IndexError:
            continue

        body_end_idx = len(body_elements)
        if end_element in body_elements:
            body_end_idx = body_elements.index(end_element)

        for i in range(body_end_idx - 1, -1, -1):
            element = body_elements[i]
            if element == start_element:
                if isinstance(element, CT_P):
                    elements_to_delete.append(element)
                break
            if isinstance(element, (CT_P, CT_Tbl)):
                elements_to_delete.append(element)

    for element in elements_to_delete:
        if element.getparent() is not None:
            element.getparent().remove(element)
    return


def remove_entfallene_anforderungen(dokument):
    paragraphs = dokument.paragraphs
    body_elements = list(dokument.element.body.iterchildren())

    entfallen_pattern = re.compile(r"\b[A-Z]{2,}\.(\d+\.){1,3}A\d+\s+ENTFALLEN\b")
    anforderung_heading_pattern = re.compile(r"\b[A-Z]{2,}\.(\d+\.){1,3}A\d+\b")

    i = 0
    while i < len(paragraphs):
        para = paragraphs[i]
        if entfallen_pattern.search(para.text):
            start_index = i
            i += 1
            while i < len(paragraphs):
                next_para_text = paragraphs[i].text.strip()
                if anforderung_heading_pattern.match(next_para_text) or next_para_text in ["Standard-Anforderungen", "Anforderungen bei erhöhtem Schutzbedarf", "Weiterführende Informationen"]:
                    break
                i += 1
            for j in range(start_index, i):
                el = paragraphs[j]._element
                if el in body_elements and el.getparent() is not None:
                    el.getparent().remove(el)
            continue
        i += 1

# Integriert die Werte der Checklisten ins Dokument, indem Anforderungen, die nicht die Bedingungen erfüllen, entfernt werden
def checklist_integration(checklist_path, filename, dokument, implemented, partly_implemented, not_implemented, unnecessary):
    docx_short = filename.split()[0]
    if docx_short.startswith("CCON"):
        docx_short = "CON" + docx_short[4:]

    found_checklist = None
    for checklist in os.listdir(checklist_path):
        if get_name(checklist, True) == docx_short:
            found_checklist = os.path.join(checklist_path, checklist)
    if found_checklist is None:
        print(f"Keine passende Checkliste für {filename} gefunden")
        return

    df = load_data(found_checklist)
    df = remove_specific_requirements(df, "Titel", "ENTFALLEN")
    if implemented:
        df = remove_specific_requirements(df, "Umsetzung", "Ja")
    if partly_implemented:
        df = remove_specific_requirements(df, "Umsetzung", "Teilweise")
    if not_implemented:
        df2 = get_specific_df_with_two_conditions_and_emptiness(df, "Umsetzung", "Nein", "Entbehrlich", "Nein")
        contents_to_remove = set(df2["Inhalt"].unique())
        df = df[~df["Inhalt"].isin(contents_to_remove)] # ~not
    if unnecessary:
        df = remove_specific_requirements(df, "Entbehrlich", "Ja")

    df = df[["ID-Anforderung", "Inhalt"]]

    paragraphs = dokument.paragraphs
    body_elements = list(dokument.element.body.iterchildren())

    valid_ids = set(df["ID-Anforderung"].unique())

    # Falls keine Anforderung übrig ist, gesamten Abschnitt entfernen
    if not valid_ids:
        section_titles = [
            "Beschreibung",
            "Anforderungen",
            "Weiterführende Informationen",
        ]
        sections_to_remove_flags = {}
        sections_to_remove_flags["Anforderungen"] = True
        sections_for_removal = [title for title, remove in sections_to_remove_flags.items() if remove]
        remove_sections(dokument, sections_for_removal, section_titles)

    heading_pattern = re.compile(r"\b([A-Z]{2,}\.(\d+\.){1,3}A\d+)\b")

    i = 0
    while i < len(paragraphs):
        para = paragraphs[i]
        heading_match = heading_pattern.match(para.text.strip())
        if heading_match:
            current_id = heading_match.group(1)
            start_index = i
            i += 1
            while i < len(paragraphs):
                next_para_text = paragraphs[i].text.strip()
                if (heading_pattern.match(next_para_text) or next_para_text in
                        ["Standard-Anforderungen", "Anforderungen bei erhöhtem Schutzbedarf", "Weiterführende Informationen"]):
                    break
                i += 1
            end_index = i

            if current_id not in valid_ids:
                for j in range(start_index, end_index):
                    el = paragraphs[j]._element
                    if el in body_elements and el.getparent() is not None:
                        el.getparent().remove(el)
        else:
            i += 1

# Speichert einen Dataframe in einem gewünschten Format
def save_df(df, export_file_path, index_number):
    file_format = input("In welchem Format soll die Tabelle gespeichert werden?\n\n"
                        "1. Excel\n2. CSV\n3. JSON\n4. Markdown\n5. HTML\n6. XML\n"
                        "7. Leerzeichengetrennt\n8. Tabstoppgetrennt\n9. Benutzerdefiniertes Trennzeichen\n\n"
                        "Auswahl (1-9): ")

    if file_format == "1":
        df.to_excel(export_file_path + ".xlsx", index=index_number)
    elif file_format == "2":
        df.to_csv(export_file_path + ".csv", index=index_number)
    elif file_format == "3":
        df.to_json(export_file_path + ".json", orient="records")
    elif file_format == "4":
        df.to_markdown(export_file_path + ".md", index=index_number)
    elif file_format == "5":
        df.to_markdown(export_file_path + ".html", index=index_number)
    elif file_format == "6":
        df.to_xml(export_file_path + ".xml", index=index_number)
    elif file_format == "7":
        df.to_csv(export_file_path + ".txt", sep=" ", index=index_number)
    elif file_format == "8":
        df.to_csv(export_file_path + ".tsv", sep="\t", index=index_number)
    elif file_format == "9":
        delimiter = input("\nTrennzeichen: ")
        df.to_csv(export_file_path + ".txt", sep=delimiter, index=index_number)
    else: print("Keine gültige Auswahl, wird als .xlsx Datei gespeichert")
    print("Datei erfolgreich gespeichert")

# Durchsucht die Tabellen eines Ordners nach verschiedenen Möglichkeiten
def search(directory):
    if not os.path.isdir(directory):
        print(f"Fehler: '{directory}' ist kein gültiges Verzeichnis.")
        return

    all_dfs = []
    print("Lade Dateien...")
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if is_format(file_name):
            df = load_data(file_path)
            if df is not None:
                all_dfs.append(df)

    if all_dfs:
        df = pd.concat(all_dfs, ignore_index=True)
    else:
        print("Keine Datei im Format Checkliste_XXX.X.X.xlsx gefunden")
        return
    df = df[["ID-Anforderung", "Titel", "Inhalt", "Typ", "Entbehrlich", "Begründung für Entbehrlichkeit", "Umsetzung", "Umsetzung bis", "Verantwortlich", "Bemerkungen / Begründung für Nicht-Umsetzung", "Kostenschätzung"]]

    choice = input("Auf welche Art sollen die Tabellen durchsucht werden?\n\n1 - Text\n2 - Regex\n3 - SQL\n\nAuswahl (1-3): ")
    if choice == "1":
        search_term = input("\nSuchbegriff: ")
        mask = df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)
        df = df[mask]
    elif choice == "2":
        regex_pattern = input("\nRegulärer Ausdruck: ")
        mask = df.apply(lambda row: row.astype(str).str.contains(regex_pattern, regex=True).any(), axis=1)
        df = df[mask]
    elif choice == "3":
        sql_pattern = input("\nDie SQL-Abfrage muss \"FROM df\" beinhalten.\nEingabe: ")
        df = duckdb.query(sql_pattern).df()
    else: print("Ungültige Auswahl, Vorgang wird abgebrochen")

    if len(df) == 1:
        print("1 Ergebnis gefunden")
    else: print(f"{len(df)} Ergebnisse gefunden")
    if len(df) == 0:
        return

    export_dir = os.path.join(os.path.abspath(directory), "Search result")
    os.makedirs(export_dir, exist_ok=True)
    export_file_path = os.path.join(export_dir, f"Search result {datetime.today().strftime('%d-%m-%Y')}")
    save_df(df, export_file_path, False)

# Analysiert die abgedeckten elementaren Gefährdungen einer Datei
def risk_analysis(file_path):
    df = load_data(file_path)
    implemented = get_specific_df(df, "Umsetzung", "ja")
    covered_risks = set()
    covered_cia = set()

    id_status = id_check(file_path)
    if id_status == 1:
        ids = implemented["ID-Anforderung"].unique()
    elif id_status == 2:
        ids = [req_id[:-1] for req_id in implemented["ID-Anforderung"].unique()]
    else:
        print(f"Die Datei {file_path} enthält sowohl eindeutige als auch nicht eindeutige IDs, möglicherweise können nicht alle Gefährdungen zugeordnet werden")
        ids = implemented["ID-Anforderung"].unique()

    for req_id in ids:
        for item in mapping.krt:
            if item['id'] == req_id:
                covered_risks.update(item['gefahren'])
                if item['cia']:
                    for char in item['cia']:
                        if char not in covered_cia:
                            covered_cia.add(char)
                break

    return covered_risks, covered_cia

# Handler für Datei oder Ordner
def risk_handler(file_or_dir):
    if os.path.isfile(file_or_dir) and is_format(file_or_dir):
        covered_risks_codes, covered_cia_codes = risk_analysis(file_or_dir)

        print(f"\n--- Analyse für Datei: {os.path.basename(file_or_dir)} ---")

        if covered_risks_codes:
            print("(Teilweise) abgedeckte elementare Gefährdungen:")
            for risk_code in sorted(list(covered_risks_codes)):
                print(f"- {risk_code}: {mapping.gefahren[risk_code]}")
        else:
            print("\nKeine elementaren Gefährdungen abgedeckt.")

        if covered_cia_codes:
            print("\n(Teilweise) abgedeckte CIA-Attribute:")
            for cia_code in sorted(list(covered_cia_codes)):
                full_name = mapping.cia.get(cia_code)
                print(f"- {full_name} ({cia_code})")
        else:
            print("\nKeine CIA-Attribute abgedeckt.")

    elif os.path.isdir(file_or_dir):
        all_covered_risks_across_files = set()
        all_covered_cia_across_files = set()
        processed_files_count = 0

        for file_name in os.listdir(file_or_dir):
            file_path = os.path.join(file_or_dir, file_name)
            if os.path.isfile(file_path) and is_format(file_name):
                covered_risks_for_file, covered_cia_for_file = risk_analysis(file_path)

                all_covered_risks_across_files.update(covered_risks_for_file)
                all_covered_cia_across_files.update(covered_cia_for_file)
                processed_files_count += 1
            else:
                print(f"Skipping: {file_name} (Kein gültiges Dateiformat)")

        if processed_files_count == 0:
            print("Keine gültigen Dateien im Ordner gefunden")
            return

        print(f"\n--- Analyse für Ordner: {os.path.basename(file_or_dir)} ---")

        total_possible_risks = set(mapping.gefahren.keys())
        missing_risks = total_possible_risks - all_covered_risks_across_files

        print("\nSummierte (teilweise) abgedeckte elementare Gefährdungen:")
        if all_covered_risks_across_files:
            for risk_code in sorted(list(all_covered_risks_across_files)):
                print(f"- {risk_code}: {mapping.gefahren[risk_code]}")
        else:
            print("Keine elementaren Gefährdungen abgedeckt.")

        if missing_risks:
            print("\nAn keiner Stelle abgedeckte elementare Gefährdungen:")
            for risk_code in sorted(list(missing_risks)):
                print(f"- {risk_code}: {mapping.gefahren[risk_code]}")
        else:
            print("\nAlle möglichen elementaren Gefährdungen sind an mind. einer Stelle abgedeckt!")

        total_possible_cia = set(mapping.cia.keys())
        missing_cia = total_possible_cia - all_covered_cia_across_files

        if all_covered_cia_across_files:
            print("\nSummierte (teilweise) abgedeckte CIA-Attribute:")
            for cia_code in sorted(list(all_covered_cia_across_files)):
                full_name = mapping.cia.get(cia_code, cia_code)
                print(f"- {full_name} ({cia_code})")

        if missing_cia:
            print("\nNoch nicht an mind. einer Stelle abgedeckte CIA-Attribute:")
            for cia_code in sorted(list(missing_cia)):
                full_name = mapping.cia.get(cia_code, cia_code)
                print(f"- {full_name} ({cia_code})")

    else:
        print("Kein gültiger Pfad: Bitte geben Sie eine gültige Datei im Format Checkliste_XXX.X.X.xlsx oder einen Ordner an.")

# Überprüft, ob IDs eindeutig sind
def id_check(file_or_dir):
    if os.path.isfile(file_or_dir):
        df = load_data(file_or_dir)
        df = df[["ID-Anforderung"]].dropna()

        if df["ID-Anforderung"].astype(str).str.match(r'.*\d$').all():
            return 1
        else:
            if df["ID-Anforderung"].duplicated().any():
                return 3
            else:
                return 2
    else:
        results = {}
        for file_name in os.listdir(file_or_dir):
            file_path = os.path.join(file_or_dir, file_name)
            if os.path.isfile(file_path) and is_format(file_name):
                df = load_data(file_path)
                df = df[["ID-Anforderung"]].dropna()

                if df["ID-Anforderung"].astype(str).str.match(r'.*\d$').all():
                    results[file_name] = 1
                else:
                    if df["ID-Anforderung"].duplicated().any():
                        results[file_name] = 3
                    else:
                        results[file_name] = 2

        unique_values = set(results.values())
        if len(unique_values) == 1:
            return unique_values.pop()
        else:
            status_map = {1: "Nicht eindeutige IDs", 2: "Eindeutige IDs", 3: "Gemischte IDs"}
            return {file: status_map.get(status) for file, status in results.items()}

# Setzt die IDs einer Datei, eindeutig bei 1, zurück auf nicht eindeutig bei 2
def id_setter(file, mode):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook.active

    if mode == 1:
        id_counts = defaultdict(int)
        for row in range(6, sheet.max_row + 1):
            cell = sheet.cell(row=row, column=2)
            original_value = str(cell.value) if cell.value else ""
            if original_value:
                letter_to_add = string.ascii_lowercase[id_counts[original_value]]
                cell.value = f"{original_value}{letter_to_add}"
                id_counts[original_value] += 1

    elif mode == 2:
        for row in range(6, sheet.max_row + 1):
            cell = sheet.cell(row=row, column=2)
            if cell.value and isinstance(cell.value, str) and cell.value[-1].isalpha():
                cell.value = cell.value[:-1]

    workbook.save(file)

# Behandelt für Dateien und Ordner, wie mit der Eindeutigmachung der IDs umgegangen werden soll
def id_handler(file_or_dir):
    if os.path.isfile(file_or_dir) and is_format(file_or_dir):
        mode = id_check(file_or_dir)
        if mode not in [1,2]:
            print("Sowohl eindeutige als auch nicht eindeutige IDs in der Datei vorhanden. Vorgang wird abgebrochen.")
            return
        id_setter(file_or_dir, mode)
        if mode == 1: print("Eindeutige IDs erfolgreich hinzugefügt")
        elif mode == 2: print("Eindeutige IDs erfolgreich wieder entfernt")
    elif os.path.isdir(file_or_dir):
        print("Starte ID-Modifikation...")
        mode = id_check(file_or_dir)
        if mode not in [1,2]:
            print("Sowohl eindeutige als auch nicht eindeutige IDs gefunden, wie soll verfahren werden?")
            choice = input("\n1. Alle IDs eindeutig machen\n2. Alle IDs auf nicht eindeutig zurücksetzen\n3. Liste ausgeben\n4. Abbruch\n\nAuswahl: ").strip()
            if choice in ['1','2']:
                mode = int(choice)
            elif choice == '3':
                for file, status in mode.items():
                    print(f"- {file}: {status}")
                print("\nWie soll verfahren werden?")
                choice2 = input("\n1. Alle IDs eindeutig machen\n2. Alle IDs auf nicht eindeutig zurücksetzen\n3. Abbruch\n\nAuswahl: ").strip()
                if choice2 in ['1','2']:
                    mode = int(choice2)
                elif choice2 == '3':
                    print("Vorgang wird abgebrochen")
                    return
                else:
                    print("Ungültige Auswahl, Vorgang wird abgebrochen.")
                    return
            elif choice == '4':
                print("Vorgang wird abgebrochen.")
                return
            else:
                print("Ungültige Auswahl, Vorgang wird abgebrochen.")
                return

        for file_name in os.listdir(file_or_dir):
            if is_format(file_name):
                file_path = os.path.join(file_or_dir, file_name)
                id_setter(file_path, mode)
        if mode == 1: print("Eindeutige IDs erfolgreich hinzugefügt")
        elif mode == 2: print("Eindeutige IDs erfolgreich wieder entfernt")
    else: print("Keine gültige Datei gefunden")

def main():
    parser = argparse.ArgumentParser(description='Arbeitet mit IT-Grundschutz-Check Excel Tabellen')
    parser.add_argument('file_or_dir', nargs="?", help='Pfad zur Datei oder zum Ordner')
    parser.add_argument('--mapping', action='store_true', help='Ordne der/den Tabelle(n) den Namen des Bausteins zu')
    parser.add_argument('--prozent', action='store_true', help='Zeigt wie viel Prozent eines Bausteins umgesetzt sind (ENTFALLEN und Entbehrlich wird ignoriert, Teilweise zählt als nicht umgesetzt)')
    parser.add_argument('--profil', action='store_true', help='Verschiebt nicht relevante Bausteine in einen Ordner nach IT-Grundschutz-Profilen (Menü öffnet sich); Auch für IT-Grundschutz-PDFs nutzbar')
    parser.add_argument('--ignore-standard', action='store_true', help='Setzt alle leeren Standard Anforderungen auf entbehrlich')
    parser.add_argument('--ignore-hoch', action='store_true', help='Setzt alle leeren Anforderungen des erhöhten Schutzbedarfs auf entbehrlich')
    parser.add_argument('--fully', action='store_true', help='(Mit --ignore-[...]) Setzt auch Anforderungen mit Umsetzung = Ja/Nein/Teilweise auf entbehrlich')
    parser.add_argument('--list', action='store_true', help='Listet Dateien eines Ordners nach verschiedene Kriterien (Menü öffnet sich)')
    parser.add_argument('--wiba-transfer', action='store_true', help='Markiert alle leeren, in WiBA enthaltenen Anforderungen als umgesetzt')
    parser.add_argument('--set-scale', action='store_true', help='Ändert die Umsetzungsskala. Führt evtl. zu Funktionseinschränkungen des Tools.')
    parser.add_argument('--export', action='store_true', help='Exportiere beliebige Spalten der Dateien in verschiedene Formate')
    parser.add_argument('--report', action='store_true', help='Erstelle einen PDF-Report für eine oder alle Dateien')
    parser.add_argument('--merge', nargs=2, metavar=("file1", "file2"), help="Führt zwei Tabellen der selben Art zusammen und behandelt Konflikte")
    parser.add_argument('--modify', action='store_true', help='Modifiziert alle Bausteine eines Ordners im docx-Format, wahlweise Export zu PDF (Menü öffnet sich)')
    parser.add_argument('--search', action='store_true', help='Durchsuche alle Tabellen eines Ordners auf verschiedene Arten')
    parser.add_argument('--risks', action='store_true', help='Zeigt die von umgesetzten Anforderungen abgedeckten elementaren Gefährdungen an')
    parser.add_argument('--id', action='store_true', help='Gibt den einzelnen Anforderungen eine eindeutige ID bzw. entfernt sie wieder')


    args = parser.parse_args()

    actions = {
        args.mapping: lambda: map_xlsx_files(args.file_or_dir),
        args.prozent: lambda: percentages(args.file_or_dir),
        args.profil: lambda: profile_handler(args.file_or_dir),
        args.ignore_standard: lambda: ignore_empty_requirements_handler(args.file_or_dir, "Typ", "Standard","Umsetzung", args.fully),
        args.ignore_hoch: lambda: ignore_empty_requirements_handler(args.file_or_dir, "Typ", "Hoch", "Umsetzung", args.fully),
        args.list: lambda: sort_list(args.file_or_dir),
        args.wiba_transfer: lambda: wiba_transfer(args.file_or_dir),
        args.set_scale: lambda: scale_setter_handler(args.file_or_dir),
        args.export: lambda: export_handler(args.file_or_dir),
        args.report: lambda: report(args.file_or_dir),
        args.modify: lambda: modify(args.file_or_dir),
        args.search: lambda: search(args.file_or_dir),
        args.risks: lambda: risk_handler(args.file_or_dir),
        args.id: lambda: id_handler(args.file_or_dir)
    }

    for condition, action in actions.items():
        if condition:
            action()
            return

    if args.merge:
        merge_tables(args.merge[0], args.merge[1])
        return

    if args.file_or_dir:
        if os.path.isfile(args.file_or_dir):
            analyze_single_file(args.file_or_dir)
        elif os.path.isdir(args.file_or_dir):
            analyze_all_files(args.file_or_dir)
        else:
            print("Datei oder Ordner nicht gefunden")
    else: print("Fehlendes Argument file_or_dir")


if __name__ == '__main__':
    main()
