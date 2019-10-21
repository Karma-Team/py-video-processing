import numpy as np
import cv2

print("OpenCV version:", cv2.__version__)

# Load the image
#img = cv2.imread('/home/ahu/Workspace/py-video-processing-rsc/opencv-master/samples/data/lena.jpg', 1)

# Create an image
# args : [height, width, RGB], data type
img = np.zeros([512, 512, 3], np.uint8)

# Draw a line in the image
# args : image, coordinates begin, coordinates end, color, thickness
img = cv2.line(img, (0, 0), (255, 255), (0, 0, 255), 5)
img = cv2.arrowedLine(img, (0, 255), (255, 255), (0, 255, 255), 2)

# Draw rectangle
# args : image, coordinates begin, coordinates end, color, thickness
img = cv2.rectangle(img, (150, 0), (300, 150), (255, 0, 0), 10)
img = cv2.rectangle(img, (350, 0), (400, 150), (255, 0, 0), -1)

# Draw circle
# args : image, center coordinates, radius, color, thickness
img = cv2.circle(img, (100, 100), 50, (255, 255, 255), -1)

# Put text in the image
# args : img, text, coordinates begin, fontface, size, color, thickness, line type
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCv', (10, 500), font, 4, (0, 0, 0), 15, cv2.LINE_AA)

# Display the image
cv2.imshow('Lena', img)

# Keep image display and wait for action (escape or save)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
