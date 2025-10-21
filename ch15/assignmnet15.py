# assignment15.py

print("-----------6번-------------")
numbers = [1, 2, 3, 4, 5]
iter_numbers = iter(numbers)
for i in iter_numbers:
    print(i)

print("-----------7번-----------")
fruits = ["apple", "banana", "cherry"]
iter_fruits = iter(fruits)
while (True):
    try:
        print(next(iter_fruits))
    except StopIteration:
        break

print("-----------8번-----------")
squared = [x**2 for x in range (0,10)]
for i in squared:
    print(i)


print("-----------9번-----------")
even_num = [x for x in range (0,11) if x%2==0]
for i in even_num:
    print(i)


print("---------10번---------")
class MyRange:
    def __init__(self,start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start < self.stop:
            current_value = self.start
            self.start += self.step
            return current_value
        else:
            raise StopIteration

my_range = MyRange(0,10,1)
for item in my_range:
    print(item)          