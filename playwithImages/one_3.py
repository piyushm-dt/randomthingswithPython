import cv2
import numpy as np
# draw a line: cv2.line(img, (0,0), (f,f), (255,255,255), thickness)
# rect. top left and botttom right coordinates
# circle center and radius

img = cv2.imread('give path to image with extension', cv2.IMREAD_COLOR)

pix = img[55,55]
img[55,55] = [240,120,190]
pix = img[55,55]
print(pix)

img[100:150,100:150] = [200,200,200]
print(img.shape)
print(img.size)
print(img.dtype)

watch_face = img[37:111,107:194]
img[0:74,0:87] = watch_face

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


