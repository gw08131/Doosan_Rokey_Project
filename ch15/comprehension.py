# comprehension.py

# 리스트 컴프리헨션
# [표현식 for 변수 in 이터러블 if 조건]

numbers = [ 1,2,3,4]
squared = [x**2 for x in numbers]
print(squared)                       # [1, 4, 9, 16]
print(type(squared))                 # <class 'list'>

#조건문이 참인 경우, 요소를 포함하여 표현식 수행
even_numbers = [x**2 for x in numbers if x%2 == 0]
even_numbers = [x**2+1 for x in numbers if x%2 == 0]
print(even_numbers)

print("----------------------------")
# 딕셔너리 컴프리헨션
# {key:vlaue, key:value, key:value}
# {key표현식: value표현식 for item in 이터러블 if 조건}

squared_dict = {x:x**2 for x in range(5)}
print(squared_dict)

# even_squared_dict = {x:x**2 for x in range(5) if x%2==0}
# print(even_squared_dict)

even_squared_dict = {
    x:x**2
    for x in range(5)
    if x%2 == 0
}
print(even_squared_dict)        # {0: 0, 2: 4, 4: 16}

print("----------------------------")
# 제너레이터 컴프리헨션
# (표현식 for 변수 in 이터러블 if 조건)
gen = (i*i for i in range(1,100))
print(next(gen))        # 1
print(next(gen))        # 4
print(next(gen))        # 9
for item in gen:
    print(item)         # 99X99까지 나옴 (9801)    
# print(next(gen))        # StopIteration -> 이미 for문에서 range 다 소진했기때문에

print("-----------------------------")
bad_words = ["spam", "ad?", "click*", "promo"]

import re

pattern = "|".join([re.escape(word) for word in bad_words])         # "|" = or의 개념 => 네 단어 중 하나라도도
print(pattern)                                                      # spam|ad|click|promo
text = "This is a spam message with promo content."
match_obj = re.findall(pattern, text)                       
print(match_obj)                                                    # ['spam', 'promo']