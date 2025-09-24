#global1.py

na = 10

#지역 변수 => 전역(global) 사용
def funcA():
    global na            #지역이지만, 전역 공간에서 쓰임
    print("na", na)         
    return

funcA()
print("na", na)
