# dict_func.py

a = {1:"월", "tue":"화", "wed":"수"}
print(a)
x = a
print(x)
x[1] = '일'
print(x)
print(a)

print("-------------------")
def fch(x):
    x[1] = "일"

a = {1:"월", "tue":"화", "wed":"수"}
print(a)
fch(a)
print(a)


print("-------------------")

# * : 가변(위치) 인자 -> tuple 형태로 전달됨
def fsum(*args):
    return sum(args)

print(fsum(1, 2, 3))       # 6 출력
print(fsum(4, 5, 6, 7))    # 22 출력


# ** : 가변 키워드 인자 -> dict 형태로 전달됨
def show_info(**kwargs):
    print(kwargs)

show_info(name="홍길동", age="500")
