### EE374 Project Phase 2 ###
###  Arda Unver  2444081  ###

import csv
import math


def termproject(input_txt_file, input_csv_file):
    studentID = 2444081

    # Open the text file in read mode
    with open(input_txt_file, "r") as file:
        # Read all lines from the file
        lines = file.readlines()

        # Choose the row number you want to read

        # At the first index (second row), Sbase (MVA) is written
        row = lines[1]
        # Remove any trailing newline character
        Sbase = float(row.rstrip("\n") + "e6")

        # At the third index (fourth row), Vbase (kV) is written
        row = lines[3]
        # Remove any trailing newline character
        Vbase = float(row.rstrip("\n") + "e3")

        # At the 7th index (eight row), Number of bundle conductors per phase is written
        row = lines[7]
        # Remove any trailing newline character
        bundle_per_phase = float(row.rstrip("\n"))

        # At the 9th index (10th row), Bundle distance (m) is written
        row = lines[9]
        # Remove any trailing newline character
        dist_bundle = float(row.rstrip("\n"))

        # At the 11th index (12th row), Length of the line (km) is written
        row = lines[11]
        # Remove any trailing newline character
        len_of_line = row.rstrip("\n")

        # At the 13th index (14th row), ACSR conductor name is written
        row = lines[13]
        # Remove any trailing newline character
        ACSR_Cond_Name = row.rstrip("\n")

        # At the 15th index (16th row), center[0] of the Phase C is written
        row = lines[15]
        # Remove any trailing newline character
        C_center_0 = int(row.rstrip("\n"))
        # At the 16th index (17th row), center[1] of the Phase C is written
        row = lines[16]
        # Remove any trailing newline character
        C_center_1 = int(row.rstrip("\n"))

        # At the 18th index (19th row), center[0] of the Phase B is written
        row = lines[18]
        # Remove any trailing newline character
        B_center_0 = int(row.rstrip("\n"))
        # At the 19th index (20th row), center[1] of the Phase B is written
        row = lines[19]
        # Remove any trailing newline character
        B_center_1 = int(row.rstrip("\n"))

        # At the 21th index (22th row), center[0] of the Phase A is written
        row = lines[21]
        # Remove any trailing newline character
        A_center_0 = int(row.rstrip("\n"))
        # At the 22th index (23th row), center[1] of the Phase A is written
        row = lines[22]
        # Remove any trailing newline character
        A_center_1 = int(row.rstrip("\n"))

    # Open the CSV file
    with open(input_csv_file, "r") as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)

        # Define the target string to search for
        target_string = ACSR_Cond_Name

        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Check if the first element of the row starts with the target string
            if row[0].startswith(target_string):
                # convert inch to m (*= 0.0254) Outside Diameter
                # convert ohm/1000ft to ohm/1000km (*= 0.3048) DC Resistance

                # create the dictionary object with the required key-value pairs
                row_entries_dict = {
                    "Code Word": row[0],
                    "Aluminum Area": row[1],
                    "Stranding": row[2],
                    "Layers of Aluminum": row[3],
                    "Outside Diameter": row[4],
                    "DC Resistance": row[5],
                    "AC Resistance": row[6],
                    "GMR": row[7],
                }
                break

    # for Aluminum Area (cmil) row[1]
    cmil_to_square_meters = 5.067075e-10

    # for Outside Diameter (in) row[4]
    inch_to_meters = 0.0254

    # for DC Resistance 20°C (ohm/1000 ft) row[5]
    ohm_per_1000ft_to_ohm_per_meter = 3.28084

    # for AC 50 Hz Resistance 20°C (ohm/mi) row[6]
    ohm_per_mi_to_ohm_per_m = 0.621371192 / 1000

    # for GMR (ft) row[7]
    ft_to_meters = 0.3048

    outside_diameter = float(row_entries_dict["Outside Diameter"]) * inch_to_meters

    ac_resistance = float(row_entries_dict["AC Resistance"]) * ohm_per_mi_to_ohm_per_m

    GMR = float(row_entries_dict["GMR"]) * ft_to_meters

    len_of_line = float(len_of_line) * 1000

    # result = [studentID, Sbase, Vbase, bundle_per_phase, dist_bundle, len_of_line, ACSR_Cond_Name,
    #          outside_diameter, ac_resistance, GMR]

    r_eq_bundle = outside_diameter
    GMRc = GMR

    # For per unit calculations
    Z_base = Vbase**2 / Sbase

    distance_BC = math.sqrt(
        (B_center_0 - C_center_0) ** 2 + (B_center_1 - C_center_1) ** 2
    )
    distance_CA = math.sqrt(
        (C_center_0 - A_center_0) ** 2 + (C_center_1 - A_center_1) ** 2
    )
    distance_AB = math.sqrt(
        (A_center_0 - B_center_0) ** 2 + (A_center_1 - B_center_1) ** 2
    )
    GMD = (distance_AB * distance_BC * distance_CA) ** (1 / 3)

    # For the earth
    H_AA = 2 * A_center_1
    H_BB = 2 * B_center_1
    H_CC = 2 * C_center_1
    H_AB = math.sqrt((A_center_0 - B_center_0) ** 2 + (A_center_1 + B_center_1) ** 2)
    H_BC = math.sqrt((B_center_0 - C_center_0) ** 2 + (B_center_1 + C_center_1) ** 2)
    H_CA = math.sqrt((C_center_0 - A_center_0) ** 2 + (C_center_1 + A_center_1) ** 2)

    # Same as H_AB, H_BC, H_CA
    H_AC = math.sqrt((A_center_0 - C_center_0) ** 2 + (A_center_1 + C_center_1) ** 2)
    H_BA = math.sqrt((B_center_0 - A_center_0) ** 2 + (B_center_1 + A_center_1) ** 2)
    H_CB = math.sqrt((C_center_0 - B_center_0) ** 2 + (C_center_1 + B_center_1) ** 2)

    outside_radius = outside_diameter / 2

    if bundle_per_phase == 1:
        GMR_bundle = GMRc
        r_eq_bundle = outside_radius

    elif bundle_per_phase == 2:
        GMR_bundle = (GMRc * dist_bundle) ** (1 / 2)
        r_eq_bundle = (outside_radius * dist_bundle) ** (1 / 2)

    elif bundle_per_phase == 3:
        GMR_bundle = (GMRc * dist_bundle**2) ** (1 / 3)
        r_eq_bundle = (outside_radius * dist_bundle**2) ** (1 / 3)

    elif bundle_per_phase == 4:
        GMR_bundle = 1.09 * ((GMRc * dist_bundle**3) ** (1 / 4))
        r_eq_bundle = 1.09 * ((outside_radius * dist_bundle**3) ** (1 / 4))

    elif bundle_per_phase == 5:
        diagonal_1_squared = 2 * (dist_bundle**2) * (1 - math.cos(math.radians(108)))
        GMR_bundle = (GMRc * (dist_bundle**2) * diagonal_1_squared) ** (1 / 5)
        r_eq_bundle = (
            outside_radius * (dist_bundle**2) * (diagonal_1_squared**2)
        ) ** (1 / 5)

    elif bundle_per_phase == 6:
        diagonal_1_squared = 3 * (dist_bundle**2)
        diagonal_2 = 2 * dist_bundle
        GMR_bundle = (GMRc * (dist_bundle**2) * diagonal_1_squared * diagonal_2) ** (
            1 / 6
        )
        r_eq_bundle = (
            outside_radius * (dist_bundle**2) * diagonal_1_squared * diagonal_2
        ) ** (1 / 6)

    elif bundle_per_phase == 7:
        diagonal_1_squared = (
            2 * (dist_bundle**2) * (1 - math.cos(math.radians(128.57)))
        )
        diagonal_2_squared = (
            diagonal_1_squared
            + (dist_bundle**2)
            - (
                2
                * (diagonal_1_squared ** (0.5))
                * dist_bundle
                * math.cos(math.radians(128.57 - 25.71))
            )
        )
        GMR_bundle = (
            GMRc * (dist_bundle**2) * diagonal_1_squared * diagonal_2_squared
        ) ** (1 / 7)
        r_eq_bundle = (
            outside_radius
            * (dist_bundle**2)
            * diagonal_1_squared
            * diagonal_2_squared
        ) ** (1 / 7)

    elif bundle_per_phase == 8:
        diagonal_1_squared = (dist_bundle**2) * (1 + math.sqrt(2))
        diagonal_2_squared = (
            diagonal_1_squared
            + (dist_bundle**2)
            - (
                2
                * (diagonal_1_squared ** (0.5))
                * dist_bundle
                * math.cos(math.radians(135 - 22.5))
            )
        )
        diagonal_3_squared = (
            diagonal_2_squared
            + (dist_bundle**2)
            - (
                2
                * (diagonal_2_squared ** (0.5))
                * dist_bundle
                * math.cos(math.radians(135 - 22.5 - 22.5))
            )
        )
        GMR_bundle = (
            GMRc
            * (dist_bundle**2)
            * diagonal_1_squared
            * diagonal_2_squared
            * (diagonal_3_squared ** (0.5))
        ) ** (1 / 8)
        r_eq_bundle = (
            outside_radius
            * (dist_bundle**2)
            * diagonal_1_squared
            * diagonal_2_squared
            * (diagonal_3_squared ** (0.5))
        ) ** (1 / 8)

    else:
        print("Invalid bundle per phase value.")

    total_resistance = ac_resistance * len_of_line / bundle_per_phase
    Inductance_per_meter = 2 * math.log(GMD / GMR_bundle) * 10**-7

    total_inductance = 2 * math.pi * 50 * Inductance_per_meter * len_of_line

    first_element = math.log(GMD / r_eq_bundle)
    second_element = math.log(
        ((H_AB * H_CA * H_BC) ** (1 / 3)) / ((H_AA * H_BB * H_CC) ** (1 / 3))
    )

    Shunt_Capacitance_per_meter = (
        2 * math.pi * 8.85 * 10**-12 / (first_element - second_element)
    )

    total_Shunt_Susceptance = (
        2 * math.pi * 50 * Shunt_Capacitance_per_meter * len_of_line
    )

    total_resistance_pu = total_resistance / Z_base
    total_inductance_pu = total_inductance / Z_base
    total_shunt_susceptance_pu = total_Shunt_Susceptance / (1 / Z_base)

    result = [
        float(studentID),
        float(total_resistance_pu),
        float(total_inductance_pu),
        float(total_shunt_susceptance_pu),
    ]

    return result


if __name__ == "__main__":
    result = termproject("Input_file_example.txt", "library.csv")

    print(result)
