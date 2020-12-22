import requests
from bs4 import BeautifulSoup

# 먼저 분석하려는 사이트를 선택하고
response = requests.get("https://workey.codeit.kr/ratings/index")

# 해당 사이트를 분석하기 좋게 beautifulSoup 이용해서 parser 한다.
soup = BeautifulSoup(response.text, 'html.parser')

# 이 코드는 계속 변경되지 않는다.

# print(soup.select('td'))

# 어떤 데이터를 가져올 것인지, tag를 선택한다.
# 4번째 td 까지 가져오기, slicing 
# list type으로 저장한다. 
td_tags = soup.select('td')[:4]

for tag in td_tags:
  print(tag.get_text())
