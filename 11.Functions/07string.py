# 5 strings 씩 출력

div_string =[]

def print_5xn(string):
  # print(string[:5])

# 5씩 잘라서 출력, steps 5로 
  div = (len(string) // 5)
  for i in range(div):
    # div_string[i].append(string[5*i:5*(i+1)])
    # append에 list로 안되겠지
    div_string[0] = string[0:5]
    print(div_string[i])

print_5xn("아이엠어보이유알어걸")
