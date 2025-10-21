# reverse_iterator.py

class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.position = len(self.data)-1

    def __iter__(self):
        return self

    def __next__(self):
        if self.position >= 0:
            result = self.data[self.position]
            self.position -= 1
            return result
        else:
            raise StopIteration

rev = ReverseIterator([1,2,3,4])
for i in rev:                       # 아니면 for i in range(len(rev.data)) 가능!
    print(i)
    print(f"위치: {rev.position}")

print(next(i))
