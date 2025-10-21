import json

folder_path = r"C:\rokey\python\WeeklyAssignment\week5"
file_path = f"{folder_path}/config.ini"

# ini 파일 읽기
with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

# ini → dict 변환
config_dict = {}
for line in lines:
    if "=" in line:
        key, value = line.strip().split("=")
        config_dict[key.strip()] = value.strip()

# dict → JSON 파일 저장
json_path = f"{folder_path}/config.json"
with open(json_path, "w", encoding="utf-8") as file:
    json.dump(config_dict, file, ensure_ascii=False, indent=4)

print(config_dict)





