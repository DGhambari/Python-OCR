from PIL import Image
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

step_number_img = '../images/step_num.jpg'
valve_list_img1 = '../images/valve_list1.jpg'
valve_list_img2 = '../images/valve_list2.jpg'
valve_states_img1 = '../images/valve_states1.jpg'
valve_states_img2 = '../images/valve_states2.jpg'

#def convert():
step_num = (pytesseract.image_to_string(Image.open(step_number_img).convert('L')))
valve_list1 = (pytesseract.image_to_string(Image.open(valve_list_img1).convert('L')))
valve_list2 = (pytesseract.image_to_string(Image.open(valve_list_img2).convert('L')))
valve_states_img1 = (pytesseract.image_to_string(Image.open(valve_states_img1).convert('L')))
valve_states_img2 = (pytesseract.image_to_string(Image.open(valve_states_img2).convert('L')))

print(valve_list1)
print(valve_states_img1)
print(valve_list2)
print(valve_states_img2)

"""
    return step_num, \
           valve_list1, \
           valve_states_img1, \
           valve_list2, \
           valve_states_img2

f = open("testfile.txt", "a+")
f.write(text)
f.close()

# Remove the blank lines
result = ""
with open("testfile.txt", "r+") as file:
    for line in file.readlines():
        if (len(line.strip()) == 0):
            continue
        if line:
            result += line

    file.seek(0)
    file.write(result)

"""










# filename = '../images/image003.jpg'
# filename2 = 'C:/Users/Gham/PycharmProjects/Text_Recognition/images/image_02.jpg'

# img1 = np.array(Image.open(filename))
# text = pytesseract.image_to_string(img1)
# print(text)
# text = (pytesseract.image_to_string(Image.open(filename)))
# filename = 'C:/Users/Gham/PycharmProjects/Text_Recognition/images/image_01.jpg'
# filename = '../images/screen_1.jpg'
# filename = '../images/image002.png'
#updated_text = text.replace('\r', '')
#print("Updated list : \n" + updated_text)
# print("Original list : \n" + str(text))

# print(pytesseract.image_to_string(Image.open(filename2)))
# list = [pytesseract.image_to_string(Image.open(filename))]
# print(list)