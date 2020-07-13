numbers = [3, 6, 9, 1, 5, 5, 9]
n = sorted(numbers)
n1 = sorted(numbers, reverse=True)

print(numbers)  # numbers 자체를 sorting 하지는 않는다.
print(n1)

print(numbers.sort())  # numbers가 sorted로 변경된다.
print(numbers)

print(numbers.sort(reverse=True))
print(numbers)
