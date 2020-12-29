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
