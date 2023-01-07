#자료형 chapter 2
#1 숫자형

a=14e10+12e9  #실수형
print(a)
a=0o25 #8진수
b=0x22 #16진수
c=0b1011 #2진수
#변환 함수: bin(84) #84를 2진수로 변환 int(01101)#2진수를 10진수로 변환 비슷하게, oct(),hex() 이용 앞의
#진법 표시 0x~ 0o~ 0b~를 지울려면 답[2:]로 슬라이싱을 하면된다!
print(int(0b10),int(0o10),int(0x10),'2진수, 8진수, 16진수')
print(type(int(0b10)))
print(type(bin(64)),bin(64)) #bin은 반환시 정수를 문자형 이진수로 반환
#int(string,base)-->string안의 base 진법의 숫자를 10진수 int로 변환해준다. 즉 int 출력은 항상 10진수
print(int('302',4)) 
#10진수에서 n진수로의 변환은 코드를 직접짜야한다!(2,4,8제외)

#숫자들을 활용하는 연산자
#거듭제곱: ** 이용 ex) 2**4 == 16 or pow(2,4)이용
print(pow(2,4),2**4)
#나눗셈후 나머지 반환: % : ex) 5%2==1
#나눗셈후 몫 반환: // : ex) 4//2: 2 5//2 ==2 즉, 정수값만 반환
#14를 3으로 나누었을때 몫과 나머지를 반환하는 코드:
def dividing(num,x):
    a=num//x
    b=num%x
    return a,b
print(dividing(14,3))

#2 문자형 자료형
# 방법: '',"",""",''' , 그리고 큰따옴표안에 작은 따옴표 있으면 작은 따옴표는 인식되지 않는다
"hello this is Tony's "#여기서 작은 따옴표는 인식 x 역도 성립
#만약 기호 자체를 사용하고 싶으면 backslash 이용 ex) \', \" 등등
#여러줄의 문자열 적기
multiline='''안녕하세요 
채성진 입니다.'''
multiline2="안녕하세요\n채성진 입니다" #중간에 줄바꿈 \n 을 넣어주어야함! 하지만 '''을 쓰면 그러지 않아도 됨
print(multiline,multiline2)
#문자열 연산하기 파이썬은 문자열을 더하고 뺴는 것을 지원한다
#더하기 ,곱하기 지원
head='hello my name is'
tail=' Tony Chae'
answer=head+tail
print(answer)
tail=tail*2
print(tail) #2번 반복해서 붙이기
#문자열 길이 구하기 : len(문자열) 이용

#==================================================================================================
#문자열 포맷팅 관련 내용 ===========================================================================


#문자열 indexing and slicing 항상 0부터 숫자를 센다!!!!순서
letter='apple is red'
print(letter[1])
print(letter[:4]) #0~3번째까지  인덱싱 !!!
#참고: 문자열은 list와 다르게 바꿀수 없는 자료형이다.! immutable
a='pithon'
#a[1]='y' #오류 , 바꿀수 없음!!
output=a[:1]+'y'+a[2:] #이런식으로 직접 슬라이싱을 한후 붙여서 수정해야한다 !!
print(output)
#문자열 formatting하기 즉 특정부분만 계속 바꿔야 할 때 사용 !! 중요
'ex) 현재 온도가 18도 입니다 --> 현재 온도가 30도 입니다' #로 바꿔야하는경우
format='현재 온도가 %d 도 입니다' %3 #이렇게 바로 대입가능!
print(format)
format='현재 %s가 30도 입니다.' %'온도' #이렇게 문자도 대입가능
print(format)
format3='현재 %s가 %d 도 입니다.' %('온도',30) #이렇게 문자도 대입가능 
print(format3)
string='온도' 
temp=30
format4='현재 %s가 %d 도 입니다.' %(string,temp) #이렇게 변수로도 대입가능 
print(format4)
#%d,%f,%c,%s 여기서 %s는 숫자면 자동으로 문자열로 바꿔준다, 문자는 항상  따옴표 이용해야하고!

#참고할점: 문자열안에 %d와 같은 포맷 코드가 존재할 경우 %를 같이 사용불가능 %를 문자열안에 함께쓰려면
#반드시 %%라고 사용하여야 한다!!!!
#line= 'error is %d%' ,%98 #에러남!!
line= 'error is %d%%' %98 # %% 로 작성해야 출력됨 포맷코드 %d랑 같이 사용할 경우
print(line)


#포맷팅 관련 심화
#1. 정렬과 공백
'%10s' %'hi' #10칸 중에 오른쪽 정렬하기
'%-10s' %'hi' #10칸 중에 왼쪽 정렬하기 
a= "%-10sjane" %'hi' #hi는 10칸중 왼쪽 정렬,jane은 그대로 'hi       jane'
print(a)
#또다른 정렬의 방식 포맷 함수 이용하기 , OOP방식 객체지향형
age=20
l = "Hello my name is {0} and age is {1}".format('Tony',age) #여기서 0과 1은 순서를 나타낸다
print(l)
l2 = "Hello my name is {name} and age is {age}".format(name='John',age=16)
print(l2)
#왼쪽정렬
c= "{0:<10} and {1:>10} and {2:!^8}".format('hello','hi','great') 
#순서대로 10칸중 왼쪽 정렬,10칸중 오른쪽정렬, 8칸중 가운데정렬,나머지는 ! 로 채우기
print(c)
number=3.13144214
d= "{0:!>10.4f} 는 결과".format(number)  #:> 오른정렬, :< 왼정렬, :^ 가운데 정렬 
#10칸중에 number의 소수점 4자리까지만 가져오고, 오른쪽 정렬을 한후, 나머지는 느낌표로 채우기!
print(d)
#2.소수점 표현하기





