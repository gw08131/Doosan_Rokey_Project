# Q20-6.py

import statsmodels.api as sm

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

X = sm.add_constant(x)

model = sm.OLS(y,X).fit()

print("기울기:", model.params[1])
print("절편:", model.params[0])

# 혹은...
import statsmodels.api as sm
import pandas as pd

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

X = pd.DataFrame({'x': x})
X = sm.add_constant(X)           # const 열 추가
model = sm.OLS(y, X).fit()

print("기울기:", model.params['x'])       # 2.0 (근사값)
print("절편:", model.params['const'])    # 0.0 (근사값)
