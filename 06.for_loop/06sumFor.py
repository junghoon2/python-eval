# for 반복문 각 element 출력
sum = 0
for i in range(1, 11):
  sum += i

print(sum)

sum = 0
num = []

for i in range(1, 11):
  num.append(i)

print(len(num))

for i in range(int(len(num) / 2) + 1):
  sum += num[i] + num[-i]

print(sum)

# 홀수 합만 출력
sum = 0
for i in range(1, 11, 2):
  sum += i

print(sum)

# 곱한 값 출력
multi = 1
for i in range(1, 11):
  multi = multi * i

print(multi)

result = 1
for i in range(1, 11) :
    result *= i
print(result)
