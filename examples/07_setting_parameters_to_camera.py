import cv2

print("OpenCV version:", cv2.__version__)

# Video to read
cap = cv2.VideoCapture('/home/ahu/Workspace/py-video-processing-rsc/opencv-master/samples/data/Megamind.avi');

# Get video parameters
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Set video parameters
# NB : the camera set the resolution available, unless we set customized width and height values
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3000)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 3000)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Capture frame continuously
while(cap.isOpened()):
    # Read the frame
    ret, frame = cap.read()

    if ret == False:
        break

    else:
        # Change color
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Show the capture frame
        cv2.imshow('frame', gray)

        # Wait for the user input
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()


