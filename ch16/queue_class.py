# queue_class.py

# 큐 리스트 생성

# enqueue 기능

# dequeue 기능
# - 큐가 비어있는 경우

# 큐에 대한 상태 확인


# 큐 리스트 생성
class Queue:
    def __init__(self):
        self.queue = []

    # enqueue 기능
    def enqueue(self, data):
        self.queue.append(data)

    # dequeue 기능
    # - 큐가 비어있는 경우
    def dequeue(self):
        if not self.is_empty() == True:
            return self.queue.pop(0)
        return

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False      

    # 큐에 대한 상태 확인
    def status_queue(self):
        return self.queue
    

q1 = Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
print(q1.status_queue())        # [1, 2, 3]

q1.dequeue()
print(q1.status_queue())        # [2, 3]
q1.dequeue()
print(q1.status_queue())        # [3]
q1.dequeue()
print(q1.status_queue())        # []
q1.dequeue()
print(q1.status_queue())        # []


