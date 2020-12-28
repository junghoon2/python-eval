# 리스트 합 출력하기
nums = [1, 2, 3, 4, 5]
print(sum(nums))


# 자리수 합 리턴
#a = 0  # 초기 값
def sum_digit(num):
    # 코드를 입력하세요.
    a = 0
    str_num = str(num)  # int 를 string 으로 변환
    for i in range(len(str_num)):  # 숫자 자리수 만큼 반복
        a += int(str_num[i])
    return(a)

num = 32
print(sum_digit(num))

#print(a)


# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
# 코드를 입력하세요.
total = 0
for i in range(1, 1001):
    total += sum_digit(i)

print(total)