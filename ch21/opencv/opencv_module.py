# opencv_module.py

import cv2

# 이미지 파일 읽기
image = cv2.imread(r"C:\rokey\python\ch21\opencv\rocket-launch-67643_1280.jpg")


resized=cv2.resize(image,(300,300))
# 픽셀 (색상)값들의 배열
print(resized)
# print(type(resized))            # <class 'numpy.ndarray'>

# 이미지 창에 표시
cv2.imshow('Resized image',resized)
cv2.waitKey(0)      # 0 = 무한대기
cv2.destroyAllWindows()     # 모든 openCV 창 닫기
