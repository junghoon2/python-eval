# 변수를 선언하고 사용하는 방법

# 변수 선언은 간단히 이름 쓰고 = 등호 사용해서 할당만 하면 된다.
my_var="Hello"

# 사용하려면 따옴표 등 없이 이름만 명시하면 된다.
print(my_var)

# 쉼표 형태로 변수 할당 가능(신기하군)
check = 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5
print(check)
print(check[4])

#burger_a=4600 # 띄워쓰기 없이 붙히는 게 권장일까?
burger_a = 4600 # 수학 등호가 아니라, 지정 연산자. 
burger_b=5600

drink = 3400

print(burger_a + burger_b)
print(burger_a * 2 + drink)