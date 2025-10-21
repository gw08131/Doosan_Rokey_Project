# pd_data1.py

import pandas as pd

data = {
        'ID':[1,2,3],
        'Name':['Alice','Bob','Charlie'],
        'Age':[30,35,25]
        }
df = pd.DataFrame(data)
print(df)

print("열 추가-----------------")
df['Salary'] = [50000,60000,70000]
print(df)

print("행 추가/수정-----------------")
df.loc[len(df)] = [4,'David',40,80000]
print(df)

print("행 삭제-----------------")
df = df.drop(1)
print(df)

# 행 번호 주의
# print(len(df))          # 3
# df.loc[len(df)] = [5,'Eve',50,90000]
# print(df)

print("데이터 연결-----------------")
data2 = {
        'ID':[5,6],
        'Name':['Eve','Frank'],
        'Age':[28,33]
        }

df2 = pd.DataFrame(data2)
print(df2)

print("-----------------")
concated = pd.concat([df,df2])
print(concated)

# print("------------------")
# # 결축값(NaN)으로 인해 정수 타입이 실수타입으로 표현
# # => NaN은 실수형(float) 데이터로 표현됨
# concated.info()

# print("인덱스 초기화------------------")
# # 0부터 시작하는 새 정수 index를 생성
# # drop=True: 기존 index 열을 버림
# reseted = concated.reset_index(drop=True)
# print(reseted)

print("데이터 병합-----------------")
data3 = {
        'ID':[1,2,3,4,5,6],
        'Department':['HR',
                      'Engineering',
                      'Sales',
                      'R&D',
                      'Finance',
                      'Sales']
        }

df3 = pd.DataFrame(data3)
merged = pd.merge(concated, df3)
print(merged)

#데이터 처리
print("결측치(NaN) 처리-----------------")
print(merged.isnull())          # True라고 뜨는건 결측치이다
print(merged.isnull().sum())    # 각 열에 몇개의 null이 있는지 숫자로 찾아줌


meanVal = merged['Salary'].mean()
merged['Salary'] = merged['Salary'].fillna(meanVal)
print(merged)

print("중복 데이터 처리-----------------")
data1 = {
        'ID':[1,3],
        'Name':['Alice','Charlie'],
        'Age':[30,35],
        'Salary':[50000,70000],
        'Department':['HR','Sales']
        }

df1 = pd.DataFrame(data1)
df1 = pd.concat([merged,df1])
print(df1)                      # Alice랑 Charlie 중복

print(df1.duplicated())       
df1_1 = df1.drop_duplicates()

print(df1_1)