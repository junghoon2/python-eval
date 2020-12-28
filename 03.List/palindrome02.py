def is_palindrome(word):
    for left in range(len(word) // 2):
        right = left + 1
        if word[left] != word[-(right)]:
            return False
    return True

print(is_palindrome("racecar"))
print(is_palindrome("stars"))

