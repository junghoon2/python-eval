# 언어 사전의 단어와 뜻을 서로 바꿔주는 함수

def reverse_dict(dict):
    new_dict = {}  # 새로운 사전
    
    # dict의 key와 value를 뒤집어서 new_dict에 저장
    # 코드를 입력하세요.
    # for i in dict.keys():
    #     new_dict[dict[i]] = i

    for key, value in dict.items():  # items 로 key, value 둘 다 받을 수 있다. 
        new_dict[value] = key  # [], index 로 하나하나 씩 넣을 수 있다. 

    return new_dict  # 변환한 새로운 사전 리턴


# 영-한 단어장
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
    'privilege': '특권',
    'principles': '원칙'
}

print(reverse_dict(vocab))

# 기존 단어장 출력
print("영-한 단어장\n{}\n".format(vocab))

# 변환된 단어장 출력
reversed_vocab = reverse_dict(vocab)
print("한-영 단어장\n{}".format(reverse_dict(vocab)))