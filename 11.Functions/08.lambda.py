add = lambda x: 3 * x  
# lambda 사용하면 한 줄로 함수 만들 수 있다.
# 하지만 가독성이 떨어져서 잘 안 쓴다. 
 
print(add(3))

# 환율 계산기
dollar = lambda won: won * 0.00086
won = lambda dollar: dollar * 1170

print(dollar(100000))
print(won(86))