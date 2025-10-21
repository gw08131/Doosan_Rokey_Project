# opencv.color.py

import cv2

# 이미지 파일 읽기
image = cv2.imread(r"C:\rokey\python\ch21\opencv\rocket-launch-67643_1280.jpg")

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

# 이미지 창에 표시
cv2.imshow('gray image',gray)
# cv2.imshow('rgb image',rgb)
# cv2.imshow('hsv image',hsv)
cv2.waitKey(0)      # 0 = 무한대기
cv2.destroyAllWindows()     # 모든 openCV 창 닫기

# GRAY 방식
# 1 채널만 사용(밝기만 표현) 255 흰색/0검정
# 이미지 연산의 양을 줄여서 속도를 높이는데 필요

# HSV 방식
# RGB와 마찬가지로 3개의 채널을 갖는 색상 이미지 표현법
# 3 채널은 H(Hue, 색조), S(Saturation, 채도), V(Value, 명도)