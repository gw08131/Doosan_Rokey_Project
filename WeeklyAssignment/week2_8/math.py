# math.py

def factorial(num):
    total = 1
    for num in range(1,num+1,1):
        total = total * num
    return total

#print(factorial(5))