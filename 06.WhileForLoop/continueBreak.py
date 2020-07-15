
count = 1

# break는 전체 while문을 벗어나기
while count < 10:
    if count % 2 == 0:
        break
    print(f"We're counting odd numbers: {count}")
    count += 1

print(count)

# Continue는 while 조건 문 실행
while count < 10:
    if count % 2 == 0:
        count += 1
        # continue는 실행 무시하고 바로 while문 조건으로 넘어가는 듯
        continue
        # count +=1
    print(f"We're counting odd numbers: {count}")
    count += 1

