import cv2
import numpy as np
from matplotlib import pyplot as plt

print("OpenCV version:", cv2.__version__)

# Canny edge detectors is an edge detection operator that uses a multi-stage algorithm to detect a wide range of edges in images
# Five steps :
# 1 > Noise reduction
# 2 > Gradient calculation
# 3 > Non-maximum suppresion
# 4 > Double threshold
# 5 > Edge Tracking by Hysteresis

img = cv2.imread('/home/ahu/Workspace/py-video-processing-rsc/opencv-master/samples/data/lena.jpg', 0)

#args : img, 1st threshold value, 2nd threshold value
canny = cv2.Canny(img, 100, 200)

titles = ['image', 'canny']
images = [img, canny]

for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

