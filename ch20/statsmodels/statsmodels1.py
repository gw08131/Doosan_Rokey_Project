# statsmodels1.py

import statsmodels.api as sm
import pandas as pd

data = sm.datasets.get_rdataset("mtcars").data
# print(data)

x = data["hp"]      # 마력
y = data["mpg"]     # 연비

X = sm.add_constant(x)      # x 절편

model = sm.OLS(y,x).fit()   # 학습
print(model.summary())