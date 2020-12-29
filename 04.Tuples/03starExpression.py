# 여러 개 element 할당

# 복수 element(혹은 list type으로) 를 단일 key 지정 가능
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
my_dict = { 
    "a": scores[0], 
    "b": scores[1],
    "c": scores[2:]
    }

print(my_dict)

# _ -> 빈 값을 의미?
# 나머지 제외하고 할당 시 *valid_score, * 사용 가능
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_,*valid_score, _, _= scores
print(valid_score)

# 변수 할당하는 방법
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, b, *valid_score = scores
print(valid_score)
print(type(valid_score))
