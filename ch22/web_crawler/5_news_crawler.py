# 5_news_crawler.py

# 뉴스 웹사이트에서 제목과 URL을 수집하는 프로그램
# requests 모듈과 pandas 모듈, 
# bs4 모듈의 BeautifulSoup 클래스를 사용하여 
# 수집할 뉴스 URL 리스트를 작성하고 
# 해당 URL의 뉴스 제목을 스크래핑 하여 
# URL과 제목 목록을 출력하는 프로그램을 작성하시오.

import requests
from bs4 import BeautifulSoup
import pandas as pd

# 결과를 저장할 리스트
url_list = []
title_list = []

mbc_url = "https://imnews.imbc.com/"
news_mbc_url = "https://imnews.imbc.com/news/2025/econo/"

response = requests.get(news_mbc_url)
soup = BeautifulSoup(response.text,"html.parser")
# print(response.status_code)

# find_all : 첫번째 태그만 검색하지 않고 모두 찾기
newsList = soup.find_all('li', class_="item")


# news.a.get("href")
# 계층구조로 된 태그 접근시 접근 연산자(.)활용
# get("html 태그 속성명")
# 뉴스 url
for news in newsList:
    print(news_mbc_url+news.a.get("href"))
    url_list.append(news_mbc_url+news.a.get("href"))

for url in url_list:
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")

    title = soup.select_one("span",class_="tit.ellipsis2").get_text(strip=True)
    title_list.append(title.text)
    print(title.h2.text)

data = {"뉴스 URL": url_list, "제목": title_list}
df = pd.DataFrame(data)
print(df)