# 대소문자 변경 프로그램

letter = input("영어 문자 하나를 입력하세요: ")
if letter.islower() :
  print(letter.upper())
elif letter.isupper():
  print(letter.lower())
else:
  print("정확히 하나의 영어 문자를 입력해 주세요")
