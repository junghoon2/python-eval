import csv, os

# csv_file = open("data/매수종목.csv", "w", encoding='cp949')

# 파일을 먼저 지정하고, 파일을 읽을 건지 쓸건지 정하고
# 파일 쓰는 (혹은 읽는) 메소드 사용
# csv_file = open("data/매수종목.csv", "w", encoding='utf-8')
# csv_writer = csv.writer(csv_file)

# # csv, row 작성은 writerrow 함수 사용
# csv_writer.writerow(['종목명', '종목코드', 'PER'])
# csv_writer.writerow(['삼성전자', '005930', '15.79'])
# csv_writer.writerow(['NAVER', '035420', '55.82'])

# # 파일 쓰고 나면 꼭 닫아주고
# csv_file.close()

os.chdir('/home/spkr/03.Python/14.csvExcel')

a = [ ['Gu', 'Korean', 'Foreigner', 'Senior'],
['Total', "9,740,398","285,529","1,468,146"],
['Jongrogu',"151,767","11,093","27,394"],
['Jongru',"126,409","10,254","23,025"],
['Yongsangu',"228,830","16,159","38,531"] ]

# f = open('abc.csv', 'w', newline='')

# # csv 리스트를 csv 형태의 파일로 쓰기 위해서는 csv.writer 메소드 사용
# csvobject = csv.writer(f, delimiter = ',')

# # 여러 줄을 한번에 입력할 때는 writerows 메소드 사용
# csvobject.writerows(a)

# f.close()

# CSV 형태 list를 csv 파일로 저장하는 함수 
def writecsv(filename, the_list):
  # f.open(filename, 'w', newline='')
  with open(filename, 'w', newline = '') as f:
    a = csv.writer(f, delimiter = ',')
    a.writerows(the_list)

writecsv('bcd.csv', a)