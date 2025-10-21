# iterator.py

class MyIterator:
    def __init__(self,data):
        self.data = data            # self.data = [1,2,3]이 들어옴
        self.position = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.position < len(self.data): 
            result = self.data[self.position]
            self.position += 1
            return result
        else:
            raise StopIteration

if __name__ == "__main__":
    i = MyIterator([1,2,3])
    print(type(i))                       # <class '__main__.MyIterator'>
    print(next(i))          
    # next(i) 호출 → __next__() 실행
    # self.position = 0 → result = self.data[0] = 1
    # self.position = 1 로 증가 → 1 return(반환) → 1 출력
    print(f"위치 : {i.position}")       # position = 1


for item in i:          # class 호출로 iter()->next() 반복호출
    print(item)         # 2, 3
    print(f"위치 : {i.position}")

print(next(i))          
# position=3 상태에서 다시 next() 호출
# 조건 실패 → StopIteration 예외 발생 (출력 아님)