# 정수 n의 약수 전체 출력

# i = 1
# n = 120
# sum = 0

# while i <= n:
#     if n % i == 0:
#         print(i)
#         sum +=1
#     i +=1

# print(f"{n}의 약수는 총 {sum}개입니다.")


def div(n): 
    i = 1
    n = 120
    sum = 0

    while i <= n:
        if n % i == 0:
            print(i)
            sum +=1
        i +=1

    print(f"{n}의 약수는 총 {sum}개입니다.")

div(120)