from random import randint

# test = []

# # for i in range(3):
# #     test[i] = randint(0, 9)


# test.append(randint(0, 9))
# print(test)

# test[0] = 3

# print(test)

num_count = 3
my_numbers = []

for i in range(num_count):  # list type으로 변수 할당
    my_numbers.append(int(input(f"{i+1}번째 숫자를 입력하세요: ")))
    print(type(my_numbers[i]))
    if my_numbers[i] < 0 or my_numbers[i] > 9:
        print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        my_numbers[i] = input(f"{i+1}번째 숫자를 입력하세요: ")
