#Human.py

class Human:
    #메모리에 인스턴스 생성
    #인스턴스 변수 초기화
    #return 반환 없음
    def __init__(self,age,name):
        self.age = age
        self.name = name
    
    def intro(self):
        print("나이:",self.age,"살", end=" ")
        print("이름:", self.name)


Kim = Human(10,"김수로")
#print(Kim.age)
#print(Kim.name) 
Kim.intro()       
Lee = Human(15, "이수근")
Lee.intro()   #이게 없으면 출력 불가 (class안에 intro 만들기만했지 호출/실행 X니까)