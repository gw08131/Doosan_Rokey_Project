# re_module.py

import re

p = re.compile("[a-z]+")
m = p.match("python")

m = re.match("[a-z]+", "python")
print(m)                            # match='python'
print(m.group())                    # python