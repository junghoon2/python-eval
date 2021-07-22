import os, csv, re
import usecsv

os.chdir('/home/spkr/03.Python/14.csvExcel')

population = usecsv.readcsv('popSeoul.csv')

# print(population)

# for item in population[:5]:
#   print(item)
def switch(listName):
  for i in listName:
    for j in i:
      try:
        i[i.index(j)] = (float(re.sub(',', '', j)))
      except:
        pass
  return listName

switch(population)

print(population)

# for i in population:
#   try:
#     population[population.index(i)] = (float(re.sub(',', '', i)))
#   except:
#     pass

# print(population)

# print(type(population[2][2]))

# k = []

# # , 콤마 들어간 숫자를 숫자로 바꾸기
# for item in population:
#   if re.search(r'\D', item):
#     k.append(item)
#   else:
#     k.append(int(re.sub(',', '', item)))

# print(k)

# list element의 string 을 number 변경하기
# a = '3,555,999'  # 쉼표 있는 숫자를 어떻게 int 타입으로 인식할까?

# # Regex 의 sub 사용해서 , 쉼표 제거한다. 
# a = int(re.sub(',', '', a))

# print(int(a))

# # population[2] = re.sub(',', '', population[2])
# # print(population[2])

# k = []

# # 리스트 안 element 스티링 타입 숫자를 float 변경하기
# for item in population[2]:
#   # if re.search(r'\d', item):  # re, search 함수 사용
#   #   k.append(float(re.sub(',', '', item)))
#   # else:
#   #   k.append(item)  # list, append 함수 사용
#   # if re.search(r'[a-z가-힣]', item):
#   if re.search(r'\D', item):  # \D, 숫자가 아닌 것으로 조건 변경 가능
#     k.append(item)
#   else:
#     k.append(float(re.sub(',', '', item)))


# print(k)
