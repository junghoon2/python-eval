import re

sentence = 'i really love dog. 진짜냐? 아닌 것 같은데. 아무튼!!! 이걸 대체해 보자.'

# 실제 변경해서 저장하려면 한번 더 변수 적어준다.
sentence = re.sub(r'\?', 'bread', sentence)

print(sentence)

# 문장 기호 .?! 단위로 나눈다. 
# print(re.split(r'[.?!]', sentence))
split_sentence = re.split(r'[.?!]', sentence)

# 문자 시작이 공백으로 되어 있는 것의 공백 지우기
print(split_sentence)
# print(re.sub(r'\s', '', split_sentence))

