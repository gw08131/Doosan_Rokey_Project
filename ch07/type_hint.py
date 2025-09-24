# type_hint.py

def add(x,y):
    return x+y
print((add(3,5)))
print((add(3.2,5)))
print((add("type ", "hint")))

print("---------------------")

def add(x:int,y:int) -> int:    #type hint는 강제성 X 
    return x+y
print((add(3,5)))
print((add(3.2,5)))             #float로 출력
print((add("type ", "hint")))   #<class 'str'>로 출력
#print((add(13, "hint")))       #이건 연산자에 위배 => 오류