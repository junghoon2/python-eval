# 파이썬 모듈 만들기
# import로 계속 사용 가능하다. 

# module 파일 위치는?

# CSV 형태 list를 csv 파일로 저장하는 함수 
import csv


def writecsv(filename, the_list):
  # f.open(filename, 'w', newline='')
  with open(filename, 'w', newline = '') as f:
    a = csv.writer(f, delimiter = ',')
    a.writerows(the_list)

def readcsv(filename):
  with open(filename, 'r') as f:
    reader = csv.reader(f)
    new = []
    for item in reader:
      new.append(item)
      return new
