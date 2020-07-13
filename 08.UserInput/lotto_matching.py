# 두 리스트 간 공통인 element 숫자 합 return
# def count_matching_numbers(list_1, list_2):
#     sum = 0  # 겹치는 숫자, 횟수는 이제 count 라고 변수 지정
#     # count = 0
#     for e in list_1:
#         for f in list_2:
#             if e == f:
#                 sum +=1
#     return sum  

def count_matching_numbers(numbers, winning_numbers):
    count = 0

    for num in numbers:
        if num in winning_numbers:
            count = count + 1

    return count

# list 함수 자체에서 두 list 겹치는 element 찾는 함수는 없는 듯 

list_1 = [3, 4, 6, 7, 8]
list_2 = [1, 8]

print(count_matching_numbers(list_1, list_2))
