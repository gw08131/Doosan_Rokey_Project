# while1.py

#조건에 사용된 변수 초기화
# while 조건:
#   코드 블록
#   반복문을 빠져나올 수 있는 증감식

num = 0
while num <3:
    print('안녕 거북이',num)
    num += 1

"""
while True:
    print("ctrl+c를 누르세요. ")
"""


stra = "파이썬"
strb = "프로그래밍"
# stra = stra + strb
stra += strb
print(stra)


num1 = 10
num2 = 20
num1 += num2
print(num1)
