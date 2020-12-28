# 문자열은 list 타입으로 저장되어, slicing 가능하다.

# 문자열은 immutable, 왜 그럴까?
lang = 'python'
# lang[0] = 'P'
print(lang)

#문자열 합치기, 곱하기
a = "3"
b = "4"
print(a + b)

# 곱하기는 공백 없이 붙힌다.
print("Hi" * 3)
print("-" * 80)

t1 = 'python'
t2 = 'java'
t3 = t1 + ' ' + t2 + ' '
print(t3 * 4)

