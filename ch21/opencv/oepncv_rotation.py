# oepncv_rotation.py

import cv2

# 이미지 파일 읽기
image = cv2.imread(r"C:\rokey\python\ch21\opencv\rocket-launch-67643_1280.jpg")
print(image.shape)

(h,w) =image.shape[:2]
center = (w/2,h/2)
M = cv2.getRotationMatrix2D(center,45,1.0)
rotated = cv2.warpAffine(image,M,(w,h))

# 이미지 창에 표시
cv2.imshow('Rotated image',rotated)
cv2.waitKey(0)      # 0 = 무한대기
cv2.destroyAllWindows()     # 모든 openCV 창 닫기

# (0,0)--------------------> x축 (너비,width)
