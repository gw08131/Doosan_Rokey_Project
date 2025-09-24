# assignment5.py

print("----------2번----------")
for 변수 in [10,20,30]:
    print (변수)

print("----------3번----------")
가격리스트 = [100,200,300]
tax = 10
for price in 가격리스트:
    print(price+tax)

print("----------4번----------")
리스트 = ['dog', 'cat', 'parrot']
for name in 리스트:
    count = len(name)
    print(name, count)
    
print("----------5번----------")
리스트 = ["가", "나", "다", "라"]
for letter in 리스트:
    if letter != "가":
        print(letter)


print("----------6번----------")
리스트 = [3,-20,-3,44]
for number in 리스트:
    if number < 0:
        print(number)


print("----------7번----------")
for year in range(2002,2051,4):
    print(year)

   
print("----------9번----------")
num = 0
total = 0
while 0 <= num <= 100:
    total = num + total
    num += 1
print(total) 


print("----------10번----------")
for number in range (1,31):
    if number % 2 != 0:
        print(number,": 홀수")
    else:
        print (number, ": 짝수")



print("----------11번----------")
홀수 = []; 짝수 = []
for number in range (1,31):
    if number % 2 != 0:
        홀수.append(number)
    else:
        짝수.append(number)
print("홀수:", 홀수,"\n 짝수:",짝수)