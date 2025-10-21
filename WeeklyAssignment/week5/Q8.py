# Q8.py
import os
import json

folder_path = r"C:\rokey\python\WeeklyAssignment\week5"
json_path = os.path.join(folder_path, "config.json")

if not os.path.exists(json_path):
    sample = {"1반": "짱구", "2반": "루피", "3반": "스누피", "4반": "스폰지밥"}
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(sample, f, indent=4, ensure_ascii=False)


with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

print(data)


