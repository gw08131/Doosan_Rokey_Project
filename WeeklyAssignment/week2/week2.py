# week2.py

print("--------1번--------")
def fadd (a,b):
    return a + b

x = int(input("첫번째 숫자:"))
y = int(input("두번째 숫자:"))
print(fadd(x,y))


print("--------2번--------")
def sum_to_n(x):
    total = 0
    for num in range(1,x+1,1):
        total = total + num
    return total

n = int(input("n을 정하시오."))
print(sum_to_n(n))

print("--------4번--------")
x = 5

def example1():
    global x        # 함수 안에서도 global 변수 x를 그대로 쓰겠다고 선언
    x = 15          # global x = 15로 바뀜
    print(x)    

example1()
print(x)


print("--------5번--------")
lst = [10,14,2,89,1.3,100,0.8]
min_num = lst[0]
for i in range(0,len(lst),1):
    if min_num > lst[i]:
        min_num = lst[i]
print(min_num)


print("--------8번--------")
import math

print(math.factorial(5))


print("--------9번--------")
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog_bark = Dog()
print(dog_bark.speak())

print("--------10번--------")
class Person:
    def __init__(self,name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}"
    
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
    

kim = Student("김수지",2022568)
print(kim.introduce(),kim.student_id)