import numpy as np
import cv2

cap = cv2.VideoCapture('rtsp://admin:pg7ggc385h84@192.168.10.24:31102/h264.sdp.html')

while(True):

    ret, frame = cap.read()
    cv2.imshow('Stream IP Camera OpenCV', frame)
    print("cameraOn")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()