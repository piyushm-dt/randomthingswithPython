import cv2
import numpy
from matplotlib import pyplot as plt

img = cv2.imread('a4.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('Marshall',img)
cv2.imwrite('king mathers',img)
