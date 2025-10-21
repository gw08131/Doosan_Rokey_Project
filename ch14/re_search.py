# re_search.py

import re

p = re.compile("python")
print(p.search("3 python"))     # match='python'
print(p.search("3pyt8hon"))     # None

p = re.compile("Python")
text = "When I first discovered Python, " \
       "I was impressed by how intuitive Python syntax was," \
       "and the more I used Python, " \
       "the more I appreciated its flexibility in handling everything " \
       "from data analysis to web development."
print(p.search(text))           # span=(24, 30), match='Python' -> 24번째에 P가 시작 
#search여서 처음 Python이라고 나온 것만 찾음

p = re.compile("[a-z]+")        # [a-z]범위 내의 알파벳 1번 반복부터 
print(p.search("3pyt8hon"))     # span=(1, 4), match='pyt'
p = re.compile("[a-z]*")        # [a-z]범위 내의 알파벳 0번 반복부터 
print(p.search("3pyt8hon"))     # span=(0, 0), match=''


