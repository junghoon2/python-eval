# Random 한 voca quiz 프로그램 

# dict 자료형, key value 형태 

import random 
voca = {}  # dictionary type 으로 initial 변수 만들기

with open("data/voca01.txt", "r") as f:
    for line in f:
        data = line.strip().split(": ")  # 공통 부문을 하나로 묶기
        # eng_word = line.strip().split(": ")[0]
        # kor_word = line.strip().split(": ")[1]  # 2개를 하나로 묶는 코드는?
        eng_word, kor_word = data[0], data[1]  # 2개를 하나로 
        voca[eng_word] = kor_word # 새로운 dic 자료형 만들기
        # dict에 하나하나 element 로 넣어주기 


    # 반복하기
    while True:
        # random quiz word 할당
        eng_word, kor_word = random.choice(list(voca.items()))  
        answer = input(f"{eng_word}: ")
        if answer == "q":
            break
        elif answer == kor_word:
            print("맞았습니다!")
        else:
            print(f"아쉽습니다. 정답은 {kor_word}입니다.")
