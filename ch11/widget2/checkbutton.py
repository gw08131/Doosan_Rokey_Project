# checkbutton.py

from tkinter import Tk
from tkinter import Checkbutton
from tkinter import Button
from tkinter import BooleanVar

# 1. 생성
otk = Tk(className="커피 주문")
otk.geometry("200x200")

check_value = {}

check_value[0] = BooleanVar()
check_value[1] = BooleanVar()
check_value[2] = BooleanVar()
check_value[3] = BooleanVar()

# check_value[0].set(-1)
# check_value[0].get()

coffee = {0:'아메리카노', 1: '라떼', 2:'카푸치노',3:'에스프레소'}
for i in range(len(coffee)):
    ocheckbutton = Checkbutton(otk,text=coffee[i],variable=check_value[i])
    ocheckbutton.pack(anchor="w")       #왼쪽 정렬

def Order():
    for i in check_value:
        if check_value[i].get() == True:
            print(check_value[i], coffee[i])


obtn = Button(otk, text="주문",command = Order)

# 2. 배치
obtn.pack()

# 3. 이벤트
otk.mainloop()