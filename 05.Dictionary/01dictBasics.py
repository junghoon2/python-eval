# dictionary basics

# key-value 형태로 선언, 순서가 없을 듯 
# version 3.6부터 key가 ordered 지원

# 선언하기: Curly brace 사용 
my_dict = {
    5: 25,
    2: 4,
    4: 9
}

temp = {}
print(temp)


ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

# Element 삭제
ice.pop('메로나')
print(ice)

# pop, del 두가지 가능
# list에 가능한 remove는 안되네
del ice['폴로포']
print(ice)

# ice.remove(0)

# pop index로 안되네
ice.pop(0)
print(ice)


# index, 호출하기는 list와 거의 동일하네 
print(my_dict[4])

# 리스트로 key, value 저장 가능
my_dict[9] = 81

print(my_dict)

# value로 리스트, nested dict 다 가질 수 있네 
my_dict = {
    "엄마": [25, 43, 43],
    "아빠": {"사람": 4, "인간": 9},
    "누나": 9
}

print(my_dict)
# print(my_dict["아빠"[1]])
print(my_dict["아빠"])

# 지우려면? 
# 전체 지우기, 부문 지우기
# my_dict.clear("엄마")

my_dict.clear()
print(my_dict)

# 부문 지우기, remove가 아니라 pop 사용, list에서도 동일
my_dict = {
    "엄마": [25, 43, 43],
    "아빠": {"사람": 4, "인간": 9},
    "누나": 9
}

my_dict.pop("아빠")
print(my_dict)