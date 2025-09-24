#logic.py
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not True)
print(not False)

print("--------------------------")

print(9>4 and 3>2)
print(9<4 and 3>2)
print(9<4 or 3<2)
print(9<4 or 3>2) #OR 연산은 하나만 참이어도 True

print("--------------------------")
print(1 and 1)
print(1 and 0)
print(0 and 1)
print(0 and 0)

print(1 or 1)
print(1 or 0)
print(0 or 1)
print(0 or 0)

print("--------------------------")
print(9>4 or 3<2 and 4>2)
#True or False and True
#True and True
#True

print((3-5)+3<1 and 3-5>1)