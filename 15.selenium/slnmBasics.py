# Selenium import
from selenium import webdriver
import time

# 크롬 드라이버 생성 - 경로 설정 필요 없음
driver = webdriver.Chrome()
driver.implicitly_wait(3)

# 사이트 접속하기
driver.get('https://workey.codeit.kr/costagram/index')

# css 선택자 선택
# click 하면 click 실행해서 화면까지 뜬다
driver.find_element_by_css_selector('a.top-nav__login-link').click()
time.sleep(1)


# id, 비밀번호 입력
driver.find_element_by_css_selector('.login-container__login-input').send_keys('codeit')
driver.find_element_by_css_selector('.login-container__password-input').send_keys('datascience')

# 로그인 버튼 클릭
driver.find_element_by_css_selector('.login-container__login-button').click()

driver.quit()