import cv2

print("OpenCV version:", cv2.__version__)

# Load and display image
img = cv2.imread('/home/ahu/Workspace/py-video-processing-rsc/opencv-master/samples/data/lena.jpg', -1)
cv2.imshow('Lena', img)

# Keep image display and wait for action (escape or save)
key = cv2.waitKey(0) & 0xFF
if key == 27: # "Escape" key
    cv2.destroyAllWindows()
elif key == ord("s"): # "s" key
    cv2.imwrite('data/image/lena_copy.png', img)
    cv2.destroyAllWindows()
