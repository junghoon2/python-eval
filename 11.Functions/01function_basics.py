# 변수가 값을 바인딩 하는 것처럼 함수는 코드를 바인딩한다.

# 문법은 def 사용
def hello():
  print("Hello World")

# 호출은 (), 괄호까지 포함
hello()

def print_coin():
  print("비트코인")

print_coin()

# 호출 100번 하기
for i in range(100):
  print_coin()

# print_coin() * 100

# 함수 100번 실행하는 새로운 함수 만들기
def print_coins():
  for i in range(100):
    print("비트코인")
  

print_coins()