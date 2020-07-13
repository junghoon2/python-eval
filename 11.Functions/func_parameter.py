def hello(name, age):
  print("Hello " + name) # 변수 호출 하는 방법은? script 처럼 $ 이런 건 쓰지 않는 것 같고
  # + 하면 되나
  # print 함수에서 + 를 사용하려면 양쪽의 변수 타입이 동일히야 한다. 
  # "Hello" + 20 은 에러 
  print("Welcome")

  print("Hi" + " world again")
  print(name) # print 로 문자열을 받으면 그걸 출력한다. 
  print(age + 10) # age 를 자동으로 integer로 받아들이네 

hello(20, 44)