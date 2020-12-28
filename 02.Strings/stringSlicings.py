# 문자열은 list 타입으로 저장되어, slicing 가능하다.

a = ":)"
b = "Hello"

print(a)
print(a + b)

letters = 'python'
print(letters[0], letters[2])

# 문자열 슬라이싱, 문자열 자르기
license_plate = "24가 2210"
print(license_plate[-4:])

#
string = "홀짝홀짝홀짝"
print(string[::2])

# 문자열 뒤집어 출력하기
string = "PYTHON"
print(string[::-1])

# 문자열 치환,변경
phone_number = "010-1111-2222"
print(phone_number.replace('-', ' '))
print(phone_number.replace('-', ''))

string = 'abcdfe2a354a32a'
print(string.replace('a', 'A'))


