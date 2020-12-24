# 파일 지정
with open('data/매수종목2.txt', 'r') as f:
  lines = f.readlines()

stocks = {}

# dict element 추가하기
# data 두개로 나누고 각각 key, value로 추가
# stocks[k] = v 로 가능
for line in lines:
  line = line.strip()
  k, v = line.split()
  # stocks.append[line[0]] = line[1]
  stocks[k] = v

print(stocks)

f.close()