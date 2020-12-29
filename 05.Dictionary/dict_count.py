# 투표 결과 리스트
votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자', \
'최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기', \
'강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기', '김영자']

print(votes[0])

# 후보별 득표수 사전
vote_counter = {}

count1 = 0
count2 = 0
count3 = 0

# 리스트 votes를 이용해서 사전 vote_counter를 정리하기
for name in votes:
    # 코드를 작성하세요.
    if name == "김영자":
        count1 +=1
    elif name == "강승기":
        count2 +=1
    else:
        count3 +=1

vote_counter["김영자"] = count1
vote_counter["강승기"] = count2
vote_counter["최만수"] = count3

#print(count1, count2, count3)

# 후보별 득표수 출력
print(vote_counter)

# 후보별 득표수 사전
vote_counter = {}

# 리스트 votes를 이용해서 사전 vote_counter를 정리하기
for name in votes:  # list 는 for loop 의 in 조건문으로 가능 
    if name not in vote_counter:  # if in 조건문으로 dictionary 도 가능 
        vote_counter[name] = 1
    else:
        vote_counter[name] += 1  # dictionary value 값은 integer 로 integer 연산 가능 
