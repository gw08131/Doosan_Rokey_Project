# re_finditer.py

import re

# finditer 매서드
p = re.compile("[a-z]+")
print(p.finditer("life is too short"))      #callable_iterator object at
# 주소값으로 나와서 list로 변환해야함

print(list(p.finditer("life is too short")))
#[<re.Match object; span=(0, 4), match='life'>, 
# <re.Match object; span=(5, 7), match='is'>, 
# <re.Match object; span=(8, 11), match='too'>, 
# <re.Match object; span=(12, 17), match='short'>]

matchObjs = list(p.finditer("life is too short"))
for matchObj in matchObjs:
    print(matchObj.group())     # life
    print(matchObj.start())     # 0
    print(matchObj.end())       # 4    
    print(matchObj.span())      # (0,4)     