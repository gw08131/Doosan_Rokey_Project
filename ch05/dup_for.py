# dup_for.py

for j in range(5):              #10개 * 줄이 5번 찍힘
    for i in range(10):         #10개의 *이 괄호로 찍힘
        print("*", end = " ")
    print()                     #총 50개의 면 형태 출력


for num in [3,1,2]:
    print(num)


print("---------------------")
for num in range (2):
    print(num)

print("---------------------")
clovers = ['클로버1','클로버2','클로버3']
for clover in clovers:
    print(clover)

for num in [0,1,2]:
    print(clovers[num])
print(len(clovers))

for num in range(3):
    print(clovers[num])

print("---------------------")
count = 0
while count < 3:
    print(count)
    count += 1

print("---------------------")
count = 1
while count < 4:        
    count += 1
    print(count)

print("---------------------")
count = 0
while count <= 5:
    if count % 2 != 0:      #홀수일 때
        print(count)
    count += 1


"""
print("---------------------")
price = 0
while price != -1:
    price = int(input('가격을 입력하세요 (종료:-1): '))
    if price > 10000:
        print('너무 비싸요. ')
    elif price > 5000:
        print('괜찮은 가격이네요. ')
    elif price > 0:
        print ('정말 싸요. ')
"""
"""
print("---------------------")
for number in range(101):
    if number % 3 == 0:
        print(number)
        number += 1

for num in range(0, 101, 3):
    print(num)
"""

print("---------------------")
i = 0
while 0 <= i < 10:
    i += 1
    if i % 3 != 0:
        print(i)
        continue 
    
print("---------------------")
one = 1
for value in range (1,10):
    answer = one * value
    print(one, " X ", value, " = ", answer)
    value += 1

one = 1
for value in range (1,10):
    print(one, "X", value, "=" ,one*value)