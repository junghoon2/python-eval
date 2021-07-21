# 파이썬 csv 파일 읽기

import os, csv

os.chdir('/home/spkr/03.Python/14.csvExcel')

def csvReader(filename):
  with open(filename, 'r') as f:
    reader = csv.reader(f)
    new = []
    for item in reader:
      new.append(item)
      return new

  # f = open(filename, 'r')
  # reader = csv.reader(f)
  # new = []
  # for item in reader:
  #   new.append(item)
  # return new
  # f.close()

csvReader('a.csv')

# print(new)

# f = open('a.csv', 'r')
# # f_read = f.read()
# # f.close()

# # print(f_read)

# # CSV 파일 형식으로 읽기
# # python csv 형식은 [[], []] 이다.

# # csv.reader로 읽으면 list로 저장된다.
# f_csv = csv.reader(f)
# print(f_csv)
# # f.close()

# # for은 list로 읽는다.
# # for item in f_csv:
# #   print(item)

# # 일반 csv 파일을 파이썬에서 사용 가능한 list 타입으로 변경한다.
# # 파이썬 list 타입에서 사용 가능한 다양한 메소드(append, select 등)를 활용 가능하다.
# fcsv_list =[]

# for item in f_csv:
#   fcsv_list.append(item)

# print(fcsv_list)

# # python CSV 형식은 리스트로 표현된다.
# # [['국어', ' 영어', ' 수학'], ['5', '6', '7']]

# f.close()