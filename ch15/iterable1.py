# iterable1.py

a = [1,2,3]
#next(a)            # TypeError: 'list' object is not an iterator

ia = iter(a)
print(type(ia))      # <class 'list_iterator'>
print(next(ia))      # ia의 현재 위치는 0 → a[0] = 1 반환 → 1 출력
print(next(ia))      # ia의 현재 위치는 1 → a[1] = 2 반환 → 2 출력
print(next(ia))      # ia의 현재 위치는 2 → a[2] = 3 반환 → 3 출력
print(next(ia))      # ia의 현재 위치는 3 (데이터 없음) → StopIteration 예외 발생
# print(next(ia))

for i in ia:        # 1, 2, 3 출력 -> 이때 이미 이터레이터 끝까지 다 소비됨
    print(i)
for i in ia:        # (출력 없음)
    print(i)

print(next(ia))     # StopIteration -> 이미 위에서 iterator은 다 소비됨..