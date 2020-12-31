# list, indexing
# index는 0부터 시작해서 하나 더 추가
my_list = ["a", "b", "c", "d"]
print(my_list[3])

for i in range( len(my_list)-1, 0, -1):
  print(my_list[i], my_list[i-1])

# 2개 변수 간 차이 출력
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

for i in range(len(low_prices)):
  print(high_prices[i] - low_prices[i])
  