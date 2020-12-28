# 웹툰 요일별 인기순 제목 가져오기

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
response = requests.get(url)
rating_pages = response.text

# parser, 정리 함수. 원하는 html tag 쉽게 가져 올 수 있다. 
soup = BeautifulSoup(rating_pages, 'html.parser')

# 인기순 제목 저장
titles = []

# for 반복문 리스트 만들기
# id는 #로 검색, tag를 포함하는 상위 태그 선택하고 하위 태그 선택

# 리스트로 선택하려면 해당 tag 전체를 포함해야 한다.
# for tag in soup.select('#realTimeRankFavorite'):
for tag in soup.select('#realTimeRankFavorite li'):
  title = tag.select_one('a').get_text()
  # text가 아닌 tag 이름 가져오는 방법
  titles.append(title)

print(titles)