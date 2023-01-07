#사용자 입출력: 사용자가 입력한 변수값을 대입하고 싶다면 어떻게?
a=input('입력하세요: ') #input은 입력되는 모든 것을 문자열로 취급한다
print(a,type(a))
#print 자세히 알기
#우리가 입력한 자료형을 출력해준다

#문자열 띄어쓰기는 콤마로한다
print('life','is','too','short')
#마지막은 default가 줄 건너뛰기
for i in range(10): #한줄로 결과 출력하기
    print(i,end=' ') #이렇게 하면 print의 마지막 default를 ' '로 바꿀수있음!
