import cv2
import numpy as np
from matplotlib import pyplot as plt

print("OpenCV version:", cv2.__version__)

img = cv2.imread('/home/ahu/Workspace/py-video-processing-rsc/opencv-master/samples/data/opencv-logo.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply threshold and find the contours
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
# contours is a Python list of all the contours in the img.
# each individual contour is a Numpy array of (x, y) coordinates of boundary points of the object.
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of contours = " + str(len(contours)))
# print(contours[0])

# Join the coordinates of the contours
# third arg : contour n°
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)


cv2.imshow("Image", img)
cv2.imshow("Image GRAY", imgray)

cv2.waitKey(0)
cv2.destroyAllWindows()

