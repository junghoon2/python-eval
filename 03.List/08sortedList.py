# 리스트 element 정렬하기

# sorted, sort 2가지 
data = [2, 4, 3, 1, 5, 10, 9]
print(sorted(data))

# 오름차순, 내림차순 정리
numbers = [3, 6, 9, 1, 5, 5, 9]
n = sorted(numbers)
n1 = sorted(numbers, reverse=True)

print(numbers)  # numbers 자체를 sorting 하지는 않는다.
print(n1)

# sort()는 변수 자체를 변경한다.
print(numbers.sort())  # numbers가 sorted로 변경된다.
print(numbers)

print(numbers.sort(reverse=True))
print(numbers)
