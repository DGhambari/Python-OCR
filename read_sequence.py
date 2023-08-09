import xlrd
import json

loc = "C:/Users/DGhambari/OneDrive - Rockwell Automation, Inc/Documents/College/Final Project/Python-OCR/State_Matrix.xls"
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
valves = {}
valve_list = './json/HMI_valve_list.json'

# ============================================================================ #
# Read the text file that contains the step number
# ============================================================================ #


def find_step_num():
    f = open(valve_list)
    data = json.load(f)
    if 'step_number' in data:
        result = data['step_number']
    f.close()
    return result[0]


step_number = find_step_num()

# ============================================================================ #
# Find the cell that contains the step number. The easiest way to do this is to
# use the first column and search for "Type" as this is the top left cell of
# each section. The step numbers begin from column D of that row number.
# ============================================================================ #

# sheet.col_values(0)   - Displays all column values
# sheet.row_values(0)   - Displays all row values
# sheet.cell(0,0)       - Displays cell value
# Cell format is (row, col)
# Update - check for cell values using .value rather than converting to strings
# Update - sheet.cell_type(row,col) == xlrd.XL_CELL_EMPTY checks if a cell
# is empty

# For each row in column 0, find "type" and append it to a list
# The only comparisons that seem to work are str to str, the data type returned
# by xlrd does not seem to be comparable any other way


def find_start_rows():
    result = []
    cols = sheet.col_values(0)
    for row in range(sheet.nrows):
        if "type" in str(cols[row]).lower():
            result.append(row)
    return result

# For each row, check if the step number matches the cell: (row, iterable column)
# Only seems to be working for the first index of step_num_rows


def find_step_num(step_num):
    x = 3
    result = []
    for row in step_num_rows:
        while x < sheet.ncols:
            if str(step_num) in str(sheet.cell(row, x)):
                result = [row, x]
            x += 1
        x = 3
    return result

# ============================================================================ #
# Convert the state matrix syntax into English: A = Open, B = Closed
# ============================================================================ #


def convert_valve_states(state):
    result = []
    for i in range(len(state)):
        if state[i] == "A":
            result.append("Open")
        elif state[i] == "R":
            result.append("Closed")
        else:
            result.append(f"{state} - Manual Inspection Required")
    return result

# ============================================================================ #
# Once the cell that the step number is in is found, the valve states begin two
# rows below it in the same column. The valve tags can be found in column C,
# also two rows below the step number
# ============================================================================ #


def find_valve_states(step_cell):
    result = []
    row = step_cell[0] + 2
    col = step_cell[1]
    while sheet.cell(row, col).value != "":
        result.append(sheet.cell(row, col).value)
        row += 1
    return result


def find_valve_tags(step_cell):
    result = []
    row = step_cell[0] + 2
    col = 2
    while sheet.cell(row, col).value != "":
        result.append(sheet.cell(row, col).value)
        row += 1
    return result

# ============================================================================ #
# Combine the valve tags list and valve states into a dictionary
# ============================================================================ #


def combine_lists(tags, states):
    result = {}
    if len(tags) == len(states):
        result = {tags[i]: states[i] for i in range(len(tags))}
    else:
        result = {["Tag list and state list are not equal in size"]}
    return result

# ============================================================================ #
# Function to convert the French valve state to English
# ============================================================================ #


def translate(text):
    result = ""
    close_list = {"Fermé", "Ferme"}
    if text == "Ouvert":
        result = "OPEN"
    elif text in close_list:
        result = "CLOSE"
    return result

# ============================================================================ #
# Write the text to file
# ============================================================================ #

def write_to_file(list):
    data = {
        "valves" : list
    }
    file_name = "./json/doc_valve_list.json"

    with open(file_name, "w") as json_file:
        json.dump(data, json_file)


if __name__ == '__main__':
    step_num_rows = find_start_rows()
    step_cell = find_step_num(step_number)
    valve_states = convert_valve_states(find_valve_states(step_cell))
    valve_tags = find_valve_tags(step_cell)
    valves = combine_lists(valve_tags, valve_states)
    write_to_file(valves)
