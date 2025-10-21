# opencv_detectEdge.py

import cv2

# 이미지 파일 읽기
image = cv2.imread(r"C:\rokey\python\ch21\opencv\rocket-launch-67643_1280.jpg")
print(image.shape)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,threshold1=100,threshold2=150)

# 이미지 창에 표시
cv2.imshow('Canny Edge Detection',edges)
cv2.waitKey(0)      # 0 = 무한대기
cv2.destroyAllWindows()     # 모든 openCV 창 닫기

# (0,0)--------------------> x축 (너비,width)
