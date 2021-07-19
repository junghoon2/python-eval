import re
import os
import codecs  # 파일 코덱 변경

pattern = r'test'
# search_script = 'test txt'  # 파일이 아니라 script
# 파일에서 찾으려고 하면 따로 파일을 읽어 들여야 겠지

# search_script = ''' 엄청 긴 테스트 파일을  
# 1일: 453400
# 2일: 388600
# test
# '''

id_num = '내 주민번호 234533 - 1xxxxxx 너는 387983-2xxxxxx'

# search 대상이 없으면 error 나온다.

# 정규 표현식 사용, \d, {6}
result_num = re.findall(r'\d{6}', id_num)
print(result_num)

sentence_example = 'I love a lovely dog, really. I am not telling a lie.'

# ly 로 끝나는 단어만 추출하기
# \w 숫자나 문자로 시작하는 
# result_ly = re.findall(r'\s.+?ly', sentence_example)
result_ly = re.findall(r'\w+ly', sentence_example)
print(result_ly)

