import csv

# csv_file = open("data/매수종목.csv", "w", encoding='cp949')

# 파일을 먼저 지정하고, 파일을 읽을 건지 쓸건지 정하고
# 파일 쓰는 (혹은 읽는) 메소드 사용
csv_file = open("data/매수종목.csv", "w", encoding='utf-8')
csv_writer = csv.writer(csv_file)

# csv, row 작성은 writerrow 함수 사용
csv_writer.writerow(['종목명', '종목코드', 'PER'])
csv_writer.writerow(['삼성전자', '005930', '15.79'])
csv_writer.writerow(['NAVER', '035420', '55.82'])

# 파일 쓰고 나면 꼭 닫아주고
csv_file.close()