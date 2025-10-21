# Q23-7.py

# 7. requests 모듈을 사용하여 JSONPlaceholder API 
# (https://jsonplaceholder.typicode.com/todos/1)에서 데이터를 가져오세요.

import json
import requests

# 1. API 주소 지정
api = "https://jsonplaceholder.typicode.com/todos/1"

# 2. API 요청 보내기
response = requests.get(api)

# 3. 응답 데이터를 JSON(문자열)에서 Python 딕셔너리로 변환
data = json.loads(response.text)

# 4. 결과 확인
print(type(data))   # <class 'dict'>
print(data)
