import cv2
import numpy as np

print("OpenCV version:", cv2.__version__)


# callback fct : x current position of the trackbar
def nothing(x):
    print(x)


# Create a black image, a window
cv2.namedWindow('image')

# Create a trackbar
cv2.createTrackbar('CurrentPosition', 'image', 10, 400, nothing)
# args : trackbar name, window name, value count, callback fct

# Add a switch using a trackbar
switch = '0 : OFF\n 1 : ON'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    img = cv2.imread('/home/ahu/Workspace/py-video-processing-rsc/opencv-master/samples/data/lena.jpg', -1)

    # Write the trackbar position on the image
    pos = cv2.getTrackbarPos('CurrentPosition', 'image')
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img, str(pos), (50, 150), font, 4, (0, 0, 255), 10)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # Get trackbar position
    s = cv2.getTrackbarPos(switch, 'image')

    if s == 0:
        pass
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = cv2.imshow('image', img)


cv2.destroyAllWindows()
