clovers = ('클로버1', '하트2', '클로버3')
print(clovers[1])
print(clovers[2])

my_tuple1 = ()
print(my_tuple1)         #() 괄호로 생성

my_tuple2 = (1, -2, 3.14, 'hi', True)
print(my_tuple2)

my_tuple3 = '앨리스', 10, 1.0, False        #괄호 없이도 tuple 생성 가능
print(my_tuple3)                            #('앨리스', 10, 1.0, False) 

print('---------------')

my_int = (1)
print(type(my_int))         #<class 'int'> 튜플이 아님

my_tuple = (1,)
print(type(my_tuple))       #<class 'tuple'>

my_tuple = 1,
print(type(my_tuple))       #<class 'tuple'>

print('---------------')
a = (1,2,3)
print(a[0])

#Tuple 수정 시도!
#a[0] = 7        #에러.. "TypeError: 'tuple' object does not support item assignment"
print(type(a))   #<class 'tuple'>
b = list(a)
b[0] = 7
a = b
print(a)

print('---------------')
a=5
list1 = [a]
print(list1)
a=10
print(list1)



