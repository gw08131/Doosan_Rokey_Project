# Q23-6.py

# 6. Python의 json 모듈을 사용하여 다음 데이터를 JSON 파일(data.json)로 저장하세요.

import json


json_dict=  {
            "name": "홍길동",
            "age": 25,
            "city": "서울"
            }


path = "C:/rokey/python/ch23/assignmnet23/data.json"
with open(path,"w") as file:
    json.dump(json_dict,file,indent=4)