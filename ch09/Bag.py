# Bag.py

#가방클래스
class Bag:
    def __init__(self):     #변수 초기화
        self.data = []
    
    def add(self,x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x) 

handbag = Bag()     #self = handbag
print(handbag.data)
handbag.add("지갑")
handbag.add("보조배터리")
handbag.addtwice("신용카드")
print("핸드백:",handbag.data)


backpack = Bag()    #self = backpack
backpack.data
backpack.add("립스틱")
print("백팩:",backpack.data)

# clutch = Bag()      #self = clutch
# clutch.data
# clutch.add()