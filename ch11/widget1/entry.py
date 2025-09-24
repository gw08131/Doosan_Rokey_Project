# entry.py
#~를 typing 할 때 사용

from tkinter import Tk          #부모 윈도우 (위젯)
from tkinter import Entry       #엔트리 위젯
from tkinter import StringVar   #문자열 변수 클래스
from tkinter import Label       #라벨 위젯

otk = Tk()
otk.geometry("300x200")

ostring = StringVar()  #문자열(변수) 값 위젯과 연결가능: 문자열로해서 데이터 저장
oentry = Entry(otk, textvariable=ostring)   #네모박스 보임
oentry.pack()       #print 같은 역할

olabel = Label(otk, bg = "white", textvariable = ostring)  #ostring에 저장한 문자열을 Lable해줌
olabel.pack()

otk.mainloop()