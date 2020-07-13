# Generate Lotto Number, 보너스 번호 1개 
from random import randint

lotto_numbers = []
my_numbers = []

def generate_numbers():
    lotto_numbers = []
    while len(lotto_numbers) < 7:  # 7개 숫자 할당
        new_number = randint(1, 45)  # 1 ~ 45까지 임의 숫자 할당
        if new_number not in lotto_numbers:  # 중복 숫자 제거
            lotto_numbers.append(new_number)  
    
    # 6번째까지 일반 숫자 Sorting, 7번째 보너스 숫자 할당
    lotto_numbers = sorted(lotto_numbers[:6]) + lotto_numbers[6:] 
    return lotto_numbers

# 내 로또 번호 생성
def my_lotto_numbers():
    my_numbers = []

    for i in range(1, 7):
        num = int(input(f"1 ~ 45 사이의 숫자 중 {i}번째 로또 숫자를 입력하십시요: "))
        if num in my_numbers:
            print("중복되지 않는 숫자를 입력하여 주십시요.")
        elif num < 0 or num > 45:
            print("0 ~ 45 사이의 숫자를 입력하여 주십시요.")
        elif num not in my_numbers and 0 <= num and num <= 45:
            my_numbers.append(num)
            i += 1

    return sorted(my_numbers)

print("로또 번호가 생성 되었습니다.")
print(generate_numbers())

print("나의 로또 번호를 입력 하세요.")
print(my_lotto_numbers())

# 일치하는 번호 Count
def count_numbers():
    count = 0
    for num in my_numbers:
        if num in lotto_numbers:
            count += 1
    return count

print(count_numbers())