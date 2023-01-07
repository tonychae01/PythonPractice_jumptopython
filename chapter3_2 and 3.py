#while 문법과 for 문
#continue: 맨처음으로 다시 돌아가기 break: 루프 빠져나가기
i=10 #3의 배수를 제외하고 프린트하는 출력문 만들기

while i>0:
    if i%3==0:
        i=i-1
        continue
    else: 
        print(i)
        i=i-1
#While 문 무한 루프 종료법 : control+ C 누르기!!

#for 문 : for 변수 in (튜플,리스트,문자열): 모두 가능..

a=[(1,2),(3,4),(5,6)]
for (first,last) in a:
    print(first+last) #for문도 continue 사용가능!

a=range(10) #0~9의미!!
#range(a,b,c) 시작=a ,끝=b-1,c=건너뛸 만큼 간격

#리스트 내포로 한줄로 코딩
a=[1,2,3,4]
result= [num*3 for num in a if num%2==0]
print(result)