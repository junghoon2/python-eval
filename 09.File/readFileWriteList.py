# 파일 읽어서 line 단위로 변수로 저장

# file 읽어 들이기

# with는 머지? as는?
with open('data/매수종목1.txt', 'r') as f: 
    lines = f.readlines()

# 저장할 list type 변수 지정
stocks = []
    # stocks.append(f.readlines)

# line 하나하나 단위로 저장
for line in lines:
    code = line.strip()
    stocks.append(code)

print(stocks)

f.close()