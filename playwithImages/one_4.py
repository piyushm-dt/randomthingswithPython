import cv2
import numpy as np

# 500 x 250
img1 = cv2.imread('a8.jpg')
img2 = cv2.imread('a10.jpg')

#add = cv2.add(img1,img2)
add = cv2.addWeighted(img1,0.6,img2,0.4,0.9)
cv2.namedWindow('add',cv2.WINDOW_NORMAL)
cv2.resizeWindow('add',720,640)

cv2.imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows()
