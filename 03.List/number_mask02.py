
def mask_security_number(security_number):
    # 코드를 입력하세요.
    new_num = security_number[:-4] + "****"
    return(new_num)


# 테스트
print(mask_security_number("880720-1234567"))
