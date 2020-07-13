# Fibonacchi Sequence code
i = 1  # 1씩 증가
previous = 1  # 1번째 전 변수
pre_previous = 1  # 2번째 전 변수

print(pre_previous)
print(previous)

while i <= 48:  # 앞에 2번 이미 출력 했으니 50번 중 2번 제외한다.
    # 우리가 반복적으로 무엇을 해야 할까요?
    current = previous + pre_previous  # 먼저 합    
    print(current) 
    pre_previous = previous  # 하나씩 뒤로 저장 
    previous = current    
    i += 1