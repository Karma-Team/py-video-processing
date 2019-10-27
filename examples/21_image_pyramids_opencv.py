import cv2
import numpy as np
from matplotlib import pyplot as plt

print("OpenCV version:", cv2.__version__)

img = cv2.imread('/home/ahu/Workspace/py-video-processing-rsc/opencv-master/samples/data/lena.jpg')

# Image pyramids create the initial img in many resolutions
# cv2.imshow("Orignal image", img)
# Lower resolution
# lr1 = cv2.pyrDown(img)
# lr2 = cv2.pyrDown(lr1)
# cv2.imshow("pyrDown 1 image", lr1)
# cv2.imshow("pyrDown 2 image", lr2)
# Higher resolution
# hr1 = cv2.pyrUp(lr2)
# hr2 = cv2.pyrUp(hr1)
# cv2.imshow("pyrUp 1 image", hr1)
# cv2.imshow("pyrUp 2 image", hr2)

# Gaussian pyramid
layer = img.copy()
gp = [layer]
for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i), layer)

layer = gp[5]
cv2.imshow("upper level Gaussian Pyramid", layer)

# Laplacian pyramid
lp = [layer]
for i in range(5, 0, -1):
    gaussian_expanded = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_expanded)
    cv2.imshow(str(i), laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()

