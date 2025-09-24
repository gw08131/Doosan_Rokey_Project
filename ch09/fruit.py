# fruit.py

#다음과 같은 속성과 동작을 포함한 과일(Fruit) 클래스를 생성하고,
#오렌지(orange) 객체를 생성하여 속성을 출력하고 동작을 수행하시오.
#속성: 이름(name) = '오렌지', 색상(color)='노란색'
#동작: '새콤하다' 맛이나다(taste)

class Fruit:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def set_taste(self,taste):
        self.taste = taste

    def fprint(self):
        print("과일 이름=", self.name, ", 색상=", self.color, ", 맛=",self.taste)

orange = Fruit('오렌지','노란색')
orange.set_taste('새콤하다')
orange.fprint()