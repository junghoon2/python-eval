# selenium 으로도 web scrape 가능

# Selenium import
from selenium import webdriver
import time

# 크롬 드라이버 생성 - 경로 설정 필요 없음
driver = webdriver.Chrome()
driver.implicitly_wait(3)
url = "https://workey.codeit.kr/music"

# 사이트 접속하기
driver.get(url)

# 원하는 정보, 리스트 타입으로 저장
artists = []

for tag in driver.find_elements_by_css_selector('ul.popular__order li'):
  artists.append(tag.text.stripe())

print(artists)