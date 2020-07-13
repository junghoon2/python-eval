# 문자열이 대칭(Palindrom)인지 확인

def is_palindrome(word):
    n = len(word) // 2  # 문자열 길이의 반만큼 검증
    count = 0  # 일치 여부 검증 
    for i in range(n):
        if word[i] != word[-(i+1)]:
            count += 1
    
    if count == 0:
        return True
    else:
        return False


print(is_palindrome("토마토"))
print(is_palindrome("하이"))