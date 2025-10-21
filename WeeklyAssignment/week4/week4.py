# week4.py

stack1 = ['두산', '로키', '부트','캠프']

class Stack():
    def __init__(self,stack):
        self.stack = stack

    def push(self,data):
        self.stack.append(data)
        return self.stack
    
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False
    
    def pop(self):
        if self.is_empty()==False:
            self.stack.pop(-1)
            return self.stack
        return
    

    
s = Stack(stack1)
print(s.pop())

