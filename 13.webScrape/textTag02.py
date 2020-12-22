# 검색어 순위 데이터만 뽑아내기

import requests
from bs4 import BeautifulSoup
# import BeautifulSoup

response = requests.get("https://workey.codeit.kr/music")
soup = BeautifulSoup(response.text, 'html.parser')

tags = soup.select('ul.rank__order li')

for tag in tags:
  print(tag.stripped_strings())