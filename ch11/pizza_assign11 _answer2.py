from tkinter import Tk, Label, Checkbutton, Button, IntVar

# 1. 윈도우 생성
otk = Tk(className="조각 피자 주문 프로그램")
otk.geometry("400x300")

Label(otk, text="피자").pack()

# 체크박스 상태 변수
cheese_var = IntVar()
combo_var  = IntVar()
bul_var    = IntVar()

# 메뉴 & 가격 딕셔너리
pizza = {0:"치즈 피자 (3200원)", 1:"콤비네이션 피자 (3500원)", 2:"불고기 피자 (3600원)"}
pizza_price = {0:3200, 1:3500, 2:3600}

# 결과를 출력할 라벨 (처음엔 비어있음)
result_label = Label(otk, text="")
result_label.place(x=140, y=150)

def Order():
    selected = []
    total = 0
    
    if cheese_var.get() == 1:
        selected.append(pizza[0])
        total += pizza_price[0]
    if combo_var.get() == 1:
        selected.append(pizza[1])
        total += pizza_price[1]
    if bul_var.get() == 1:
        selected.append(pizza[2])
        total += pizza_price[2]
    
    if selected:
        order_text = "\n".join([f"- {item}" for item in selected])
        order_text += f"\n총 가격: {total}원"
    else:
        order_text = "선택된 메뉴가 없습니다."
    
    # 라벨 내용 갱신
    result_label.config(text=order_text)

# 체크박스 생성
ocheck_btn1 = Checkbutton(otk, text=pizza[0], variable=cheese_var)
ocheck_btn2 = Checkbutton(otk, text=pizza[1], variable=combo_var)
ocheck_btn3 = Checkbutton(otk, text=pizza[2], variable=bul_var)

# 주문 버튼
obtn = Button(otk, text="주문", command=Order)

# 배치
ocheck_btn1.place(x=2,y=20)
ocheck_btn2.place(x=2,y=50)
ocheck_btn3.place(x=2,y=80)
obtn.place(x=185,y=110)

otk.mainloop()
