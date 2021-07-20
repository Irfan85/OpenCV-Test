# Ref: https://docs.opencv.org/4.5.2/db/deb/tutorial_display_image.html

import cv2 as cv
import sys

# Loading an image. It will be imported in "BGR" format
img = cv.imread("Confused Bean.jpg")

# Checking if image is loaded properly
if img is None:
    sys.exit("Could not read the image.")

# The image is imported as a matrix which is numpy combatible. Let's look at its shape
print(img.shape)

cv.imshow("Hello", img)

# We have to wait for a key for the window to stay. '0' means wait forever
k = cv.waitKey(0)

# Press 's' to write the image to a file. ord() converts a character to its unicode value
if k == ord('s'):
    cv.imwrite("Bean.png", img)

