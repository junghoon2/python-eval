# 파일 확장자 확인하고 변경하기 또는 붙히기

# 파일 이름 확장자 확인하기
file_name = "보고서.csv"
print(file_name.endswith('xlsx'))

# print(file_name.endswith('xls', 'xlsx'))

# 파일 이름 접두어 or 검색
# 괄호를 2개 한다. 전체 묶어서 (), 괄호 안에 넣어준다.
print(file_name.endswith(('xls', 'xlsx', 'csv')))
