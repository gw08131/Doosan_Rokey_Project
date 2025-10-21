# assignment14.py

import re

print("----------------6번----------------")
text = "이메일 목록: test@example.com, hello@world.net, user123@domain.org"
p = re.compile("[a-zA-z0-9]{1,10}@[a-zA-z0-9]{1,10}[.][a-zA-z0-9]{,10}")
print(p.findall(text))

p = re.compile(r"[\w\.]+@[\w\.]+\.[A-Za-z]{2,}")
print(p.findall(text))



print("----------------7번----------------")
text = "연락처: 010-1234-5678, 02-987-6543, 031-456-7890"
p = re.compile("[0-9]{1,4}\-[0-9]{1,5}\-[0-9]{1,4}")
print(p.findall(text))

print("----------------8번----------------")
text = "I love Python. Java is also popular. Python is great for AI."
new_text = text.split(".")
lst = []
for i in range (0,len(new_text),1):
    if re.search(r"Python", new_text[i]):
        lst.append(new_text[i])
print(lst)


print("----------------9번----------------")
text = "상품 코드: A123, B456, C789, 가격: 12000원"
p = re.compile("[0-9]+")
print(p.findall(text))

print("----------------10번----------------")
text = "NASA is working on AI projects with IBM and Google."
p = re.compile("[A-Z]+[A-Z]+")
print(p.findall(text))
