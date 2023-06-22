import tkinter as tk
import subprocess
import take_screenshot
import convert_image as convert
# window = tk.Tk()

# greeting = tk.Label(text="Hello, Tkinter")
# greeting.pack()

# window.mainloop()

# Areas to take screenshots from
def take_screenshot():
    with open("take_screenshot.py") as f:
        exec(f.read())

# Open the state matrix
def read_excel(excel_file):
    valve_list = []
    return valve_list

option = input("Please select an option:\n\n"
                "\t1: Take Screenshot\n"
                "\t2: Convert Images to Text\n"
                "\t3: Read State Matrix\n"
                "\t4: Compare Files\n")

while option != 0:
    if option == 1:
        exec(take_screenshot.py)
        print("Taking Screenshots")
    elif option == 2:
        print("Converting Images to Text")
        print(convert.step_num)
    elif option == 3:
        print("Read IO List")
    elif option == 4:
        print("Comparing Files")

# exec_script()
#take_screenshot()

# Write the steps, valves numbers and states to a json file
#def create_json():

# Function to take multiple screenshots and save them as separate files. One for the step number and four for the
# valves (2 for the valve tags and 2 for the states)

# Open tkinter to draw the outline of where the screenshots should be taken from
