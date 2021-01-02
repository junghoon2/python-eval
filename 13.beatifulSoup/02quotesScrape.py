# 명언 scrape 
# 명언, 저자, 태그 저장

import os, re
# import usecsv
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs

# 이 코드는 계속 변경되지 않는다.
url = "https://quotes.toscrape.com/"
soup = bs(ur.urlopen(url).read(), 'html.parser')

# 원하는 태그 선택
# find_all = select, find = select_one
tags = soup.select('div.quote')

# print(tags[0])

for quote in tags:
  print(quote.get_text())
