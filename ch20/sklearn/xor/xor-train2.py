# xor-train2.py

from sklearn import svm         # 알고리즘
from sklearn import metrics     # 평가
import pandas as pd


xor_data = [
        [0,0,0],
        [0,1,1],
        [1,0,1],
        [1,1,0]
]

xor_df = pd.DataFrame(xor_data)
# xor_df.loc[전체데이터,추출할데이터]
# 학습 데이터
data = xor_df.loc[:,0:1]               # 모든 행에서, 0~1번 열의 데이터 가져옴
# 정답 레이블
label = xor_df.loc[:,2]                # 모든 행에서, indx = 2인 열 데이터 가져오기

# 데이터 학습하기
clf = svm.SVC()     # 분류 알고리즘

# 학습(모델 생성)
# fit(학습데이터, 학습레이블)
clf.fit(data,label)


# 데이터 예측하기
# predict(테스트데이터)
pre = clf.predict(data)
print("예측결과:",pre)

# 결과 확인
ac_score = metrics.accuracy_score(label,pre)
print(f"정답률: {ac_score}")