# Q20-8.py  

from sklearn import svm

X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

clf = svm.SVC()
clf.fit(X,y)

# train_data,test_data,train_label,test_label =\
#     train_test_split(X,y)

# # clf.fit(train_data,train_label)
# pre = clf.predict(test_data)
# # print(pre)

# ac_score = metrics.accuracy_score(test_label,pre)
# # print(ac_score)

pre = clf.predict([[4.5],[6.5]])
print(pre)



# 로지스틱 회기모델을 학습을 시키라:
from sklearn.linear_model import LogisticRegression

X = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
y = [0,0,0,0,1,1,1,1,1,1]

clf = LogisticRegression()   # ← 로지스틱 회귀
clf.fit(X, y)
print(clf.predict([[4.5],[6.5]]))
