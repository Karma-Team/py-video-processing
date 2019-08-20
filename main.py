import numpy as np
import cv2

from scipy import signal as sig

cap = cv2.VideoCapture('finale_match_1_full.mp4')
fast = cv2.FastFeatureDetector_create()

SobelX = np.array([ [-1, 0, 1],[-2, 0, 2], [-1, 0, 1]]) 
SobelX = np.array([ [-1, 0, 1],[-2, 0, 2], [-1, 0, 1]]) 
SobelY = SobelX.transpose()


while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == 0:
        break

    cv2.imshow('frame',frame)
    #cv2.waitKey(0)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    Sx = sig.convolve2d(gray, SobelX) 
    Sy = sig.convolve2d(gray, SobelY) 
    S = np.sqrt(np.power(Sx, 2) + np.power(Sy, 2)).astype('uint8')

    cv2.imshow('S',S)


    whiteImg = np.full((720,1280), 255, dtype='uint8')
    img = frame
    kp = fast.detect(gray,None)
    cv2.drawKeypoints(whiteImg, kp, img, color=(255,0,0))

    cv2.imshow('FAST',img)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
