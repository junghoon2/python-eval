# 내장 함수
print("ahk")
print("as'd'f")
print('as"d"f')

# 외장 함수 선언하는 방법은?
# a = 4
# b = 8

#func_a = (a * b)

# 함수 정의하는 법
def func_a(a, b): # 함수의 첫 줄을 헤더라고 한다.
  # 인자 정의
  print(8 * a * b)
  print("Hello world Func")
  print(max(a, b))

# 함수를 print 인자로 가능할까?
# 함수 안에 print, 출력 함수를 포함해야 하네
func_a(3, 2)
func_a(1, 6)
func_a(7, 4)

# 코드를 작성하세요. 
def cafe_mocha_recipe():
    print("준비된 컵에 초코 소스를 넣는다.")
    print("에스프레스를 추출하고 잔에 부어 준다.")
    print("초코 소스와 커피를 잘 섞어 준다.")
    print("거품기로 우유 거품을 내고, 잔에 부어 준다.")
    print("생크림을 얹어 준다.")
# 테스트 코드
cafe_mocha_recipe()