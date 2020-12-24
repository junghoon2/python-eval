
# for 선언하기
# 반복 부문 리스트로 선언

my_list = [2, 5, 6, 10, 12]

# for, in 
for number in my_list:
    print(number)

# range 함수
for i in range(1, 10):
    print(i)

for e in range(10, 15):
    print(e)

# import string

# print(string.ascii_lowercase[:15])

for i in ["A", "B", "C"]:
    print(i)

# print("++++")
for i in ["++++", 10, 20 ,30]:
    # print(type(i))
    print(i)
    # print("-------")

for i in range(4):
    print("-------")

for i in [100, 200, 300]:
    print(i + 10)

for i in ["김밥", "라면", "튀김"]:
    # print("오늘의 메뉴: " + i)
    print("오늘의 메뉴 : {}".format(i))

# 문자열 길이 출력
for i in ["SK하이닉스", "삼성전자", "LG전자"]:
    print(len(i))

# 문자와 문자열 길이 같이 출력
for i in ["dog", "cat", "parrot"]:
    print(i + ' ' + str(len(i)))

# 숫자를 문자열로 변환 후 출력 
# 숫자 문자 이어붙혀서 출력
for i in [1, 2, 3]:
    # print('3 ' + '* ' + str(i))
    # print('3 x ' + str(i))
    print('3 x ' + str(i) +' = ' + str(3*i))