# 숫자형 변수 선언하기 & 사용하기 

# integer & float type 변수 사용 
n = 4
m = 3.0  # 소수점만 붙히면 쉽게 float 타입으로 가능

# number 바로 변수 지정 가능
# 숫자 지정 후 쉼표 사용은 안 됨

# 한글로 변수 지정 가능
삼성전자 = 50000
print(삼성전자 * 10)

# int는 [], index 지정 안된다.
# 삼성전자[0]

시가총액 = 298000000000000
현재가 = 50000
PER = 15.79

print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))

print(2 + 2 * 3)

x = 254
y = 355

# int, float, str 등으로 변수 타입 변환 가능
# 변수 타입 변환 후 사칙 연산 등 가능
print(type(x))
print(str(x))

num_str = "720"
print(int(num_str))

num = 100
result = str(num)

# type으로 변수 타입 확인 가능
print(result, type(result))

print(n + m)
print(n / m)
print(n % m)

print(x)
print(x + x*2)

a = 3
b = 3.0
c = -6.2 

print(a + b)
print(a * c)

print(a ** 2)
print(a % 2)

print(7 // 2) # 버림 나눗셈 
print(7.0 // 2) # 버림 나눗셈 
print(7 / 2) # 나누기
print(8 % 3) # 나머지

# round 반올림
print(round(3.14592))
print(round(3.6787, 2))

st = "15.79"
num = float(st)
print(num + 100, type(num))

year = "2000"
year = int(year)
print(year - 2, year - 1, year)

price = 48584
total_price = price * 36
print(total_price)