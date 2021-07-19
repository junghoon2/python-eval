# 정규 표현식 이용
import re

pattern = r'test'
# search_script = 'test txt'  # 파일이 아니라 script
# 파일에서 찾으려고 하면 따로 파일을 읽어 들여야 겠지

search_script = ''' 엄청 긴 테스트 파일을  
1일: 453400
2일: 388600
3일: 485300
4일: 477900
5일: 432100
6일: 665300
7일: 592500
8일: 465200
9일: 413200
10일: 523000
11일: 488600
12일: 431500
13일: 682300
14일: 633700
15일: 482300
16일: 391400
17일: 512500
18일: 488900
19일: 434500'''

# re.match(pattern, search_file).group()

if re.match(pattern, search_script):
  print('match')
else:
  print('not match')

# search 대상이 없으면 error 나온다.
print(re.search(pattern, search_script).group())