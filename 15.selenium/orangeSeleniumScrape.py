# selenium 으로도 web scrape 가능

# Selenium import
from selenium import webdriver
import time

# 크롬 드라이버 생성 - windows 경로 설정 시 추가 경로 설정 필요 없음
driver = webdriver.Chrome()
driver.implicitly_wait(3)
url = "https://workey.codeit.kr/orangebottle/index"

# 사이트 접속하기
driver.get(url)

# 원하는 정보, 리스트 타입으로 저장
branch_infos = []

# find_elements로 원하는 정보 가져오기
for info in driver.find_elements_by_css_selector('div.branch'):
  # stripe value 없는 듯..
  # python string type은 strip() 메소드 지원
  branch_name = info.find_element_by_css_selector('p.city').text.strip()
  address = info.find_element_by_css_selector('p.address').text.strip()
  phone_number = info.find_element_by_css_selector('span.phoneNum').text.strip()
  branch_infos.append([branch_name, address, phone_number])

print(branch_infos)

driver.quit()