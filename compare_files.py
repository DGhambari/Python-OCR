import json

hmi_list = './json/HMI_valve_list.json'
doc_list = './json/doc_valve_list.json'

# Retrieve the live system valve states, converted from
# a screenshot to text


def retrieve_hmi_valve_list():
    f = open(hmi_list)
    data = json.load(f)
    if 'valves' in data:
        result = data['valves']
    f.close()
    return result[0]


hmi_valves = retrieve_hmi_valve_list()


# Retrieve the list of valve states from the documentation
def retrieve_doc_valve_list():
    f = open(doc_list)
    data = json.load(f)
    if 'valves' in data:
        result = data['valves']
    f.close()
    return result[0]


doc_valves = retrieve_doc_valve_list()

print(hmi_valves)
print(doc_valves)

for x in doc_valves:
    if doc_valves[x] == hmi_valves[x]:
        print(
            f"The valve state for {doc_valves[x]} \
                ({doc_valves.get(x)}) matches between the two \n)")
    else:
        print(
            f"The documentation states that valve {doc_valves.get(x)} \
                should be {doc_valves[x]} but the system is showing it as {hmi_valves[x]}")


def write_to_file():
    data = {
        "Documetation Valves": doc_valves,
        "System Valves": hmi_valves
    }
    file_name = "./json/valve_list_comparison.json"

    with open(file_name, "w") as json_file:
        json.dump(data, json_file)
