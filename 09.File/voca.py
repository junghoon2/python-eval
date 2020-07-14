# 영어 단어장 프로그램

eng_voca = ""  # "" 로 initialize 가능한가?
kor_voca = ""

# q, 나올때 까지 반복문 실행 
while True: 
    # 사용자 입력 받기
    eng_voca = input("영어 단어를 입력하세요: ")  # 영어 단어  
    if eng_voca == "q":
        # exit()
        break  # while 바깥으로 빠져 나가는 것은 break 

    kor_voca = input("한국어 뜻을 입력하세요: ")  # 한국어 뜻 
    if kor_voca == "q":
        exit()  # while 전체 종료
    
    # 파일에 저장
    with open("data/voca01.txt", "a") as f:
        f.write(f"{eng_voca}: {kor_voca}\n")
