# Q1.py

import cv2

image=cv2.imread(r"C:\rokey\python\WeeklyAssignment\week5\sweetpotato-1975990_1280.jpg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Potato image",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

