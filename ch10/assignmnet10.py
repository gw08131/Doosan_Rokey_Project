# assignment10.py

print("---------------------")
class Phone:
    def __init__(self,number,color):
        self.number = number
        self.color = color
    
    def showInfo(self):
        print("전화번호:",self.number)
        print("색상:",self.color)
    
class SmartPhone(Phone):
    def __init__(self, number, color, company):
        super().__init__(number, color)
        self.company = company
    
    def showInfo(self):
        super().showInfo()
        print("회사:",self.company)
    


phone = Phone("010-1234-5678","검정")
phone.showInfo()
print(phone.number)
print(phone.color)

print("---------------------")
apple = SmartPhone("010-1234-5678","검정","애플")
apple.showInfo()

print(apple.number)
print(apple.color)
print(apple.company)