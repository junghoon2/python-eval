# String 타입으로 변수 지정, "" 사용하면 된다.
id = "821010-1635210"


# - 특수 기호만 제외하기
id_1st = id.split("-")[0]
id_2nd = id.split("-")[1]

print(id_1st)
print(id_2nd)

# string 합치기
id = id_1st + id_2nd[:-2]
print(id)

# tuple 형태 변수 할당
# 쉼표 형태로 변수 할당 가능(신기하군)
check = 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5
print(check)

# 곱한 수 변수 할당
multi = []
# 리스트 개별 element 합치기
sum = 0

for i in range(len(id)):
  # id{}.format(i+1) = int(id_1st[i]) 
  # id{}.format(i+1) = id_1st[i]
  # print(id)
  # multi.append = int(id[i]) * int(check[i])
  # append는 해당 element 추가한다
  multi.append(int(id[i]) * int(check[i]))
  sum += multi[i]

# list 개별 element끼리 합하기
# sum = 0
# for i in range(len(multi)):
#   sum += multi[i]

print(sum)
