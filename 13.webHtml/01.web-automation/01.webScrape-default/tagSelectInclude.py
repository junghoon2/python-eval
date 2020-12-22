import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/orangebottle/index")
# 이 코드는 계속 변경되지 않는다.
soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.select('div.branch'))

# 지점 이름, 주소, 전화번호 리스트 저장

branch_infos =[]

branch_tags = soup.select('div.branch')

for branch_tag in branch_tags:
  name = branch_tag.select_one('p.city').get_text()
  address = branch_tag.select_one('p.address').get_text()
  phone = branch_tag.select_one('span.phoneNum').get_text()
  # name = branch_tags.select('p.city').get_text()
  # address = branch_tags.select('p.address').get_text()
  # phone = branch_tags.select('span.phoneNum').get_text()

  branch_infos.append([name, address, phone])

print(branch_infos)

# # 지점 이름, 주소, 전화번호 tag 지정
# name_tags = soup.select('p.ave')
# address_tags = soup.select('p.address')
# phone_tags = soup.select('span.phoneNum')

# # 이름 리스트 만들어서 해당 리스트에 값을 append로 추가
# name =[]
# address =[]
# phone =[]

# # # 3개의 리스트에서 하나하나씩 element 선택해서 새로운 list 만들기
# # for name, address, phone in name_tags, address_tags, phone_tags:
# #   branch_infos.append([name, address, phone])


# for tag in name_tags:
#   name.append(tag.get_text())

# for tag in address_tags:
#   address.append(tag.get_text())

# for tag in phone_tags:
#   phone.append(tag.get_text())

