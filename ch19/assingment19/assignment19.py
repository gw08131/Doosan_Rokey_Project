# assignment19.py

import pandas as pd

print("----------6번-----------")
path = r"C:\rokey\python\ch19\assingment19\data.csv"
df = pd.read_csv(path)

print(df)
print("Age 평균:",df['Age'].mean()," 최댓값:",df['Age'].max()," 최솟값:",df['Age'].min())
print("Salary 평균:",df['Salary'].mean()," 최댓값:",df['Salary'].max()," 최솟값:",df['Salary'].min())

print("----------7번-----------")
print(df[(df['Age']>=30) & (df['Salary']>=60000)])



print("----------8번-----------")
import numpy as np

arr = np.arange(1, 11)
arr_sq = arr ** 2
print("원본 배열:", arr)
print("제곱 배열:", arr_sq)
print("평균:", arr_sq.mean(), "최댓값:", arr_sq.max(), "최솟값:", arr_sq.min())


print("----------9번-----------")
import numpy as np

arr1 = np.random.randint(1, 13, (3,4))  
result = []

for i in range(len(arr1)):
    result.append(int(arr1[i].max()))

print("원본 행렬:\n",arr1)
print("각 행의 최댓값:",result)


print("----------9번-----------")
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.plot(x,y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Line Plot")
plt.grid()
plt.show()

