# list append 하는 방법
# 추가하고 삭제하는 방법 

a = [3, 5, 6, 0]
a.append(3)  # append는 하나만 가능하구나

print(a)

# 그럼, 2개 이상 list를 붙히려면? 합치기, join 하면 되려나? 

b = [3, 4]

# join 이라는 함수는 없나?
# print(join(a, b))  

# 리스트끼리 바로 더하기가 가능하구나 

print(a + b)

a.insert(2, 4)
print(a)

numbers = []
print(len(numbers))  # length, len 함수 사용 가능 

#numbers.append = "1"  # append 는 함수이다.
numbers.append("1")  # 함수 이므로 () 괄호로 사용 

# list 에 element 추가는 [i] 이 아니라 append 로 추가

print(numbers)

#numbers.extend("3", "5", "9")  # 복수 element 추가 할 수는 없다.

#numbers.remove("1")
numbers.remove(numbers[-1])  # index 로 삭제도 가능
numbers.append(8)
numbers.append(9)
# numbers.extend(9)

print(numbers)
