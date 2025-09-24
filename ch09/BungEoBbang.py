# 붕어빵 틀 (클래스)

# 속성 : filling(재료), price(가격)
# 기능 : show() → 붕어빵 정보 출력

class BungEoBbang:
    # 클래스 변수 (모든 붕어빵 공통) → 설계도에 직접 적힘
    shape = "붕어빵"

    # 인스턴스 변수 (붕어빵마다 다름) → self로 찍어낼 때 넣음
    
    #__init__ 없는 틀: “나는 모양만 찍을 줄 아는데 왜 속재료 넣으래?” → 에러 발생
    #__init__ 있는 틀: “아, 팥 넣는 법도 배워뒀어. 팥 붕어빵 찍어줄게!” → 정상 작동
    def __init__(self, filling, price):    #__init__은 클래스에서 만든 객체의 여러 속성을 한 번에 초기값 세팅
        self.filling = filling      # 각각 다른 속 재료
        self.price = price          # 각각의 가격

    def show(self):
#        print(f"이건 {self.shape}, 속은 {self.filling}, 가격은 {self.amount}원 입니다.")
        print(f"{self.filling} {self.shape}은 {self.price}원 입니다.")

    

# 붕어빵 찍기 (인스턴스 만들기)
bb1 = BungEoBbang("팥", 1000)      # 첫 번째 붕어빵 → 팥
bb2 = BungEoBbang("슈크림",1500)  # 두 번째 붕어빵 → 슈크림
bb3 = BungEoBbang("피자", 3000)    # 세 번째 붕어빵 → 피자

# 각각 보여주기
bb1.show()
bb2.show()
bb3.show()

# 클래스 변수는 설계도에서 바로 볼 수 있음
#print("붕어빵틀 모양:", BungEoBbang.shape)

# 인스턴스 변수는 찍어낸 붕어빵마다 따로 있음
# print("1번 붕어빵 속:", bb1.filling)
# print("2번 붕어빵 속:", bb2.filling)
# print("3번 붕어빵 속:", bb3.filling)
