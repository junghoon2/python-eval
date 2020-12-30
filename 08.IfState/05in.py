# 여러 요소들 중에 있는 가를 판단하는 statement, in

# in도 되고 not in도 된다. 

# >>> 2 in [1, 2, 3]
# True
# >>> 4 in [1, 2, 3]
# False
# >>> 2 not in [1, 2, 3]
# False
# >>> 4 not in [1, 2, 3]
# True

# 주민번호로 성별 구분
id = input("주민번호 13자리를 입력해 주세요. ex) 123456-1234567: ")
id1 = id.split("-")[1]

if id1[0] in ["1", "3"]:
  print("남자") 
else:
  print("여자")

# int 변경 후 range 조건 실행

fruits = ["사과", "포도", "홍시"]
fruit = input("과일 이름을 입력하세요: ")

if fruit in fruits:
  print("정답입니다.")
else:
  print("오답입니다.")

warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
invest = input("투자 중인 종목 중 하나의 종목을 입력하세요.")

if invest in warn_investment_list:
  print("투자 경고 종목입니다.")
else:
  print("투자 경고 종목이 아닙니다.")

fruits = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
fruit = input("과일 이름을 입력하세요.: ")

# value 중 하나 출력
if fruit in fruits.values():  # 메소드 호출은 괄호 포함
  print("정답입니다.")
else:
  print("오답입니다.")