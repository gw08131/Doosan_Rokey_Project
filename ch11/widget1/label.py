#label.py
from tkinter import Tk
#from tkinter import Button
from tkinter import Label

# 1. 생성
otk = Tk() 
otk.geometry("400x300")

# 2. 배치
olable1 = Label(otk, text="적",bg ="red", width=20)
olable2 = Label(otk, text="녹",bg ="green", width=20)
olable3 = Label(otk, text="파",bg ="blue", width=20)

# 3. 이벤트
olable1.pack()
olable2.pack()
olable3.pack()

otk.mainloop()