# 특정 단어가 들어가 있는 문장만 별도로 저장하기 
# user input 받아서 해당 변수로 문장 찾는건 어렵네. 

import os, re

os.chdir(r'./09.regularExpress')

f = open('friends101.txt', 'r')
script = f.readlines()
f.close()

# 원하는 단어 입력하기
word = input('찾고자 하는 단어를 입력하세요: ')

# 단어에 포함된 게 아니라 단일 단어로 찾기
# word_search = word

# re.findall(r'word')

regex = '{}$'.format(re.escape(word))

for item in script:
  # if re.search('would', item):
  # if re.findall(r'^word\s', item):
  # if re.findall(word'\w$', item.strip()):
  if re.match(regex, item, re.IGNORECASE): 
    print(item)
  # if word in item:  # list에서 string 찾을 수 있나?
  #   print(item)

# re 정규표현식 메소드 중 search, match, findall 