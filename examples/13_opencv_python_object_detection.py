import cv2
import numpy as np

print("OpenCV version:", cv2.__version__)

# HSV : Hue, Saturation, Value
# Hue : color component (base pigment : 0-360)
# Saturation : amount of color (depth of the pigment : 0-100%)
# Value : brightness of the color (0-100%)


# callback fct : x current position of the trackbar
def nothing(x):
    pass


# Create a tracking window
cv2.namedWindow('Tracking')

# Open a video
cap = cv2.VideoCapture('/home/ahu/Workspace/py-video-processing-rsc/video_data/finale_match_1_full.mp4')

# Create a trackbar for :
# LH (Lower Hue)
# LS (Lower Saturation)
# LV (Lower Value)
# UH (Upper Hue)
# US (Upper Saturation)
# UV (Upper Value)
cv2.createTrackbar("LH", 'Tracking', 0, 255, nothing)
cv2.createTrackbar("LS", 'Tracking', 0, 255, nothing)
cv2.createTrackbar("LV", 'Tracking', 0, 255, nothing)
cv2.createTrackbar("UH", 'Tracking', 255, 255, nothing)
cv2.createTrackbar("US", 'Tracking', 255, 255, nothing)
cv2.createTrackbar("UV", 'Tracking', 255, 255, nothing)

while True:
    #frame = cv2.imread('/home/ahu/Workspace/py-video-processing-rsc/opencv-master/samples/data/smarties.png', -1)
    ret, frame = cap.read()

    # Convert a color img to a HSV img
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold the HSV img for a range of color (lower and upper values)
    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")

    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    # Lower and upper blue color
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    #cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()
