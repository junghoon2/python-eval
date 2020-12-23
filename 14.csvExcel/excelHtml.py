import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = Workbook(write_only=True)
ws = wb.create_sheet('TV Ratings')
ws.append(['순위', '채널', '프로그램', '시청률'])

response = requests.get("https://workey.codeit.kr/ratings/index")
# 이 코드는 계속 변경되지 않는다.
soup = BeautifulSoup(response.text, 'html.parser')

for tr_tag in soup.select('tr.row'):
  td_tags = tr_tag.select('td')
  # td_tags = tr_tag.td
  row = [
    td_tags[0].get_text(), # 순위
    # td_tags[0].stripped_strings(), # 순위
    # tr_tag.td[0].get_text(), # 순위
    td_tags[1].get_text(), # 채널
    # td_tags[2].get_text(),
    # td_tags[3].get_text()
    # td_tags[1].stripped_strings()
  ]
  ws.append(row)

wb.save('시청률_2010년 1월 1주차.xlsx')
