import csv


def termproject(text_path: str, library_path: str):
    text = {}

    with open(text_path, "r") as file:
        # Read the file and remove the \n
        lines = [line.strip() for line in file]

        # Get the values from the input file
        s_base = lines[1]
        v_base = lines[3]
        number_of_circuits = lines[5]
        number_of_bundles = lines[7]
        bundle_distance = lines[9]
        length_of_line = lines[11]
        acsr_name = lines[13]
        c1_phase_c = lines[15:17]
        c1_phase_a = lines[18:20]
        c1_phase_b = lines[21:23]

        # Create a dictionary with the values
        text = {
            "s_base": s_base,
            "v_base": v_base,
            "number_of_circuits": number_of_circuits,
            "number_of_bundles": number_of_bundles,
            "bundle_distance": bundle_distance,
            "length_of_line": length_of_line,
            "acsr_name": acsr_name,
            "c1_phase_c": c1_phase_c,
            "c1_phase_a": c1_phase_a,
            "c1_phase_b": c1_phase_b,
        }

    # print(f"Input text from{text_path}:", "\n", text, "\n")

    #
    library = {}

    # Read library csv file
    with open(library_path, "r") as file:
        reader = csv.reader(file)

        # Exclude title
        title_row = next(reader)
        for row in reader:
            if row[0]:
                library[row[0]] = row[1:]

    # print(f"Library from {library_path}", "\n", library, "\n")

    acsr_name = text["acsr_name"]
    acsr_data = library[acsr_name]

    acsr_outside_diameter_in = acsr_data[3]
    acsr_ac_resistance_ohm_over_mi = acsr_data[5]
    acsr_gmr_ft = acsr_data[6]

    acsr_outside_diameter_si = float(acsr_outside_diameter_in) * 0.0254
    acsr_ac_resistance_ohm_over_m = float(acsr_ac_resistance_ohm_over_mi) * 1 / 1609.34
    acsr_gmr_si = float(acsr_gmr_ft) * 0.3048

    # print(f"ACSR name: {acsr_name}", f"ACSR data: {acsr_data}", "\n")

    # print(
    #    f"ACSR outside diameter in: ",
    #    acsr_outside_diameter_in,
    #    " SI: ",
    #    acsr_outside_diameter_si,
    # )

    length_of_line = int(text["length_of_line"]) * 1000

    # Add my student ID
    output = ["2443307"]

    output.append(text["s_base"])
    output.append(text["v_base"])
    output.append(text["number_of_bundles"])
    output.append(text["bundle_distance"])
    output.append(length_of_line)
    output.append(acsr_name)
    output.append(acsr_outside_diameter_si)
    output.append(acsr_ac_resistance_o§hm_over_m)
    output.append(acsr_gmr_si)

    print(output)

    return output


termproject("Input_file_example.txt", "library.csv")
