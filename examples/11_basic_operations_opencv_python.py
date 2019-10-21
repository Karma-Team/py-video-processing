import cv2
import numpy as np

print("OpenCV version:", cv2.__version__)

# img = cv2.imread('/home/ahu/Workspace/py-video-processing-rsc/opencv-master/samples/data/lena.jpg', -1)
img1 = np.zeros((250, 500, 3), np.uint8)
img2 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = cv2.rectangle(img2, (250, 0), (500, 250), (255, 255, 255), -1)

# Tuple of number of rows, columns and channels
print(img1.shape)
print(img2.shape)

# Display images
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)

# Bitwise operations
bitAnd = cv2.bitwise_and(img1, img2)
cv2.imshow('bitAnd', bitAnd)
bitOr = cv2.bitwise_or(img1, img2)
cv2.imshow('bitOr', bitOr)
bitXor = cv2.bitwise_xor(img1, img2)
cv2.imshow('bitXor', bitXor)
bitNotImg1 = cv2.bitwise_not(img1)
cv2.imshow('bitNotImg1', bitNotImg1)
bitNotImg2 = cv2.bitwise_not(img2)
cv2.imshow('bitNotImg2', bitNotImg2)

cv2.waitKey(0)
cv2.destroyAllWindows()
