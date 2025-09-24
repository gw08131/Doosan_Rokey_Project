# radio.py
# 선택 범주 중에 하나 선택

from tkinter import Tk
from tkinter import Button
from tkinter import Radiobutton
from tkinter import IntVar      #정수 변수 연결 클래스

# 1.생성
otk = Tk()
otk.geometry("200x200")

radio_value = IntVar()
# set(-1)을 통해 아무것도 선택되지 않는 RadButton을 만든다
# radio_value.set(0)으로 하면 lunch[0]이 선택되어있는거임
# 결국 버튼 선택 orb1이 선택되면 vlaue의 0값이 radio_value가 되서 A런치가 프린트 됨
radio_value.set(-1)     #IntVar 객체 맴버 변수 값 저장하기
print(radio_value.get())

lunch = {0:"A런치", 1:"B런치",2:"C런치"}
def Order():
    value = radio_value.get()   #orb1이 선택되면 radio_value 안의 숫자 0이 꺼내짐
    print(lunch[value])

# radio_value => 어떤 버튼이 선택 되어있는지 저장할 변수
# variable => 클릭된 버튼의 정보를 저장할 변수명 설정
# value => radio_value에 저장될 데이터를 저장하는 인수
orb1 = Radiobutton(otk,text=lunch[0], variable=radio_value, value = 0)      #1번 선택하면 value의 0값이 IntVal()함수를 통해 radio_Value객체에 저장
orb2 = Radiobutton(otk,text=lunch[1], variable=radio_value, value = 1)
orb3 = Radiobutton(otk,text=lunch[2], variable=radio_value, value = 2)

# 3. 이벤트 바인딩
obtn = Button(otk,text="주문",command=Order)

# 2. 배치
orb1.pack()
orb2.pack()
orb3.pack()
obtn.pack()


otk.mainloop()


# # order 함수에 인수를 항에 전달하고 싶으면
# # 1. 람다 함수 사용
# # 2. 라이브러리 활용 (partial)

# from functools import partial
# obtn = Button(otk, text="주문", command =partial(Order,"햄버거"))