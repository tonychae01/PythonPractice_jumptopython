#매개변수(parameter) 와 인수(argument) 
def add(a,b): #여기서 a,b는 매개변수, 함수의 입력으로 전달된 값을 받는 변수
    return a+b
print(add(3,4)) #여기서 3,4는 인수 즉 함수를 호출할때의 입력 값
#입력값이 없고 결과값만 있는 함수
def say():
    return 'hi'
a=say() #a라는 변수에 결과값(반환값) hi 가 저장된다.
print(say())
#입력과 결과 모두 없는 함수
def hi():
    print('Hiheloo')
    return None
a=hi() #print실행만 되고 a에는 아무것도 저장 x
hi()
print(a) #아무 것도 출력되지 않음

#함수의 입력값이 몇개가 될지 모를때는 how? def 함수이름(*parameter이름(매개변수)) 형식으로 사용!
#여기서 매개변수 이름 앞에 *을 붙이면 입력값을 전부 모아서 튜플로 만들어준다!

def add_mul(choice,*args):
    if choice=='add':
        result=0
        for i in args:
            result+=i
    return result

result=add_mul('add',1,3,4,5) #여기서 args=(1,3,4,5) 튜플 형식으로 전달!
print(result)

#keyword parameter 앞에 **를 붙이면 그 매개변수는 딕셔너리가 된다.
def key(**kword):
    print('hello')
    return kword
a=key(a='1',b='2',c='3') 
print(a) #매개변수를 딕셔너리로 만들어준다!

#함수의 결과값(반환값) 은 언제나 return이며, 항상 한개이다!!!
#함수는 return이 되면 바로 함수를 빠져나간다! 또 return 만 써서 함수를 빠져나갈수도 있다.!(자주 사용팁)
#함수는 여러개의 값이 들어있다면 튜플로 한개로 만들어서 결과값을 반환 한다
def mul(a,b):
    return a+b,a*b
result1,result2=mul(3,5) #튜플형식으로 받기(result1,result2) 괄호 생략가능!

print(result1,result2)

#함수 매개변수의 초기화(default 값 설정) #반드시 초기화된 변수를 가장 뒤에 둘것!!
#왜냐하면 중간에 들어가면 오류남
def say_my(name,old,man=True):
    print('name',name)
    print('old',old)
    if man:
        print('남자입니다.')
    return
say_my('TOny',25) #이렇게 인수(argument)를 2개만  줘도 나머지 한개는 디폴트로 처리됨!

#함수내 변수의 효력 범위 -->함수 내에서만 작동
a=1
def vartest(a):
    a=a+1
vartest(a) #실행,return None
print(a) #a는 여전히 1 왜냐하면 함수 내부의 변수에 영향 X
#즉 함수 내부의 변수이름은 바깥의 변수이름과는 전혀상관이 없다.

#해결법 1: return을 통하여 값을 구한후 그것을 외부의 변수에 다시 대입하는것!
#해결법 2: global 명령어를 사용하기!!(전역변수 선언) 좋은 방법은 아님

a=1
def vartest2():
    global a #내부의 변수를 바깥에도 적용하겠다는 뜻!
    a=a+1

vartest2()
print(a) #여기서는 a가 2로 출력됨!

#lambda!! 
#함수를 생성할때 사용하는 예약어로, def와 동일한 역할을 한다. but 함수를 한줄로 간결하게 만들때 사용
#lambda 매개변수 1,매개변수 2, ... : 매개변수를 사용한 표현식

add=lambda a,b:a+b #함수이름 :add , lambda는 return 명령어가 없어도 결과를 반환해준다!

result=add(3,4)
print(result)