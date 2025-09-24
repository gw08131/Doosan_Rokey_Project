# Car.py

# 속성: 차량번호
# 기능: 없음

class Car:
    def __init__(self, num, speed):
        self.num = num
        self.speed = speed
    def fprint(self):
        print("차량번호: ", self.num)
        print("속도: ", self.speed)

new_car = Car(2023, 90)
new_car.fprint()

old_car = Car(8902, 60)
old_car.fprint