# elif 구간 사이 검증

score = input("점수를 입력하세요: ")
score = int(score)

if score > 80 :
    print("A")
elif score < 81 and score > 60:
    print("B")
elif score < 61 and score > 40:
    print("C")
elif score < 41 and score > 20:
    print("D")
elif score < 21 and score > 0:
    print("E")

# 외화 금액 출력
fmoney = input("외화 금액을 입력하세요: ")
money = int(fmoney.split(' ')[0])
exchange = fmoney.split(' ')[1]

if exchange == "달러":
    print(int(money * 1167), "원")
elif exchange == "엔":
    print(int(money * 1.096), "원")
elif exchange == "유로":
    print(int(money * 1268), "원")
elif exchange == "위안":
    print(int(money * 171), "원")



# grade 출력
def print_grade(midterm_score, final_score):
    total = midterm_score + final_score
    # 코드를 쓰세요.
    if total >= 90:
        print("A")  
    # indentation 4개를 지켜야 한다? 
    elif total >= 80:
        print("B")
    elif total >= 70:
        print("C")
    elif total >= 60:
        print("D")
    # else:
    #     print("F")

# 테스트
print_grade(40, 45)
print_grade(30, 32)
print_grade(50, 45)

# Else 조건이 없으면 그냥 실행되지 않는다.
print_grade(20, 35)
