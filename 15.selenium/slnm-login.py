# 웹사이트 로그인 하기
# 3개 함수 사용
# find_element_by_css_selector, click, send_keys

# Selenium 임포트
from selenium import webdriver

# 크롬 드라이버 생성 - 경로 설정 필요 없음
driver = webdriver.Chrome()
driver.implicitly_wait(3)

# 사이트 접속하기
driver.get('https://workey.codeit.kr/costagram/index')

# css 선택자 선택
# click 하면 click 실행해서 화면까지 뜬다
driver.find_element_by_css_selector('a.top-nav__login-link').click()

# find_element_by_tag_name, find_element_by_id
# driver.find_element_by_tag_name('tag_name')
# driver.find_element_by_id('id-name')
# driver.find_element_by_class_name('class-name')

# 복수를 선택하는 경우, element 에 s만 붙혀서 elements 한다.
# CSS 선택자
# driver.find_elements_by_css_selector('selector')
# 리스트 타입, 리턴

# 태그 이름
# driver.find_elements_by_tag_name('tag_name')

# class 이름
# driver.find_elements_by_class_name('class-name')


# id, 비밀번호 입력
driver.find_element_by_css_selector('.login-container__login-input').send_keys('codeit')
driver.find_element_by_css_selector('.login-container__password-input').send_keys('datascience')

# 로그인 버튼 클릭
driver.find_element_by_css_selector('.login-container__login-button').click()
