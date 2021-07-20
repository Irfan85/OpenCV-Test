# Ref: https://docs.opencv.org/4.5.2/dd/d43/tutorial_py_video_display.html

import cv2 as cv
import sys

# Create a VideoCapture object. The object function takes a device id or filename as input
cap = cv.VideoCapture(0)

# FourCC specifies the video codec the VideoWriter will use to process the output video file. More info at: http://www.fourcc.org/codecs.php
# We'll output our video as .avi for which XVID codec works
fourcc = cv.VideoWriter_fourcc('X', 'V', 'I', "D")

# We'll output the video file at 20fps, 640x480 frame res (Default) and grayscale mode that means no color. So last argument is false
out = cv.VideoWriter("Output.avi", fourcc, 20.0, (640, 480), False)

# Check whether the capture has been opened or not
if not cap.isOpened():
    print("Can't open the capture")
    exit()

# We'll capture the video frame by frame
while cap.isOpened():
    # The we recieve a return object with each frame that indicates whether the frame was read properly or not
    ret, frame = cap.read()

    # If frame was not read properly, or the video file is over; close the capture
    if not ret:
        print("Can't recieve frame. Exiting...")
        break

    # Turn each frame to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Write the frame to the VideoWriter
    out.write(gray)

    # Display the frame as well
    cv.imshow("Hello", gray)


    # Wait 1ms to recieve a key input from the user. Too much wait time will show down the video
    if cv.waitKey(1) == ord('q'):
        break

# Release the capture after we're done
cap.release
# Also release the VideoWriter
out.release()
# Close all the windows created by OpenCV
cv.destroyAllWindows()