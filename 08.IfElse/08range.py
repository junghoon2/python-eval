# 주민번호로 성별 구분
id = input("주민번호 13자리를 입력해 주세요. ex) 123456-1234567: ")
id1 = id.split("-")[1]

if int(id1[1:3]) in range(9):
  print(int(id1[1:2]))
  print("서울 입니다.")
else:
  print("서울이 아닙니다.")

