# 우편번호로 해당하는 구 출력
postal_code = input("우편번호를 입력하세요: ")
digit3 = postal_code[:3]

# 3개 조건을 하나의 문장으로 지정 가능할건데
# if digit3 == "010" or digit3 == "011" or digit3 == "012":
if digit3 in ["010", "011", "012"]:
  print("강북구")

# And 조건 지정
my_time = input("아래 형식으로 현재 시간을 입력하세요. \n ex) 05:40 ")
# AND 조건 지정하기
# if my_time[-1] == str(0) and my_time[-2] == str(0):
if my_time[-1] == "0" and my_time[-2] == "0":
# if my_time[-2:] == str(00):
# if my_time[-2:] == "00": # string type 지정은 " " 따옴표 사용한다. 
  print("정각 입니다.")
else:
  print("정각이 아닙니다.") 

# 괄호 사용 가능
# if 0 <= int(뒷자리[1:3]) <= 8:
#     print("서울입니다.")

# 3개 숫자 중 가장 큰 숫자 출력
def print_max(i, j, k):
  if i >= j and i >= k:
    print(i)
  elif j >= k:
    print(j)
  else:
    print(k)

print_max(3, 4, 5)
