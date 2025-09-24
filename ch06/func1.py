# func1.py

"""
def 함수명(매개변수):
    코드블록
    return 반환값

def 함수명(매개변수):
    코드블록
    return 반환값
"""

def my_func():              #함수에 대한 정의(설계)
    print("토끼야 안녕!")  
my_func()           #호출

print("------------------------")
def fhello():
    print("매개변수 없는 함수 호출하기")
fhello()

print("------------------------")
na = 10
nb = 11
nc = na + nb 
print(na, "+", nb, "=", nc)

print("------------------------")
def funca(na,nb):
    print(na, "+", nb, "=", na+nb)
funca(10, 11)                   #인수 잊지 않고 꼭 넣기!
