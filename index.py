from operator import truediv
from tkinter import FALSE

'''숫자 자료형 출력'''
print(5) 
print(-10)
print(3.14)
print(1000)
print(5+3)
print(3*2)
print(3*3+1)

'''문자열 출력'''
print('작은따옴표')
print("큰따옴표")
print('z'*9)

#참/거짓
print(5>10)
print(10>5)
print(True)
print(FALSE)
print(not True)
print(not (5>10))

#변수
dog = '연탄이'
age = 4 #정수를 문자열에서 사용하려면  str(변수)로 감싸주는 형태가 필요하다
hobby = '산책'
adult = age >= 3
print("우리집 강아지의 이름은 " + dog +" 입니다")
print(dog+"는 "+str(age)+"살이며, "+hobby+"을 아주 좋아합니다")
print(dog+"는 성인인가요? "+str(adult))
#콤마를 사용할 경우 str 없이 정수형 변수 사용이 가능하다.
#대신 한 칸 띄워져서 출력된다.
print(dog,"는 ",(age),"살이며, ",hobby,"을 아주 좋아합니다")

#주석
''' 여러문장 여러줄 주석 처리 가능합니다
crtl + / 를 누르면 드래그된 문장 전체가 주석처리됩니다.
해제는 동일합니다.'''
# 2-6퀴즈 22-04-30 24:40



