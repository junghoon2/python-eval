# 100 이하 자연수 중 8의 배수이지만 12의 배수는 아닌 것

# While loop문 안에 다른 if 문들 자유롭게 사용 가능
i = 1

while i <= 100:
    if i%8 == 0 and i%12 != 0:  # 8의 배수이지만 12의 배수는 아닌 것
        print(i)
    i +=1
