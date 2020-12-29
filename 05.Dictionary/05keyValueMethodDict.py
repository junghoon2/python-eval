# dict 의 key, value만 따로 호출하기

# 1. 단어장 만들기
vocab = {
    # 코드를 입력하세요.
    "sanitizer": "살균제",
    "ambition": "야망",
    "conscience": "양심",
    "civilization": "문명"
}

# Key만 따로 호출, value만 따로 호출 
print(vocab.values())
print(vocab.keys())

for value in vocab.values():
    print(value)

# key 값만 가지기
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(icecream.keys())

keys =[]
for key in icecream.keys():
    keys.append(key)

print(keys)

ice = list(icecream.keys())
print(ice)

price = list(icecream.values())
print(price)
print(sum(price)) # list type에 sum 함수 적용

