# 검색어 순위 데이터만 뽑아내기

import requests
from bs4 import BeautifulSoup
# import BeautifulSoup

response = requests.get("https://workey.codeit.kr/music")
soup = BeautifulSoup(response.text, 'html.parser')

popular_searches = []

print(soup.select('ul.rank__order li'))
tags = soup.select('ul.rank__order li')

for tag in tags:
  popular_searches.append(list(tag.stripped_strings)[2])

print(popular_searches)