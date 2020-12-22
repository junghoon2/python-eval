# 라이브러리 필요, 외부 / 내부 라이브러리

# import os # 내장 라이브러리

import requests

# response = requests.get("https://google.com")

for i in range(5):
  url = "https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex={}".format(i)
  # print(url)
  response = requests.get(url)
  print(response.text)

