import cv2
import numpy
from matplotlib import pyplot as plt

img = cv2.imread('give path to image with extension',cv2.IMREAD_GRAYSCALE)
cv2.imshow('WinOne',img)
cv2.imwrite('Title',img)
