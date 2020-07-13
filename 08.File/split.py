# split
my_string = "1. 2. 3. 4. 5. 6"
print(my_string)
print(my_string.split("."))
print(my_string.split(". "))  # 문자열의 띄워쓰기도 포함해서 구분

full_name = "Kim, Yuna"
print(full_name.split(", "))
name_data = full_name.split(", ")

last_name = name_data[0]
first_name = name_data[1]

print(first_name)

print(" \n \t asdf \n \t asdf \t adsfa \n\n\n")
print(" \n \t asdf \n \t asdf \t adsfa \n\n\n".split())  
# whitespace 전체를 지우고 나눈다.

# split 도 역시 string type 이라 정수형 사용하려면 형 변환, int 해야 한다. 
