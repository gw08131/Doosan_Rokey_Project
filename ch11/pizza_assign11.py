# pizza_assign11.py

from tkinter import Tk
from tkinter import Label
from tkinter import Checkbutton
from tkinter import Button
from tkinter import IntVar

# 1. 생성
otk = Tk(className="조각 피자 주문 프로그램")
otk.geometry("400x300")
olabel = Label(otk,text="피자")
total_label = Label(otk, text="총액: 0원")

cheese_var = IntVar()
combo_var = IntVar()
bul_var = IntVar()

pizza = {0:"치즈 피자 (3200원)",1:"콤비네이션 피자 (3500원)",2:"불고기 피자 (3600원)"}
# cheese_var.set(-1)
# combo_var.set(-1)
# bul_var.set(-1)

pizza_price = {0:3200,1:3500,2:3600}

def Order():
    selected_pizza = []
    selected_pizza_price = []
    print("주문내역:")
    if cheese_var.get() == 1:
        selected_pizza.append(pizza[0])
        selected_pizza_price.append(pizza_price[0])
        #print(pizza[0])    

    if combo_var.get() == 1:
        selected_pizza.append(pizza[1])	
        selected_pizza_price.append(pizza_price[1])
        #print(pizza[1])
    
    if bul_var.get() == 1:
        selected_pizza.append(pizza[2])
        selected_pizza_price.append(pizza_price[2])
        #print(pizza[2])

    if selected_pizza:
        total = 0
        for i in range (len(selected_pizza_price)):
            total = selected_pizza_price[i] + total
            #print(selected_pizza[i])
            Label(otk, text=f"- {selected_pizza[i]}").place(x=140, y=150 +i* 20)
        #print(total)
        Label(otk, text=f"총 가격: {total}원").place(x=160, y=200)

ocheck_btn1 = Checkbutton(otk,text=pizza[0],variable=cheese_var, onvalue=1, offvalue=0)
ocheck_btn2 = Checkbutton(otk,text=pizza[1],variable=combo_var, onvalue=1, offvalue=0)
ocheck_btn3 = Checkbutton(otk,text=pizza[2],variable=bul_var, onvalue=1, offvalue=0)
obtn = Button(otk,text="주문",command=Order)


# 2. 배치
olabel.pack()
ocheck_btn1.place(x=2,y=20)
ocheck_btn2.place(x=2,y=50)
ocheck_btn3.place(x=2,y=80)
obtn.place(x=185,y=110)


# 3. 이벤트 바인딩
otk.mainloop()



