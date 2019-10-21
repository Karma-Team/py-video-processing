import numpy as np
import cv2

print("OpenCV version:", cv2.__version__)

# Get all events (button, mouse, ...) in the cv2 library
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)


# Listen for a mouse event
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ', ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', ' + str(y)
        cv2.putText(img, strXY, (x, y), font, 0.5, (255, 255, 0), 2)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        # cv2 : img is shown in openCV in the form of BGR format
        # print out the BGR channels of the img
        # get the blue channel
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, strBGR, (x, y), font, 0.5, (0, 255, 255), 2)
        cv2.imshow('image', img)


#img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('/home/ahu/Workspace/py-video-processing-rsc/opencv-master/samples/data/lena.jpg', -1)
cv2.imshow('image', img)

# Callback function
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()