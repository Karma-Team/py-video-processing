import numpy as np
import cv2

cap = cv2.VideoCapture('finale_match_1_cut.mp4')

_, frame = cap.read()
add = frame.astype('uint64')
cpt = 1

fgbg = cv2.createBackgroundSubtractorKNN()

while(cap.isOpened() and cpt < 5000):
    ret, frame = cap.read()
    if ret != 1:
        print("Ret: %d cpt: %d" % (ret,  cpt))
        break

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    add += frame
    cpt += 1

    fgmask = fgbg.apply(frame)

    cv2.imshow('frame',frame)
    cv2.imshow('fgmask',fgmask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

moy = add/cpt
moy = moy.astype('uint8')

cv2.imshow('background', moy)
cv2.imwrite('background.png',moy)
cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()
