# assignment6.py
print("---------5번----------")
def print_hello():
    print("안녕하세요")

for num in range(100):
    print_hello()


print("---------8번----------")
def greet(name = 'Guest'):
    print("Hello,", name, "!")
    return name

greet("Alice")

print("---------10번----------")
def multiply(a,b):
    result = a*b
    return result
print(multiply(4,5))