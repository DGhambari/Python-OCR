import tkinter as tk
import subprocess
import convert_image as convert

# ============================================================================ #
# Take screenshots of the areas to be converted to text
# ============================================================================ #

def take_screenshot():
    with open("take_screenshot.py") as f:
        exec(f.read())

# ============================================================================ #
# Convert the images to text
# ============================================================================ #

def convert_images():
    with open("convert_image.py") as f:
        exec(f.read())

# ============================================================================ #
# Open the state matrix and return a list of valves for a particular step
# ============================================================================ #

def read_excel(excel_file):
    with open("read_sequence.py") as f:
        exec(f.read())

# ============================================================================ #
# Prompt the user to select an option
# ============================================================================ #

option = input("Please select an option:\n\n"
                "\t1: Take Screenshot\n"
                "\t2: Convert Images to Text\n"
                "\t3: Read State Matrix\n"
                "\t4: Compare Files\n")

while option != 0:
    if option == 1:
        print("Taking Screenshots")
        take_screenshot()
    elif option == 2:
        print("Converting Images to Text")
        convert_images()
    elif option == 3:
        print("Read State Matrix")
        valve_list = read_excel()
    elif option == 4:
        print("Comparing Files")
