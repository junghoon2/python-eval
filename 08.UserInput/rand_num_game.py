import random

ran_num = random.randint(1, 20)
print(ran_num)

for i in range(4, -1, -1):  # 총 기회는 4번
    if i != 0:
        num = int(input(f"기회가 {i}번 남았습니다. 1~20 사이의 숫자를 맞춰 보세요: "))
        if num == ran_num:  # 숫자 비교
            print(f"축하합니다. {5 - i}번 만에 숫자를 맞추셨습니다.")
            exit()  # exit 은 함수라서 () 필요한가?
        elif num < ran_num:
            print("Up")
        elif num > ran_num:
            print("Down")
    else:
        print(f"아쉽습니다. 정답은 {ran_num}입니다.")