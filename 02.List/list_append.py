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