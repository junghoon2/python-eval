import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/ratings/index")
# 이 코드는 계속 변경되지 않는다.
soup = BeautifulSoup(response.text, 'html.parser')

# 태그의 key 값과 속성을 가져오기
# tag 선택하면 tag의 전체 값을 가져온다.
# tag 안의 속성 값은 key 값 list로 가능하다.
print(soup.select_one('img')['src'])

# tag 모든 속성은 사전 형태로 저장되어 있다
print(soup.select_one('img').attrs)