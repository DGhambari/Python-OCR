import pyscreenshot
import json
import cv2
import sys

valve_list = './json/coordinates.json'
coordinates = {
    "step_number": 0,
    "valve_list1": 0,
    "valve_list2": 0,
    "valve_states1": 0,
    "valve_states2": 0
}

# ============================================================================ #
# If the coordinates have been set already then this function will find the
# key and populate the coordinates dictionary with the relevant value from the
# json file
# ============================================================================ #


def find_coords(key):
    result = []
    f = open(valve_list)
    data = json.load(f)
    if key in data:
        result = data[key]
    f.close()
    return result

# ============================================================================ #
# Save the screenshots
# ============================================================================ #


def save_screenshot(IMAGE):
    img = cv2.imread(f"./images/{IMAGE}")
    cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(
        "window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("window", img)
    cv2.waitKey(0)

    for key in coordinates:
        coordinates[key] = find_coords(key)
        img = pyscreenshot.grab(bbox=(coordinates[key]))
        img.save(f"./images/{key}.jpg")


if __name__ == '__main__':
    IMAGE = sys.argv[1]
    save_screenshot(IMAGE)
