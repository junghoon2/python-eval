# 이메일 주소 찾기
# 아직은 이해가 잘 안되는 걸로

# 이메일은 계정@도메인.최상위도메인 형식이며 계정에 +, -, _, . 등의 문자를 붙이기도 합니다. 또한, 도메인에 - 문자를 사용할 수 있고, 최상위 도메인이 여러 단계일 수도 있습니다. 이러한 규칙에 맞추어서 정규표현식을 작성합니다.
# ^[a-zA-Z0-9+-_.]+@는 이메일에서 @을 기준으로 계정을 나타내며 앞에 ^가 붙었으므로 계정이 맨 앞에 오는지 판단합니다. 또한, [a-zA-Z0-9+-_.]+와 같이 영문 대소문자, 숫자, +, -, _, .으로 되어 있어야 하고 문자 1개 이상인지 판단합니다.
# [a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$는 도메인과 최상위 도메인(TLD)를 나타냅니다. 먼저 [a-zA-Z0-9-]+와 같이 영문 대소문자, 숫자, -이면서 문자 1개 이상인지 판단합니다. 그리고 중간에 \.를 넣어서 도메인.최상위도메인 형식인지 판단합니다. 여기서 .은 정규표현식에 사용하는 특수 문자이므로 앞에 반드시 \를 붙여야 합니다. 특히 최상위 도메인은 여러 단계일 수도 있으므로 [a-zA-Z0-9-.]+$와 같이 범위에 .을 넣어줍니다. 또한, $를 붙여서 최상위 도메인이 마지막에 오는지 판단합니다.

# 참조 : https://velog.io/@ash3767/python-%EC%A0%95%EA%B7%9C%EC%8B%9D

import os
import re

os.chdir(r'/home/spkr/03.Python/09.regularExpress')

f1 = open('friends-test01.txt', 'r')
script1 = f1.read()

# \w.+@.+\.\w
# mail_script = re.findall(r'\w.+@.+\w', script1)
# + for 반복
mail_script = re.findall(r'\w+@\w+\.\w+', script1)

# from stackoverflow
# mail_script = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', script1)
# mail_script = re.findall(r'\S+@+\.+\S+', script1)
# mail_script = re.findall(r'\S+@+\.+\S+', script1)
# mail_script = re.findall(r'\w.+@.+\..+\w', script1)
f1.close()

print(mail_script)


a = '''제 이메일 주소는 greatking.22@naver.com 입니다. 오늘 저는 travel@daum.net 라는
주소로 메일을 보내려고 합니다. 저는 apple@gmail.com, life@abc.co.kr 라는 메일도 사용
하고 있습니다.'''

# b = re.findall(r'[a-z]+@[a-z]+\.[a-z]+', a)
# b = re.findall(r'[a-z]+@[a-z]+\.[a-z.]+', a)
b = re.findall(r'[\w.-_]+@[a-z]+\.[a-z.]+', a)

print(b)