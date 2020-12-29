numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
# 코드를 입력하세요.
temp = []

for i in range(len(numbers)):
    # print(i)
   temp.append(numbers[-(i + 1)])

numbers = temp
print("뒤집어진 리스트: " + str(numbers))
#numbers.extend()
numbers.insert()
