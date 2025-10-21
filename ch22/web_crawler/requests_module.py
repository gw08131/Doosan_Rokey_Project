# requests_module.py

import requests
from bs4 import BeautifulSoup

url = "https://example.com/"
response = requests.get(url)
# print(response.status_code)     # 200 <- 제대로 데이터 가져옴
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")

# 첫번째 태그 가져오기
header1 = soup.find("h1")       # <h1>Example Domain</h1>
print(header1.text)

html = """
<html>
<head>
    <div class="title">
        <title>Example Domain</title>
    </div>
</head>
<body>
    <div id="content">
        <h1>Hello, Web!</h1>
    </div>
    <div>
        <h1>Example Domain</h1>
        <p>This domain is for use in documentation examples
        without needing permission. Avoid use in operations. </p>
    </div>
</body>
</html>
"""
soup = BeautifulSoup(html,"html.parser")

# 특정 클래스(.title)를 가진 첫번째 요소 가져오기
title= soup.find("div",class_="title")
print(title.text)                            # Example Domain

#  특정 ID 를 가진 첫번째 요소 가져오기
content = soup.find("div",id="content")
print(content.text)                         # Hello, Web!