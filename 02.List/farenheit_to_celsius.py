# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
def fahrenheit_to_celsius(fahrenheit):
    # 코드를 입력하세요.
    # celsius = ((fahrenheit - 32) * 5) / 9
    # return celsius
    return ((fahrenheit - 32) * 5) / 9

celsius = round(fahrenheit_to_celsius(40))
print(celsius)

temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력

# t = fahrenheit_to_celsius(temperature_list)  # list 로 입력될까?
# print(t)


# 리스트의 값들을 화씨에서 섭씨로 변환하는 코드를 입력하세요.
# print("섭씨 온도 리스트: " + str(temperature_list))  # 섭씨 온도 출력

celsius = []

i = 0

while i < len(temperature_list):
    celsius.append(fahrenheit_to_celsius(temperature_list[i]))
    i +=1

print(celsius)

