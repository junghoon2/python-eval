# 네이버 미세먼지 데이터 가져오기

import requests
from bs4 import BeautifulSoup

url = "https://weather.naver.com/"
response = requests.get(url)
rating_pages = response.text

# parser, 정리 함수. 원하는 html tag 쉽게 가져 올 수 있다. 
soup = BeautifulSoup(rating_pages, 'html.parser')

# select text 선택
dust_level = soup.select_one('.level4_2 em.level_text').get_text()
ultradust_level = soup.select_one('.level4_3 em.level_text').get_text()

print('미세먼지 : ' + dust_level)
print('초미세먼지 : ' + ultradust_level)