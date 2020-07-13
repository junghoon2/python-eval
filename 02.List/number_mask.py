def mask_security_number(security_number):
    # 코드를 입력하세요.
    new_num = list(security_number)  # string 인자를 먼저 list 로 변환
    for i in range(1, 5):  # 마지막 4자리 * masking 처리
        new_num[-i] = "*"  

    str_num = new_num[0]  # 초기 변수 지정
    for j in range(1, len(security_number)):  # List to String 변환
        str_num += new_num[j]
    
    return(str_num)


# num = "880720-1234567"
# print(list(num[-3:]))

# 테스트
print(mask_security_number("880720-1234567"))

#''.join()

