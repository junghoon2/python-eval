# 중첩으로 dict 사용 가능
my = {
	"메로나": 1000,
	"폴라포": 1200,
	"빵빠레": {"콘": 1800, "바": 1500}
}

print(my)

# 중첩된 dict 지정하는 방법은?
# 순서대로 key 지정
print(my["빵빠레"]["콘"])

inventory = {
	"메로나": [300, 20],
  "비비빅": [400,	3],
	"죠스바":	[250,	100]
}

print(inventory)
print(str(inventory["메로나"][0]) + " 원")

# print 함수 , 는 2개 element 붙힌다.
print(inventory["메로나"][0], "원")

print(inventory["메로나"][1], "개")

inventory = {
	"메로나": {'가격': 300, '재고': 20},
  "비비빅": [400,	3],
	"죠스바":	[250,	100]
}

print(inventory)
