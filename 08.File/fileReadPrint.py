# file 읽어 들이기
with open('data/chicken.txt', 'r') as f:  # open 함수로 r, read 로 읽겠다. 
# 경로를 잘 지정해야 함.
    print(type(f))
    for line in f:
        print(line.strip())  # 파일을 list 처럼 인식한다. 
