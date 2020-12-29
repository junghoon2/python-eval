# dict에 새로운 element 추가하기
# 사전에 element는 자유롭게 key, value 추가해서 확장 가능

# 1. 단어장 만들기
vocab = {
    # 코드를 입력하세요.
    "sanitizer": {"살균제", "오염제"},
    "ambition": "야망",
    "conscience": "양심",
    "civilization": "문명"
}
print(vocab)
print(vocab["ambition"])

# 2. 새로운 단어들 추가
# 코드를 입력하세요.
vocab["privilege"] = "특권"
vocab["principle"] = "원칙"

print(vocab)

# dict 정의
# 중첩으로 dict 사용 가능
my = {
	"메로나": 1000,
	"폴라포": 1200,
	"빵빠레": {"콘": 1800, "바": 1500}
}

print(my)

# 중첩된 dict 지정하는 방법은?
print(my["빵빠레"]["콘"])

# dict element 추가하기
my["죠스바"] = 1200
my["월드콘"] = 1500 

print(my)

inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}

inventory["월드콘"] = [500, 7]

print(inventory)

# element 추가, update 메소드 사용 
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}

# 기존 dict에 update 메소드 사용하여 element 추가
icecream.update(new_product) # update 메소드 인자로 dict 사용 가능?
print(icecream)