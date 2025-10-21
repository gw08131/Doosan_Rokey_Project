# set1.py

numbers = {1,2,3,4}
print(numbers)

numbers.add(5)
print(numbers)
numbers.remove(3)
print(numbers)

set1={1,2,3}
set2={3,4,5}

#교집합
print(set1 & set2)
#합집합
print(set1|set2)
#차집합
print(set1-set2)

print(type(set1 & set2))
print(type(set1|set2))
print(type(set1-set2))


# 자동 정렬 안됨 => sorted()
# 순서 보장 여부
# - 3.7 버전부터 입력 순서 유지

numbers = {4,3,5,1,2}
print(numbers)