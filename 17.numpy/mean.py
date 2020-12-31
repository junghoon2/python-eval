# 3일 간의 종가 평균 출력

import numpy as np

my_list = [100, 200, 400, 800, 1000, 1300]

for i in range(4):
  a = np.array(my_list[i:i+3])
  print(a.mean())

