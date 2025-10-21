# re_findall.py

import re

p = re.compile("[a-z]+")                        # [a-z]범위 내의 알파벳 0번 반복부터 
print(p.findall("3pyt8hon"))                    # ['pyt', 'hon']
print(p.findall("life is too short"))           #['life', 'is', 'too', 'short']

p = re.compile("Python")
text = "When I first discovered Python, " \
       "I was impressed by how intuitive Python syntax was," \
       "and the more I used Python, " \
       "the more I appreciated its flexibility in handling everything " \
       "from data analysis to web development."
print(p.findall(text))                          # ['Python', 'Python', 'Python']

# *(0회이상) -=> 빈문자열 매치
# 3 앞에서 " "
# 5 앞에서 " "
# 마지막 " "
p = re.compile("[a-z]*")        #0번 반복
print(p.findall("3pyt5hon"))    # ['', 'pyt', '', 'hon', '']