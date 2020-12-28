# 속성값 가져오기 

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
response = requests.get(url)
rating_pages = response.text

# parser, 정리 함수. 원하는 html tag 쉽게 가져 올 수 있다. 
soup = BeautifulSoup(rating_pages, 'html.parser')

# 리스트로 선택하려면 해당 tag 전체를 포함해야 한다.
for tag in soup.select('div.thumb img'):
# 속성 가져오기, []로 가져올 수 있다.
  image_src = tag['src']
  print(image_src)
