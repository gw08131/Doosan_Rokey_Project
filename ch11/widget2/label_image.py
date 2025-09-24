# label_image.py

from tkinter import Tk
from tkinter import PhotoImage
from tkinter import Label
from tkinter import Button



# 1. 생성
otk = Tk()
otk.geometry("200x100")

img1 = PhotoImage(file =r"C:\rokey\python\ch11\widget2\1-cab606a6.png")  #\를 /로 바꾸기 혹은 r"C:\rokey\python\ch11\apple.png" 형태로
img_label = Label(otk,image=img1)
obtn1 = Button(otk,text="PUSH1")
obtn2 = Button(otk,text="PUSH2")
obtn3 = Button(otk,text="PUSH3")

# 2. 배치
img_label.place(x=-20,y=-20)
obtn1.pack()
obtn2.pack()
obtn3.pack()

# 3. 이벤트 바인딩
otk.mainloop()