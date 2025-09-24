#assingment8.py
print("-----------5번-----------")
x = 42
y = 42
print(id(x) == id(y))


print("-----------6번-----------")
#6. 리스트에서 첫 번째 짝수와 마지막 홀수를 찾아 서로 스왑하는 프로그램을 작성하시오.
a = [3, 6, 7, 4, 9, 10, 13]
#앞에서부터 짝수 찾기
for i in range(0,len(a),1):
    if a[i] % 2 == 0:
        even_index = i
        even = a[even_index]
        print(even)
        break

#뒤에서부터 홀수 찾기
for i in range(len(a)-1,-1,-1):     
    if a[i] % 2 != 0:
        odd_index = i
        odd = a[odd_index]
        print(odd)
        break
    
#스왑
temp = a[even_index]
a[even_index] = a[odd_index]
a[odd_index] = temp

print(a)


print("-----------7번-----------")
#파이썬으로 최대값을 찾는 알고리즘을 구현하시오.
def find_max(fu):
    max_index = 0
    for i in range (len(fu)):
        if fu[max_index] < fu[i]:
            max_index = i
    return fu[max_index]

lst = [10,901,8,23,55,300,890,1000]
max_val = find_max(lst)
print(max_val)


print("-----------9번-----------")
#리스트를 오름차순으로 정렬
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # 빈칸에 들어갈 코드
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

data = [64, 25, 12, 22, 11]
print(selection_sort(data))


print("-----------10번-----------")
#주어진 딕셔너리에서 모든 값의 합을 구하는 함수를 작성하세요. 
#( 예를 들어, 딕셔너리 { 'a': 10, 'b': 20, 'c': 30 }가 주어졌을 때, 합은 60 )

dic = { 'a': 10, 'b': 20, 'c': 30 }
total = 0
for i in dic.keys():
    total = dic.get(i) + total
#   total = total + dic[i]      #이것도 가능!
print( total)
