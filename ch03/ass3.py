print(3 == 5)
print ((3 == 3) and (4 != 3))

print("4번-------------------")
if 4 < 3:
      print("Hello World.")
else:
      print("Hi, there.")


print("5번-------------------")
if True :
      if False:
          print("1")
          print("2")
      else:
          print("3")
else :
      print("4")
print("5")

'''
print("6번-------------------")
num = input ("숫자를 입력하세요 ")
num = int(num)

if num%2 == 0:
    print("짝수")
else :
    print("홀수")


print("7번-------------------")

number = input("숫자를 입력하세요 ")
number20 = int(number)+20

if number20 <= 255:
    print(number20)
else:
     print(255)



print("8번-------------------")

number = input("숫자를 입력하세요 ")
number20 = int(number)-20

if number20 >= 255:
    print(255)
elif number20 < 0:
    print(0)
else:
     print(number20)
     
'''

'''
print("9번-------------------")

time = input("시간을 입력하세요 (HH:MM): ")
if time == '00:00':
    print("정각 입니다")
elif time == '01:00': 
     print("정각 입니다")
elif time == '02:00':
    print("정각 입니다")
elif time == '03:00':
    print("정각 입니다")
elif time == '04:00':
    print("정각 입니다")
elif time == '05:00':
    print("정각 입니다")
elif time == '06:00':
    print("정각 입니다")
elif time == '07:00':
    print("정각 입니다")
elif time == '08:00':
    print("정각 입니다")
elif time == '09:00':
    print("정각 입니다")
elif time == '10:00':
    print("정각 입니다")
elif time == '11:00':
    print("정각 입니다")
elif time == '12:00':
    print("정각 입니다")
elif time == '13:00':
    print("정각 입니다")
elif time == '14:00':
    print("정각 입니다")
elif time == '15:00':
    print("정각 입니다")
elif time == '16:00':
    print("정각 입니다")
elif time == '17:00':
    print("정각 입니다")
elif time == '18:00':
    print("정각 입니다")
elif time == '19:00':
    print("정각 입니다")
elif time == '20:00':
    print("정각 입니다")
elif time == '21:00':
    print("정각 입니다")
elif time == '22:00':
    print("정각 입니다")
elif time == '23:00':
    print("정각 입니다")
elif time == '24:00':
    print("정각 입니다")
else:
    print("정각이 아닙니다.")

'''

print("9번-------------------")

time = input("시간을 입력하세요 (HH:MM): ")

if time == "00:00" or time == "01:00" or time == "02:00" or time == "03:00" \
   or time == "04:00" or time == "05:00" or time == "06:00" or time == "07:00" \
   or time == "08:00" or time == "09:00" or time == "10:00" or time == "11:00" \
   or time == "12:00" or time == "13:00" or time == "14:00" or time == "15:00" \
   or time == "16:00" or time == "17:00" or time == "18:00" or time == "19:00" \
   or time == "20:00" or time == "21:00" or time == "22:00" or time == "23:00":
    print("정각 입니다")
else:
    print("정각이 아닙니다")


'''
print("10번-------------------")
score = int(input("score: "))
if 81 <= score <= 100:
    grade = "A"
elif 61 <= score <= 80:
    grade = "B"
elif 41 <= score <= 60:
    grade = "C"
elif 21 <= score <= 40:
    grade = "D"
else:
    grade = "E"
print("grade is", grade)
'''