# string1.py

muna = "python"
print(muna[0])      #p
print(muna[1])      #y
print(muna[2])      #t  
print(type(muna))
#muna[0] = 'k'       # 문자열은 문자열 상수이다. 상수는 변경할 수 없어 이름 오류 발생
#TypeError: 'str' object does not support item assignment

print("------------------")
munb = ["python"]
print(munb[0])      #python
print(type(munb))   #<class 'list'

print("------------------")
munc = ["p","y","t","h","o","n"]
print(munc[0])          #p
print(munc[1])          #y
print(munc[2])          #t
print(munc)
print(type(munc[0]))    #<class 'str'>

munc[0] = "k"
print(munc)


print("------------------")
for i in range (0,6,1):
    print(munc[i])

    length = len(munc)
    print(length)

for i in range (0,len(munc),1):
    print(munc[i])