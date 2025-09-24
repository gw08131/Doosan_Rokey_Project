# global3.py

# a를 전역 변수로 사용하도록 변경
b = 0
print("b의 값은", b)
b = 1
print("b의 값은", b)

def scope_test():
    global a
    a = a + 3
    print("scope_test() 함수 안의 a 값은", a)

a = 0
print("scope_test() 함수 밖(호출 전) a 값은", a)
# scope_test() 호출 → global a 덕분에 함수 안에서 a는 전역 a를 가리킴.
scope_test()
print("scope_test() 함수 호출 후 a 값은", a)


print("-------------------------")
# a를 지역 변수로 사용하는 방법
b = 0
print("b의 값은", b)
b = 1
print("b의 값은", b)

def scope_test(x):
    a = x
    a = a + 3
    print("scope_test() 함수 안의 a 값은", a)
    return a

a = 0
print("scope_test() 함수 밖(호출 전) a 값은", a)
#scope_test()
print("scope_test() 함수 호출 후 a 값은", scope_test(a))