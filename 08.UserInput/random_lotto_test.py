# 1~45 중 6개의 숫자 무작위로 뽑기
from random import randint

num = []  # initial

def generate_numbers(n):
    for i in range(n):  # 중복 숫자 제거
        # 중복 숫자 제거
        a = randint(1, 45)  # random number 할당 
        while a in num:
            a = randint(1, 45) 
        num.append(a)  # num list 추가
    num.sort()
    return num  # sorting 

generate_numbers(7)
#print(num[:6])
num = sorted(num[:6]) + num[6:]

print(num)