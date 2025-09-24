#tkinter_module1.py

# import tkinter

# # 1. 생성
# otk = tkinter.Tk()      #부모 윈도우 (위젯)
# obtn = tkinter.Button(otk, text = "click")  #버튼 위젯

# # 2. 배치
# obtn.pack()

# #이벤트 바인딩
# otk.mainloop()

print("-------------------------")
from tkinter import *

def hello():
    print("hello there")

# 1. 생성
otk = Tk()      #부모 윈도우 (위젯)
otk.geometry("100x150-100+0")

print("-------------------------")
hello() #함수 호출
# 함수 (괄호 없이 사용된 케이스)
# 1. 함수는 변수에 저장
# 2. 다른 함수에 전달
# 3. 반환값으로 사용가능
hello
print("-------------------------")


obtn = Button(otk, text = "click",command=hello)  #버튼 위젯

# 2. 배치
obtn.pack()

#이벤트 바인딩
otk.mainloop()