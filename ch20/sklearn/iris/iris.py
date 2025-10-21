# iris.py

from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split

# 1. Iris 데이터셋 로드
iris = load_iris()
# print(iris)

df = pd.DataFrame(data=iris.data,
                  columns=iris.feature_names)
df['target'] = iris.target          # target 열 추가
# print(df)

target_names = {
    0:iris.target_names[0],
    1:iris.target_names[1],
    2:iris.target_names[2]
}
df['target'] = df['target'].map(target_names)
#print(df)

# 2. 필요한 열 추출하기
iris_data = df[[
            "sepal length (cm)",
            "sepal width (cm)",
            "petal length (cm)",
            "petal width (cm)"
                ]]
iris_label = df["target"]

# print(iris_data)        
# print(iris_label)

# 3. 학습 전용 데이터와 테스트 전용 데이터로 나누기
# 기본 분할 비율: 25%, 75%
train_data, test_data, train_label, test_label = \
    train_test_split(iris_data,iris_label)

from sklearn import svm, metrics

# 4. 데이터 학습시키고 예측하기
clf = svm.SVC()
clf.fit(train_data,train_label)
pre = clf.predict(test_data)

ac_score = metrics.accuracy_score(test_label, pre)
print(f"정답률: {ac_score}")            # 정답률: 0.9736842105263158
# accuracy가 올라가려면 데이터를 더 제공해주면 됨
