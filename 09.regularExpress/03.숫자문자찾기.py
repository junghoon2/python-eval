import re

example = '저는 77년 태어났습니다. 88사년 올림픽, 2002년 월드컵이 있었습니다.'

# 연도만 출력하기
print(re.findall(r'\d.+년', example))
print(re.findall(r'\d.+?년', example))
print(re.findall(r'\d+.년', example))