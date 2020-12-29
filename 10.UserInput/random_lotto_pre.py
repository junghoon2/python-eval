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


def draw_winning_numbers():
    generate_numbers(6)  # numbers 6 할당
    # 중복 아닌 채로 7개의 숫자 할당
    while len(numbers) < 7:
        num = randint(1, 45)
        if num not in numbers:  # 기존 numbers와 중복 금지
            numbers.append(num)
    return numbers

print(draw_winning_numbers())
