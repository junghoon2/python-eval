import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/ratings/index")
# 이 코드는 계속 변경되지 않는다.
soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.select('tr.get_text')[1])

# 특정 태그 안에서 원하는 태그를 선택하도록 범위를 좁혀준다.

# 전체 tr tag 중 인덱스 1번 tag 선택
# 상위 tag 선택하고 그 안에 포함된 tag 선택하기 

# tr, table raw 중 첫번째 tr 선택
tr_tag = soup.select('tr')[1]

# tr 에서 td, table data tag만 select
td_tags = tr_tag.select('td')

# 해당 td 리스트의 text 정보 print
for td in td_tags:
  print(td.get_text())
