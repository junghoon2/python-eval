# String, Split
분기 = "2020/03(E) (IFRS연결)"
print(분기.split("(E"))
print(분기.split("(E")[0])

# split 타입으로 변수 지정하기
환율 = {"달러": 1167, 
        "엔": 1.096, 
        "유로": 1268, 
        "위안": 171}
user = input("입력: ")
# split 하면 순서대로 바로 지정됨
num, currency = user.split()
print(float(num) * 환율[currency], "원")


# Comma 제거 하기
# python comma  타입은 , 컴마 지원하지 않는다.
상장주식수 = "5,969,782,550"

print(int(상장주식수.replace(',', '')))

a = "hello world"
print(a.split(' '))

ticker = "btc_krw"
print(ticker.split('_'))

date = "2020-05-01"
print(date.split('-'))