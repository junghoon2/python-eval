# voca quiz 프로그램

# 파일로 부터 읽어 들여서 사용자 인풋으로 출력

with open("data/voca01.txt", "r") as f:
    for kor_voca in f:  # 이러면 반복으로 들어가나?
        kor_voca = kor_voca.strip().split(": ")  # string 을 ": " 기준으로 나누고
        answer = input(f"{kor_voca[0]}: ")  # 영어 단어 입력을 answer 저장
        if answer == kor_voca[1]:
            print("맞았습니다!")
        else:
            print(f"아쉽습니다. 정답은 {kor_voca[1]}입니다.")
