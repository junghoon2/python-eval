# 짝수이면 True, 홀수이면 False
# def is_evenly_divisible(number):
#     # 코드를 작성하세요
#     return(not bool(number % 2))

def is_evenly_divisible(number):
    # 코드를 작성하세요
    return(number%2 == 0)


# print(bool(4 % 2)) 

# print(not True)  # True 를 False 로 변환하는 방법은?
# print(!  True)  # ! 로 True, False 변경 안 된다. 


# 테스트
print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))
print(is_evenly_divisible(218))
print(is_evenly_divisible(317))