# 나머지 계산 함수
def calculate_change(payment, cost):
    # 코드를 작성하세요.
    remain = payment - cost  # 나머지 총액
    a50 = remain // 50000  # 5만원 권 수량
    print(f"50,000원 지폐: {a50}장")

    remain = remain - 50000*a50  # 5만원 권 수량 제외한 나머지 총액
    a10 = remain // 10000 # 1만원 권 수량
    print(f"10,000원 지폐: {a10}장")

    remain = remain - 10000*a10  # 1만원 권 수량 제외한 나머지 총액
    a5 = remain // 5000 # 5천원 권 수량
    print(f"5,000원 지폐: {a5}장")

    remain = remain - 5000*a5  # 5천원 권 수량 제외한 나머지 총액
    a1 = remain // 1000 # 1만원 권 수량
    print(f"1,000원 지폐: {a1}장")


# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)
