# 파일 이름 시작 검색하기

file_name = "2019_보고서.xlsx"
print(file_name.startswith('2020'))

# 2개 이상 or 조건 검색
print(file_name.startswith(('2020', '2019')))

# python 에서 파일 이름 시작 검색
# python 에서 명령어 결과를 변수로 저장 가능할까?

# [spkr@erdia22 ~ ]$ ls |egrep ^0
# 01.Ansible
# 02.k8s
# 03.Python
# 04.BashScript
# 05.NGINX
# 06.dockerfile
# 07.Go
# 08.MariaDB
# 09.Grafana
