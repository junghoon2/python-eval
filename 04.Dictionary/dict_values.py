# 1. 단어장 만들기
vocab = {
    # 코드를 입력하세요.
    "sanitizer": "살균제",
    "ambition": "야망",
    "conscience": "양심",
    "civilization": "문명"
}

# Key만 따로 호출, value만 따로 호출 
print(vocab.values())
print(vocab.keys())

for value in vocab.values():
    print(value)
