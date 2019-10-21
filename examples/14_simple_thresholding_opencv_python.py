import cv2
import numpy as np

print("OpenCV version:", cv2.__version__)

img = cv2.imread('/home/ahu/Workspace/py-video-processing-rsc/opencv-master/samples/data/gradient.png', 0)

# Get the threshold information
# args : img, threshold value, maximum value, threshold type
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# If the value is lesser than 127, the value is set to 0, else, to 255
ret, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# The inverse result of THRESH_BINARY
ret, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
# If the value is greater than 127, it is set to 127
ret, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
# If the value is lesser than 127, it is set to 0
ret, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
# The inverse result of THRESH_TOZERO

cv2.imshow("Image", img)
cv2.imshow("th1", th1)
cv2.imshow("th2", th2)
cv2.imshow("th3", th3)
cv2.imshow("th4", th4)
cv2.imshow("th5", th5)

cv2.waitKey(0)
cv2.destroyAllWindows()
