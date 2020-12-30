# 사용자 입력으로 if 조건문 수행

# num = input("숫자를 입력하세요: ")
# if (int(num) % 2) == 0:  # 나머지 출력 함수
#   print("짝수")

# num = input("숫자를 입력하세요: ")
# num = int(num)
# if num >= 235:
#   num = 235

# print(num + 20)

num = input("숫자를 입력하세요: ")
num = int(num)
result = num - 20

if result < 0:
  result = 0
# else는 조건이 없나보네
# else:
#   result = 250
elif result > 255:  # else 문법
  result = 255 

print(result)
