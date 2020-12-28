# 1 ~ 100 정수 중 짝수만 저장된 tuple 생성
# tuple은 변수 추가, append가 없잖아.

odds =()
for i in range(2, 100, 2):
  print(i)

# range 함수는 int를 하나씩 return 한다. 그 결과를 tuple 타입으로 저장 가능
data = tuple(range(2, 100, 2))
print(data)

data = list(range(2, 100, 2))
print(data)

print(range(2, 100, 2))