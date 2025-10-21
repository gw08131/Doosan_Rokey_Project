# xor.py

from sklearn import svm         # 알고리즘
from sklearn import metrics     # 평가


# 데이터 학습하기
clf = svm.SVC()     # 분류 알고리즘

# 학습(모델 생성)
# fit(학습데이터, 학습레이블)
clf.fit([
        [0,0],
        [0,1],
        [1,0],
        [1,1]
        ],
        [0,1,1,0]
)

# 데이터 예측하기
# predict(테스트데이터)
pre = clf.predict([
                   [0,1],
                   [1,1]
                    ])
print(pre)

# 결과 확인
#metric.accuracy_score(정답/결과레이블,예측데이터)
ac_score = metrics.accuracy_score([1,0],pre)
print(f"정답률: {ac_score}")