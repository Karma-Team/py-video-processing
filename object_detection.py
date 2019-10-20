import cv2
import numpy as np

print("OpenCV version:", cv2.__version__)

# HSV : Hue, Saturation, Value
# Hue : color component (base pigment : 0-360)
# Saturation : amount of color (depth of the pigment : 0-100%)
# Value : brightness of the color (0-100%)

blue = np.uint8([[[255, 0, 0]]])
hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
print("hsv_blue: ", hsv_blue)
# 120 (70/120) ; (115/255) ; (115/255)
b_l_h = 70
b_l_s = 115
b_l_v = 115
b_u_h = 120
b_u_s = 255
b_u_v = 255

green = np.uint8([[[0, 255, 0]]])
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
print("hsv_green: ", hsv_green)
# 0 (35/90) ; (75 /255) ; (75:255)
g_l_h = 35
g_l_s = 75
g_l_v = 75
g_u_h = 90
g_u_s = 255
g_u_v = 255

red = np.uint8([[[0, 0, 255]]])
hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
print("hsv_red: ", hsv_red)
# 60 (0/10) : (75/255) ; (175:255)
r_l_h = 0
r_l_s = 75
r_l_v = 175
r_u_h = 10
r_u_s = 255
r_u_v = 255


# callback fct : x current position of the trackbar
def nothing(x):
    pass


# Create a tracking window
cv2.namedWindow('Tracking')

# Open a video
cap = cv2.VideoCapture('finale_match_1_full.mp4')

# Create trackbars for :
# LH (Lower Hue) ; LS (Lower Saturation) ; LV (Lower Value)
# UH (Upper Hue) ; US (Upper Saturation) ; UV (Upper Value)
cv2.createTrackbar("LH", 'Tracking', 0, 255, nothing)
cv2.createTrackbar("LS", 'Tracking', 0, 255, nothing)
cv2.createTrackbar("LV", 'Tracking', 0, 255, nothing)
cv2.createTrackbar("UH", 'Tracking', 255, 255, nothing)
cv2.createTrackbar("US", 'Tracking', 255, 255, nothing)
cv2.createTrackbar("UV", 'Tracking', 255, 255, nothing)
blueDetection = 'Blue 0:OFF / 1:ON'
cv2.createTrackbar(blueDetection, 'Tracking', 0, 1, nothing)
greenDetection = 'Green 0:OFF / 1:ON'
cv2.createTrackbar(greenDetection, 'Tracking', 0, 1, nothing)
redDetection = 'Red 0:OFF / 1:ON'
cv2.createTrackbar(redDetection, 'Tracking', 0, 1, nothing)

while (cap.isOpened()):
    ret, frame = cap.read()
    # print(frame.shape)
    frame = cv2.resize(frame, (900, 600))
    # print(frame.shape)

    # Convert a color img to a HSV img
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get the position of the trackbars
    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")
    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")
    b = cv2.getTrackbarPos(blueDetection, "Tracking")
    g = cv2.getTrackbarPos(greenDetection, "Tracking")
    r = cv2.getTrackbarPos(redDetection, "Tracking")

    if b == 1:
        l_h = b_l_h
        l_s = b_l_s
        l_v = b_l_v
        u_h = b_u_h
        u_s = b_u_s
        u_v = b_u_v
    elif g == 1:
        l_h = g_l_h
        l_s = g_l_s
        l_v = g_l_v
        u_h = g_u_h
        u_s = g_u_s
        u_v = g_u_v
    elif r == 1:
        l_h = r_l_h
        l_s = r_l_s
        l_v = r_l_v
        u_h = r_u_h
        u_s = r_u_s
        u_v = r_u_v

    # Threshold the HSV img for a range of color (lower and upper color values)
    lower_color = np.array([l_h, l_s, l_v])
    upper_color = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsv, lower_color, upper_color)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Blue detection
    lower_color = np.array([b_l_h, b_l_s, b_l_v])
    upper_color = np.array([b_u_h, b_u_s, b_u_v])
    b_mask = cv2.inRange(hsv, lower_color, upper_color)
    b_res = cv2.bitwise_and(frame, frame, mask=b_mask)
    b_res = cv2.resize(b_res, (300, 200))

    # Green detection
    lower_color = np.array([g_l_h, g_l_s, g_l_v])
    upper_color = np.array([g_u_h, g_u_s, g_u_v])
    g_mask = cv2.inRange(hsv, lower_color, upper_color)
    g_res = cv2.bitwise_and(frame, frame, mask=g_mask)
    g_res = cv2.resize(g_res, (300, 200))

    # Red detection
    lower_color = np.array([r_l_h, r_l_s, r_l_v])
    upper_color = np.array([r_u_h, r_u_s, r_u_v])
    r_mask = cv2.inRange(hsv, lower_color, upper_color)
    r_res = cv2.bitwise_and(frame, frame, mask=r_mask)
    r_res = cv2.resize(r_res, (300, 200))

    # cv2.imshow('frame', frame)
    # cv2.imshow('mask', mask)
    cv2.imshow('Tracking', res)
    # cv2.imshow('Blue Detection', b_res)
    # cv2.imshow('Green Detection', g_res)
    # cv2.imshow('Red Detection', r_res)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()
