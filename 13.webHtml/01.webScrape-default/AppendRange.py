import requests

### 코드를 작성하세요 ###

# list 변수 지정
rating_pages = []

# 연도 데이터 : 2010 ~ 2018, 달 1 ~ 12, 주차 1, 5
# 중첩 for loop

# range 함수는 시작 숫자 포함, 마지막 숫자는 -1. range 함수는 0부터 시작
for i in range(2010, 2019):
  for j in range(1, 13):
    for k in range(5):
      url = "https://workey.codeit.kr/ratings/index?year={0}&month={1}&weekIndex={2}".format(i,j,k)
      response = requests.get(url)
      rating_pages.append(response.text) # list 함수에 element 하나씩 추가하기

# 출력 코드
print(len(rating_pages)) # 가져온 총 페이지 수 
print(rating_pages[0]) # 첫 번째 페이지의 HTML 코드
