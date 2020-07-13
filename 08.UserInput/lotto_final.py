# 1~45 중 6개의 숫자 무작위로 뽑고 정렬하기
from random import randint

numbers = []  # initial, num list이니 numbers로

# argument 만큼 random 정수 생성
def generate_numbers(n):
    for i in range(n):  
        # a = randint(1, 45)  # 1~45까지 중 random number 할당 
        # a는 의미 없는 숫자이니 사용 안하는 게 낫다
        num = randint(1, 45)
        
        # 중복 숫자 안 나올때까지 다시 생성
        while num in numbers:
            num = randint(1, 45) 
        numbers.append(num)  # num list 에 random 숫자 추가
    numbers.sort()
    return numbers  

# print(generate_numbers(6))

def draw_winning_numbers():
    winning_numbers = generate_numbers(6)  # numbers 6 할당
    # 중복 아닌 채로 7개의 숫자 할당
    while len(winning_numbers) < 7:
        num = randint(1, 45)
        if num not in winning_numbers:  # 기존 numbers와 중복 금지
            winning_numbers.append(num)
    return winning_numbers

numbers = generate_numbers(6)
winning_numbers = draw_winning_numbers()

def count_matching_numbers(numbers, winning_numbers):
    count = 0

    for num in numbers:
        if num in winning_numbers:
            count = count + 1

    return count


# def check(numbers, winning_numbers):
#     count_gen = count_matching_numbers(numbers, winning_numbers[:6])  # 일반 번호 로또 일치한 숫자 횟수

#     if count_gen == 6:  # python 은 case class 사용 안하나?
#         return 1000000000
#     elif count_gen == 5:  # 특수 번호 포함한 2등 당첨 번호 분리
#         count_special = count_matching_numbers(numbers, winning_numbers)  # 특수 번호 포함하여 일치한 숫자 횟수
#         if count_special == 6:
#             return 50000000
#         else:
#             return 1000000
#     elif count_gen == 4:
#         return 50000
#     elif count_gen == 3:
#         return 5000
#     else:
#         return 0

def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0

print(check(numbers, winning_numbers))