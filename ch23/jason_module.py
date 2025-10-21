# jason_module.py

import json

#JSON 문자열을 파이썬 객체로 변환
json_string = '{"name":"Alice","age":25,"city":"Seoul"}'


# JSON 문자열 -> 딕셔너리 변환
data = json.loads(json_string)
print(type(data))
data["name"]

# 파이썬 객체를 JSON 문자열로 변환
python_dict = {"name":"Bob","age":30,"city":"Busan"}

# Jason 포멧 변환
json_output = json.dumps(python_dict,indent=4)
print(type(json_output))
print(json_output)

# JSON 파일 저장
path = "C:/rokey/python/ch23/data.json"
with open(path,"w") as file:
    json.dump(python_dict, file, indent=4)

# JSON 파일 불러오기
with open(path,"r") as file:
    loaded_data = json.load(file)
print(type(loaded_data))
print(loaded_data)