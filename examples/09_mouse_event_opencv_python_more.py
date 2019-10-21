import numpy as np
import cv2

print("OpenCV version:", cv2.__version__)

# Get all events (button, mouse, ...) in the cv2 library
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)


# Listen for a mouse event
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        cv2.imshow('image', img)

        # Create an image
        mycolorImage = np.zeros((512, 512, 3), np.uint8)

        # Fill this image with the RGB color get from the first image
        mycolorImage[:] = [blue, green, red]

        cv2.imshow('color', mycolorImage)
    if event == cv2.EVENT_RBUTTONDOWN:
        # Create a circle
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        points.append((x, y))
        if len(points) >= 2:
            # Create a line between the last two points (circles)
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)
        cv2.imshow('image', img)


img = cv2.imread('/home/ahu/Workspace/py-video-processing-rsc/opencv-master/samples/data/lena.jpg', -1)
cv2.imshow('image', img)

# Create an array of points
points = []

# Callback function
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()