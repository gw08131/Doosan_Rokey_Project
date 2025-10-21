# generator1.py

import time

def longtime_job():
    print("job start")
    time.sleep(1)
    return "done"

# generator 컴프리헨션
list_job = (longtime_job() for i in range(5))
print(next(list_job)) 

# next 함수 1회 실행에 따른 약 1초의 시간만 소요
# 미리 실행 5회가 아닌 1회만 호출
# 연산을 늦추는 방식 => 느긋한 계산법 (lazy evaluation)

print(next(list_job)) 
print(next(list_job)) 
print(next(list_job)) 
print(next(list_job)) 
print(next(list_job)) 