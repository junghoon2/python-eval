import os

# 현재 디렉토리 출력, get 다음 c 까지 붙힌다.
print(os.getcwd())
# print(os.getwd())

# 디렉토리 변경
os.chdir('/home/spkr/03.Python/09.File')

print(os.getcwd())
print(os.listdir())

# 파일 열기, os open 이 아니고 그냥 open
# f = os.open('a.txt', 'w')
f = open('a.txt', 'w')

# 파일에 내용 쓰기
f.write('test 용도 파일 작성')

f.close()
