import re

example = '저는 77년 태어났습니다. 88사년 올림픽, 2002년 월드컵이 있었습니다.'

# 연도만 출력하기
# print(re.findall(r'\d.+년', example))
# print(re.findall(r'\d.+?년', example))
# print(re.findall(r'\d+.년', example))

# 언제 탐욕수러운 결과가 나오지?
print(re.findall(r'\d+년', example))

# a로 시작하는 문자 찾기
words = ['apple', 'cat', 'brave', 'drama', 'arise', 'blow', 'coat', 'above', 'a', 'a100']

# \D for 숫자가 아닌 것
for i in words:
  m = re.match(r'a\D+', i)
  if m:
    print(i)
  
# 문자 단위로 짜르기
d = 'I have a dog. I am not a girl. You are not alone. I am happy. '

# split_sentence = re.findall(r'[A-Z]+.\.', d)
# split_sentence = re.findall(r'[A-Z].+\.', d)
split_sentence = re.split(r'\.', d)

print(split_sentence)