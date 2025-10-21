# Q4.py
import os

folder_path = r"C:\rokey\python\WeeklyAssignment\week5"
os.makedirs(folder_path, exist_ok=True)
ini_path = os.path.join(folder_path, "config.ini")

# 저장 (쓰기)
content = [
    "1반 = 홍길동",
    "2반 = 김철수",
    "3반 = 박영희",
    "4반 = 최로키",
]
with open(ini_path, "w", encoding="utf-8") as f:
    f.write("\n".join(content))

# 읽기
print(ini_path)
with open(ini_path, "r", encoding="utf-8") as f:
    with open(ini_path, "r", encoding="utf-8") as f:
        lines = f.readlines()  
    for line in lines:
        print(line.strip()) 


