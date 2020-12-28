# list 를 string 으로 합치려면 간단히 join 메소드(함수가 아니라) 사용하면 된다.
# string type으로 변경된다.

# 메소드, 함수, 클래스 차이

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# 2개를 join 하는데, ' ' 앞의 인자 기준으로 하겠다.
print(' '.join(interest))
print('/'.join(interest))

# 줄 바꿈 출력, 특수 문자 사용 가능
print('\n'.join(interest))

num = ['8', '8', '0', '7', '2', '0', '-', '1', '2', '3', '*', '*', '*', '*']
print(''.join(num))

# 사이에 특정 기호를 넣으려면 '', 따옴표 사이에 넣으면 되고
print('-'.join(num))
