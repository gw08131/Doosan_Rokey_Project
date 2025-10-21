# opencv_detectObj.py

import cv2

image = cv2.imread(r"C:\rokey\python\ch21\opencv\people.jpg")

# 2. 얼굴 검출을 위한 모델 확인
face_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

# 3. 이미지를 그레이스케일로 변환
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# 4. 케스케이드 분류기 생성
face_cascade = cv2.CascadeClassifier(face_path)

faces = face_cascade.detectMultiScale(gray,
                                      scaleFactor=1.1,
                                      minNeighbors=3,
                                      minSize=(30,30))
print(faces)
# [[514  90  62  62]
#  [646  98  61  61]
#  [789 149  63  63]]
# 3명 검출

for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),
                  (x+w,y+h),
                  (255,0,0),2)
    
cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()