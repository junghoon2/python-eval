# list 형태의 dictionary 타입

# value 값을 list 형태로 저장 가능
stock = {
  '시가': [100, 200, 300],
  '종가': [80, 210, 330]
}

# print는 nested 형태 가능
print(stock['시가'][0])

# 10/10	80	110	70	90
# 10/11	210	230	190	200

stock = {
  '10/10': [80, 110, 70, 90],
  '10/11': [210, 230, 190, 200]
}

