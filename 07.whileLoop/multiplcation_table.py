# 구구단 계산기

m = 1  # 구구단 첫 숫자
n = 1  # 구구단 다음 숫자

while m <= 9:
    while n <= 9:  # 9까지 곱하기
        print (f"{m} * {n} = {m * n}")        
        n += 1
    print ()  # 한바퀴 돌고 한 줄 띄우기
    n = 1  # 다음 수 넘어가기
    m +=1