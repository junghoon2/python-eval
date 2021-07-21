# import 파일 위치는 현재 디렉토리 내 파이썬 파일 호출
# 하위 경로이면 from 디렉토리 import 파이썬 파일 형식으로

import usecsv, os 

os.chdir('/home/spkr/03.Python/14.csvExcel')

a = [['국어', '영어', '수학'], [80, 90, 100]]

usecsv.writecsv('cde.csv', a)
