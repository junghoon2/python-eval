# 지문만 출력하기 
# 지문이란? (), 괄호로 쌓인 문자만 출력하기 

import os
import re

os.chdir('./09.regularExpress')

f = open('friends101.txt', 'r')
script = f.read()
f.close()

# 지문만 저장
# line = re.findall(r'[()\[\]][\w\s]+[()\[\]]', script)

# ? 앞 패턴이 없거나 하나이어야 함
# ? 사용하면 greedy 멈춘다.
line = re.findall(r'\([A-Za-z].+?[a-z:\.]\)', script)

print(line)