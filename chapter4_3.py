#출력 방식 1. 모니터 방식 2. 파일로 입출력
#파일 생성하기 --> 내장함수 open이용 , 파일객체=open(파일이름,파일열기모드)

f=open('newfile.txt','w') 
f.close()
#파일 열기모드 :
# 1. r (읽기모드)2. w(쓰기모드-새로운 파일에 쓸때) 3. a(추가모드-있던 파일에 새로운내용 추가할때 사용) 

#파일을 쓰기모드로 열면 해당파일이 이미있으면 원래있던 내용이 모두사라진다.
#만약 없다면 새로운 파일이 생성된다. (쓰기모드일 경우)
#쓰고 열었던 파일을 닫지않고 다시 사용하려면 오류가 생기기에 f.close()를 항상 마지막에 해주자!
#만약 존재하지 않는 파일을 r 모드로 열면 오류가난다.!!

#파일쓰기 모드로 열어서 출력값적기
f=open("새파일.txt",'w')
for i in range(1,11):
    #data="%d 첫번째 줄입니다.\n" %i 이렇게 하던지 아래처럼 하던지
    data="{} line is it. \n".format(i)
    f.write(data) #print(data) 와 별로 다를 것없는 방식!
f.close()

#외부에 저장된 파일을 읽는법! --> 항상 문자열로 읽어준다!
#1. readline함수 사용하기
f=open('새파일.txt','r')
line=f.readline() #파일읽기모드로 연후 한줄만 읽는다
line=f.readline() #한번더 실행하면 다음줄이 된다.!
print(line) #즉 2번째 줄이 출력된다.
f.close
#모든 줄을 출력하고 싶다면,,
f=open('새파일.txt','r')
while True:
    line=f.readline()
    if not line: break #readline함수는 더이상 읽을 게 없다면 None(즉 false)를 리턴한다
    print(line,end='') #이미읽는파일의 마지막에 end=\n이 있으므로 여기서 print마지막을 end=''로바꿔준다
f.close()

#2. readlines 함수 활용하기!!-->모든 줄을 읽어서 각줄을 요소로같는 리스트를 만들어준다
#새파일.txt에서 lines=['1 line is it.\n','2 line is it.\n'....이거다]
f=open('새파일.txt','r')
lines=f.readlines()
for line in lines:
    print(line) #두줄간격으로 출력된다.
print(lines) #원래 lines는 수정되지 않음
f.close
#아래는 문자열 슬라이싱을 이용한 응용예시(뒤에 \n 삭제하기)
f=open('새파일.txt','r')
lines=f.readlines()
for i in range(len(lines)):
    lines[i]=lines[i][:-3] #원래 리스트 수정
    print(lines[i]) #두줄간격으로 출력된다.
print(lines)
f.close

#파일읽는방법 3. read 이용하기 --> 파일 내용 전체를 문자열로 돌려준다!!
f=open('새파일.txt','r')
data=f.read()
print(data)
f.close

#원래있던 내용에 추가하기 (만약w로 열면 기존에 있던 내용은 사라진다!!)
f=open('새파일.txt','a')
for i in range(11,21):
    data='%d is it\n' %i
    f.write(data)
f.close

#참고:with 문-->자동으로file.close해준다
with open('foo.txt','w') as f: #파일객체==f
    f.write('life is too short')