
# for 선언하기, 리스트 타입으로 변수 지정
# 반복 부문 리스트로 선언

my_list = [2, 5, 6, 10, 12]

# 반복문에 들어가는 변수는 list 타입이면 가능
price_list = [32100, 32150, 32000, 32500]
for i in price_list:
  print(i)
  
# 대괄호 가능한데, .. 연속은 안된다.
for i in {1, 3}:
# for i in {1..3}:
    print(i)

for 변수 in ["A", "B", "C"]:
  print(변수)

# for, in 
for number in my_list:
    print(number)

# range 함수
for i in range(1, 10):
    print(i)

for e in range(10, 15):
    print(e)

# import string

# print(string.ascii_lowercase[:15])

for i in ["A", "B", "C"]:
    print(i)

# print("++++")
for i in ["++++", 10, 20 ,30]:
    # print(type(i))
    print(i)
    # print("-------")

for i in range(4):
    print("-------")

for i in [100, 200, 300]:
    print(i + 10)

for i in ["김밥", "라면", "튀김"]:
    # print("오늘의 메뉴: " + i)
    print("오늘의 메뉴 : {}".format(i))


li = ["a", "b", "c", "d"]
# li = ["가", "나", "다", "라"]

# 리스트 slicing
# for i in li[1:]:
#     # if j != 0
#     # if li[j]
#     print(i)

# 0, 2 번째 list 출력
# li = li[::2]

for i in li[: :2]:
    print(i)

# 리스트 거꾸로 출력
for i in li[: : -1]:
    print(i)

# print, 쉼표, 2개 변수를 이어 붙힌다.
for 메뉴 in ["김밥", "라면", "튀김"]:
    print("오늘의 메뉴:", 메뉴)

price_list = [32100, 32150, 32000, 32500]

for i in price_list:
    print(i)

for i in range(len(price_list)):
  print(i, price_list[i])
