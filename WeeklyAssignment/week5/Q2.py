# Q2.py

import cv2

image=cv2.imread(r"C:\rokey\python\WeeklyAssignment\week5\sweetpotato-1975990_1280.jpg")
(h,w) = image.shape[:2]
center = (w//2,h//2)
M=cv2.getRotationMatrix2D(center,-90,1.0)
rotate = cv2.warpAffine(image,M,(w,h))
cv2.imshow("Rotated Potato image",rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()

