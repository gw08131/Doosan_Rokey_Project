# opencv_inRange.py

import cv2
import numpy as np

image = cv2.imread(r"C:\rokey\python\ch21\opencv\MnMs.jpg")

hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

green_lower = np.array([35,100,100])
green_upper = np.array([85,255,255])
green_mask = cv2.inRange(hsv,green_lower,green_upper)
result = cv2.bitwise_and(image,image,mask=green_mask)

cv2.imshow('Green Color Filtering',result)
cv2.waitKey(0)
cv2.destroyAllWindows()