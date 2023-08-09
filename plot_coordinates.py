import cv2
import json
import os.path
import sys

# function to write to a JSON file


def write_json(data_to_write, area, filename='./json/coordinates.json'):
    with open(filename, 'r+') as json_file:
        # First load existing data into a dict.
        file_data = json.load(json_file)
        # Join new_data with file_data inside coordinates
        file_data.update(data_to_write)
        # Sets file's current position at offset.
        json_file.seek(0)
        # Convert back to json.
        json.dump(file_data, json_file, indent=4)

# Function to plot coordinates of the portions of the screen to be converted to text


def plot_coordinates(AREA, IMAGE):

    coordinates = []
    image = cv2.imread(f"./images/{IMAGE}")
    r = cv2.selectROI("Select Area", image)

    # r[0] = x1,
    # r[1] = y1,
    # r[2] = distance from x1 (add this to x1 to get x2),
    # r[3] = distance from y1 (add this to x1 to get y2)

    cropped_image = image[int(r[1]):int(r[1]+r[3]),
                          int(r[0]):int(r[0]+r[2])]

    # Save cropped image
    cv2.imwrite(f'./images/{AREA}.jpg', cropped_image)
    print(f"\nFile saved as {AREA}.jpg in /images\n")

    # Define the values for the coordinates
    for x in range(4):
        if x >= 2:
            coordinates.append(r[x] + r[x-2])
        else:
            coordinates.append(r[x])

    # Create dictionary to add to a json file
    data_to_write = {AREA: coordinates}

    file_name = "./json/coordinates.json"
    path = 'json'

    # If the file already exists
    if os.path.isfile(file_name) == True:
        write_json(data_to_write, AREA)

    # If the directory exists but not the file
    elif os.path.exists(path) == True:
        with open(file_name, "w+") as json_file:
            json.dump(data_to_write, json_file)

    # If the directory does not exist
    elif os.path.exists(path) == False:
        os.mkdir('json')
        with open(file_name, "w+") as json_file:
            json.dump(data_to_write, json_file)
    cv2.waitKey(0)


if __name__ == "__main__":
    AREA = sys.argv[1]
    IMAGE = sys.argv[2]
    plot_coordinates(AREA, IMAGE)
