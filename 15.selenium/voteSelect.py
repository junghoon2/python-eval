# 선거 당선인 명부 조회, 당선인 정보 저장
# select method 사용

import csv
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# 웹페이지 저장
driver = webdriver.Chrome()
driver.implicitly_wait(3)
url = "http://info.nec.go.kr/main/showDocument.xhtml?electionId=0020200415&topMenuId=EP&secondMenuId=EPEI01"

driver.get(url)
time.sleep(1)

# CSV 파일 생성
csv_file = open('비례대표_당선인명부.csv', 'w')
csv_writer = csv.writer(csv_file)

# # 헤더 행 추가
csv_writer.writerow(['당명', '당선인'])

# '국회의원선거'탭 클릭 
driver.find_element_by_css_selector('#electionId7').click()

# 당명 선택, select 함수 사용
propo_rep_select = Select(driver.find_element_by_css_selector('#proportionalRepresentationCode'))
propo_rep_select.select_by_value('5049')

# '검색'버튼 클릭
driver.find_element_by_css_selector('#spanSubmit').click()

# 국회의원 정보 상위 태그 선택
# 각 태그 별 rank, name 선택
for element in driver.find_elements_by_css_selector('tbody tr'):
  rank = element.find_element_by_css_selector('td.alignC').text
  # 특수문자, 새로운 행 \n 기준으로 split 가능
  name = element.find_elements_by_css_selector('td.alignC')[2].text.split('\n')[0]

  csv_writer.writerow([rank, name])

# 파일 닫기
csv_file.close()
driver.quit()
