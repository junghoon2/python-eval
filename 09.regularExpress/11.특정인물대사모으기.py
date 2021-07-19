# 특정 등장 인물의 대사만 모으기
os.chdir(r'/home/spkr/03.Python/09.regularExpress')

f = open('friends101.txt', 'r')
# f = codecs.open('friends101.txt', 'r', encoding = 'utf-8')

# read로 새로운 객체 만든다.
script101 = f.read()

# print(script101[:100])

# joey script만 찾는다.
# .+ 로 반복되는 문자 찾는다
joey_script = re.findall(r'Joey:.+', script101)

# joey_script = re.split('joey_script', '')
# print(joey_script[2])

# 파일 열기
# with open('./friends101.txt', 'r') as f:
# # with open('./friends.101.txt', 'r') as f:
#   joey_script = re.findall(r'Joey:.+', f)
#   print(joey_script)

# 보기 좋게 출력하기
# 리스트에 있는 걸, 하나씩 개행 출력한다. 
# for item in joey_script:
#   print(item)

f.close()

# 새로운 파일 만들어서 조이 대사 적기
f = open('joey.txt', 'w', encoding = 'utf-8')
joey = ''

for i in joey_script:
  joey += i + '\n'  # 리스트 저장 할 때 마다 \n 넣기

print(joey[:10])

f.write(joey)
f.close()