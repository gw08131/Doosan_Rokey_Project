# geometry_pack.py

from tkinter import *

# 1. 생성
otk = Tk()      #부모 윈도우 (위젯)
otk.geometry("200x150+400+400")

obtn1 = Button(otk, text = "PUSH1")  #버튼 위젯
obtn2 = Button(otk, text = "PUSH2")  #버튼 위젯
obtn3 = Button(otk, text = "PUSH3")  #버튼 위젯

# 2. 배치
obtn1.pack(side="left")
obtn2.pack(side="right")
obtn3.pack(side="top")

#이벤트 바인딩
otk.mainloop()

