# tag 안에서 text 뽑아내기
# get_text() 또는 stripped_strings 사용 
# strings가 list 형태로 가능하여 좀 더 용이하구나 

import requests
from bs4 import BeautifulSoup
# import BeautifulSoup

# 이 코드는 계속 변경되지 않는다.
response = requests.get("https://workey.codeit.kr/music")
soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.select('ul.popular__order li'))

# 아직도 먼가 흐릿하다.
# 먼가, 사고의 순서와 맞지 않다. 
# 내 코드가 내가 생각하는 순서와 맞지 않다. 

# 내가 필요한 기능을 어떤 함수, 메소드에서 구현 가능한지 흐릿하다.
# 함수, 메소드의 정확한 사용법을 아직 모른다. 
artists = []

# 먼저, 내가 원하는 text를 포함하는 상위 태그를 선택
# tags = soup.select('ul.popular__order li').get_text()
tags = soup.select('ul.popular__order li')

# 상위 태그 안의 정보를 하나씩 가져오기 위해서 for 반복문 실행
for tag in tags:
  # artists.append(tag.get_text())
  # get_text(), tag 안 전체 text를 가져온다.
  # strip으로 공백 처리
  # 숫자만 제외 등 python 문자열 처리 함수 사용 가능
  # artists.append(tag.get_text().strip())

  # tag text 가져오는 2번째 방법
  # tag.strings는 list 형식이다.
  # print(list(tag.strings)[2])
  # print(tag.strings)
  # print(list(tag.strings)[2].strip())
  # artists.append(list(tag.strings)[2].strip())
  print(list(tag.stripped_strings))

print(artists) 
