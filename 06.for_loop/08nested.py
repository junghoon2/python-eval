# print nested list

apart = [ [101, 102], [201, 202], [301, 302] ]

# 중첩 리스트를 전부 프린트 하려면 중복 for 문 사용하면 되겠지
for i in range(len(apart)):
  for j in range(len(apart[0])):
    print(apart[i][j], '호')

for row in apart:
    for col in row:
        print(col, "호")
        print('-'*4)

for row in apart:
  for col in row:
    print(col, "호")
  print('-'*5)

# 각 element 수수료 포함한 가격 출력
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

for row in data:
  for col in row:
    print(round(float(col)*(1.00014)))
  print('-'*4)

# nested list 선언
# 리스트를 만들고 조건으로 nested로 추가한다.
result = []

# result[0] = data[0]
# result[1] = data[1]
# result[2] = data[2]

# print(result)

for i in range(len(data)):
# 빈 list column 만드는 게 이해가 안되네
  result.append([])
  for row in data[i]:
    result[i].append(row * 1.00014)

print(result)

# list의 마지막 element 출력, 종가 데이터 출력
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for i in range(1, len(ohlc)):
    print(ohlc[i][-1])

# list 둘째행 부터 출력, [1:]
for row in ohlc[1:]:
# row[3], 특이하네
# list 형태인 경우 [], index 지정 가능
    print(row[3])

for row in ohlc[1]:
    print(row)

# 새로운 게 나오면 외우려 하지 말고,
# 멈추어 서서(설사 이해가 되지 않는다고 해도) 충분히 생각해 본다.