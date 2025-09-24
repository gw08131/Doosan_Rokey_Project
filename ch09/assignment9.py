# assignment9.py

class Phone:
    def setInfo(self, company, year, color):
        self.company = company
        self.year = year
        self.color = color
        print(self.company, self.year, self.color)
        
    def info(self):
        print(self.company, self.year, self.color)
    


my_phone = Phone()
my_phone.company = "현대"
my_phone.year = 2020
my_phone.color = "black"
my_phone.info()



print("-------------------------------")
class Phone:
    def __init__(self, company, year, color):
        self.company = company
        self.year = year
        self.color = color
        
    def info(self):
        print(self.company, self.year, self.color)

my_phone = Phone("현대",2020,"black")
my_phone.info()
