import numpy as np
import cv2

from scipy import signal as sig

import HeatMap as HM

cap = cv2.VideoCapture('finale_match_1_full.mp4')
fast = cv2.FastFeatureDetector_create()

HEATMAP_SIZE = 20
HEATMAP_TRIGGER = 80
HEATMAP_TRANSPARENCY = 0.6
HEATMAP = ( (0, HEATMAP_TRIGGER), ( (0,0,255), (0,255,0)))

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


    """ Sobel convolution """
    Sx = sig.convolve2d(gray, SobelX) 
    Sy = sig.convolve2d(gray, SobelY) 
    S = np.sqrt(np.power(Sx, 2) + np.power(Sy, 2)).astype('uint8')

    """ Heat Calculation"""
    hmF,hmA = HM.HeatMap(S, HEATMAP_SIZE, HEATMAP)

    Sc = cv2.cvtColor(S, cv2.COLOR_GRAY2BGR)
    imgHM = cv2.addWeighted(hmF, HEATMAP_TRANSPARENCY, Sc, 0.8, 0)

    HMSx = sig.convolve2d(hmA, SobelX)
    HMSy = sig.convolve2d(hmA, SobelY)
    HMS = np.sqrt(np.power(HMSx, 2) + np.power(HMSy, 2)).astype('uint8')
    whiteImg = np.full(HMS.shape, 255, dtype='uint8')
    HMF = hmA
    kp = fast.detect(gray,None)
    cv2.drawKeypoints(whiteImg, kp, img, color=(255,0,0))


    cv2.imshow('S',S)
    cv2.imshow('HM',hmF)
    cv2.imshow('S+HM',imgHM)
    cv2.imshow('HMS',HMS)

    """ Fast feature detector """
    whiteImg = np.full((720,1280), 255, dtype='uint8')
    img = frame
    kp = fast.detect(gray,None)
    cv2.drawKeypoints(whiteImg, kp, img, color=(255,0,0))

    cv2.imshow('FAST',img)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
