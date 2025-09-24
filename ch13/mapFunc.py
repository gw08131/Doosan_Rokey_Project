#mapFunc.py

def square(x):
    return x**2

print(square(2))        #4

numbers = [1,2,3,4,5]
squared_numbers = map(square,numbers)
#map(함수, 이터러블)
print(type(squared_numbers))        #<class 'map'>
print(squared_numbers)              #<map object at 0x0000022D2791BD30>  <- 이터레이터형태로써 list로 바꿔야 우리가 볼 수 있음
print(list(squared_numbers))        #[1, 4, 9, 16, 25]

print("------------------")
data = {"a":1,"b":2,"c":3}
new_data = dict(map(lambda kv: (kv[0].upper(), kv[1]*10),data.items()))     #upper = 대문자
print(new_data)


print("--------------------")
#외부 변수 사용 가능
num = 2
numbers = [1,2,3,4,5]
result = map(lambda x: (x+1)**num,numbers)
print(list(result))