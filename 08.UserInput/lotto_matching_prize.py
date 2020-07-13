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

print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))

