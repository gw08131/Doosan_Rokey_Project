# range1.py

print(range(10))        #range(0, 10)

print('-------------------------')
num = range(10)
num_list = list(num)
print(num_list)         #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(4,10)))      
print(list, range(10))


print('-------------------------')
print(list(range(4,10,2)))       #[4, 6, 8]
print(list(range(8,14,3)))       #[8, 11]
print(list(range(10,0,-1)))      #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


print('\n','-------------------------')
for num in range(3):
    print(num, end=' ')

print('\n','-------------------------')
for num in range(0,3):
    print(num, end=' ')

print('\n','-------------------------')
for num in range(0,9,2):
    print(num, end=' ')