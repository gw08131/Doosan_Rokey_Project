# Q23-8.py

# 8. https://randomuser.me/api/에서 
# 랜덤 유저 정보를 가져오고, name 값을 출력하세요.

import json
import requests

api = "https://randomuser.me/api/"

response = requests.get(api)

data = json.loads(response.text)

print(type(data))
# print(json.dumps(data, indent=4))

user = data["results"][0]
user_name = user["name"]
user_first_name = user_name["first"]
user_last_name = user_name["last"]

print("유저 정보: ",user_first_name,user_last_name)


"""
{
    "results": [
        {
            "gender": "female",
            "name": {
                "title": "Ms",
                "first": "Florence",
                "last": "White"
            },
            "location": {
                "street": {
                    "number": 5989,
                    "name": "Lakeview Ave"
                },
                "city": "Kingston",
                "state": "Saskatchewan",
                "country": "Canada",
                "postcode": "M7F 8M2",
                "coordinates": {
                    "latitude": "-68.1310",
                    "longitude": "60.6238"
                },
                "timezone": {
                    "offset": "+7:00",
                    "description": "Bangkok, Hanoi, Jakarta"
                }
            },
            "email": "florence.white@example.com",
            "login": {
                "uuid": "7ffc998e-2ff8-4c0d-8642-0e328cea9aa9",
                "username": "blackbear889",
                "password": "davide",
                "salt": "88HWb1bA",
                "md5": "094ef2cc01d2edddecb75ddf84d4ddc2",
                "sha1": "afd4b0e4501596b03230b4ddbee82b56e4184d04",
                "sha256": "93704177e1d200f2bb6445eb6bc775a8a4cbc6e539aaea009685920a1a63d88e"
            },
            "dob": {
                "date": "1957-03-08T02:36:26.756Z",
                "age": 68
            },
            "registered": {
                "date": "2004-12-02T20:16:02.886Z",
                "age": 20
            },
            "phone": "U86 O66-5561",
            "cell": "W62 C27-6160",
            "id": {
                "name": "SIN",
                "value": "957420011"
            },
            "picture": {
                "large": "https://randomuser.me/api/portraits/women/52.jpg",
                "medium": "https://randomuser.me/api/portraits/med/women/52.jpg",
                "thumbnail": "https://randomuser.me/api/portraits/thumb/women/52.jpg"
            },
            "nat": "CA"
        }
    ],
    "info": {
        "seed": "de97c5c13295d26f",
        "results": 1,
        "page": 1,
        "version": "1.4"
    }
}
"""