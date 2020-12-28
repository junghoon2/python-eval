# slicing, 리스트 변수를 부문으로 자르는 방법

price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# 2씩 증가, 짝수만 출력
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])
print(nums[1::2])

# 리스트 숫자 역방향 출력
print(nums[::-1])

# 역방향도 2씩 가능할까?
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[::-2])
print(interest[::2])

# 리스트가 아닌 string type 출력은 index 지정
print(interest[0], interest[2])

a = [4, 6, 9, 12, 4]
print(a[3:])
print(a[-1])
