# def hello(name, age):
#   print("Hello " + name) # 변수 호출 하는 방법은? script 처럼 $ 이런 건 쓰지 않는 것 같고
#   # + 하면 되나
#   # print 함수에서 + 를 사용하려면 양쪽의 변수 타입이 동일히야 한다. 
#   # "Hello" + 20 은 에러 
#   print("Welcome")

#   print("Hi" + " world again")
#   print(name) # print 로 문자열을 받으면 그걸 출력한다. 
#   print(age + 10) # age 를 자동으로 integer로 받아들이네 

# hello("jerry", 44)

# # string 으로 받네
# def 함수(문자열) :
#     print(문자열)

# 함수("안녕")
# 함수("Hi")
# 함수(10)

# # parameter를 변환 또는 지정 가능하겠지

# def print_with_smile(s) :
#   print(s + ":D")
#   print(s, ":D")

# print_with_smile("Jerry") 

# # 상환가 출력 함수
# def print_upper_price(price):
#   print(price * 1.3)

# # 2개의 입력값 합하는 함수
# # 그냥 내장 함수 sum 사용하면 되지
# def print_sum(i, j):
#   print(i + j)

# print_sum(9, 3)

# print(3/4)

# # 합, 차, 곱, 나눗셈 함수 
def print_arithmetic_operation(i, j):
  print("{} + {} = {}".format(i, j, i+j))
  print("{} - {} = {}".format(i, j, i-j))
  print("{} * {} = {}".format(i, j, i*j))
  print("{} / {} = {}".format(i, j, i/j))
# 이게 더 깔끔하기도 한 것 같고
  print(f"{i} / {j} = {i/j}")

print_arithmetic_operation(3, 4)

# 사칙 연산 함수, 2개 수 입력 받아서 사칙 연산 결과 프린트
def arith(a, b):
  print(a+b, a-b, a*b, round(a/b, 1))

num_a =int(input('첫번째 숫자를 입력하세요: '))
num_b =int(input('두번째 숫자를 입력하세요: '))

arith(num_a, num_b)
