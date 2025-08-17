import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read() # _ = it stores previous pictures and values

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    '''low_green = np.array([36, 40, 40])
    high_green = np.array([85, 255, 255])

    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask = green_mask)'''
    
    low = np.array([0, 40, 0])
    high = np.array([179, 255, 255])

    mask = cv2.inRange(hsv_frame, low, high)
    output = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow("Frame", frame)
    cv2.imshow('output', output)

    key = cv2.waitKey(1)
    if key == 27:
        break