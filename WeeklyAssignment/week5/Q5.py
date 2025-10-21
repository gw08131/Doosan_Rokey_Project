# Q5.py
import os

folder_path = r"C:\rokey\python\WeeklyAssignment\week5"
os.makedirs(folder_path, exist_ok=True)
ini_path = os.path.join(folder_path, "config.ini")

# 없으면 기본 템플릿으로 생성
if not os.path.exists(ini_path):
    template = [
        "1반 = ",
        "2반 = ",
        "3반 = ",
        "4반 = ",
    ]
    with open(ini_path, "w", encoding="utf-8") as f:
        f.write("\n".join(template))

# 읽기
with open(ini_path, "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())


        
