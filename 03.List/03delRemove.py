# 리스트에서 element 지우기
numbers = [3, 4, 5, 6, 8, 9]

# del은 index 기준으로 삭제
del numbers[3]  
print(numbers)

# remove는 object 내용으로 삭제
numbers.remove(4)
print(numbers)

# 순서를 지우는 게 아니라 object 내용으로
a = [2, 3, 7, 3 ,5, 5, 3, 8]
a.remove(2)  

# remove는 object로 지우고 pop은 index로 지우고
a.pop(0)
print(a)

# 복수 element 삭제
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']

# index, slicing 지정해서 삭제 가능
# del은 별도 함수로 제공
del movie_rank[2:]
print(movie_rank)

# movie_rank.remove(("스플릿", "배트맨")) 지원하지 않음 
# movie_rank.remove[2, 3]
print(movie_rank)

# 리스트 간 빼기 혹은 set간 빼기 
# 리스트는 빼기 지원하지 않는다. 순서가 있으니까. 
remove_rank = ["스플릿", "배트맨"]
# print(movie_rank - remove_rank)

# list에서 복수 element 삭제는 set으로 변경 후 삭제
# set란? 순서가 없는 타입, 교집합 등에 사용, {} 중괄호 사용 
# print(set(movie_rank) - set(remove_rank))
print(list(set(movie_rank) - set(remove_rank)))

# 복수 개를 remove 하지는 못하고 하나만 지우는 구나
print(a)

# 여러 개를 지우려면 slice해서 [], empty 할당한다.
a[:2] = []
print(a)

# index로 지우려면 [], none을 할당하면 되나?
# a[0] = [ ]
# a[0] = None

