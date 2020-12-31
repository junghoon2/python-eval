# for 반복문 안에서 if 문 사용

리스트 = [3, -20, -3, 44]

for i in 리스트:
  if i < 0:
    print(i)

# 3의 배수만 출력
리스트 = [3, 100, 23, 44]

# % 나머지
for i in 리스트:
  if i % 3 == 0:
    print("3의 배수", i)

# 20보다 작은 3의 배수
# AND 조건
리스트 = [13, 21, 12, 14, 30, 18]

for i in 리스트:
  if i % 3 ==0 and i < 20:
    print(i)

# 3글자 이상만 출력
리스트 = ["I", "study", "python", "language", "!"]
for i in 리스트:
  if len(i) > 5:
    print(i) 

# 대문자만 출력
리스트 = ["A", "b", "c", "D"]
