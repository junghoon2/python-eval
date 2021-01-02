#  key 값만 출력하는 함수

def print_keys(i):
  for data in i.keys():
    print(data) 
  # print(i.keys())

print_keys ({"이름":"김말똥", "나이":30, "성별":0})

print_keys={"이름":"김말똥", "나이":30, "성별":0}
print(print_keys.keys())