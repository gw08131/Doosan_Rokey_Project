# Q7.py

import json
import os

folder_path = r"C:\rokey\python\WeeklyAssignment\week5"
file_path = os.path.join(folder_path, "config.ini")
json_path = os.path.join(folder_path, "config.json")

# ini 파일 읽기
with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

# 각 줄을 '반=이름' 형태로 분리 → 딕셔너리 변환
config_dict = {}
for line in lines:
    if "=" in line:
        key, value = line.strip().split("=")
        config_dict[key.strip()] = value.strip()
        
print(config_dict)

# 딕셔너리를 JSON 파일로 저장
with open(json_path, "w", encoding="utf-8") as json_file:
    json.dump(config_dict, json_file, indent=4, ensure_ascii=False)

print(json_path)
