# p1.py

def fadd(x=1,y=5):
    ohap = x + y
    return ohap

ohap = fadd(10,20)
print("ohap의 값은",ohap)

ohap2 = fadd(10)
print("ohap2의 값은",ohap2)

ohap3 = fadd()
print("ohap3의 값은",ohap3)


print("----------------------")
class Cadd:
    def fadd (self,a=1,b=5):
        self.x = a
        self.y = b
        self.hap = self.x+self.y

obj = Cadd()
obj.fadd(10,20)
print("hap값은 ", obj.hap)

obj.fadd(10)
print("hap값은 ", obj.hap)

obj.fadd()
print("hap값은 ", obj.hap)

print("----------------------")
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        
    def show(self):
        print(self.name,"은/는", self.sound, "소리를 내다")

cat = Animal("고양이", "야옹")
cat.show()