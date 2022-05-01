
from imp import IMP_HOOK
from lib2to3.pgen2.token import RPAR
from pickletools import read_int4
from re import A
from traceback import print_tb


# 연산자
print(2**2)  #제곱
print(5%3)   #나머지 
print(5//3)  #목
print(3==3)
A = 3
print(A+3==6)
print(1!=3)  # !, not 부정
print(not 3 == 5)
print((3>0) and (3>5))
print((3>0) & (3<5))
print((3>0) or (3>5))
print((3>0) | (3>5))
print(5>4>7)

#수식
print(2+3*4)
print((2+3)*4)
number = 2+3
print(number)
number = number + 5
number+= 2     #+= -= /= %= *=
print(number)  
number-=3
print(number)
number%=5  
print(number)
number/=2
print(number)

#숫자처리함수
print(abs(-10)) #절대값
print(pow(4,2)) #4^2 = 16 제곱
print(max(4,12))
print(min(4,12))
print(round(3.14)) #round 반올림
print(round(4.69))

from math import*
print(floor(4.99)) #내림
print(ceil(4.19)) #올림
print(sqrt(16))   #제곱근

#랜덤함수
from random import*
print(random()) #0.0 ~ 1.0 임의값
print(random()*10) #0.0 ~ 10.0 임의값
print(int(random()*10)) #int 항으로 감싸주어 정수형으로 출력
print(int(random()*10))
print(int(random()*10)+1) #1부터 10이하의 임의값
print(int(random()*45)+1)
print((randrange(1,46))) #1부터 46 미만의 임의값
print(randint(1,45 )) #1부터 45이하의 임의값

#문자열
sentence = '나는 소년입니다'
print(sentence)
sentence = "파이썬은 쉬워요"
print(sentence)
a='''나는 소년이고 
파이썬은 쉬워요'''
print(a)

#슬라이싱
num = "990020-8234567"
print("성별 : "+num[7])
print("연 : "+num[0:2]) #0부터 2직전까지
print("월 : "+num[2:4]) 
print("생년월일 : "+num[:6]) #처음부터 6직전까지
print("뒷자리 : "+num[7:])
print("뒤에서부터 " +num[-7:])

#문자열 처리함수
a = "Python is Amazing"
print(a.lower())
print(a.upper())
print(a[0].isupper()) #대문자가 맞으면 true
print(len(a))         #길이  
print(a.replace("Python", "Java")) #문자열 치환
index = a.index("n") # 해당 문자 위치 
print(index)
index = a.index("n", index +1 ) #해당 문자 첫위치 다음위치
print(index)

print(a.find("Java")) # 원하는 값 없을 경우 -1 반환
# print(a.index("Java"))  에러처리
print(a.count("n")) #해당 글자 갯수

#문자열 포맷
print("a"+ "a")
print("A"+"b")
    #정수 문자열 문자 %d %s %c
    #방법 1
print("나는 %d살입니다" % 20)
print("나는 %s을 좋아해요" % "파이썬")
print("Apple 은 %c로 시작해요" % "A")
print("나는 %s살입니다" % 20) #%s는 만능인가
print("나는 %s과 %s을 좋아해요" % ("빨간색" , "파란색"))
    #방법 2 
print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간") )
print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간"))
    #방법 3
print("나는 {age}살이며, {color}색을 좋아해요".format(age=20, color="빨간색"))
    #방법 4
age = 20
color = "빨간" #f는 기존 변수값을 가져와 사용한다
print(f"나는 {age}살이며, {color}색을 좋아해요")

#탈출문자
print("문장을 줄바꿈하려면\n이렇게합니다")
print('저는 \"SnChul\" 입니다') #\" 문자로 그대로 출력 \"
    #문장 내에서 \를 출력하려면 \\
print("C:\\Users\\we202\\Documents\\GitHub\\Python_project")
    #\r 커서 맨 앞으로 이동
print("Red Apple\rPine")
    #\b 백스페이스 (한글자 삭제)
print("REdd\bApple")
    #\t tab 기능
print("REd\tApple")

































