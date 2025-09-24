# Human.py

#부모클래스(super), 추상적
class Human:
    #속성 정의
    eyes = 2
    nose = 1
    mouth = 1
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #매소드(기능/동작) 정의
    def introduce(self):
        print("이름:",self.name)
        print("나이:",self.age)
    def eat(self):
        print("먹다.")
    def sleep(self):
        print("자다.")
    def talk(self):
        print("말하다.")

#자식클래스(sub), 구체적
class Student(Human):       #상속
    def __init__(self, name, age, studentNum):
        super().__init__(name, age)
        self.studentNum = studentNum

    def introduce(self):
        super().introduce()
        print(f"학번:",{self.studentNum})

    def study(self):
        print("공부하다.")


lee = Human("이수근",45)
lee.introduce()
lee.sleep()
print(lee.eyes)     #속성값 바로 프린트

print("-----------------------")
kim = Student("김수로",15,20225163)      # Human class를 받아 써서 인수에 2개 값 넣기!
kim.introduce()
kim.eat()
print(kim.eyes)
kim.study()

print("-----------------------")
choi = Human("최수종",18)
choi.introduce()

print("-----------------------")
hong = Human("홍길동",33)
hong.introduce()
kim2 = Student("김유빈", 20, 20220523)
kim2.introduce()
kim.study()