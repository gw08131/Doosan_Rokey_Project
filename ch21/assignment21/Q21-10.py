# Q21-10.py

import cv2

image = cv2.imread(r"C:\rokey\python\ch21\assignment21\tulips-9587986_1280.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,20,40)
cv2.imshow('Edge Detection',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()