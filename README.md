# Python-OCR
Python Scripts to Extract Text From Images On A Screen

Prior to running these scripts Googles Tesseract needs to be installed, the windows installer can be found here: https://github.com/UB-Mannheim/tesseract/wiki.

The installation path for this must be included in convert_image_to_text.py. The default path is in the script already but it should be changed if installing it elsewhere.

# Objective

The aim of this project is to minimise the amount of time required to manually verify the correlation between design documentation and a live control system. One of the most
time consuming aspects of testing during commissioning a control system is checking what state a group of valves should be in at a particular stage in the process. This project
aims to reduce that.

By using Googles OCR software, Teseract, which converts images to text, valves states can be read and translated into text from screenshots taken of a live control system, and 
compared against the design specification documentation.

# Functionality

To begin with, a screenshot of the SCADA/HMI of a control system with the status of the valves to be tested visible on the screen, is required. There are sample images in the images 
folder that can be used as a reference.The scripts are executed via the command line and once set up it should only take a few keyboard presses for subsequent images to be processed.

First run main_script.py, from here there are a couple of options: 

Option 1 prompts the user to type the filename of the screenshot that is to be converted to text. In further versions this will instead provide a list of the screenshots
in the /images folder and allow the user to press a number to speed the selection up but for now it has to be typed.

Option 2 opens the screenshot and prompts the user to select/crop sections of the screenshot, saving them to the /images folder. Press enter after an area is selected to continue. 
The coordinates of each cropped screenshot is also saved to a json file in the /json folder so that subsequent images can be cropped and saved quickly.

Option 3 converts the cropped images to text and saves the converted text to a json file in the /json folder.

Option 4 reads the step number from the json file created in option 3, searches for it in the design documentation and creates another json file with the valve
names and states.

Option 5 is an alternative to option 2 in that it can use the image coordinates saved from option 2 to quickly save cropped images that will then be converted to text.

Option 6 compares the two json files created in option 3 and 4 and returns a description of whether each valve matches or not to the console. It also executes the create_report script
which generates a report containing the screenshot that was used from option 1, along with a table containing the expected valve states based on the information retrieved from the design
documentation and the actual valve states converted from the live control system screenshot.
