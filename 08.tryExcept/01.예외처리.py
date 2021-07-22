import re

i = ['123!@#', '', '123,498', '@#$333asfㅇㅁㅁ']

# try 문에 오류가 발생하면
# except 예외적으로 except 실행하라 

# 오류(try & except) 발생 시 실행할 명령어를 미리 정의해 놓는다.
# 오류가 발생해도 그냥 넘어가라 라는 코드를 만들 수 있다.

# for j in i:
#   try:
#     i[i.index(j)] = float(re.sub(',', '', j))
#   except:
#     pass

# 예외처리 안하면 에러 발생해서 코드가 실행되지 않는다. 
for j in i:
  i[i.index(j)] = float(re.sub(',', '', j))


print(i)