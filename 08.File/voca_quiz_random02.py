# Random voca quiz 프로그램 

import random 
voca = {}  # initial dictionary type 변수

with open("data/voca01.txt", "r") as f:
    for line in f:
        # 영어, 한국어 변수 할당
        data = line.strip().split(": ")  
        eng_word, kor_word = data[0], data[1]  

        # dictionary type 변수 저장
        voca[eng_word] = kor_word 

    # Random 단어 생성
    while True:
        # random quiz word 할당
        eng_word, kor_word = random.choice(voca.items())  # random.choice 함수 사용
        answer = input(f"{eng_word}: ")
        if answer == "q":
            break
        elif answer == kor_word:
            print("맞았습니다!")
        else:
            print(f"아쉽습니다. 정답은 {kor_word}입니다.")
