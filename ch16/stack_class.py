# stack_class.py

# class로 stack을 구현하시오

# push 기능 구현
# - 데이터 저장공간 (리스트)

# pop 기능 구현
# - 스텍 내 데이터 유무 확인


# 스택 최상위 (top) 데이터 확인
# - 스텍 내 데이터 유무 확인

# 스텍에 대한 상태 확인


class Stack:
    # 데이터 저장공간 (리스트)
    def __init__(self):
        self.stack = []

    # push 기능 구현
    def push(self,data):
        self.stack.append(data)
           
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False
    
    # pop 기능 구현
    # - 스텍 내 데이터 유무 확인
    def pop(self):
        # if len(self.stack) == 0:
        #     return
        # return self.stack.pop() 
        if not self.is_empty() == True:             # is_empty라는 함수 사용해서 표현
            return self.stack.pop()
        return 
    
    # 스택 최상위 (top) 데이터 확인
    # - 스텍 내 데이터 유무 확인
    def peak(self):
        if len(self.stack) == 0:
            return
        return self.stack[-1]           # stack 리스트의 제일 첫번째 데이터니까 (-1번째는 0번인덱스의 전번이니까 마지막 숫자)

    # 스텍에 대한 상태 확인
    def status_stack(self):
        return self.stack


s1 = Stack()
print(s1.peak())        # None
s1.pop()                # return을 통해 프로그램만 종료해서 아무 내용 출력 X
s1.push(1)
s1.push(2)
print(s1.peak())            # 2
print(s1.status_stack())    # [1,2]
s1.pop()
print(s1.peak())            # 1
print(s1.status_stack())    # [1,2]
s1.push(3)
s1.push(4)
print(s1.peak())            # 4
print(s1.status_stack())    #[1,3,4]

s1.pop()  
print(s1.status_stack())    #[1,3]
s1.pop()  
print(s1.status_stack())    #[1]
s1.pop()  
print(s1.status_stack())    #[]
s1.pop()  
print(s1.status_stack())    #[]