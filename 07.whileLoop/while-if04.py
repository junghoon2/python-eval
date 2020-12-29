money = 50000000  # 바둑 대회 상금
year = 1988  # 해당 연도
rate = 1.12  # 은행 이자
apart_price = 1100000000  # 2016년 아파트 가격

while year <= 2015: # 2015년까지 12% 이자로 은행 예치
    money *= rate # 매년 복리로 계산
    year +=1

if money > apart_price:
    diff_a = money - apart_price # 아파트 가격과 차이
    print(f"{diff_a:.0f}원 차이로 동일 아저씨 말씀이 맞습니다.")
else:
    diff_b = apart_price - money
    print(f"{diff_b:.0f}원 차이로 미란 아주머니 말씀이 맞습니다.")