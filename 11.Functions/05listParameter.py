# 입력을 리스트 타입으로

# 입력 리스트, 평균 출력
# parameter에 따로 type을 지정하지 않는다.
def print_score(i):
  print(sum(i) / len(i))

print_score ([1, 2, 3])

# 짝수만 출력하는 함수
# list 타입임을 감안해서 알아서 함수를 잘 설계해야 함
def print_even(numbers):
  for i in numbers:
    if i % 2 == 0:
      print(i)

print_even ([1, 3, 2, 10, 12, 11, 15])
