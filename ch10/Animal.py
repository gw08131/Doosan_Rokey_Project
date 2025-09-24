# Animal.py

class Animal:
    def eat(self):
        print("먹다.")
    def move(self):
        print("이동하다.")
    def sound(self):
        print("소리내다")
    
class Cat(Animal):
    def eat(self):
        print("잡식하다.")      #동작변경

    def sound(self):
        print("야옹~")           #동작변경
        print(super().sound())   #부모클래스의 sound 출력!

    def jump(self):
        print("점프하다")       #기능확장

# 부모 클래스 
animal = Animal()
animal.eat()
animal.sound()

print("----------------")
# 자식 클래스 overriding
cat1 = Cat()
cat1.eat()      #재정의 기능사용
cat1.move       #부모 기능사용
cat1.sound()