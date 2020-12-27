# 전체 페이지(scroll) scrape 하기

import time
from selenium import webdriver

# 웹페이지 가져오기
driver = webdriver.Chrome()
driver.implicitly_wait(3)
url = "https://workey.codeit.kr/costagram/index"

driver.get(url)
time.sleep(1)

# 로그인 페이지 클릭
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
  print(image_url)

  # img = driver.find_element_by_css_selector('div.post-container__image').get_attribute('style').split
  # print(img)

  # tag, text 값이 아닌 url 정보 가져오기

  driver.find_element_by_css_selector('button.close-btn').click()
  time.sleep(1)

# driver 닫기
driver.quit()