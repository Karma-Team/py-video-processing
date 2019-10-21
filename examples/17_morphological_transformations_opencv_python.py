import cv2
import numpy as np
from matplotlib import pyplot as plt

print("OpenCV version:", cv2.__version__)

# Morphological transformations are some simple operations based on the image shape
img = cv2.imread('/home/ahu/Workspace/py-video-processing-rsc/opencv-master/samples/data/smarties.png', cv2.IMREAD_GRAYSCALE)
ret, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((5, 5), np.uint8)

# Decrease the size of the little black balss
# args : img, kernal (rectangle), iterations nb
dilation = cv2.dilate(mask, kernal, iterations=2)

# Increase the size of the little black balls
erosion = cv2.erode(mask, kernal, iterations=1)

# Opening = Erosion + Dilation
# ars : img, type of morphological operations, kernal
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)

# Closing = Dilation + Erosion
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)

# Gradient
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)

# Top Hat
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(4, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

