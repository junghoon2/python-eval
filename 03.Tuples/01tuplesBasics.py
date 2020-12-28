# Tuple type 선언하기
# 순서는 있지만 수정이 불가능한 변수 type

# { }는 set라고 한다.. 
# a = {3, 45, 8}  

# tuple은 ( ), 괄호 사용한다. 
# 제일 많이 사용하는 (), 괄호를 사용하네.
a = (3, 4)
b = [3, 4, 55]

print(type(a))
print(a)

# immutable 하다
# a.

# b같은 list에서 지원하는 append, remove 등 다양한 메소드들을 지원하지 않는다.
# b.

my_tuple =()
print(my_tuple)

movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
print(movie_rank)

# 하나의 데이터를 저장하는 경우 튜플로 인식하지 않는다. 왜 그럴까? 
my_tuple =(1)
print(my_tuple)

my_tuple =(1, )
print(my_tuple)

t = (1, 2, 3)
# 수정이 불가능한 tuple type
# t[0] = 'a'
print(t[0])

# 아무런 타입 정의 없이 나열하는 걸로 변수 지정이 가능하나?
t = 1, 2, 3, 4
# 괄호 없어도 tuple로 저장하네. default 인가? 사용자 편의를 위해 가능하다?
print(t)
print(type(t))
print(t[2])

# 수정이 불가능한 tuple을 수정하는 방법은?
# 기존 변수 저장 안되고 새로운 변수 만들어야 한다.
t = ('a', 'b', 'c')
# t[0] = 'A' 안 됨
t = ('A', 'b', 'c')

# upper 등이 가능한가, upper는 string type에 적용된다.
print(t[0].upper())

# tuple을 리스트로 변환
# 쉽게 변환 가능하네.
interest = ('삼성전자', 'LG전자', 'SK Hynix')
print(list(interest))

# list to tuple 변환
interest = ['삼성전자', 'LG전자', 'SK Hynix']
print(tuple(interest))

# 희안하네. 
temp = ('apple', 'banana', 'cake')
# 쉼표로 변수 지정 가능?
a, b, c = temp
print(a, b, c)
