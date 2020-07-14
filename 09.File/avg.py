# 파일로 부터 평균 구하기

# file pre-processing

sum = 0  # 일별 매출 총액
day_count = 0   # 누적 날짜

with open("data/chicken.txt", "r") as f:
    for line in f:
        # line = line.strip()
        # new = line.split(": ")  # 날짜와 매출 분리
        data = line.strip().split(": ")
        sum += int(data[1])
        day_count += 1
        # print(new)
    # print(f)  # 읽은 파일을 print 하는 방법은?
    # with open 으로 읽은 object는 바로 출력이 가능한 형태가 아니다. 

    #print(len(line))  # 파일 라인 수를 알 수 있는 함수는? 

print(round(sum / day_count))
    