import csv
import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/orangebottle/index")
soup = BeautifulSoup(response.text, 'html.parser')

# CSV 파일 생성
csv_file = open('오렌지_보틀.csv', 'w')
csv_writer = csv.writer(csv_file)

# 헤더 행 추가
csv_writer.writerow(['지점 이름', '주소', '전화번호'])

branches = soup.select('div.branch')

for branch in branches:
  row = [
      branch.select_one('p.city').get_text(),
      branch.select_one('p.address').get_text(),
      branch.select_one('span.phoneNum').get_text()

      # list(branch.select_one('p.city').stripped_strings),
      # list(branch.select_one('p.address').stripped_strings),
      # list(branch.select_one('span.phoneNum').stripped_strings)
      # list(branch.select_one('p.city').stripped_strings, branch.select_one('p.address').stripped_strings, branch.select_one('span.phoneNum').stripped_strings)
  ]

  csv_writer.writerow(row)

csv_file.close()