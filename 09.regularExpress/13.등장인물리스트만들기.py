# 대문자로 시작하는 문장에서 대문자 포함된 단어만 찾기
# \n 개행 문자 이 후 찾는 방법은

import os
import re

# 대문자 시작 검색
os.chdir('./09.regularExpress')
f = open('friends101.txt', 'r')
script = f.read()

f.close()

# print(script[:100])

# [A-Z]
# character = re.findall(r'^[A-Z].+:', script)  
# 왜 ^ 시작 문자 넣으면 안될까?
character = re.findall(r'[A-Z][a-z]+:', script)

# 중복된 element 제거
character = set(re.findall(r'[A-Z][a-z]+:', script))

# 이제 scene, note, all 등 제거 

# :, 콜론 제거하기
character_lst = list(character)
# print(character_lst)

character_new =[]

# 각 element 마다 마지막 : 제거
for item in character_lst:
  item = item[:-1]
  # 이걸 다시 하나의 리스트로 만들려면
  # list로 다시 만들어서 추가
  character_new += [item]
# print(character_new)

# list element 제거 : all, note
# character = del(character[All:])
character_new.remove('All')
character_new.remove('Note')

print(character_new)