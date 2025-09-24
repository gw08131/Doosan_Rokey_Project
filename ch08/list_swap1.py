# list_swap1.py

na = 10
nb = 11
print("na:", na, "nb: ", nb)

temp = na
na = nb
nb = temp
print("na:", na, "nb: ", nb)


print("------------------")
ca = [10,11]
print("ca[0]: ", ca[0], "ca[1]: ", ca[1])

temp = ca[0]
ca[0] = ca[1]
ca[1] = temp
print("ca[0]: ", ca[0], "ca[1]: ", ca[1])


print("------------------")
def funca(na,nb):
    temp = na
    na = nb
    nb = temp

ca = [10, 11]
print("ca[0]: ", ca[0], "ca[1]: ", ca[1])       #ca[0]:  10 ca[1]:  11


funca(ca[0], ca[1])
print("ca[0]: ", ca[0], "ca[1]: ", ca[1])       #ca[0]:  10 ca[1]:  11 swap 없음
# Swap이 안된 이유:
# funca(ca[0, ca[1]])의 각 10, 11이 na, nb로 지정됨
# 즉 na, nb는 ca의 원소가 아니라, int 10 (별도의 지역변수)으로 지정됨 (int는 immutable 타입이니까)
# 함수 안에서 na = 11, nb = 10이 되지만, 지역 변수 안에서만 유효
# 함수가 종료되면 지역 변수 na, nb는 사라지고
# 리스트 ca와 연결도 X => ca는 원래 값 [10, 11]을 유지


# Swap 해결 방법
# 1. return으로 돌려받기 (return na nb)
#    def funca(na, nb):
#        temp = na
#        na = nb
#        nb = temp
#        return na, nb
#    ca = [10, 11]
#    ca[0], ca[1] = funca(ca[0], ca[1])
# 2. 리스트 자체로 전달받기 (mutable 타입)
#    def funca(cb):
#       temp = cb[0]
#       cb[0] = cb[1]
#       cb[1] = temp


print("------------------")
ca = [10,11]
cb=ca
print("리스트 ca 값은 ", ca)
print("리스트 cb의 값은 ", cb)

print("------------------")
ca = [10,11]
cb=ca
print("ca",ca)
print("ca", id(ca))     #ca 2684799853952
print("ca[0]", id(ca[0]))
print("ca[1]", id(ca[1]))

print("cb", cb)         
print("cb", id(cb))     #cb 2684799853952 (ca랑 주소값이 같음)
print("cb[0]", id(cb[0]))
print("cb[1]", id(cb[1]))


print("------------------")
ca = [10, 11]
ca = cb
print("ca",ca)
print("cb", cb)  

temp = cb[0]
cb[0] = cb[1]
cb[1] = temp   

print("ca",ca)
print("cb", cb)         #ca를 swap 했지만 cb도 같이 swap이 됨 (왜냐면 cb=ca로 id(메모리)를 공유하니까!)


print("------------------")
def funca(cb):
    temp = cb[1]
    cb[1] = cb[0]
    cb[0] = temp

ca = [10,11]
print("함수 전 ca",ca)
funca(ca)
print("함수 이후 ca",ca)