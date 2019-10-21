import cv2
import numpy as np

print("OpenCV version:", cv2.__version__)

img = cv2.imread('/home/ahu/Workspace/py-video-processing-rsc/opencv-master/samples/data/sudoku.png', 0)

# Calculate the threshold for a small region of pixels of an image
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# args : img, maximum value, adaptive method, threshold type, blocksize, C constant
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
# ADAPTIVE_THRESH_MEAN_C : threshold is the mean of the blocksize*blocksize neighborhood of (x,y) minus C (constant)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# ADAPTIVE_THRESH_GAUSSIAN_C : threshold is a weighted sum of the blocksize*blocksize neighborhood of (x,y) minus C (constant)

cv2.imshow("Image", img)
cv2.imshow("th1", th1)
cv2.imshow("th2", th2)
cv2.imshow("th3", th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
