# regarding morphological transformation
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame,mask=mask)

    kernel = np.ones((5,5),np.uint8)
    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
   # erosion = cv2.erode(mask,kernel,iterations=1)
    #dilation = cv2.dilate(mask,kernel,iterations=1)

    cv2.imshow('o',frame)
    #cv2.imshow('e',erosion)
    cv2.imshow('m',mask)
    #cv2.imshow('d',dilation)
    cv2.imshow('op',opening)
    cv2.imshow('cl',closing)

    k = cv2.waitKey(5) & 0xFF
    if k==27:
        break
cv2.destroyAllWindows()
cap.release()

# idea of opening and closing is to remove false positives and false negatives.
# try cv2.imshow => tophat and blackhat
