#문자열 관련 함수들! 사용빈도 높다 !!!!
#주로 문자열변수.함수이름 () 형식으로 내장함수를 사용!! 
#1. 문자열함수 종류들
a='hobby'
x= a.count('b') #특정 문자 몇개 있는지 세기
print(x)
a= 'Python is the best choice'
x=a.find('b') #b가 처음 나온 위치를 반환해준다 존재하지 않는다면 -1 반환
print(x,a[x])
x=a.index('t') #find와 다른점은 없으면 오류를 발생시킨다. 
print(x)
x=','.join('abcd') #문자열 각각 사이에 ,를 삽입한다. tuple이나 list에도 사용가능한 메소드이다!
print(x)
y=','.join(['a','b','c'])
print(y,type(y)) #list에 join을 사용하면 하나로 합쳐준다. !!

a='hi'
a.upper() #대문자
print(a)
b='HI'
b.lower() #소문자
print(b)

a=' hi  '
print(a.lstrip(), a.rstrip(),'왼쪽 공백지움, 오른쪽 공백지움')
print(a.strip(),'양쪽 공백지움')

#문자열 바꾸기 replace
a='life is too short'
y=a.replace('life','leg') #특정 문자열을 오른쪽것으로 바꾸기! 보통 문자열은 수정불가능하지만 이거는 가능!
print(y)

#문자열 나누기 split
z=a.split()
print(z) #공백을 기준으로 리스트로 나누어준다 !!!
b='life:is:to:short'
z=b.split(':') #  :를 기준으로 리스트로 나누어준다 !!!!!
print(z)