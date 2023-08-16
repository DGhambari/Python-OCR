import json
import subprocess

hmi_list = './json/HMI_valve_list.json'
doc_list = './json/doc_valve_list.json'

# Retrieve the live system valve states, converted from
# a screenshot to text
def retrieve_valve_list(file_path):
    with open(file_path) as f:
            data = json.load(f)
    result = data.get('valves', {})
    return result

# Compare the documentation list against the live system list to
# see if the valve states match
def compare(dict_a, dict_b):
    for key_b, value_b in dict_b.items():
        if key_b in dict_a:
            value_a = dict_a[key_b]
            if value_a == value_b:
                print(f"Match - Documentation states {key_b} should be {value_b} and the system has {key_b} in the {value_a} state \n")
            else:
                print(f"There is a mismatch for {key_b}\n")
        else:
            stripped_tag_b = strip_tag(key_b)
            matching_keys = [key_a for key_a in dict_a if strip_tag(key_a) == stripped_tag_b]
            if matching_keys:
                print(f"Tag names have been adjusted but are a match for '{stripped_tag_b}' instead.\n")
            else:
                print(f"{key_b} not found in system.\n")


# If valve names fail to match then remove the "XV" from the 
# name and see if the numbers match instead.
def strip_tag(valve):
    return valve[-6:]

if __name__ == '__main__':
    hmi_valves = retrieve_valve_list(hmi_list)
    doc_valves = retrieve_valve_list(doc_list)
    compare(hmi_valves, doc_valves)
    subprocess.run(['python', 'create_report.py'])