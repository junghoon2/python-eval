import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/ratings/index")
# 이 코드는 계속 변경되지 않는다.
soup = BeautifulSoup(response.text, 'html.parser')

print(soup.select('tr'))

