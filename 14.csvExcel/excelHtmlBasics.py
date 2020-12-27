import requests
from selenium import webdriver
from openpyxl import Workbook

wb = Workbook(write_only=True)
ws = wb.create_sheet('플레이 리스트')
ws.append(['제목', '해쉬태그', '좋아요 수', '곡 수'])

# URL
url = "https://workey.codeit.kr/music"

# selenium 설정 
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(url)

# find_elements로 원하는 정보 가져오기
for info in driver.find_elements_by_css_selector('.playlist__meta'):
  playlist_name = info.find_element_by_css_selector('h3.title').text.strip()
  tag = info.find_element_by_css_selector('a.tag').text.strip()
  likes = info.find_element_by_css_selector('span.data__like-count').text.strip()
  musics = info.find_element_by_css_selector('span.data__music-count').text.strip()

  ws.append([playlist_name, tag, likes, musics])

wb.save('플레이_리스트.xlsx')
