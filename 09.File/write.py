# 파일에 내용 쓰기

# 파일 지정
# open, a, write 
# with open("data/매수종목1.txt", "a") as f:
#     f.write("005930\n")  # 줄 바꿈 필요
#     f.write("005380\n")  # 줄 바꿈 필요
#     f.write("035420\n")  # 줄 바꿈 필요

with open("data/매수종목2.txt", "a") as f:
    f.write("005930 삼성전자\n")
    f.write("005380 현대차\n") 
    f.write("035420 NAVER\n")
    f.close()
