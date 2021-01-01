ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

# 시가에 매수해서 종가에 매도할 경우 수익금
profits =[]
# list 합 계산

for data in ohlc[1:]:
  profits.append(data[-1] - data[0])

# sum 으로 list 원소 합 계산 가능
print(profits)
print(sum(profits))