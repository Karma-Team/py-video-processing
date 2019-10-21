import cv2
import numpy as np
from matplotlib import pyplot as plt

print("OpenCV version:", cv2.__version__)

img = cv2.imread('/home/ahu/Workspace/py-video-processing-rsc/opencv-master/samples/data/opencv-logo.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# opencv read the img in BGR
# matplotlib read the img in RGB

# Homogeneous filter : each output pixel is the mean of its kernel neighbors
# --> Reduce noise on the img
# kernel expl :
# K = (1/(K_width*K_height)). [[1 1 1 1 ...] [1 1 1 1 ...] ...]
# K = (1/(5*5)). [[1 1 1 1 1] [1 1 1 1 1] ...]
kernel = np.ones((5, 5), np.float32)/25
# args : img, desire depth of the dst img, kernel
dst = cv2.filter2D(img, -1, kernel)

# HPF filters helps in removing edges in the images
# Low Pass Filter (LPF) helps in removing noises, blurring the images
# args : img, kernel
kernel = (5, 5)
blur = cv2.blur(img, kernel)

# Gaussian filter
# Gaussian filter is nothing nut using different-weight-kernel, in both x and y direction
# args : img, kernel, sigma value
gblur = cv2.GaussianBlur(img, kernel, 0)

# Median filter
# Median filter is something that replace each pixel's value with the median of its neighboring pixels (great when dealing with salt-and-pepper noise)
# args: img, kernelSize > 1
median = cv2.medianBlur(img, 5)

# Bilateral filter
# args : img, diameter of each pixel, sigma color, sigma space
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['image', '2D Convolution', 'blur', 'GaussianBlur', 'median', 'bilateralFilter']
images = [img, dst, blur, gblur, median, bilateralFilter]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

