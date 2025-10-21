# np_module.py

import numpy as np

# 배열 기본 생성
arr = np.array([1,2,3,4,5])
print(type(arr))            # ndarray <= n차원 array
print(arr)

print(arr.shape)        # (5,)
print(arr.dtype)        # int64

print("0으로 초기화된 배열----------------------")
zeros = np.zeros((3,3))
print(zeros)

print("1로 초기화된 배열----------------------")
ones = np.ones((2,4))
print(ones)
print(ones.shape)
print(ones.dtype)

print("값으로 초기화된 배열----------------------")
full = np.full((2,2),7)
print(full)

print("단위 행렬----------------------")
identity1 = np.eye(2,3)     # 직사각행렬 
print(identity1)

identity2 = np.identity(3)  # 정사각행렬
print(identity2)

print("난수 배열----------------------")
# 0 이상 1 미만 범위의 정수 난수 생성 
random = np.random.rand(3,3)
print(random)
print(random.shape)
print(random.dtype)

print("------------------------")
# 1 이상 10 미만 범위의 정수 난수 생성 
randint = np.random.randint(1,10,(3,3))
print(randint)
print(randint.shape)
print(randint.dtype)


print("기본 산술 연산------------------------")
arr = np.array([1,2,3,4])
print(arr+5)
print(type(arr+5))
print(arr+2)

print("통계 함수------------------------")
print(arr.sum())
print(arr.mean())
print(arr.max())
print(arr.min())

print("배열 간 연산------------------------")
# 브로드캐스팅
arr1 = np.array([1,2,3])
print(arr1)
print("------------")
arr2 = np.array([[1],[2],[3]])
print(arr2)
print("------------")
# 브로드캐스팅: 자동으로 (모양을) 맞춰서 늘려준다.
# arr1은 1차원이지만 연산시 (1,3) 자동 동작
result = arr1+arr2
print(result)

print("행렬곱-----------------------")
matrix1 = np.array([[1,2],[3,4]])
matrix2 = np.array([[5,6],[7,8]])
result = np.dot(matrix1,matrix2)
print(result)

print("기본 인덱싱-----------------------")
arr = np.array([10,20,30,40])
print(arr[2])

arr = np.array([[1,2,3],[4,5,6]])
print(arr)
print(arr[1,2])

print("슬라이싱-----------------------")
print(arr[0,:])
print(arr[:,1])

print("조건부 연산-----------------------")
arr = np.array([1,2,3,4,5,6])
filtered = arr[arr>3]
print(filtered)

import pandas as pd
df = pd.DataFrame(arr,columns=["Value"])
print(df)