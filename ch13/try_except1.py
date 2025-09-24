# try_except1.py

# try:
#     코드블록
# except 예외클래스1:
#     코드블록
# except 예외클래스2:
#     코드블록
# except (예외클래스3, 예외클래스4):
#     코드블록


while True:
    try:
        x = int(input("Please enter a number: "))
        break
    # except ValueError:
    except ValueError as e:
        print("Oops! That was no valid number. Try again...")
        print(e)   #invalid literal for int() with base 10: 'hi' <-오류 상세 내용 (오류 정보)