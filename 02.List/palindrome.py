def is_palindrome(word):
    # 코드를 입력하세요.
    new_word = list(word)  # new_word List type 초기화
    for i in range(len(word)):  # 문자열 거꾸로 저장
        new_word[i] = word[-(i+1)]
    new_word =''.join(new_word)  # List to String
    # print(new_word)
    if new_word == word:
        return True
    else:
        return False

# 테스트
print(is_palindrome("racecar"))

# word = "racecar"
# word1 = list(word)
# word1[0] = word[-1]
# word1[1] = word[-1]
# print(word1[0])