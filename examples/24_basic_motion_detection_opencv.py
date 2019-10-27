import cv2
import numpy as np
from matplotlib import pyplot as plt

print("OpenCV version:", cv2.__version__)

cap = cv2.VideoCapture('/home/ahu/Workspace/py-video-processing-rsc/video_data/finale_match_1_cut.mp4')

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    # Get the difference of the two img and convert it in gray scale
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # Blur the grayscale frame
    # args : gray, kernelSize, SigmaX value
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Find the threshold
    # args : blur, minimum threshold value, maximum threshold value, mode
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    # Dilate the threshold img to fill all the holes
    # args : thresh, kernel, number of iterations
    dilated = cv2.dilate(thresh, None, iterations=3)

    # Find the contours
    # args : img, mode, method
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Analyse each contour
    for contour in contours:
        # args : frame, contours, contour id, color, thickness
        # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

        # Get the contour features
        (x, y, w, h) = cv2.boundingRect(contour)

        # Prevent from noise
        if cv2.contourArea(contour) < 5000:
            continue

        # Draw the contour and put text
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)



    # Display the frame
    cv2.imshow("feed", frame1)

    # Assign frame2 in frame1 for the next iteration
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.realease()
