#퀴즈 1 변수를 이용한 문장 출력
station = '사당'
print(station+'행 열차가 들어오고 있습니다.')

#퀴즈 2 랜덤을 이용한 날짜 출력
from dataclasses import replace
from random import*
from traceback import print_tb
date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 " +str(date)+"일로 선정되었습니다.") 

#퀴즈 3 사이트별 비밀번호
site = "http://naver.com"
site = "http://daum.com"
# start = site.index("/")+2
# end = site.index(".")
# home = site[start:end]
# count = len(home)
# count2 = home.count("e")
# pw = home[:3] + str(count) + str(count2)
# print(site[start:end])
# print(site[start:])
# print(count2)
# # print(count)
# print(pw)

site = site.replace("http://", "")
site = site[:site.index(".")]
print(site)
password = site[:3] + str(len(site)) + str(site.count("e"))+"!"
print(password)
print("{0}의 비밀번호는 {1}입니다".format(site, password))
print("%s의 비밀번호는 %s입니다" % (site,  password))















