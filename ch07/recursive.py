#recursive.py

#def 함수명(매개변수):
#   return 반환값
#함수병()

#def funcA():
#    funcA()
#    return
#funcA()

#return 뒤에 아무 값이 없으면, Python은 자동으로 None을 반환
#즉 return만 써도 함수 종료의 의미가 됨

# 기능: 숫자를 카운트
def count_down(n):
    if n == 0:
        print("완료!")
        #return의 역할 = 값을 돌려주는 것(return 값) 이 아니라, 함수를 종료
        return          #꼭 필요 (재귀 종료 용도)
    print(n)
    count_down(n-1)

count_down(5)

print("--------------------------")

#문제: 팩토리얼을 계산하는 재귀 함수를 작성하시오.
# 5! = 5*4*3*2*1=120
def factorial(number):
    if number == 0:
        return 1        # 1을 안 쓰면 None 반환
    else:
       return number * factorial(number-1)


print(factorial(5))


print("--------------------------")
x = 10
def fadd(num):
    b=x+num
    print("변수x값은",x)
    print("변수b값은",b)
fadd(10)

#변수x값은 10
#변수b값은 20

#전역변수 지역변수 읽기(read) 가능
#전역변수 지역변수 쓰기(write)/수정 불가능


print("--------------------------")
x = 10
def fadd(num):
    x=x+num
    print("변수x값은",x)
fadd(10)

#UnboundLocalError: cannot access local variable 'x' where it is not associated with a value

print("--------------------------")
x = 10
def fadd(num):
    global x
    x=x+num
    print("변수x값은",x)
fadd(10)

#변수x값은 20