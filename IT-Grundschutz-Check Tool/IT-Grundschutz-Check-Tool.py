import argparse
import os
import shutil
import openpyxl
import openpyxl.utils
import pandas as pd
from openpyxl.worksheet.datavalidation import DataValidation

import mapping


# Gibt zurück, ob eine Datei dem Format der Checkliste entspricht
def is_format(filename_or_path):
    if filename_or_path.endswith('.xlsx') and "Checkliste_" in filename_or_path:
        return True
    else: return False

# Gibt den Namen eines Bausteins anhand des Dateinamens zurück, entweder kurz "APP.1.1" oder lang "Office Produkte"
def get_name(filename, short):
    if is_format(filename):
        ref = filename.split(".xlsx")[0].split('Checkliste_')[1]
        if short:
            return ref
        return mapping.bsi_ref_titles[ref]

    elif is_pdf(filename):
        ref = filename.split()[0]
        if ref.startswith("CCON"):
            ref = "CON" + ref[4:]
        if short:
            return ref
        return mapping.bsi_ref_titles[ref]
    return None

# Überprüft, ob eine PDF den Namen eines IT-Grundschutz Bausteins hat
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
        print(f"Fehler: Die Datei zu {get_name(file_path, True)} ist möglicherweise geöffnet und kann nicht gelesen werden. Vorgang wird abgebrochen.")
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
    return df[(df[column].isna() | (df[column].fillna('').str.strip().str.lower() == value)) & (df[column2].isna() | (df[column2].fillna('').str.strip().str.lower() == value2))]

# Gibt Zahlen zurück, wie viele Anforderungen entbehrlich sowie nicht, teilweise oder ganz erfüllt sind
def implementation_count(df):
    not_implemented = get_specific_df_with_two_conditions_and_emptiness(df, "Umsetzung", "nein", "Entbehrlich", "nein")
    partly_implemented = df[df["Umsetzung"].fillna("").astype(str).str.strip().str.lower() == "teilweise"]
    fully_implemented = df[df["Umsetzung"].fillna("").astype(str).str.strip().str.lower() == "ja"]
    unnecessary = df[df["Entbehrlich"].fillna("").astype(str).str.strip().str.lower() == "ja"]
    return len(not_implemented), len(partly_implemented), len(fully_implemented), len(unnecessary)

# Summiert die Kostenspalte
def cost_count(df):
    return (df["Kostenschätzung"]).sum()

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

    # Statistik ausgeben
    print(f"Gesamtanzahl Anforderungen: {len(df)}")
    print(f"Umgesetzte Anforderungen: {fully_implemented}")
    print(f"Teilweise umgesetzte Anforderungen: {partly_implemented}")
    print(f"Entbehrliche Anforderungen: {unnecessary}")
    print(f"Nicht umgesetzte Anforderungen: {not_implemented}")
    print(f"(davon Basis: {ni_basis}, Standard: {ni_standard}, Erhöhter Schutzbedarf: {ni_high})")
    print(f"Summierte Kostenschätzung: {cost}€")
    print(f"Verantwortliche: {all_responsibles}")

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
    if total_files == 0:
        print("Keine Dateien im Format Checkliste_XXX.X.X.xlsx gefunden")
        return

    print(f"Analysierte Tabellen: {total_files}")
    print(f"Gesamtanzahl Anforderungen: {total_df_count}")
    print(f"Umgesetzte Anforderungen: {total_fully_implemented}")
    print(f"Teilweise umgesetzte Anforderungen: {total_partly_implemented}")
    print(f"Entbehrliche Anforderungen: {total_unnecessary}")
    print(f"Nicht umgesetzte Anforderungen: {total_not_implemented}")
    print(f"(davon Basis: {total_basis}, Standard: {total_standard}, Erhöhter Schutzbedarf: {total_high})")
    print(f"Summierte Kostenschätzung: {total_cost}€")

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

    wb.save(file_path)
    if not fully:
        print(f"Alle leeren {value}-Anforderungen von {get_name(file_path, True)} wurden auf entbehrlich gesetzt und gespeichert.")
    else:
        print(f"Alle {value}-Anforderungen von {get_name(file_path, True)} wurden auf entbehrlich gesetzt und gespeichert.")

# Handler für Datei oder Ordner
def ignore_empty_requirements_handler(path, column, value, second_empty_type, fully):
    if os.path.isdir(path):
        for file in os.listdir(path):
            if is_format(file):
                file_path = os.path.join(path, file)
                ignore_empty_requirements(file_path, column, value, second_empty_type, fully)
    elif os.path.isfile(path) and is_format(path):
        ignore_empty_requirements(path, column, value, second_empty_type, fully)
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
            due_date = set(df["Umsetzung bis"].dropna().unique())

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

    # Überprüfung, ob Inhalt und ID gleich sind, da der Inhalt einiger Anforderungen doppelt vorkommt
    mask = (
            df["Inhalt"].isin(wiba) &
            df["ID-Anforderung"].isin(wiba_ids) &
            df["Inhalt"].map(wiba_mapping).notna() &
            (df["ID-Anforderung"] == df["Inhalt"].map(
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
        col_letter = openpyxl.utils.get_column_letter(df.columns.get_loc("Umsetzung") + 1)
        ws[f"{col_letter}{excel_row}"].value = "Ja"
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

    # Datei speichern
    original_dir = os.path.dirname(file_path)
    output_dir = os.path.join(original_dir, "Modifizierte Dateien")

    os.makedirs(output_dir, exist_ok=True)

    filename = f"Checkliste_{get_name(file_path, True)}_modified.xlsx"
    output_path = os.path.join(output_dir, filename)
    wb.save(output_path)



def main():
    parser = argparse.ArgumentParser(description='Arbeitet mit IT-Grundschutz-Check Excel Tabellen')
    parser.add_argument('file_or_dir', help='Pfad zur Datei oder zum Ordner')
    parser.add_argument('--mapping', action='store_true', help='Ordne der/den Tabelle(n) den Namen des Bausteins zu')
    parser.add_argument('--prozent', action='store_true', help='Zeigt wie viel Prozent eines Bausteins umgesetzt sind (ENTFALLEN und Entbehrlich wird ignoriert, Teilweise zählt als nicht umgesetzt)')
    parser.add_argument('--profil', action='store_true', help='Verschiebt nicht relevante Bausteine in einen Ordner nach IT-Grundschutz-Profilen (Menü öffnet sich); Auch für IT-Grundschutz-PDFs nutzbar')
    parser.add_argument('--ignore-standard', action='store_true', help='Setzt alle leeren Standard Anforderungen auf entbehrlich')
    parser.add_argument('--ignore-hoch', action='store_true', help='Setzt alle leeren Anforderungen des erhöhten Schutzbedarfs auf entbehrlich')
    parser.add_argument('--fully', action='store_true', help='(Mit --ignore-[...]) Setzt auch Anforderungen mit Umsetzung = Ja/Nein/Teilweise auf entbehrlich')
    parser.add_argument('--list', action='store_true', help='Listet Dateien eines Ordners nach verschiedene Kriterien (Menü öffnet sich)')
    parser.add_argument('--wiba-transfer', action='store_true', help='Markiert alle leeren, in WiBA enthaltenen Anforderungen als umgesetzt')
    parser.add_argument('--set-scale', action='store_true', help='Ändert die Umsetzungsskala')

    args = parser.parse_args()

    if args.mapping:
        map_xlsx_files(args.file_or_dir)

    elif args.prozent:
        percentages(args.file_or_dir)

    elif args.profil:
        profile_handler(args.file_or_dir)

    elif args.ignore_standard:
        ignore_empty_requirements_handler(args.file_or_dir, "Typ", "Standard", "Umsetzung", args.fully)

    elif args.ignore_hoch:
        ignore_empty_requirements_handler(args.file_or_dir, "Typ", "Hoch", "Umsetzung", args.fully)

    elif args.list:
        sort_list(args.file_or_dir)

    elif args.wiba_transfer:
        wiba_transfer(args.file_or_dir)

    elif args.set_scale:
        scale_setter_handler(args.file_or_dir)

    elif os.path.isfile(args.file_or_dir):
        analyze_single_file(args.file_or_dir)

    elif os.path.isdir(args.file_or_dir):
        analyze_all_files(args.file_or_dir)

    else: print("Datei oder Ordner nicht gefunden")


if __name__ == '__main__':
    main()
