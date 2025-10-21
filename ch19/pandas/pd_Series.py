# pd_Series.py

import pandas as pd

# list 데이터 활용 생성
data = [10,20,30]
series = pd.Series(data)
print(type(series))         # <class 'pandas.core.series.Series'>
print(series)

print("----------------------")
# dictionary 데이터 활용 생성
data = {'a': 10,'b':20,'c':30}
series = pd.Series(data)
print(type(series))         
print(series)