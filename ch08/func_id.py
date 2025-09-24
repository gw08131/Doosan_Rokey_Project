# func_id.py

a=[10,11,12,13]
print("list a: ", a)
b=a
print("list b: ", b)

print("--------------------")
a=[10,11,12,13]
print("list a: ", a)
print("a[1]: ", id(a[1]))       #a[1]:  140724107244776

a[1] = 21       #a[1]은 11이 저장되어있는 주소랑은 끊기고, 21 주소랑 연결
print("list a: ", a)
print("a[1]: ", id(a[1]))       #a[1]:  140724107245096 (전 a[1]주소값이랑 다름!)

b = a
print("list b: ", b)

b = [30,31,32]
print("list b: ", b)

print("--------------------")
def fk(cb):
    total = 0
    for sb in range(0,3,1):     #0~2까지 1스텝씩 증가
        total = total + cb[sb]
    cb[2] = total
    return cb

ca=[10,20,30]
print("함수 이전 ca=",ca)
cd = fk(ca)
print("함수 이후 ca=",ca)
print("함수 이후 cd=", cd)