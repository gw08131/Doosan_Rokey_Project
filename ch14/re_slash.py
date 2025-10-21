# re_slash.py

import re

p = re.compile(r'\section')
m = p.match('\section')         # None
print(m)

p = re.compile('\section')
m = p.match('\section')         # None
print(m)

p = re.compile('\\section')
m = p.match('\section')         # None
print(m)

#개선안
p = re.compile(r'\\section')
m = p.match('\section')         # match='\\section'
print(m)

p = re.compile('\\\\section')
m = p.match('\section')         # match='\\section'
print(m)

p = re.compile('\\\section')
m = p.match('\section')         # match='\\section'
print(m)


# 목적: \section
# 1. \s 화이트스페이스
# \\section
# 2. 파이썬 리터럴 규칙 (이스케이프)
# "\\" => "\"
# "\\\\" => "\\"
# "\\s" => 문자열 \와 문자열 s

# 그래서 역슬레시 앞에 r을 붙여서 사용하면 편함