from pdb import line_prefix
from re import sub


#리스트 []

# subway1=10
# subway2=10
# subway3=10

subway=[10,20,30]
print(subway[2])
print(subway.index(30))
#append 리스트 끝에 추가
subway.append(40)
print(subway)
#insert 리스트 중간에 추가
subway.insert(1,44)  #1번 위치에 삽입 나머지 한칸씩 밀림
print(subway)
#pop 리스트에서 맨뒷자리 제거 (제거할 자리 선택)
print(subway.pop())
print(subway)
print(subway.count(30))
#sort 순서대로 정렬 reverse 반대로 정렬
num = [4,2,3,1,5]
num.sort()
print(num)
num.reverse()
print(num)
#모두 지우기
num.clear()
print(num)
#다양한 자료형과 함께 사용
all =[5,2,3,5,1]
all2 = ["whi", 3, True]
#print(all) extend a.extend(b) 리스트 합체
all.extend(all2)
print(all)

#사전 {}
dic ={3:"hello", "aaa":"bye"}
print(dic[3], dic["aaa"])
print(dic.get(3))
#print(dic[7])  자료가 없을 때 프로그램종료
#print(dic.get(7)) 자료가 없을때 none으로 처리 종료X
print(3 in dic)
print(5 in dic)
dic["c"] = "wow" #추가
print(dic["c"])
print(dic)
del dic["c"]
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())
dic.clear()
print(dic)

#튜플 ()
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])
name, age, hobby = "all" , 20 , "good"
print(name,age, hobby)

#집합(set)
#중복 x 순서없음
home={1,2,3,3,4}
print(home) #중복값 무시 나머지 출력
#교집합 출력
outdoor = set([1,5,6,7])
print(home&outdoor)
print(home.intersection(outdoor))
#합집합
print(home|outdoor)
print(home.union(outdoor))
#차집합
print(home - outdoor)
print(home.difference(outdoor))
outdoor.add(10)
print(outdoor)
outdoor.remove(10)
print(outdoor)