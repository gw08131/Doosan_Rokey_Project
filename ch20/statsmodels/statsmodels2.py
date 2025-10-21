# statsmodels2.py

import statsmodels.api as sm
import pandas as pd

# 데이터 R에서 가져오기
data = sm.datasets.get_rdataset("mtcars").data
# print(data)

x = data[["hp",'wt']]      # 마력
y = data["mpg"]     # 연비


X = sm.add_constant(x)              # const 열 추가

model = sm.OLS(y, X).fit()          # 반드시 X로 적합!

print("const (절편):", model.params["const"])           # 37.22727011644722
print("hp 계수(기울기):", model.params["hp"])           # -0.031772946982162834 hp 기울기
print("wt 계수(기울기):", model.params["wt"])           # -3.877830742404683

print(model.params[1])
print(model.params[0])

print(model.summary())