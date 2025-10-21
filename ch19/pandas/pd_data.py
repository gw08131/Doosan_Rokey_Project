# pd_data.py

import pandas as pd

# 데이터 탐색
df_csv = pd.read_csv(r"C:\rokey\python\ch19\pandas\data.csv")
print(type(df_csv))
print(df_csv)

print("-------------------------")
import openpyxl

df_xl = pd.read_excel(r"C:\rokey\python\ch19\pandas\data.xlsx")
print(type(df_xl))
print(df_xl)


print("-------------------------")
print(df_csv.head())
print("-------------------------")
print(df_csv.tail())
print("-------------------------")
#print(df_csv.info())
df_csv.info()

print("-------------------------")
print(df_csv.describe())

print("-------------------------")
print(df_csv.sample(2))     # 두개의 샘플만 뽑아줌
print("-------------------------")
print(df_csv.sample(frac=0.5))     # 두개의 샘플만 뽑아줌

# 데이터 조작
print("----------------")
data = {
        'ID':[1,2,3],
        'Name':['Alice','Bob','Charlie'],
        'Age':[30,35,25]
        }
df = pd.DataFrame(data)
print(df)

print("----------------")
print(df['Name'])

print("----------------")
print(type(df['Age']>30))   # Class Series 타입

# 데이터프레임 대괄호 안에 
# 불리언 시리즈를 넣으면 True인 행만 선택됨
filtered = df[df['Age']>30]
print(filtered)

print("----------------")
#데이터 정렬: 오름차순, 내림차순
sorted_df = df.sort_values(by='Age',ascending=False)
print(sorted_df)