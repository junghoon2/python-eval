numbers = [3, 4, 5, 6, 8, 9]

# del로 index 기준으로 삭제
del numbers[3]  # del 은 function 이 아니네 
print(numbers)

# remove는 object 내용으로 삭제
numbers.remove(4)
print(numbers)

