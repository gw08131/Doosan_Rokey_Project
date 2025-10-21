# opencv_video.py

import cv2

cv2.VideoCapture(0)     #원점 사용
cap = cv2.VideoCapture(r"ch21\opencv\Skeleton.mp4")       #영상

while True:
     # ret = True/False (가져왔는지 안가져왔는지 체크)
     # 캡쳐로 가져온 영상을 이미지에 대한 frame으로 저장
    ret,frame = cap.read()         
    if not ret:         # 만약 영상이 잘 안 읽혔으면 빠져나옴
        break
    
    edges = cv2.Canny(frame,100,200)
    # cv2.imshow("Video Capture",frame)
    cv2.imshow("Edge Detection Video Capture",edges)

    if cv2.waitKey(10) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()