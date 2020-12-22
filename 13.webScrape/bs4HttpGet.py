import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/orangebottle/index")
# 이 코드는 계속 변경되지 않는다.
soup = BeautifulSoup(response.text, 'html.parser')

# index_pages = response.text

# parser, 정리 함수. 원하는 html tag 쉽게 가져 올 수 있다. 

# BeautifulSoup으로 html page 가져오고
# soup = BeautifulSoup(index_pages, 'html.parser')

# 전체 페이지 중에서 내가 원하는 tag만 select method 사용해서 선택한다.
# phone number를 select method로 선택한다.
# phone number tag만 따로 저장
phones_tags = soup.select('span.phoneNum')

# 리스트 형태의 변수 선언
phone_numbers = []

# append 메소드 사용해서 하나씩 추가
# text만 가져오기 위해서는 get_text() 메소드 선택
for phone in phones_tags:
  phone_numbers.append(phone.get_text())

print(phone_numbers)

