import pyscreenshot

# Map the coordinates of where to take screenshots from
coordinates = {
    "step_num": [592, 896, 628, 931],
    "valve_list1": [820, 517, 887, 832],
    "valve_list2": [820, 904, 886, 1085],
    "valve_states1": [1297, 511, 1410, 837],
    "valve_states2": [1299, 903, 1402, 1086]
}

# Save the screenshots
for key in coordinates:
    img = pyscreenshot.grab(bbox=(coordinates[key]))
    img.save(f"../images/{key}.jpg")
