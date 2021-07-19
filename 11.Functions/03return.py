# return이 print는 아니고 값을 가지는 거지
def retr(a, b, c):
  return (a * b * c)

retr(4, 5, 9)
print(retr(4, 5, 9) * 4)

# 좀 더 깔끔하게
y = retr(4, 5, 9)
print(y)

# 2번 print하네
def func_a():
  print("hello")
  return("Hello")

print(func_a())