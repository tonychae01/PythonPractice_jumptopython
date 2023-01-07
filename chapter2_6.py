#set 집합 자료형 !! 비어있는 집합 만들기 : s=set() 이용 !! 순서가 없다 !!
# #비어있는 집합은 ()아님!! ()이거는 튜플임!! 집합기호: {1,2,3} 이렇게 적는다!!
#list 와 tuple은 순서가 있고 set과 dict은 순서가 없다!! -->set은 인덱싱으로 값을 얻을 수 없음

s1=[1,2,3]
set_s1=set(s1)
print(s1,set_s1)

s2=set('hello') #hello를 set으로 만들기!
print(s2) #순서가 없다, 중복을 허용하지 않는다

#즉, set의 저장된 값을 인덱싱으로 접근 하려면 튜플이나 리스트로 변환하여하 순서가 생기므로 가능하다!
#tuple() or list() 이용해야함!

#교집합 차집합 합집합 구할때 매우 유용하다 !!!!
s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])
print(s1&s2) #교집합 s1.intersection(s2)와 동일
print(s1|s2 ) #합집한 s1.union(s2) 와 동일
print(s1-s2) #차집합 = s1.difference(s2)
print(s2-s1) #차집합 = s2.difference(s1) 과 동일

#값추가하기 (add,update)
s1=set([1,2,3]) 
s1.add(5) #값 한개만 추가할때
print(s1)

s1.update((3,5,7,8,10)) 
s1.update([3,2,7,7,2])#값 여러개 추가 할때! #리스트or set등을 이용해서 여러 개를 추가시켜준다!!
print(s1)

s1.remove(2) #특정값 한개만 제거
print(s1)

