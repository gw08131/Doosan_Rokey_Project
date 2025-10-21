# queue_list.py

queue = []

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)        # [1, 2, 3, 4]

queue.pop(0)
print(queue)        # [2, 3, 4]
queue.pop(0)
queue.pop(0)
print(queue)        # [4]

queue.pop(0)        # []
queue.pop(0)        # IndexError: pop from empty list
