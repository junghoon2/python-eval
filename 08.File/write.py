# 파일에 내용 쓰기

with open("data/write01.txt", "a") as f:
    f.write("Hello world\n")  # 줄 바꿈 필요
    f.write("This is my first 'Write file example'\n")  # 덮어쓰기 된다.