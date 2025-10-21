# OpenWeatherMap API를 이용해 여러 도시의 날씨 데이터를 불러오고,
# 각 도시의 최저기온을 섭씨(°C) 단위로 시각화하는 프로그램

import requests
import json
import matplotlib.pyplot as plt

# API 키 입력
apikey = "a249c80aaccb18e06ae727b0c6f4fcf9"
# city = "Seoul,KR"

# API URL 템플릿
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

# 4. 켈빈 → 섭씨 변환 함수
k2c = lambda k: k - 273.15

# 결과를 저장할 리스트
temp_min_list = []

# 여러 도시 이름 리스트
cities = ["Seoul", "New York,US", "Sydney,AU", "Tokyo,JP"]

# 각 도시별 날씨 정보 가져오기
for name in cities:
    # URL 생성
    url = api.format(city=name, key=apikey)

    # API 요청
    response = requests.get(url)
    # print(response.status_code)  # 200이면 성공
    # print(response.text)         # JSON 텍스트 출력

    # JSON 문자열을 파이썬 딕셔너리로 변환
    data = json.loads(response.text)
    # print(data)  # 전체 데이터 구조 확인용

    # 주요 정보 출력
    print("도시:", data["name"])
    print("날씨:", data["weather"][0]["description"])
    print("현재 온도:", round(k2c(data["main"]["temp"]), 2), "°C")

    # 최저기온 데이터 저장
    temp_min_list.append(k2c(data['main']['temp_min']))

# 그래프는 반복문 밖에서 한 번만 그리기!
plt.rcParams['font.family'] = 'Malgun Gothic'  # 한글 폰트 설정
plt.title("도시별 최저기온")
plt.xlabel("도시")
plt.ylabel("최저기온 (°C)")

# 산점도 그래프 (scatter)
plt.scatter(cities, temp_min_list, color="blue", label="최저기온", s=100, marker='o')

plt.legend()
plt.tight_layout()
plt.show()



# {'coord': {'lon': 126.9778, 'lat': 37.5683}, 
#  'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 
#  'base': 'stations', 
#  'main': {'temp': 295.91, 'feels_like': 296.15, 'temp_min': 295.91, 'temp_max': 296.93, 'pressure': 1019, 'humidity': 73, 'sea_level': 1019, 'grnd_level': 1009},
#  'visibility': 10000, 
#  'wind': {'speed': 4.12, 'deg': 320}, 
#  'clouds': {'all': 40}, 
#  'dt': 1760585504, 
#  'sys': {'type': 1, 'id': 8105, 'country': 'KR', 'sunrise': 1760564441, 'sunset': 1760604863}, 
#  'timezone': 32400, 
#  'id': 1835848, 
#  'name': 'Seoul', 
#  'cod': 200}`