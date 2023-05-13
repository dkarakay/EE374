def termproject(text_path: str, library_path:str):
    input_dict = {}

    with open(text_path, 'r') as file:

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
        c1_phase_b = lines[21:24]

        # Create a dictionary with the values
        input_dict = {
            lines[0]: s_base,
            lines[2]: v_base,
            lines[4]: number_of_circuits,
            lines[6]: number_of_bundles,
            lines[8]: bundle_distance,
            lines[10]: length_of_line,
            lines[12]: acsr_name,
            lines[14]: c1_phase_c,
            lines[17]: c1_phase_a,
            lines[20]: c1_phase_b,
        }

    print(input_dict)
            