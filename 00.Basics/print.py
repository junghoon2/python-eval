# Comment
print("Hello World.")

print(2.3 + 5) # 이것도 코멘트 
print("3.4")
print("3.4" + "3.2")
#print(2 + "3")
print(2.0 + 3)

# boolean
print(7 > 3)
print(3 > 8)

# List, tuple 
print("출력:", "A")

# 특수문자 출력
print('신씨가 소리질렀다. "도둑이야".')
print("신씨가 소리질렀다. \"도둑이야\".")

print("C:\Windows")

# tab, 줄 바꿈
print("안녕하세요.\n만나서\t\t반갑습니다.")

# string type, 쉼표 , 역활은?
# , 는 2개 string 같이 출력 가능하게 한다. 공백 추가
print ("오늘은", "일요일")

# print element 사이에(sep, seperate) 특수 문자 또는 공백 추가하기
print("naver;kakao;sk;samsung")
print("naver", "kakao", "sk", "samsung")
print("naver", "kakao", "sk", "samsung", sep="; ")
print("naver", "kakao", "sk", "samsung", sep="/")

# 문자와 문자열 길이 같이 출력
# print 함수에서 문자열 더하기 보다는 쉼표가 낫다. 
for i in ["dog", "cat", "parrot"]:
    print(i + ' ' + str(len(i)))
    print(i, len(i))
    
# end, 줄바꿈 수정하기
print("first");print("second")
print("first", "second", end="")

# 2개 사이(sep, seperate) 공백 없애기
print("first", "second", sep="")
print("first", end="");print("second")

print(5/3)

# 두 문자열 합해서 출력, string 간 + 는 string 붙혀서 출력한다.
s = "hello"
t = "python"

print(s + "! " + t)
