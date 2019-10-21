import cv2
import datetime

print("OpenCV version:", cv2.__version__)

# Video to read
cap = cv2.VideoCapture('/home/ahu/Workspace/py-video-processing-rsc/opencv-master/samples/data/Megamind.avi');

# Get video parameters
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# Capture frame continuously
while(cap.isOpened()):
    # Read the frame
    ret, frame = cap.read()

    if ret == False:
        break

    else:
        # Add text to the video
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(width) + ' Height: ' + str(height)
        frame = cv2.putText(frame, text, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        # args : frame, text, coordinates, font, font scale, color, thickness, line type

        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, datet, (10, 150), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

        # Show the capture frame
        cv2.imshow('frame', frame)

        # Wait for the user input
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()


