#lambda.py

# def 함수명(매개1, 매개2...):
#     코드블록
#     return 반환값

# lambda 인자: 표현식

def funcA(x):
    return x+x
print(funcA(1))
print(funcA(2))
print(funcA(3))

print("--------------------")
add = lambda x: x+x
print(add(3))
print(add(2))
print(add(1))

print("--------------------")
square = lambda x: x**2
print(square(3))

print("--------------------")
#한줄 표현식만 가능 (여러줄 나누기 불가능)

# 여러줄 나누기 불가
# square = lambda x:
#         y = x+1
#         y **2

expression1 = lambda x: (x+1)**2
print(expression1(5))

print("--------------------")
adder = lambda x,y=5: x+y     #기본값 할당시 뒤에서부터
print(adder(3))         #8
print(adder(3,10))      #13

print("--------------------")
print((lambda x,y:x+y)(2,4))

print("--------------------")
#외부 변수 사용
num = 2
expression2 = lambda x: (x+1)**2
print(expression2(2))


#리스트/딕셔너리 사용
data = [1,2,3]
dic_data = {"9월":"24"}
f = lambda x: x+data[0]
f1 = lambda x: x+dic_data["9월"]
print(f(5))
print(f1("날짜: "))