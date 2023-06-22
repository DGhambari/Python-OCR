import xlrd

loc = "C:/Users/Gham/PycharmProjects/Text_Recognition/State_Matrix.xlsx"
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
start_cell = ""
step_num_rows = []

# ============================================================================ #
# Find the cell that contains the step number. The easiest way to do this is to
# use the first column and search for "Type" as this is the top left cell of
# each section. The step numbers begin from column D of that row number.
# ============================================================================ #

# sheet.col_values(0)   - Displays all column values
# sheet.row_values(0)   - Displays all row values
# sheet.cell(0,0)       - Displays cell value
# Cell format is (row, column)

# For each row in column 0, find "type" and append it to a list
# The only comparisons that seem to work are str to str, the data type returned
# by xlrd does not seem to be comparable any other way
def find_start_rows():
    cols = sheet.col_values(0)
    for row in range(sheet.nrows):
        if "type" in str(cols[row]).lower():
            step_num_rows.append(row)

# For each row, check if the step number matches the cell: (row, iterable column)
# Only seems to be working for the first index of step_num_rows
def find_step_num(step_num):
    step_cell = []
    x = 0
    for row in step_num_rows:
        while x < sheet.ncols:
            if str(step_num) in str(sheet.cell(row, x)):
                step_cell = [row,x]
                break
            x+=1
    return step_cell

# ============================================================================ #
# Once found, add 2 to the cell number and change the column to column C.
# This is where the first valve in the sequence will be found.
# ============================================================================ #

# Checking if str's equal other str's does not seem to work either, Checking
# if a tag is IN the xlrd data type is the only way this works. It must be
# because it's not just the text of the cell that xlrd returns but maybe the
# apostrophe and "TEXT:"

# ============================================================================ #
# Function to convert the French valve state to English
# ============================================================================ #

def translate(text):
    result = ""
    close_list = {"Fermé", "Ferme"}
    if text == "Ouvert":
        result = "Open"
    elif text in close_list:
        result = "Closed"
    return result

translate("Fermé")

# ============================================================================ #
# Convert the state matrix syntax into English: A = Open, B = Closed
# ============================================================================ #

def convert_valve_state(state):
    result = ""
    if state == "A":
        result = "Open"
    elif state == "R":
        result = "Closed"
    else:
        result = f"{state} - Manual Inspection Required"
    return result

convert_valve_state("F")

# ============================================================================ #
# Iterate over a dictionary using the valve as the key and state as the value
# ============================================================================ #
