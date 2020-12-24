import requests
from openpyxl import Workbook
from bs4 import BeautifulSoup

# excel 파일 만들기
# 파일, worksheet, header 순서로 만들기
wb = Workbook(write_only=True)
ws = wb.create_sheet()
ws.append(['기간', '순위', '프로그램', '시청률'])

for year in range(2010, 2019):
  for month in range(1, 13):
    for week in range(5):
      url = "https://workey.codeit.kr/ratings/index?year={}&month={}&weekIndex={}".format(year, month, week)

      response = requests.get(url)
      soup = BeautifulSoup(response.text, 'html.parser')

      # 원하는 tag를 가지는 text 선택

      # select 이름으로 선택하니 '' 따옴표 꼭 넣어준다. 
      for tag in soup.select('tr.row')[1:]:
      # for tag in soup.select('tr')[1:]:
        # tags = tag.select('td')
        # debugging을 빨리 할 줄도 알아야 하는데
        channel = tag.select_one('td.channel').get_text()
        if channel == 'SBS':
          period = '{}년 {}월 {}주차'.format(year, month, week + 1)
          rank = tag.select_one('td.rank').get_text()
          program = tag.select_one('td.program').get_text()
          viewerRate = tag.select_one('td.percent').get_text()

          ws.append([period, rank, program, viewerRate])

      # for tr_tag in soup.select('tr')[1:]:
      #     # 데이터 행의 채널이 SBS인 경우만 데이터 행 저장
      #     channel = tr_tag.select_one('td.channel').get_text()
      #     if channel == 'SBS':
      #         # 데이터 행의 기간, 순위, 프로그램, 시청률 저장
      #         period = "{}년 {}월 {}주차".format(year, month, week + 1)
      #         td_tags = tr_tag.select('td')
      #         rank = td_tags[0].get_text()
      #         program = td_tags[2].get_text()
      #         percent = td_tags[3].get_text()

      #         ws.append([period, rank, program, percent])

wb.save('SBS_data.xlsx')