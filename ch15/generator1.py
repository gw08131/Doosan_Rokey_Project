# generator1.py

import time

def longtime_job():
    print("job start")
    time.sleep(1)
    return "done"

# 리스트 컴프리헨션
# [표현식 for 요소 in 이터러블]
list_job = [longtime_job() for i in range(5)]
print(list_job[0])  
# longtime_job을 5번 호출
# 호출될 때마다 "job start"가 출력되고 1초씩 대기 (총 5초 소요)
# 각 호출의 반환값 "done"이 리스트에 저장
# list [0]번째 인덱스 요소인 done 한개가 출력
