import cv2

print("OpenCV version:", cv2.__version__)

# Video to read
cap = cv2.VideoCapture('/home/ahu/Workspace/py-video-processing-rsc/opencv-master/samples/data/Megamind.avi');

# Save the video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('data/video/Megamind_copy.avi', fourcc, 20.0, (640, 480))
# args : video, fourcc class, frames/s, width and height

# Capture frame continuously
while(cap.isOpened()):
    # Read the frame
    ret, frame = cap.read()

    if ret == False:
        break

    else:
        # Get property ID (frame width and height)
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        # Save the video
        out.write(frame)

        # Change color
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Show the capture frame
        cv2.imshow('frame', gray)

        # Wait for the user input
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
out.release()
cv2.destroyAllWindows()


