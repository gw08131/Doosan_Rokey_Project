# func2.py

#변수명/함수명 작성시 권장 스타일
#1. 이름 의미: 데이터 형태/기능(동작)
#2. 적절히 요약된 풀네임
#3. 이름 작성시 사용하는 스타일 종료
# 3-1. snake case: 소문자+_(언더바)
#   예) 함수기능 print_get_number
# 3-2. camel cakse: 대문자+소문자
#   예) 함수기능 printGetNumber
#4. (함수작성시) 기능(동작) => 동사+명사
#   예) addInt



def add(num1, num2):
    return num1 + num2      #return이 없으면 결과값으로 반환 X
print(add(1,2))

sum = add(2,3)
print(sum)

print("----------------------------")

def funca(pa,pb):
    nc = pa+pb
    return nc       
# return으로 nc 안의 "값"만 함수 밖으로 꺼내줌
# 하지만 변수 nc 자체는 지역변수라 함수가 끝나면 사라짐
# 함수 밖에서 이 값을 쓰려면 새로운 변수(nd)에 받아야 함

na = 10
nb = 11

nd = funca(na,nb)
print(na,"+",nb,"=",nd)

#return이 값을 자동으로 global 변수에 저장 X
#return은 단순히 값을 “돌려주는” 역할만
#그 값을 받을지 말지는 함수 밖 코드에서 결정

print("----------------------------")
def fplusminus(arg):
    if arg > 0:
        return "plus"
    elif arg < 0:
        return "minus"

stra = fplusminus(0)        # None => becasue 인수가 0이면 반환할 값이 없어서
strb = fplusminus(10)   
strc = fplusminus(-5)     
print(stra)
print(strb)
print(strc)

print("----------절대값 리턴 함수------------------")
def myabs(arg):
    if arg < 0:
        result = arg *-1
    else:
        result = arg
    return result ,'hi'

print(myabs(-100),myabs(10))
"""
absolute99 = myabs(-99)
absolute10 = myabs(-10)
print(absolute99, absolute10)
"""


print("----------------------------")
def funca():
    print("funca 함수 호출")    #4

def funcb():
    funca()                    #3
    print("funcb 함수 호출")    #5

def funcc():
    funcb()                    #2
    print("funcc 함수 호출")    #6

funcc()                         #1

print("----------------------------")
def draw_stars(num):
    print('*' * num)

draw_stars(3)
draw_stars(2)
draw_stars(1)

