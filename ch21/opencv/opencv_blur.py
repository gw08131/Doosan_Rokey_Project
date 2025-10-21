# opencv_blur.py

import cv2

# 이미지 파일 읽기
image = cv2.imread(r"C:\rokey\python\ch21\opencv\rocket-launch-67643_1280.jpg")
print(image.shape)

blured = cv2.GaussianBlur(image,(29,29),0)
# 블러 함수에서 커널 크기는 홀수
# 픽셀 주변 값 평균/가중평균 등으로 처리
# 홀수 크기 커널이어야 중앙 픽셀이 존재하여 대칭각 처리 가능

# 이미지 창에 표시
cv2.imshow('Gaussian Blur',blured)
cv2.waitKey(0)      # 0 = 무한대기
cv2.destroyAllWindows()     # 모든 openCV 창 닫기
