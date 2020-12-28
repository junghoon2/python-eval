# String, Split
분기 = "2020/03(E) (IFRS연결)"
print(분기.split("(E"))
print(분기.split("(E")[0])

# Comma 제거 하기
# python comma  타입은 , 컴마 지원하지 않는다.
상장주식수 = "5,969,782,550"

print(int(상장주식수.replace(',', '')))
