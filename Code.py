
import os
import numpy as np
import matplotlib.pyplot as plt
import cv2

from skimage import data, img_as_float
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error

os.chdir(path to directory which images are saved)
print('Enter the soccer player name:\n')
x = input()
name = x + '.jpg'
print('The face detected for ', x, 'is shown here ...')


cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# Read the image
image = cv2.imread(name)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
    image,
    scaleFactor=1.3,
    minNeighbors=2,
    minSize=(10,10),
   )

print("Found {0} faces!".format(len(faces)))
print('for ', x, ' image')

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found below", image)
cv2.waitKey()