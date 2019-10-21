import cv2
import numpy as np
from matplotlib import pyplot as plt

print("OpenCV version:", cv2.__version__)

# An image gradient is a directional change in the intensity or color in an image

img = cv2.imread('/home/ahu/Workspace/py-video-processing-rsc/opencv-master/samples/data/sudoku.png', cv2.IMREAD_GRAYSCALE)

# Laplacian method
# args : img, datatype, kernelSize
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

# Sobel method
# args : img, datatype, sobelX, sobelY, kernelSize
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobelXY = cv2.bitwise_or(sobelX, sobelY)

titles = ['image', 'lap', 'sobelX', 'sobelY', 'sobelXY']
images = [img, lap, sobelX, sobelY, sobelXY]

for i in range(5):
    plt.subplot(3, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

