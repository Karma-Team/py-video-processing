import numpy as np
import cv2

FILENAME = "capture.png"
THRESHOLD_RED = 50 #  127
THRESHOLD_GREEN = 60 #  127
THRESHOLD_BLUE = 50 #  127

BLUE = 0
RED = 1
GREEN = 2

img = cv2.imread(FILENAME)
cv2.imshow("init", img)

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgB = img[:, :, BLUE]
imgR = img[:, :, RED]
imgG = img[:, :, GREEN]
retB, threshB = cv2.threshold(imgB, THRESHOLD_BLUE, 255, 0)
retR, threshR = cv2.threshold(imgR, THRESHOLD_RED, 255, 0)
retG, threshG = cv2.threshold(imgG, THRESHOLD_GREEN, 255, 0)

threshRR = threshG - threshR
threshGG = threshR - threshG

contoursR, hierarchyR = cv2.findContours(threshRR, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contoursG, hierarchyG = cv2.findContours(threshGG, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(len(contoursR))
#print(len(contoursG))
#imgResR = cv2.drawContours(img, contoursR, -1, (0, 255, 0), 3)
#imgResG = cv2.drawContours(img, contoursG, -1, (0, 0, 255), 3)
cv2.imshow("imgB", imgB)
cv2.imshow("imgR", imgR)
cv2.imshow("imgG", imgG)
cv2.imshow("threshB", threshB)
cv2.imshow("threshR", threshR)
cv2.imshow("threshRR", threshRR)
cv2.imshow("threshGG", threshGG)
cv2.imshow("threshG", threshG)
#cv2.imshow("resultR", imgResR)
#cv2.imshow("resultG", imgResG)
cv2.waitKey(0)

cv2.destroyAllWindows()
