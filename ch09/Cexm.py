# Cexm.py

class Cexm:             #설계도: 붕어빵 틀
    def fsam(self):
        print("멤버 함수 (메소드)")
    def fsbm(self, pa):
        self.x = pa
        print("멤버 변수 x는",self.x)

ca = Cexm()     #객체(인스턴스) => 첫 번째 붕어빵: 팥 붕어빵
ca.fsam()
ca.fsbm(10)
#print(Cexm.x)      #오류발생
print(ca.x)

cb = Cexm()     #객체(인스턴스) => 두 번째 붕어빵: 슈크림 붕어빵
cb.fsbm(99)


# ca = Cexm()
# Cexm = 설계도
# Cexm() = 설계도로 붕어빵 하나 찍음
# ca = 그 붕어빵(객체)을 가리키는 변수

