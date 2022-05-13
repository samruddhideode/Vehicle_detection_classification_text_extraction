# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import cv2
import imutils
import numpy as np
import pytesseract
import matplotlib.pyplot as plt

#import glob

#path = glob.glob("C:/Users/Admin/PycharmProjects/pythonProject1/cars/*.jpg")

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('cars/car.jpg', cv2.IMREAD_COLOR)
text_img = img.copy()


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# A bilateral filter: noise-reducing smoothing filter for images.
gray = cv2.bilateralFilter(gray, 13, 17, 17)

# The Canny edge detector
edged = cv2.Canny(gray, 30, 200)

contours = cv2.findContours(
    edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contours = imutils.grab_contours(contours)  # contour is boundary of an ibject
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

location = None
for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        break
print(location)


mask = np.zeros(gray.shape, np.uint8)  # created a blank mask
new_image = cv2.drawContours(mask, [location], 0, 255, -1)
new_image = cv2.bitwise_and(img, img, mask=mask)

#plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2GRAY))


(x, y) = np.where(mask == 255)
(x1, y1) = (np.min(x), np.min(y))
(x2, y2) = (np.max(x), np.max(y))
Cropped = gray[x1:x2 + 1, y1:y2 + 1]

text = pytesseract.image_to_string(Cropped, config="--psm 6")
print("Detected license plate Number is:", text)

text_img = cv2.putText(text_img, str(text), (50, 50),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 5, 5)
cv2.imshow('Image', text_img)
img = cv2.resize(text_img, (600, 400))
cv2.waitKey(0)

# code for 2nd car
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread('cars/car2.jpg', cv2.IMREAD_COLOR)
text_img = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 15, 17, 17)
edged = cv2.Canny(gray, 30, 200)
contours = cv2.findContours(
    edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contours = imutils.grab_contours(contours)  # contour is boundary of an ibject
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

location = None
for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        break
# print(location)


mask = np.zeros(gray.shape, np.uint8)  # created a blank mask
new_image = cv2.drawContours(mask, [location], 0, 255, -1)
new_image = cv2.bitwise_and(img, img, mask=mask)

(x, y) = np.where(mask == 255)
(x1, y1) = (np.min(x), np.min(y))
(x2, y2) = (np.max(x), np.max(y))
Cropped = gray[x1:x2 + 1, y1:y2 + 1]

text = pytesseract.image_to_string(Cropped, config="--psm 6")
print("Detected license plate Number is:", text)

text_img = cv2.putText(text_img, text, (10, 50),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 5, 5)
cv2.imshow('Image', text_img)
img = cv2.resize(text_img, (600, 400))
cv2.waitKey(0)

# 3rd car
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread('cars/car3.jpg', cv2.IMREAD_COLOR)
text_img = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 15, 17, 17)
edged = cv2.Canny(gray, 30, 200)
contours = cv2.findContours(
    edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contours = imutils.grab_contours(contours)  # contour is boundary of an ibject
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

location = None
for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        break
# print(location)


mask = np.zeros(gray.shape, np.uint8)  # created a blank mask
new_image = cv2.drawContours(mask, [location], 0, 255, -1)
new_image = cv2.bitwise_and(img, img, mask=mask)

(x, y) = np.where(mask == 255)
(x1, y1) = (np.min(x), np.min(y))
(x2, y2) = (np.max(x), np.max(y))
Cropped = gray[x1:x2 + 1, y1:y2 + 1]

text = pytesseract.image_to_string(Cropped, config="--psm 6")
print("Detected license plate Number is:", text)

text_img = cv2.putText(text_img, text, (10, 50),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 5, 5)
cv2.imshow('Image', text_img)
img = cv2.resize(text_img, (600, 400))
cv2.waitKey(0)
