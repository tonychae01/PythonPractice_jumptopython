#1.
print((80+75+55)/3)
#2
if 13%2==0:
    print('짝수')
else:
    print('홀수')
#3
pin='881120-1068234'
yyyymmdd=pin[:6]
num=pin[7:]
print(yyyymmdd,num)
#방법2
[yyyymmdd2,num2]=pin.split('-') #'-'로 이어진 부분을 기준으로 나누어서 리스트로 처리하기!
print(yyyymmdd2,num2)
#4
if int(num2[0])==1:
    print('man')
else:
    print('woman')
#5
a='a:b:c:d'
print(a.replace(':','#'))
#6
a=[1,3,5,4,2]
a.sort()
a.reverse()
print(a)
#7
a=['life','is','to','short']
result=' '.join(a)
print(result)
#8
a=(1,2,3)
a=a+(4,)
#a=a.add(4) 이 함수는 set에만 사용되는 함수 ! tuple에는 사용불가!
print(a)
#8-참고
a={1,2,3}
a=a.add(4) #주의 set은 a=a+{4}형식으로 요소가 추가되지 못한다!! 반드시 추가하려면 add 사용
print(a)

#9
#왜냐하면 딕셔너리 키는 변하는 값은 사용불가능 따라서key는 immutable한 숫자,문자열,tuple만 key로 사용가능
#10
a={'a':90,'b':80,'c':70}
result=a['b']
result2=a.pop('b') #리스트와 딕셔너리 등등 모두 사용가능하다,key를 뽑고, dictionary에서 삭제함!
print(result,result2,a)
b=[1,2,3]
print(b.pop(1),b) #list에서 pop을 쓰면 그 인덱스의 숫자를 사라지게 해준다!
c=(1,2,3)
#print(c.pop(1),c) #tuple은 변경 불가능한 자료형이므로 pop등을 사용할수 없다!

#11
a=[1,1,2,2,23,3]
aset=set(a)
a=list(aset)
print(a)

#12
#동일한 객체를 가르키기 때문
