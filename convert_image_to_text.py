from PIL import Image
import pytesseract
import json

# ============================================================================ #
# Path to Tesseract-OCR executable. This is required for the script to function
# ============================================================================ #

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

step_number_img = './images/step_number.jpg'
valve_list_img1 = './images/valve_list1.jpg'
valve_list_img2 = './images/valve_list2.jpg'
valve_states_img1 = './images/valve_states1.jpg'
valve_states_img2 = './images/valve_states2.jpg'

# ============================================================================ #
# Convert the screenshots of the system to text
# ============================================================================ #

custom_options = r'--user_words tesseract_words.txt --user-patterns tesseract_patterns.txt'

step_number = (pytesseract.image_to_string(
    Image.open(step_number_img).convert('L')))
valve_list1 = (pytesseract.image_to_string(
    Image.open(valve_list_img1).convert('L')))
valve_list2 = (pytesseract.image_to_string(
    Image.open(valve_list_img2).convert('L')))
valve_states_list1 = (pytesseract.image_to_string(
    Image.open(valve_states_img1).convert('L')))
valve_states_list2 = (pytesseract.image_to_string(
    Image.open(valve_states_img2).convert('L'), config='custom_options'))

#print(f"list1 " + str(len(valve_states_list1)))
#print(f"list2 " + str(len(valve_states_list2)))

if len(valve_states_list1) == 0:
    valve_states_list1 = (pytesseract.image_to_string(
        Image.open(valve_states_img1),
        config='custom_options',
        lang='eng+fra'))

if len(valve_states_list2) == 0:
    valve_states_list2 = (pytesseract.image_to_string(
        Image.open(valve_states_img2),
        config='custom_options',
        lang='eng+fra'))

#print(f"list1 " + str(len(valve_states_list1)))
#print(f"list2 " + str(len(valve_states_list2)))

# ============================================================================ #
# Tidy the lists up
# ============================================================================ #


def tidy(list):
    newlist = []

    # Write the list to a temporary file
    f = open("testfile.txt", "w+")
    f.write(list)
    f.close()

    # Read the temporary file so that the list has the
    # new lines incorporated into it. Remove all new lines
    # and create a new list with the tidied list

    with open("testfile.txt", "r") as file:
        for line in file.readlines():
            if (len(line.strip()) == 0):
                continue
            if line:
                line.replace('\r', '').replace('\n', '')
            newlist.append(line.upper())
    newlist = [item.strip() for item in newlist]
    #print(newlist)
    translated_list = translate(newlist)
    #print(translated_list)
    return translated_list

# ============================================================================ #
# Write the text to file
# ============================================================================ #


def write_to_file():
    data = {
        "step_number" : updated_step_number,
        "valves" : complete_valve_dict
    }
    file_name = "./json/HMI_valve_list.json"

    with open(file_name, "w") as json_file:
        json.dump(data, json_file)

# ============================================================================ #
# Combine dictionaries
# ============================================================================ #


def combine_dicts(valve_list, valve_state):
    result = {}
    for key in valve_list:
        for value in valve_state:
            result[key] = value
            break
    return result

# ============================================================================ #
# Replace the French valve statuses with English
# ============================================================================ #


def translate(input_list):
    result = []
    for status in input_list:
        if "FERMÉ" in status:
            result.append('CLOSE')
        elif "FERME" in status:
            result.append('CLOSE')
        elif "OUVERT" in status:
            result.append('OPEN')
        else:
            result.append(status)
    return result


if __name__ == '__main__':
    updated_valve_list1 = tidy(valve_list1)
    updated_valve_list2 = tidy(valve_list2)
    updated_step_number = tidy(step_number)
    updated_valve_states1 = tidy(valve_states_list1)
    updated_valve_states2 = tidy(valve_states_list2)
    # print(updated_valve_states1)
    # print(updated_valve_states2)
    combined_valve_dict1 = combine_dicts(
        updated_valve_list1, updated_valve_states1)
    combined_valve_dict2 = combine_dicts(
        updated_valve_list2, updated_valve_states2)
    complete_valve_dict = dict(**combined_valve_dict1, **combined_valve_dict2)
    #print(complete_valve_dict)
    write_to_file()