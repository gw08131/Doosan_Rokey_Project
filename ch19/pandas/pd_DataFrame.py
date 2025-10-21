# pd_DataFrame.py

import pandas as pd

# list 데이터 활용 생성
data = [
        [1,'Alice',30],
        [2,'Bob',35],
        [3,'Charlie',25]
        ]
df = pd.DataFrame(data,columns=['ID','Name','Age'])
print(type(df))        
print(df)

print("-------------------")
# dictionary 데이터 활용 생성
data = {
        'ID':[1,2,3],
        'Name':['Alice','Bob','Charlie'],
        'Age':[30,35,25]
        }
df = pd.DataFrame(data)
print(type(df))        
print(df)