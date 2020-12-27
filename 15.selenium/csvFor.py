# 각 항목을 csv format 다운하기 

import csv
import time
from selenium import webdriver

# 웹페이지 저장
driver = webdriver.Chrome()
driver.implicitly_wait(3)
url = "https://workey.codeit.kr/costagram/index"

driver.get(url)
time.sleep(1)

# CSV 파일 생성
csv_file = open('코스타그램.csv', 'w')
csv_writer = csv.writer(csv_file)

# 헤더 행 추가
csv_writer.writerow(['이미지 주소', '내용', '해시태그', '좋아요 수', '댓글 수'])

# 페이지 로그인
driver.find_element_by_css_selector('a.top-nav__login-link').click()

# id/pwd 입력
driver.find_element_by_css_selector('input.login-container__login-input').send_keys('codeit')
driver.find_element_by_css_selector('input.login-container__password-input').send_keys('datascience')
driver.find_element_by_css_selector('input.login-container__login-button').click()

# scroll 전체 페이지
# 페이지 끝까지 스크롤

# 현재 scrollHeight 가져오기
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # scrollHeight까지 스크롤                               
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 새로운 내용 로딩될때까지 기다림
    time.sleep(0.5)
    
    # 새로운 내용이 로딩됐는지 확인
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

time.sleep(1)

# 각 element 하나씩 전체 click
# 2개 클래스 선택하기
for post in driver.find_elements_by_css_selector('div.post-list__post.post'):
  post.click()
  time.sleep(1)

  # for 문 안에서 찾는게 아니라 전체 driver에서 찾는다
  # img = post.find_element_by_css_selector('div.post-container__image').get_attribute('url').text
  style_attr = driver.find_element_by_css_selector('.post-container__image').get_attribute('style')
  image_url = style_attr.split('"')[1]

  # text 내용 변수 저장 
  text = driver.find_element_by_css_selector('span.content__text').text

  # 복수 text의 list 타입을 string 저장하기. 
  # text 전체 포함하는 tag를 가져온다.
  tag = driver.find_element_by_css_selector('div.content__tag-cover').text

  like_count = driver.find_element_by_css_selector('span.content__like-count').text
  comment_count = driver.find_element_by_css_selector('span.content__comment-count').text
  
  csv_writer.writerow([image_url, text, tag, like_count, comment_count])

  # page 닫기
  driver.find_element_by_css_selector('button.close-btn').click()
  time.sleep(1)

# driver 닫기
driver.quit()

# csv file 닫기
csv_file.close()