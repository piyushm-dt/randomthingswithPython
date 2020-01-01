import cv2
import numpy as np

img = cv2.imread('a14.jpg')
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
th = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
# retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
retval, threshold = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
cv2.imshow('org',img)
cv2.imshow('dupx',th)
#cv2.imshow('dup',threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
