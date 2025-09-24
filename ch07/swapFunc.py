#swapFunc.py
#변수간 데이터 스왑1: 임시변수 사용
na = 10
nb = 11
print("na = ", na, "np = ", nb)
temp = na
na = nb
nb = temp
print("na = ", na, "np = ", nb)

print("------------------------")
#변수간 데이터 스왑2: 파이썬만 사용 방법
na = 10
nb = 11
print("na = ", na, "np = ", nb)
na,nb = nb,na
print("na = ", na, "np = ", nb)

print("------------------------")
#변수간 데이터 스왑3: 함수 사용 법
def funca(pa, pb):
    temp = pa
    pa = pb
    pb = temp
    return pa, pb

na = 10
nb = 11
print("na = ", na, "np = ", nb)
na, nb = funca(na, nb)
print("na = ", na, "np = ", nb)