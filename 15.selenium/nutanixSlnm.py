# 로그인까지 자동으로 하기 

# Selenium 임포트
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# 크롬 드라이버 생성 - 경로 설정 필요 없음
driver = webdriver.Chrome()
driver.implicitly_wait(1)

# 사이트 접속하기
driver.get('https://172.17.16.35:9440/')
driver.find_element_by_id('details-button').click()
driver.find_element_by_id('proceed-link').click()

# id, 비밀번호 입력
driver.find_element_by_id('inputUsername').send_keys('admin')
driver.find_element_by_id('inputPassword').send_keys('Qwer!234')

# 로그인 버튼 클릭
driver.find_element_by_id('inputPassword').send_keys(Keys.ENTER)
