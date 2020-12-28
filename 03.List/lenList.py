# list 길이 출력
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))

# 전체 element 하나씩 출력
greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]

print(greetings)
#print(greetings.count())

n = len(greetings)  # Total number of list count
i = 0  # Initial number

while i <= n-1:
    print(greetings[i])
    i +=1
