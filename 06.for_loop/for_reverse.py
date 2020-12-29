numbers = [2, 3, 5, 7, 11, 13, 17, 19]
numbers = [2, 3]
# 리스트 뒤집기
# 코드를 입력하세요.

print(len(numbers))

print(numbers[-2])

temp = []

print(numbers[-1])

temp.append(numbers[-1])
# temp[1] = numbers[-2]

# print(temp)

for i in range(len(numbers)):
    # print(i)
   temp.append(numbers[-(i + 1)])

numbers = temp

print("뒤집어진 리스트: " + str(numbers))