# List 할당하고 사용하기
# [] 괄호 사용하면 된다. 
# List는 순서를 가진다. 
# dict, key-value store는 가지려나?

# 이름 지정하고 [ ] 괄호안에 넣어준다.
# list 타입 변수 선언
my_list=[4, 5, 7]
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)


# index는 [ ], 괄호 안에 숫자를 넣는다.
print(my_list[0])
print(my_list)

# 특정 index 값 변경하기
my_list[2] = 3
print(my_list)

# 원소 추가하기, append는 마지막에 추가된다. 
movie_rank.append("배트맨")
print(movie_rank)

# 기존 원소 사이에 추가 
movie_rank[1] = "슈퍼맨" # 기존 element 변경
print(movie_rank)

# movie_rank[2].append("스플릿"), index 지정하고 append는 안 됨
# 원소 사이 추가는 insert 
movie_rank.insert(2, "스플릿")
print(movie_rank)

# element 삭제, delete는 없고 remove 
# element 이름이 아니라 index로 삭제도 가능
movie_rank.remove("럭키")
print(movie_rank)

movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']


# 리스트 더하기
# 순서는 어떻게 되려나? append? 뒤에 붙는다.
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

langs = lang1 + lang2
print(langs)

# 리스트에서 최대, 최소값 출력
nums = [1, 2, 3, 4, 5, 6, 7]
# print(nums.min())
# min, max 라는 별도 함수 제공
print(min(nums))
print(max(nums))

# 파이썬 평균, 별도 모듈 사용해야 할까?
print(sum(nums) / len(nums))

numbers = [1, 3, 5, 8, 13]

my_list = ["dell", "samsung", "huawei", "thales"]
my_list02 = ["kakao", "nc", "naver", "bigin"]

my_list03 = my_list[3] + my_list02[2]

# print index 
print(my_list[2])

print(my_list[-1])

print(my_list03)

# Print index
num_0 = numbers[0]
num_1 = numbers[1]

print(num_0 + num_1)

print(numbers[-1] + numbers[2])

# list slicing
print(numbers[0:3])
print(numbers[:2])  # :2, 2: 처음 시작과 index 가 다르다. 
print(numbers[2:])

# print(numbers[-7])

