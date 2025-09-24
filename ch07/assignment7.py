# assignment7.py

print("-----------6번-----------")
def add_numbers(a, b):
    global result
    result = a + b
    return result

add_numbers(5,6)
print(result)


print("-----------7번-----------")

def message() :
    print("A")
    print("B")
message()
print("C")
message()

print("-----------8번-----------")
print("A")
def message() :
    print("B")
print("C")
message()


print("-----------9번-----------")
def check_odd_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_odd_even(4))       #Even
print(check_odd_even(7))       #Odd


print("-----------10번-----------")
num_list = [10,20,30,40,50]
def calculate_average(list):
    count = len(list)
    total = 0
    for num in range(count):
        total = total + list[num]
#        return print(total)     #이렇게 되면 num = 0일때 결과값인 10만 출력하고 return(즉 함수 끝)
    return total/count
    
average = calculate_average(num_list)
print("평균: ", average)    