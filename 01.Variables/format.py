# 오늘은 2019년 10월 29일 입니다. 
year = 2019
month = 10
day = 29 
my = "Hello"

print("오늘은 " + str(year) + "년 " + str(month) + "월 " + str(day) + "일 입니다.")
#print("오늘은 {f.year}년 {f.month}월 {f.day}일 입니다.")
print("오늘은 {}년 {}월 {}일 입니다. {}".format(year, month, day, my)) # 완전 멋있네

print(year + month)

date_string = "오늘은 {}년 {}월 {}일 입니다. {}"
print(date_string.format(year, month, day + 2, my))

print("저는 {}, {}, {}를 좋아합니다.".format("유재석", "박지성", "김연아"))
print("저는 {2}, {1}, {0}를 좋아합니다.".format("유재석", "박지성", "김연아"))

num_1 = 1
num_2 = 3
num_3 = round(num_1 / num_2, 2)

print("{0} 나누기 {1}는 {2} 입니다.".format(num_1, num_2, num_3))
print("{0} 나누기 {1}는 {2:.3f} 입니다.".format(num_1, num_2, num_1/num_2))
print("{0} 나누기 {1}는 {2:.7f} 입니다.".format(num_1, num_2, num_1/num_2))