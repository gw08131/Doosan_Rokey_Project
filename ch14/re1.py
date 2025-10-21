# re1.py

import re
# 패턴객체 = re.compile("정규표현식")
# 매치객체 = 패턴객체.match("검색대상문자열")
# print(매치객체)

#메타문자
# []
p = re.compile("[a]")
m = p.match("banana")        # None -> match 매소드가 첫번째 문자부터 검열 (b != a) 그래서 None반환
print(m)

p = re.compile("[abc]")      # 셋중에 하나랑 첫번째 문자랑 일치하냐를 봄
print(p.match("banana"))     # match='b'

p = re.compile("[abc]+")     # 셋중에 하나랑 첫번째 + 2번째 문자랑 일치하냐를 봄
print(p.match("banana"))     # match='ba'


print(re.compile("a"))         # None
print(re.compile("b"))         # match='b'
print(re.compile("ba"))        # match='ba
print(re.compile("ab"))        # None
print(p.match("banana"))      

p = re.compile("[abc]")
print(p.match("before"))      # <re.Match object; span=(0, 1), match='b'>
print(p.match("dude"))        # None

p = re.compile("[0-5]")
print(p.match("3banana"))      # match='3'

p = re.compile("[^0-9]")
print(p.match("3banana"))      # None
print(p.match("banana"))       # match='b'           

p = re.compile("[\^0-9]")
print(p.match("3banana"))       # match='3'
print(p.match("banana"))       # None
print(p.match("^banana"))      # match='^'


p = re.compile("[A-Z]")
print(p.match("Apple"))      # match
print(p.match("banana"))     # None

p = re.compile("[a-zA-Z0-9]")
print(p.match("banana"))        # "b" match
print(p.match("Apple"))         # "A" match
print(p.match("_melon"))        # None
print(p.match(" orange"))        # None (공백도 안됨)

p = re.compile("[W]")
print(p.match("Water_melon"))   # match='W

p = re.compile("[\W]")
print(p.match("Water_melon"))   # None

# white space (화이트스페이스)
#\r = Carriage Return: 현재 줄 맨 앞으로 이동
#\f = from feed: 다음 페이지로 넘기a
#\v = vertical tab: 수직 탭
p = re.compile("\s")
print(p.match(" orange"))        # match=' '     space
print(p.match("\torange"))       # match='\t'   tap
print(p.match("\norange"))       # match='\n'   new line
print(p.match("\rorange"))       # match='\r'   

print("---------------")
# .
p = re.compile("a.b")
print(p.match("apple"))         # None
print(p.match("apbple"))        # match='apb'
print(p.match("a.b"))          # match='a.b'

p = re.compile("a.p")
print(p.match("apple"))         # match='app'

p = re.compile("a.b")
print(p.match("aab"))           # match='aab'
print(p.match("aob"))           # match='aob'
print(p.match("a0b"))           # match='a0b'
print(p.match("abc"))           # None

print(p.match("a\nb"))          # None
print(p.match("a\rb"))          # match='a\rb'


p = re.compile("a[.]b")
print(p.match("aab"))           # None
print(p.match("aob"))           # None
print(p.match("a0b"))           # None
print(p.match("abc"))           # None
print(p.match("a.b"))           # match='a.b'

print("---------------")
# *
p = re.compile("ca*t")
print(p.match("ct"))             # match='ct'
print(p.match("cat"))            # match='cat'
print(p.match("caaat"))          # match='caaat'

print("---------------")
# +
p = re.compile("ca+t")
print(p.match("ct"))             # None
print(p.match("cat"))            # match='cat'
print(p.match("caaat"))          # match='caaat'

print("---------------")
# {m,n}
p = re.compile("ca{2}t")
print(p.match("ct"))            # None
print(p.match("caat"))          # match='caat'
print(p.match("caaaat"))        # None

p = re.compile("ca{2,5}t")
print(p.match("ct"))            # None
print(p.match("cat"))           # None
print(p.match("caaaat"))        # match='caaaat'

p = re.compile("ca{2,}t")
print(p.match("ct"))            # None
print(p.match("caat"))          # match='caat'
print(p.match("caaaat"))        # match='caaaat'


print("---------------")
# ? = {0,1}
p = re.compile("ca?t")          # a가 0번 혹은 1번
print(p.match("ct"))            # match='ct'
print(p.match("cat"))           # match='cat'
print(p.match("caat"))          # None
print(p.match("caaaat"))        # None

print("---------------")
# ^
p = re.compile("^hello")            
print(p.search("kenneth, hello"))    # None
print(p.search("hello, kenneth"))    # match='hello'

print("---------------")
# $
p = re.compile("hello$")
print(p.search("hello"))                         # match='hello'
print(p.search("hello, kenneth"))                # None        
print(p.search("kim, hello. kenneth, hello"))    # match='hello'
print(p.search("hello, kim. hello, kenneth"))    # None

