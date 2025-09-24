# Singer.py

# #클래스 정의
# class 클래스명:
#     멤버변수명 = 데이터
#     def 함수명(self, 매개변수):     #항상 self가 첫 매개변수로 와야함!
#         return

# #객체 생성
# 객체명 = 클래스명()

# #객체 활용
# 객체명.멤버변수명
# 객체명.함수명()


# 속성(데이터) = 명사
# 동작(기능) = 동사
class Singer:
    name = "아이유"
    def sing(self):   
        print("이 밤 그날의 반딧불을 당신의 창 가까이 보낼게요~")

iu = Singer()
print(Singer.name)          #클래스 멤버변수 사용
print(iu.name)
iu.sing()

# 클래스 네임 스페이스
# - 클래스 변수: 클래스 매서드 외부 정의
# - 인스턴스 변수: 클래스 매서드 내부 정의