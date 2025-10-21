# assignment16.py

print("---------6번---------")
class Stack():
    def __init__(self):
        self.stack = []

    def push(self,x):
        self.stack.append(x)

    def pop(self):
        if self.stack == []:
            return -1
        return self.stack.pop()
    
    def top(self):
        if self.stack:
            return self.stack[-1]
        return -1
    
    def is_empty(self):
        if self.stack == []:
            return True
        return False
    
stack1 = Stack()
stack1.push(1)
stack1.push(2)
print(stack1.top())
stack1.push(3)
stack1.push(4)
print(stack1.top())
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
print(stack1.pop())
print(stack1.is_empty())



print("---------7번---------")

#스택은 숫자만 남는다
#연산자를 만나면 숫자 두개를 pop -> 계산 -> result push

class PostfixNotion:
    def __init__(self):
        self.stack = []

    def evaluate(self,data):
        self.stack.clear()  
        for value in data.split():
            if not value in "+-*/":
                self.stack.append(int(value))
        #return self.stack
            else:
                b = self.stack.pop()
                a = self.stack.pop()

                if value == "+":
                    result = a+b
                elif value == "-":
                    result = a-b
                elif value == "*":
                    result = a*b
                elif value == "/":
                    result = a/b
                
                self.stack.append(result)
        return self.stack.pop()

postfix = PostfixNotion()
print(postfix.evaluate("3 4 + 5 *"))


print("---------8번---------")

class Queue():
    def __init__(self):
        self.queue = []
    
    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return -1
    
    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return -1

    def is_empty(self):
        if self.queue == []:
            return True
        return False

q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.front())
q.dequeue()
q.dequeue()
print(q.dequeue())
print(q.is_empty())


print("---------9번---------")

n = 3

class CircularQueue():
    def __init__(self):
        self.queue = []
    
    def enqueue(self, x):
        if self.is_full() ==  False:
            self.queue.append(x)
        return self.queue

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
    
    def front(self):
        if self.is_empty():
            return -1
        return self.queue[0]

    def is_empty(self):
        if self.queue == []:
            return True
        return False
    
    def is_full(self):
        if len(self.queue) >= n:
            return True
        return False
    


q = CircularQueue()
print(q.is_empty())
q.enqueue(1)
q.enqueue(2)
print(q.enqueue(3))
print(q.is_full())


print("---------10번---------")

from collections import deque

class Deque():
    def __init__(self):
        self.dq = deque()

    def push_front(self,x):
        self.dq.appendleft(x)
        return self.dq

    def push_back(self,x):
        self.dq.append(x)
        return self.dq

    def pop_front(self):
        if not self.dq == []:
            self.dq.popleft()
            return self.dq
        return -1

    def pop_back(self):
        if not self.dq == []:
            self.dq.pop()
            return self.dq
        return -1
    

dq1 = Deque()
print(dq1.push_front(2))
print(dq1.push_back(3))
print(dq1.push_front(1))
print(dq1.push_back(4))

print(dq1.pop_back())
print(dq1.pop_front())
print(dq1.pop_back())
print(dq1.pop_front())