
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# 웹페이지 저장
driver = webdriver.Chrome()
driver.implicitly_wait(3)
url = "https://docs.diamanti.com/bundle?labelkey=prod-spektra"

driver.get(url)
time.sleep(1)

titles = []

for li in driver.find_elements_by_css_selector('.zDocsBundlesListBundleTitle'):
  # title = li.find_element_by_css_selector('.zDocsBundlesListBundleTitle').text
  title = li.text
  titles.append(title)

print(titles)

driver.close()
