# 키 값, value 값 각각을 사용해서 하나의 dict 만들기
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)

result = {}

# result[keys[0]] = vals[0]
# result[keys[1]] = vals[1]
# result[keys[2]] = vals[2]
# result.keys = keys
# result = keys
# result.values = vals

# for 문 인자를 2개 사용 가능할까?
for i in range(3):
    result[keys[i]] = vals[i]

# result[keys] = vals
print(result)

# zip 압축하다, 묶다.
# zip은 같은 element 수를 가지는 반복 요소를 하나로 묶어준다.
result1 = dict(zip(keys, vals))
print(result1)

date = ['09/05', '09/06', '09/07', '09/08', '09/09']
# zip 해당하는 요소 숫자가 서로 다르다면?
# 짝이 안 맞으면 그냥 무시한다.
# close_price = [10500, 10300, 10100, 10800, 11000]
close_price = [10500, 10300, 10100, 10800, 11000, 9000]
close_table = dict(zip(date, close_price))
print(close_table)
