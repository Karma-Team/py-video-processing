import numpy as np
import cv2

print("OpenCV version:", cv2.__version__)

img = cv2.imread('/home/ahu/Workspace/py-video-processing-rsc/opencv-master/samples/data/lena.jpg', -1)
img2 = cv2.imread('/home/ahu/Workspace/py-video-processing-rsc/opencv-master/samples/data/logo-225-225.png', -1)

# Tuple of number of rows, columns and channels
print(img.shape)

# Total number of pixels is accessible
print(img.size)

# Image datatype
print(img.dtype)

# Split an image in 3 channels
b, g, r = cv2.split(img)

# Merge 3 channels in an image
img = cv2.merge((b, g, r))

# Move a part of an image [y1:y2, x1:x2] (ROI : Region Of Interest)
eye = img[250:290, 250:290]
img[210:250, 290:330] = eye
cv2.imshow('image', img)

# Add 2 images
img = cv2.resize(img, (225, 225))
img2 = cv2.resize(img2, (225, 225))
dst1 = cv2.add(img, img2)
cv2.imshow('imageadd1', dst1)

# Add 2 images with weight %1stimg %2ndimg
# args : img1, alpha, img2, beta, gamma
# -> img1*alpha + img2*beta + gamma
dst2 = cv2.addWeighted(img, 0.75, img2, 0.25, 0)
cv2.imshow('imageadd2', dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()
