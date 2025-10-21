# stack_list.py

# 빈 stack 구현
stack = []          # <-굳이 매번 만들 필요 X 
stack = [1,2,3]     # <- 이렇게 보다는 append를 사용하여 push하는 방식 많이 씀!

# push 기능 구현
stack.append(4)
# 스텍에 대한 형태 확인
print("stack=", stack)

# pop 기능 구현
stack.pop(-1)
print("stack=", stack)
stack.pop()
print("stack=", stack)
stack.pop()
print("stack=", stack)
stack.pop()
print("stack=", stack)          # stack= []
stack.pop()
print("stack=", stack)          # IndexError: pop from empty list

# 빈 stack 여부 확인
if stack == []:
    print("stack is empty")



