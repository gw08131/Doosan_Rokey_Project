# geometry_grid.py

from tkinter import *

# 1. 생성
otk = Tk()      #부모 윈도우 (위젯)
otk.geometry("200x150+400+400")

obtn1 = Button(otk, text = "PUSH1")  #버튼 위젯
obtn2 = Button(otk, text = "PUSH2")  #버튼 위젯
obtn3 = Button(otk, text = "PUSH3")  #버튼 위젯

# 2. 배치
# grid는 상대적인 위치 (대소 비교의 개념)
# obtn1.grid(row=1, column = 0)       #행(세로 숫자들), 열(가로)
# obtn2.grid(row=1, column = 1)       #4열에 바로 들어가는게 아니라 가깝게 땡겨옴
# obtn3.grid(row=5, column = 4)       #row도 5라고 적혀있지만 제시되어잇는 row=1보만 크니까 땡겨와서 2열에 놓아짐

obtn1.grid(row=0, column = 0)       
obtn2.grid(row=1, column = 1)       
obtn3.grid(row=2, column = 2) 

#pack, gird 혼용 X
#나머지는 가능하나 권장 X

#이벤트 바인딩
otk.mainloop()

