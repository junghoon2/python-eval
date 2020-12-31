numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

#for i in numbers:
for j in range(len(numbers)):
    print(f"{j} {numbers[j]}")

for i in range(4, 0, -1):  # range 를 거꾸로 하는 방법은?
    print(i)

# range 함수는 0부터 시작하여, 마지막 숫자는 제외하고 출력
for i in range(100):
  print(i)

# 시작은 포함하고 마지막은 제외되고
for i in range(2002, 2051, 4):
  print(i)

# 3의 배수 출력
for i in range(3, 31, 3):
  print(i)

# 숫자 감소, -1 은 하나씩 내려간다
# -1, 마이너스 숫자 가능
for i in range(99, -1, -1):
  print(i)

# 소수점도 가능? int 타입만 가능
for i in range(10):
  print(i / 10)

# 구구단 출력, 2
for i in range(1, 10, 2):
  print("3 x", i, "=", 3*i)

# 거꾸로 출력
# range, -1 가능
price_list = [32100, 32150, 32000, 32500]

for i in range(3, -1, -1):
  print(i, price_list[i])

for i in range(1, len(price_list)):
  print(90 + i*10, price_list[i])

my_list = ["a", "b", "c", "d"]
print(my_list[3])

for i in range(3):
  print(my_list[i], my_list[i+1])

for i in range( len(my_list) - 1 ) :
  print(my_list[i], my_list[i+1])

my_list = ["a", "b", "c", "d", "e"]
for i in range( len(my_list) -2 ):
  print(my_list[i], my_list[i+1], my_list[i+2])

# 우측 값과의 차이값 출력
my_list = [100, 200, 400, 800]

# range 함수도 마지막 index는 제외하고 출력
for i in range(len(my_list) -1):
  print(my_list[i+1] - my_list[i])

