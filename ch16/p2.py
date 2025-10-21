# p2.py

# 회전 큐 구현
# 덱 사용
# 리스트로 구현
#왼쪽으로 2만큼 회전

from collections import deque

queue = [1,2,3,4,5]
n = 4  

def Rotate(data):
    dq = deque(data)
    dq.rotate(-n)            #오른쪽으로 네칸

    return dq

rtate = Rotate(queue)
print(rtate)

print("------------------------")


def Rotate(data):
    dq = deque(data)

    for i in range(n):
        x = dq.popleft()        # 꺼내서 x에 저장
        dq.append(x)

    return dq

rtate = Rotate(queue)
print(rtate)