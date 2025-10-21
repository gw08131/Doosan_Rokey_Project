# re_option.py

import re

p = re.compile("a.b")               # None
m = p.match('a\nb')    
m = p.match('a\nb')                
print(m)

# "."은 원래 줄바꿈만 못 읽는데, DOTALL을 쓰면 줄바꿈도 읽는다.
p = re.compile('a.b',re.DOTALL)    # match='a\nb'
#p = re.compile('a.b',re.S)         # match='a\nb'        
m = p.match('a\nb')                
print(m)

print(re.match("[a-z]+","python\n",re.DOTALL))              # match='python'
print(re.match("[a-z]+","python\n",re.DOTALL).group())      # python


print("------------------------")
# IGNORE(I)
p = re.compile("[a-z]+",re.IGNORECASE)
print(p.match("python"))                # match='python'
print(p.match("Python"))                # match='Python'
print(p.match("PYTHON"))                # match='PYTHON'

print("------------------------")
# MULTILINE(M) <-여러줄 텍스트 검사
# "python 단어"로 구성된 매턴 검색
#p = re.compile("^python\s\w+")             # ['python one'] 만 나옴 multi line 검사를 안해서..
p = re.compile("^python\s\w+",re.MULTILINE) # ['python one', 'python two', 'python three']
data = """python one
life is too short
python two
you need python
python three
python"""
print(p.findall(data))              

# ^python → 각 줄의 시작(^)에서 "python"으로 시작하는 줄
# \s → 공백 1개
# \w + → 단어 문자 1개 이상  (단어 1개 이상이어야해서 마지막 python은 검출 X)

print("------------------------")

p = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

# VERVOSE
p= re.compile(r"""
&[#]                    # 숫자형 엔터티 (문자 개체 참조) 시작
(
    0[0-7]+             # Octal form(8진수 형식)
    [0-9]+              # Decimal form(10진수 형식)
    x[0-9a-fA-F]+       # Hexadecimal form(16진수 형식)
)
 ;                      # 후행 semicolon
""", re.VERBOSE)

data = "&#07; &#8; &#x0A;"

print(p.findall(data))          # ['07', '8', 'x0A']
