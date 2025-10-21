# week3_assginment.py


print("-----------2번-----------")
import tkinter as tk
from tkinter import messagebox

def on_buton_click():
    messagebox.showinfo("알림", "버튼이 클릭되었습니다!")

root = tk.Tk()
root.title("간단한 Tkinter 앱")
root.geometry("300x200")

btn = tk.Button(root, text="클릭하세요",command = on_buton_click)
btn.pack(pady=20)

root.mainloop()

# print("-----------4번-----------")
# with open("data.txt",'w',encoding="utf-8") as file:
#     for i in range(1,11):
#         file.write(f"{i}번째 줄입니다.\n")
# print('파일이 성공적으로 작성되었습니다.')

# with open("data.txt","a",encoding="utf-8") as file:
#     file.write("11번째 줄입니다.")

# with open("data.txt","r",encoding="utf-8") as file:
#     contents = file.read()
# print('파일내용:')
# print(contents)

# print("-----------5번-----------")
# while True:
#     try:
#         number = input("숫자를 입력하세요: ")
#         int_number = int(number)
#         result = int_number ** 2
#         print(result)
#         break   
#     except ValueError:
#         print("올바른 숫자를 입력하세요!")

print("-----------6번-----------")    
lst = [10, 20, 30, 40, 50]
squared = lambda x: x**2
squared_list = list(map(squared,lst))
print(squared_list)

print("-----------7번-----------")
data = """python one
life is too short
python two
you need python
python three"""

import re

pattern1 = re.compile("^python\s\w+", re.IGNORECASE | re.MULTILINE)
mtch = pattern1.findall(data)
print(mtch)


print("-----------8번-----------")
email = "user@example.com"
import re
email_form = re.compile("^[\w\._-]+@[\w\._-]+\.[a-zA-Z]{2,3}$")
matched_email = email_form.search(email)
if matched_email:
    print(email)
else:
    print("None")


print("-----------10번-----------")
num = input("정수를 입력하세요")
n = int(num)
squared = (x**2 for x in range(1,n+1))
for item in squared:
    print(item)