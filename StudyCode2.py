from imp import IMP_HOOK
from lib2to3.pgen2.token import RPAR
from pickletools import read_int4
from re import A


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






















