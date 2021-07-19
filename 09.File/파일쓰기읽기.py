import os

print(os.getcwd())

f = open('test.txt', 'w')

f.write('파일쓰기 테스트')

# 파일 삭제는?
# os.remove('./test.txt')

# 파일 이동 이런 거도 있겠군

f.close()

# read는 파일 위치를 인자로 가지지 않네
with open('./test.txt', 'r') as f:
  data = f.read()
  print(data)

# with로 열면 매번 close 하지 않아도 된다. 
# f.close()

with open("data/매수종목2.txt", "a") as f:
    f.write("005930 삼성전자\n")
    f.write("005380 현대차\n") 
    f.write("035420 NAVER\n")
    # f.close()
