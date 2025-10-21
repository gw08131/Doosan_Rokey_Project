# gen_iter_class.py

gen = (i*i for i in range (1,100))
print(gen)
print(type(gen))         # <class 'generator'>
for i in gen:
    print(i)

print("----------------------------------")
class MyIterator:
    def __init__(self):
        self.data = 1

    def __iter__(self):
        return self
    def __next__(self):
        result = self.data ** 2

        if self.data >= 100:
            raise StopIteration
    
        self.data += 1
        return result

my_iter = MyIterator()
print(my_iter)
print(type(my_iter))          # <class '__main__.MyIterator'>
for item in my_iter:
    print(item)

