import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/ratings/index")
rating_pages = response.text

# parser, 정리 함수. 원하는 html tag 쉽게 가져 올 수 있다. 
soup = BeautifulSoup(rating_pages, 'html.parser')
# soup = bs4(rating_pages, 'html.parser'), 에러

# 특정 tag만 가져오려면 select 사용
# parser로 이미 분류하여 사용 가능 
# print(soup.select('title'))

# td tag의 program class 선택
# print(soup.select('td.program'))

# select로 page 요소를 select 한다. 
# select는 list 형식으로 return 한다.

# program title만 list로 저장
program_title_tags = soup.select('td.program')

# program 이름만 가져오려면? 
# text 지정하면 get_text만 가져온다.

# program_titles = []

# # list 안의 text 내용만 저장 
# for tag in program_title_tags:
#   program_titles.append(tag.get_text())

# print(program_titles)

# select_one, 가장 위 하나만 리턴한다.
print(soup.select_one('td.program'))