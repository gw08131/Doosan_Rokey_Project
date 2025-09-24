# mex1.py

class Cvalue:
    def __init__(self):
        self.lista = []
    def add(self, num):
        self.lista.append(num)
    def fprint(self):
        print(self.lista)

def plus(a, b):
    c = a + b
    return c

# 전역 변수 추가
str1 = "hello"   # 기본값 (원하는 값 넣기)

# 전역 객체
p1 = Cvalue()
p1.add(1)
p1.add(2)
p1.add(3)
p1.fprint()
