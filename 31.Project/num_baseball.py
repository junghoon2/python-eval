# 숫자 야구 게임
from random import randint

# 정답 숫자 random 생성
ans_numbers = []
my_numbers = []
num_count = 3  # 야구 게임 자리 수 입력

# random 숫자 할당
for i in range(num_count):
    ans_numbers.append(randint(0, 9))  
    
# 왜 num[0] = 1 하면 에러 발생할까? 기존 element 변경은 되지만 추가는 안된다. 

# 중복 숫자 제거
# 3자리가 아니라 10자리면 이렇게 코드 짜면 안 될텐데 
while ans_numbers[1] == ans_numbers[0]:  # 2번째 숫자 중복 제거
    ans_numbers[1] = randint(0, 9)

while ans_numbers[2] == ans_numbers[0] or ans_numbers[2] == ans_numbers[1]:
    ans_numbers[2] = randint(0, 9)

print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.")
print("숫자 3개를 하나씩 차례대로 입력하세요.")

# 0 ~ 9 범위에 맞고 중복되지 않게 숫자 입력
for i in range(num_count):  # list type으로 변수 할당
    my_numbers.append(int(input(f"{i+1}번째 숫자를 입력하세요: ")))
    if my_numbers[i] < 0 or my_numbers[i] > 9:
        print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        my_numbers[i] = int(input(f"{i+1}번째 숫자를 입력하세요: "))

    if i == 0:
        continue
    elif i == 1:
        while my_numbers[1] == my_numbers[0]:  # 2번째 숫자 중복 제거
            print("중복되는 숫자 입니다. 다시 입력하세요.")
            my_numbers[1] = int(input("2번째 숫자를 입력하세요: "))
    elif i == 2:
        while my_numbers[2] == my_numbers[0] or my_numbers[2] == my_numbers[1]:  # 2번째 숫자 중복 제거
            print("중복되는 숫자 입니다. 다시 입력하세요.")
            my_numbers[2] = int(input("3번째 숫자를 입력하세요: "))

# 0 ~ 9 사이의 숫자 입력
# for i in range(num_count):

# 중복 숫자 제거

print(ans_numbers)
print(my_numbers)

# Strike, ball, try 횟수 변수 
s_count = 0
b_count = 0
try_count = 0  

for i in range(num_count):
    if my_numbers[i] == ans_numbers[i]:
        s_count += 1
    elif my_numbers[i] in ans_numbers:
        b_count += 1
    try_count += 1

