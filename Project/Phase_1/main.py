import csv


def termproject(text_path: str, library_path: str):
    text = {}

    with open(text_path, "r") as file:
        # Read the file and remove the \n
        lines = [line.strip() for line in file]

        # Get the values from the input file
        s_base = int(lines[1])
        v_base = int(lines[3])
        number_of_circuits = int(lines[5])
        number_of_bundles = int(lines[7])
        bundle_distance = float(lines[9])
        length_of_line = int(lines[11])
        acsr_name = lines[13]

        # Get the values from the input file and convert them to int
        c1_phase_c = [int(line) for line in lines[15:17]]
        c1_phase_a = [int(line) for line in lines[18:20]]
        c1_phase_b = [int(line) for line in lines[21:23]]

        # Create a dictionary with the values from text
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

    library = {}

    # Read library csv file
    with open(library_path, "r") as file:
        reader = csv.reader(file)

        # Exclude title row
        title_row = next(reader)

        # Create a dictionary with the values from library,
        # Set key as ACSR name and value as the rest of the row
        for row in reader:
            if row[0]:
                library[row[0]] = row[1:]

    # Get the ACSR name from the text
    acsr_name = text["acsr_name"]

    # Get the corresponding data from the library
    acsr_data = library[acsr_name]

    # Get only the data that we need
    # Outside_diameter, ac_resistance, gmr
    acsr_outside_diameter_in = acsr_data[3]
    acsr_ac_resistance_ohm_over_mi = acsr_data[5]
    acsr_gmr_ft = acsr_data[6]

    # Convert the data to SI

    # 1 in = 0.0254 m
    acsr_outside_diameter_si = float(acsr_outside_diameter_in) * 0.0254

    # 1 mi = 1609.34 m
    acsr_ac_resistance_ohm_over_m = float(acsr_ac_resistance_ohm_over_mi) * 1 / 1609.34

    # 1 ft = 0.3048 m
    acsr_gmr_si = float(acsr_gmr_ft) * 0.3048

    # 1 km = 1000 m
    length_of_line_m = text["length_of_line"] * 1000

    # Add my student ID
    output = [2443307]

    # Append the values to the output list
    output.append(text["s_base"])
    output.append(text["v_base"])
    output.append(text["number_of_bundles"])
    output.append(text["bundle_distance"])
    output.append(length_of_line_m)
    output.append(acsr_name)
    output.append(acsr_outside_diameter_si)  # type: ignore
    output.append(acsr_ac_resistance_ohm_over_m)  # type: ignore
    output.append(acsr_gmr_si)  # type: ignore

    return output


output = termproject("Input_file_example.txt", "library.csv")
print(output)
