from random import randint

# 0~9 사이 서로 다른 Random 숫자 3개 할당
# count_num = 3

def generate_numbers():
    numbers = []
    # for i in range(count_num):
    #     if i == 0:
    #         numbers.append(randint(0, 9))
    #     else:
    #         numbers.append(randint(0, 9))
    #         for j in range(i -1):
    #             while numbers[i] == numbers[j]:
    #                 numbers[i] = randint(0, 9)

    while len(numbers) < 3:
        new_number = randint(0, 9)
        # for i in range(len(numbers)):
        if new_number not in numbers:
            numbers.append(new_number)

        # if len(numbers) == 0:
        #     numbers.append(new_number)
        # else:
        #     for i in range(len(numbers) -1):
        #         while new_number == numbers[i]:
        #             new_number = randint(0, 9)

        # numbers.append(randint(0, 9))
        # if len(numbers) >= 1:
        #     for i in range(len(numbers) - 1):


        # for i in range(1, len(numbers)):

        #     for j in range(1, i):
        #         if numbers[j] == numbers[i]:
        #             numbers[i] = randint(0, 9)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers

print(generate_numbers())