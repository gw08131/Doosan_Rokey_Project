# generator.py

def simple_generator():
    yield 'a'
    yield 'b'
    yield 'c'

g = simple_generator()

# generator은 iterator의 한 종류
print('__iter__'in dir(g))      # True
print('__next__'in dir(g))      # True


print(type(g))

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))      # StopIteration


for item in g:
    print(item)


print("----------------------")
def mygen():
    for i in range (1,1000):
        result = i*i
        yield result
    
gen = mygen()
print(next(gen))
for item in gen:
    print(item)
