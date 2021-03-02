#  key 값만 출력하는 함수

def print_keys(i):
  for data in i.keys():
    print(data) 
  # print(i.keys())

print_keys ({"이름":"김말똥", "나이":30, "성별":0})

print_keys={"이름":"김말똥", "나이":30, "성별":0}
print(print_keys.keys())

# 리스트와 키값 입력받아 출력 프로그램
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def print_value_by_key(i, j):
  print(i[j])

print_value_by_key(my_dict, "10/27")