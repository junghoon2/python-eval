# 통신사 출력
mobile = input("핸드폰 번호를 입력하세요: ")
digit3 = mobile[:3]

telco = {
  "011": "SKT",
  "016": "KT",
  "019": "LGU",
  "010": "알 수 없음"
}

print(telco[digit3])
print("당신은 {} 사용자 입니다.".format(telco[digit3]))

if digit3 == "011":
  print(telco["011"])
elif digit3 == "016":
  print(telco["016"])
elif digit3 == "019":
  print(telco["019"])  
elif digit3 == "010":
  print(telco["010"])

