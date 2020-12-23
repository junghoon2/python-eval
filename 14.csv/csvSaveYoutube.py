import csv
import requests
from bs4 import BeautifulSoup

# CSV 파일 생성
# csv_file = open('시청률_2010년1월1주차.csv', 'w')
# csv_writer = csv.writer(csv_file)

# 헤더 행 추가
# csv_writer.writerow(['순위', '채널', '프로그램', '시청률'])

pages = requests.get("https://www.youtube.com/channel/UCIWz0Nm1XhwsmCZGPyqXz0w/videos?view=0&sort=dd&flow=grid")
# rating_page = response.text
soup = BeautifulSoup(pages.text, 'html.parser')

print(soup.select('h3.ytd-grid-video-renderer a'))

# for tr_tag in soup.select('tr')[1:]:
#     td_tags = tr_tag.select('td')
#     row = [
#         td_tags[0].get_text(),
#         td_tags[1].get_text(),
#         td_tags[2].get_text(),
#         td_tags[3].get_text()
#     ]
#     # 데이터 행 추가
#     csv_writer.writerow(row)

# # CSV 파일 닫기
# csv_file.close()