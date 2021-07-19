# # 변수가 값을 바인딩 하는 것처럼 함수는 코드를 바인딩한다.

# # 문법은 def 사용
# def hello():
#   print("Hello World")

# # 호출은 (), 괄호까지 포함
# hello()

# def print_coin():
#   print("비트코인")

# print_coin()

# # 호출 100번 하기
# for i in range(100):
#   print_coin()

# # print_coin() * 100

# # 함수 100번 실행하는 새로운 함수 만들기
# def print_coins():
#   for i in range(100):
#     print("비트코인")
  

# print_coins()

# 사칙 연산 함수, 2개 수 입력 받아서 사칙 연산 결과 프린트
def arith(a, b):
  print(a+b, a-b, a*b, round(a/b, 1))

num_a =int(input('첫번째 숫자를 입력하세요: '))
num_b =int(input('두번째 숫자를 입력하세요: '))

arith(num_a, num_b)
