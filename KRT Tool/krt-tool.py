import collections

import mapping

def get_baustein_id_for_anforderung(anforderung_id):
    return anforderung_id.split(".A")[0]

def print_glossar(displayed_baustein_ids, displayed_gefaehrdung_ids):
    print("\n" + "=" * 25 + " GLOSSAR " + "=" * 26)

    if displayed_baustein_ids:
        print("\n--- Referenzierte Bausteine ---")
        for b_id in sorted(list(displayed_baustein_ids)):
            title = mapping.bsi_ref_titles.get(b_id)
            print(f"  {b_id}: {title}")

    if displayed_gefaehrdung_ids:
        print("\n--- Referenzierte Gefährdungen ---")
        for g_id in sorted(list(displayed_gefaehrdung_ids)):
            beschreibung = mapping.gefahren.get(g_id)
            print(f"  {g_id}: {beschreibung}")

    #print("\n--- Schutzziele ---")
    #for code, name in mapping.cia.items():
    #    print(f"  {code}: {name}")

    print("=" * 60)


def print_gefaehrdungen():
    print("\n--- Elementare Gefährdungen ---")

    displayed_baustein_ids_glossar = set()
    displayed_gefaehrdung_ids_glossar = set()
    gefaehrdungen_list = list(mapping.gefahren.items())
    for i, (gid, beschreibung) in enumerate(gefaehrdungen_list):
        print(f"  {i + 1}. {gid}: {beschreibung}")

    selected_gefaehrdung_ids = []
    while True:
        try:
            choice_str = input(
                "Wählen Sie eine oder mehrere Gefährdungen (Nummern, z.B. 1,5) oder 'alle': ").strip().lower()
            if choice_str == 'alle':
                selected_gefaehrdung_ids = [gid for gid, _ in gefaehrdungen_list]
                break
            if not choice_str:
                return

            chosen_indices = [int(x.strip()) - 1 for x in choice_str.split(',')]
            temp_selected_ids = []
            valid_selection = True
            for index in chosen_indices:
                if 0 <= index < len(gefaehrdungen_list):
                    temp_selected_ids.append(gefaehrdungen_list[index][0])
                else:
                    print(f"Ungültige Nummer: {index + 1}")
                    valid_selection = False
                    break
            if valid_selection:
                selected_gefaehrdung_ids = list(set(temp_selected_ids))
                if not selected_gefaehrdung_ids:
                    print("Keine gültigen Gefährdungen ausgewählt.")
                    continue
                break
            else:
                selected_gefaehrdung_ids.clear()
        except ValueError:
            print("Ungültige Eingabe")

    print(f"\nAusgewählte Gefährdung(en): {', '.join(selected_gefaehrdung_ids)}")

    multi = False
    if len(selected_gefaehrdung_ids) > 1:
        multi_choice = input("Nur Anforderungen anzeigen, die alle ausgewählte Gefährdungen abdecken? (j/N): ").lower()
        if multi_choice == 'j' or multi_choice == 'ja':
            multi = True


    anforderungen_fuer_gefaehrdungen = []
    for anforderung_krt in mapping.krt:
        anforderung_gefahren = set(anforderung_krt.get('gefahren', []))

        if multi:
            if all(gid in anforderung_gefahren for gid in selected_gefaehrdung_ids):
                anforderungen_fuer_gefaehrdungen.append(anforderung_krt)
        else:
            if any(gid in anforderung_gefahren for gid in selected_gefaehrdung_ids):
                anforderungen_fuer_gefaehrdungen.append(anforderung_krt)

    if not anforderungen_fuer_gefaehrdungen:
        print("Für die ausgewählten Gefährdungen wurden keine passenden Anforderungen in den Kreuzreferenztabellen gefunden.")
        return

    filtered_anforderungen = list(anforderungen_fuer_gefaehrdungen)

    while True:
        schutzziel_filter_choice = input("Möchten Sie zusätzlich nach Schutzzielen filtern? (j/N): ").strip().lower()
        if schutzziel_filter_choice == 'j' or schutzziel_filter_choice == 'ja':
            print("Schutzziele zur Filterung:")
            schutzziel_options = {}
            for code, name in mapping.cia.items():
                count = sum(
                    1 for an_krt in anforderungen_fuer_gefaehrdungen if an_krt.get('cia') and code in an_krt['cia'])
                print(f"  {code.upper()}: {name} ({count} passende Anforderungen)")
                schutzziel_options[code.upper()] = count

            selected_schutzziel_code = input(
                "Wählen Sie ein Schutzziel (C, I, A) oder 'keins' für keinen Filter: ").strip().upper()

            if selected_schutzziel_code in schutzziel_options:
                filtered_anforderungen = [
                    an_krt for an_krt in anforderungen_fuer_gefaehrdungen
                    if an_krt.get('cia') and selected_schutzziel_code in an_krt['cia']
                ]
                if not filtered_anforderungen:
                    print(
                        f"Keine Anforderungen erfüllen das Schutzziel '{selected_schutzziel_code}' in der aktuellen Auswahl.")
                    return
                print(f"Filter angewendet. {len(filtered_anforderungen)} Anforderungen verbleiben.")
                break
            elif selected_schutzziel_code == 'KEINS':
                break
            else:
                print("Ungültige Schutzziel-Auswahl.")
        else: break

    relevant_baustein_ids = set()
    anforderungen_per_baustein = collections.defaultdict(list)

    for an_krt in filtered_anforderungen:
        b_id = get_baustein_id_for_anforderung(an_krt['id'])
        if b_id:
            relevant_baustein_ids.add(b_id)
            anforderungen_per_baustein[b_id].append(an_krt)

    print("\nWählen Sie die Ansicht für die Ergebnisse:")
    print(f"  1. Betroffene Bausteine anzeigen ({len(relevant_baustein_ids)})")
    print(f"  2. Betroffene Anforderungen anzeigen ({len(filtered_anforderungen)})")

    while True:
        view_choice = input("Ihre Wahl (1 oder 2): ").strip()
        if view_choice == '1':
            print("\n--- Betroffene Bausteine ---")

            bausteine_list = sorted(list(relevant_baustein_ids))
            for i, b_id in enumerate(bausteine_list):
                title = mapping.bsi_ref_titles.get(b_id)
                num_anforderungen = len(anforderungen_per_baustein[b_id])
                print(f"  {i + 1}. {b_id}: {title} ({num_anforderungen})")

            while True:
                select_baustein_choice = input(
                    "\nBaustein anzeigen (Nummer): ").strip().lower()
                try:
                    chosen_baustein_index = int(select_baustein_choice) - 1
                    if 0 <= chosen_baustein_index < len(bausteine_list):
                        selected_b_id = bausteine_list[chosen_baustein_index]
                        print(
                            f"\n--- Anforderungen für Baustein {selected_b_id}: {mapping.bsi_ref_titles.get(selected_b_id)} ---")
                        for an_krt in sorted(anforderungen_per_baustein[selected_b_id], key=lambda x: x['id']):
                            print(f"  Anforderung: {an_krt['id']} - {an_krt.get('name')}")
                            cia_info = an_krt.get('cia')
                            gefahren_info = ", ".join(an_krt.get('gefahren', []))
                            displayed_gefaehrdung_ids_glossar.update(an_krt.get('gefahren', []))
                            if cia_info is None:
                                print(f"    Gefährdungen: {gefahren_info}")
                            else:
                                print(f"    CIA: {cia_info}, Gefährdungen: {gefahren_info}")

                        print("-" * 60)
                    else:
                        print(f"Ungültige Nummer: {chosen_baustein_index + 1}")
                except ValueError:
                    print("Ungültige Eingabe.")
                print_glossar(displayed_baustein_ids_glossar, displayed_gefaehrdung_ids_glossar)
        elif view_choice == '2':
            print("\n--- Betroffene Anforderungen ---")
            for an_krt in sorted(filtered_anforderungen, key=lambda x: x['id']):
                print(f"  Anforderung: {an_krt['id']} - {an_krt.get('name')}")
                cia_info = an_krt.get('cia')
                gefahren_info = ", ".join(an_krt.get('gefahren', []))
                displayed_gefaehrdung_ids_glossar.update(an_krt.get('gefahren', []))
                displayed_baustein_ids_glossar.add(get_baustein_id_for_anforderung(an_krt['id']))
                if cia_info is None:
                    print(f"    Gefährdungen: {gefahren_info}")
                else:
                    print(f"    CIA: {cia_info}, Gefährdungen: {gefahren_info}")
            print_glossar(displayed_baustein_ids_glossar, displayed_gefaehrdung_ids_glossar)
            break
        else:
            print("Ungültige Wahl.")


def print_bausteine():
    print("\n--- Baustein Übersicht ---")

    displayed_baustein_ids_glossar = set()
    displayed_gefaehrdung_ids_glossar = set()
    baustein_list = list(mapping.bsi_ref_titles.items())
    for i, (ref, title) in enumerate(baustein_list):
        print(f"  {i + 1}. {ref}: {title}")

    selected_baustein_ids = []
    while True:
        try:
            choice_str = input(
                "Wählen Sie einen oder mehrere Bausteine (Nummern, z.B. 1,5) oder 'alle': ").strip().lower()
            if choice_str == 'alle':
                selected_baustein_ids = [id for id, _ in baustein_list]
                break
            if not choice_str:
                return

            chosen_indices = [int(x.strip()) - 1 for x in choice_str.split(',')]
            temp_selected_ids = []
            valid_selection = True
            for index in chosen_indices:
                if 0 <= index < len(baustein_list):
                    temp_selected_ids.append(baustein_list[index][0])
                else:
                    print(f"Ungültige Nummer: {index + 1}")
                    valid_selection = False
                    break
            if valid_selection:
                selected_baustein_ids = list(set(temp_selected_ids))
                if not selected_baustein_ids:
                    print("Keine gültigen Bausteine ausgewählt.")
                    continue
                break
            else:
                selected_baustein_ids.clear()
        except ValueError:
            print("Ungültige Eingabe")

    print(f"\nAusgewählte Bausteine: {', '.join(selected_baustein_ids)}")

    filtered_anforderungen = []
    for anforderung_krt in mapping.krt:
        b_id = get_baustein_id_for_anforderung(anforderung_krt['id'])
        if b_id in selected_baustein_ids:
            filtered_anforderungen.append(anforderung_krt)

    if not filtered_anforderungen:
        print("Für die ausgewählten Bausteine wurden keine passenden Anforderungen gefunden.")
        return

    print("\n--- Anforderungen ---")
    for an_krt in sorted(filtered_anforderungen, key=lambda x: x['id']):
        print(f"  Anforderung: {an_krt['id']} - {an_krt.get('name')}")
        cia_info = an_krt.get('cia')
        gefahren_info = ", ".join(an_krt.get('gefahren', []))
        displayed_gefaehrdung_ids_glossar.update(an_krt.get('gefahren', []))
        displayed_baustein_ids_glossar.add(get_baustein_id_for_anforderung(an_krt['id']))
        if cia_info is None:
            print(f"    Gefahren: {gefahren_info}")
        else:
            print(f"    CIA: {cia_info}, Gefahren: {gefahren_info}")
    print_glossar(displayed_baustein_ids_glossar, displayed_gefaehrdung_ids_glossar)

def print_schutzziele():
    print("\n--- Schutzziele ---")

    displayed_baustein_ids_glossar = set()
    displayed_gefaehrdung_ids_glossar = set()
    schutzziel_options = {}
    for code, name in mapping.cia.items():
        count = sum(1 for an_krt in mapping.krt if an_krt.get('cia') and code in an_krt['cia'])
        schutzziel_options[code.upper()] = {'name': name, 'count': count}
        print(f"  {code.upper()}: {name} ({count} passende Anforderungen)")

    selected_schutzziel_codes = []
    while True:
        choice_str = input(
            "Wählen Sie ein oder mehrere Schutzziele (C, I, A, Komma-getrennt, z.B. C,A) oder 'alle': ").strip().upper()
        if choice_str == 'alle':
            selected_schutzziel_codes = list(mapping.cia.keys())
            break
        if not choice_str:
            print("Auswahl abgebrochen.")
            return

        chosen_codes = [x.strip() for x in choice_str.split(',')]
        temp_selected_codes = []
        valid_selection = True
        for code in chosen_codes:
            if code in schutzziel_options:
                temp_selected_codes.append(code)
            else:
                print(f"Ungültiges Schutzziel: {code}")
                valid_selection = False
                break
        if valid_selection:
            selected_schutzziel_codes = list(set(temp_selected_codes))
            if not selected_schutzziel_codes:
                print("Keine gültigen Schutzziele ausgewählt.")
                continue
            break
        else:
            selected_schutzziel_codes.clear()

    if not selected_schutzziel_codes:
        print("Keine Schutzziele ausgewählt.")
        return

    print(f"\nAusgewählte Schutzziele: {', '.join(selected_schutzziel_codes)}")

    multi = False
    if len(selected_schutzziel_codes) > 1:
        multi_choice = input("Nur Anforderungen anzeigen, die alle ausgewählte Schutzziele abdecken? (j/N): ").lower()
        if multi_choice == 'j' or multi_choice == 'ja':
            multi = True

    anforderungen_fuer_schutzziele = []
    for anforderung_krt in mapping.krt:
        anforderung_cia = set(anforderung_krt.get('cia') or [])

        if multi:
            if all(sc in anforderung_cia for sc in selected_schutzziel_codes):
                anforderungen_fuer_schutzziele.append(anforderung_krt)
        else:
            if any(sc in anforderung_cia for sc in selected_schutzziel_codes):
                anforderungen_fuer_schutzziele.append(anforderung_krt)

    if not anforderungen_fuer_schutzziele:
        print("Für die ausgewählten Schutzziele wurden keine passenden Anforderungen gefunden.")
        return

    print("\n--- Gefundene Anforderungen ---")
    for an_krt in sorted(anforderungen_fuer_schutzziele, key=lambda x: x['id']):
        print(f"  Anforderung: {an_krt['id']} - {an_krt.get('name')}")
        cia_info = an_krt.get('cia')
        gefahren_info = ", ".join(an_krt.get('gefahren', []))
        displayed_gefaehrdung_ids_glossar.update(an_krt.get('gefahren', []))
        displayed_baustein_ids_glossar.add(get_baustein_id_for_anforderung(an_krt['id']))
        if cia_info is None:
            print(f"    Gefährdungen: {gefahren_info}")
        else:
            print(f"    CIA: {cia_info}, Gefährdungen: {gefahren_info}")
    print_glossar(displayed_baustein_ids_glossar, displayed_gefaehrdung_ids_glossar)
def suchfunktion():
    print("\n--- Suchfunktion ---")
    displayed_baustein_ids_glossar = set()
    displayed_gefaehrdung_ids_glossar = set()
    search_term = input("Geben Sie den Suchbegriff ein: ").strip().lower()

    if not search_term:
        print("Kein Suchbegriff eingegeben.")
        return

    matching_anforderungen = []
    for anforderung_krt in mapping.krt:
        search_fields = [
            anforderung_krt.get('id', '').lower(),
            anforderung_krt.get('name', '').lower()
        ]
        if 'gefahren' in anforderung_krt:
            search_fields.extend([g.lower() for g in anforderung_krt['gefahren']])
            search_fields.extend([mapping.gefahren.get(g, '').lower() for g in anforderung_krt['gefahren']])

        if any(search_term in field for field in search_fields if field):
            matching_anforderungen.append(anforderung_krt)

    if not matching_anforderungen:
        print(f"Keine Anforderungen gefunden, die den Suchbegriff '{search_term}' enthalten.")
        return

    print(f"\n{len(matching_anforderungen)} Anforderungen gefunden")

    print("\n--- Passende Anforderungen ---")
    for an_krt in sorted(matching_anforderungen, key=lambda x: x['id']):
        print(f"  Anforderung: {an_krt['id']} - {an_krt.get('name')}")
        cia_info = an_krt.get('cia')
        gefahren_info = ", ".join(an_krt.get('gefahren', []))
        displayed_gefaehrdung_ids_glossar.update(an_krt.get('gefahren', []))
        displayed_baustein_ids_glossar.add(get_baustein_id_for_anforderung(an_krt['id']))
        if cia_info is None:
            print(f"    Gefährdungen: {gefahren_info}")
        else:
            print(f"    CIA: {cia_info}, Gefährdungen: {gefahren_info}")
    print_glossar(displayed_baustein_ids_glossar, displayed_gefaehrdung_ids_glossar)

def main():
    print("--- Tool zur Ansicht der Kreuzreferenztabellen des BSI IT-Grundschutzes (2023) ---")

    while True:
        print("\nWählen Sie eine Option per Zahl aus:")
        choice = input("1. Elementare Gefährdungen\n2. Bausteine\n3. Schutzziele\n4. Suchfunktion\n\nAuswahl: ")
        if choice == "1":
            print_gefaehrdungen()
            break
        elif choice == "2":
            print_bausteine()
            break
        elif choice == "3":
            print_schutzziele()
            break
        elif choice == "4":
            suchfunktion()
            break
        else:
            print(f"\nUngültige Auswahl")


if __name__ == '__main__':
    main()
