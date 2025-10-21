# p2.py

file_path = r"C:\rokey\python\자기소개.txt"
data = """안녕하세요.
저는 지윤입니다.
저는 서울에 살고 있어요.
나이는 25살입니다.
두산 로키캠프 2반입니다."""

def write_file(file_path):
    with open(file_path,'w',encoding="utf-8") as file:
        file.write(data)
    
write_file("자기소개.txt")

# 파일에서 한줄씩 읽기
# 1. Generator yield 사용
def read_file():
    with open(file_path,'r',encoding="utf-8") as file:
        for line in file.readlines():
            yield line.strip()

read = read_file()
print(type(read))
for item in read:
    print(item)

print("------------------------------")
# 2. Generator 컴프리헨션 사용
with open(file_path,'r',encoding="utf-8") as file:
    read_line = (line for line in file.readlines())
for i in read_line:
    print(i.strip())
