#assignment13.py

# try:
#     x = int("abc")
# except ValueError:
#     print("ValueError occurred!")
# finally:
#     print("Execution finished.")


# #exception_raise.py
# print('-----7번-----')
# try:
#     raise KeyError          
# except KeyError:
#     print("Key is missing!")

# print('-----8번-----')
# add = lambda x, y: x+y
# result = add(int(input("x값을 입력하세요.")),int(input("y값을 입력하세요.")))
# print(result)

print('-----9번-----')
per = ["10.31", "", "8.00"]
for i in per:
    try:
        print(float(i))
    except ValueError:
        print(0)

print('-----10번-----')
numbers = [10, 20, 30]
try:
    idx = int(input("인덱스를 입력하세요: "))
    print(numbers[idx])
except IndexError:
    print("잘못된 인덱스입니다.")
except ValueError:
    print("숫자를 입력하세요.")
