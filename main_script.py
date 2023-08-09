import subprocess
import os

screenshot_list = ["step_number",
                   "valve_list1",
                   "valve_list2",
                   "valve_states1",
                   "valve_states2"]

# ============================================================================ #
# Functions to call other scripts
# ============================================================================ #


def exec_script(script_name):
    try:
        subprocess.run(['python', script_name])
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}:", e)


def exec_script_arg(script_name, arg):
    try:
        subprocess.run(['python', script_name, arg])
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}:", e)


def exec_script_args(script_name, a, b):
    try:
        subprocess.run(['python', script_name, a, b])
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}:", e)


# ============================================================================ #
# Prompt the user to select an option
# ============================================================================ #

option = 999

while option != 0:
    if option == 1:
        print("************************************************************\n")
        image = input("Which screenshot should be examined?: ")
        print(f"Image {image} selected\n")

    if option == 2:
        for area in screenshot_list:
            print("************************************************************\n"
                f"\nSelect the area to crop for {area}\n")
            exec_script_args("plot_coordinates.py", area, image)
            input("Press Enter to continue to the next area or '0' to exit: \n")

    elif option == 3:
        print("************************************************************\n"
              "Converting Images to Text")
        exec_script('convert_image_to_text.py')

    elif option == 4:
        print("************************************************************\n"
              "Reading State Matrix")
        valve_list = exec_script('read_sequence.py')
        print(valve_list)

    elif option == 5:
        print("************************************************************\n"
              "Taking Screenshots")
       # subprocess.run(['python', 'take_screenshot.py', image])
        exec_script_arg('take_screenshot.py', image)

    elif option == 6:
        print("Comparing Files")

    elif option == 0:
        print("Exiting")

    option = int(input("************************************************************\n"
                   "\nPlease select an option or '0' to exit:\n\n"
                   "\t1: Select Screenshot to examine\n"
                   "\t2: Select Image Areas to Convert\n"
                   "\t3: Convert Images to Text\n"
                   "\t4: Read State Matrix\n"
                   "\t5: Use Existing Coordinates and Take New Screenshots\n"
                   "\t6: Compare Files\n"
                   "\t0: Exit\n"
                   "\nOption: "))
