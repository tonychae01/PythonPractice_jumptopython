#클래스!!(가장 중요한 단원)

'''클라스 관련된 내용
-굳이 클라스가 없어도 프로그램을 만들수는 있다. 예를들어 C언어도 클라스가 없다
- 파이썬의 꽃이다.
- 함수나 자료형 처럼 꼭 프로그램에 필요한 요소는 아니지만 강력하다
- 계산기의 더하기 기능을 이용한 프로그램으로 클래스를 익혀보자
- 3을 입력한후 7을 입력한후 4를 더하는 계산기의 경우 계속 이전 결과값을 저장하고 있어야한다. 
이것을 프로그래밍 해보자
'''
result = 0
def add(num): #add는 추가되는 숫자
    global result #전역변수로 선언 외부랑 동기화 !! 함수안에서 만 사용가능
    result+=num
    return result

print(add(3))
print(add(4)) 

#만약 이런 기능을 하는 함수를 만들었는데 2대의 계산기가 필요한 상황이라면 어떻게 해야하나?
#각각을 다른 함수를 2개를 만들어야한다
result1 = 0
result2 = 0
def add1(num): #add는 추가되는 숫자
    global result1 #전역변수로 선언 외부랑 동기화 !! 함수안에서 만 사용가능
    result1+=num
    return result1

def add2(num): #add는 추가되는 숫자
    global result2 #각 함수에서 계산한 결과값을 유지하면서 저장하는 전역변수 
    result2+=num
    return result2

print(add1(3))
print(add1(4))
print(add2(5))
print(add2(6))

#하지만 이대로 계산기가 개수가 10개가 필요하면 함수를 10개, 변수를 10개 만들어야된댜...매우귀찮
#이때, 계산기 라는 특정한 클라스를 만들어서 add 라는 method(기능) 을 추가해보면 어떨까?

class calculator:
    def __init__(self):
        self.result=0
    
    def add(self,num):
        self.result+=num
        return self.result

cal1=calculator() #cal1과 cal2는 이 클라스의 인스턴스(in terms of 관계성)이자. 객체이다.
cal2=calculator() #calculator 클라스로 찍어낸 객체인 cal1 과 cal2 둘은 서로 독립적이다!!! 관계없음

print(cal1.add(4))
print(cal2.add(7)) #단일한 메소드를 사용가능!(기능=함수역할 but 여러개 안만들어도 됨!)
print(cal2.add(3))
#위에서 클라스로 만든 객체는 각각의 역할을 수행하고 다른 계산기의 결과와상관없이 독립적인 값을 유지한다
#계산기의 대수가 늘어나더라도 객체를 생성만 하면 되기 때문에 함수를 사용하는 것보다 간단해진다. 또 여러기능 을 추가가능
'''클라스와 객체
클라스는 과자틀 객체(object)는 찍어낸 과자이다. 객체마다 고유한 성격을 가진다!!!!
그리고 동일한 클라스로 만든 객체는 서로 영향을 주지 못한다. 클라스도 객체를 생성하는 기능이 있다
#인스턴스는 객체와 비슷한 말인데 a는 cookie 클라스의 인스턴스이다. 처럼 관계성속에서 인스턴스라는 단어를 사용하고
a는 인스턴스이다. 보다는 a는 객체이다. 라는 말이 더 어울린다. 보다 주체성과 독립성을 강조

클라스를 만들때는 어떤 속성을 지니게 하는 클라스를 구상을 하고, 그 클라스의 객체가 사용할수있는 기능들은
무엇이 있을지 추가하는 것이다!!
'''
#ex 사칙연산 클라스(class FourCal)
''' a= FourCal() 객체 생성
- 사칙연산을 하려면 두 숫자를 입력받는 setdata 메소드  a.setdata(2,4)
 - 더하고 빼고 나누고 곱하는 add sub div mul method 들 a.add() or a.mul() 등등 하면 반환값이 메소드의 결과

'''
#######################################################
#1. 클라스 구조 만들기!!
class FourCal:
    pass #아무것도 안하기
a= FourCal() #a가 클라스 FourCal의 객체이다.
print(type(a)) #a의 타입이 class이고 클라스 안에 아무것도 없어도 객체를 만드는 기능은 동작한다

#2. 객체에 숫자 지정할수 있게 해주기
class FourCal:
    def setdata(self,first,second): #'클라스 안에 구현된 함수'를 method 라고 한다(명칭 중요)
        self.first=first     #객체에 객체변수 first가 생성되고 값 first가 저장된다. 
        self.second=second  #!!!!객체변수!!!!란 객체에 생성되는 객체만의 변수이다.!!전역변수는 아님
#self의 의미가 중요하다!!메소드의 첫번째 매개변수인 self는 객체 a가 자동으로 전달된다.
#첫번째 방식 (객체 지향적 방식)
# a=FourCal()
# a.setdata(4,2)  객체.메소드(self를 제외한 파라미터) 로 작성
#두번째 방식
# a = FourCal()
# FourCal.setdata(a,4,2) #이렇게 객체자신을 따로 전달해주어야한다!! 이방법은 잘사용하지 않음
a=FourCal()
a.setdata(4,2)#-->self.first=4,self.second= 2 ,self에 객체 a가 전달됨 이렇게 해석
print(a.first) #객체변수 first에 첫번째 값이 4가 전달됨 
print(a.second) #객체변수 second에 두번째 값인 2가 전달됨

#여기서 새로운 객체인 b=FourCal()을 만들자
b=FourCal()
b.setdata(5,3)
print(b.first) #여기서 first변수는 b만의 객체변수이기 때문에a.first와 값이 다르다
print(b.second) #즉 객체끼리는 모든 속성이서로 독립적이다!! 객체변수끼리는 독립적이다.

#더하기 기능 method 만들기
class FourCal: #객체 생성시 생성자의 매개변수가 없으므로 그냥 a=FourCal() 로 생성가능
    def setdata(self,first,second): #'클라스 안에 구현된 함수'를 method 라고 한다(명칭 중요)
        self.first=first     #객체에 객체변수(attribute 라고함) first가 생성되고 값 first가 저장된다. 
        self.second=second 
    def add(self): #self를 입력하면 a객체가 자동으로 전달된다.
        result=self.first+self.second
        return result
a=FourCal()
a.setdata(5,5)
print(a.add())

#########################생성자(Constructor)#####################
a= FourCal()
'''a.add()''' #이렇게 a.setdat(4,2) 이걸실행하지 않으면 객체변수 first,second가 생성되지 않는다 
#따라서 setdata method를 수행하지 않고 method add를 실행하면 오류가 발생한다. (객체변수를 생생먼저해야함)
#따라서 객체에 초기값을 설정해야할 필요가 있을때는 method setdata를 이용하는 것보다는
#생성자를 구현하여(constructor) 객체를 만들때 자동으로 호출되도록 하는 것이 좋다.
#즉 생성자란 객체를 생성할때 자동으로 호출되는 메소드이다!!!!ex 여기서 setdata대신 __init__만들면
#자동으로 객체변수를 만들어준다.

#ex setdata메소드 대신 생성자 __init__사용하기
class FourCal:
    def __init__(self,first,second): #객체 생성시 자동으로 생성된다. 따라서 a=FourCal(4,2) 이런식으로 생성해야함
        self.first=first            #객체 생성시 생성자의 매개변수를 함께 넣어주어야 한다!
        self.second=second   
    def add(self):
        result=self.first+self.second
        return result
    def sub(self):
        result=self.first-self.second
        return result
    def mul(self):
        result=self.first*self.second
        return result
    def div(self):
        result=self.first/self.second
        return result
############클라스의 상속(inheritance) ##############물려받기-->기존 클라스 확장시 사용
#다른 클라스의 기능을 물려받을수 있게하는것!!
#예를 들어 우리가 만든 FourClass에 제곱을 구할 수 있는 기능을 만들자 a^b

#앞에서 FourCal는 이미 만들었으므로 이를 상속하는 MoreFourCal를 만들자(기능 추가가능)
class MoreFourCal(FourCal):#상속
    pass

x=MoreFourCal(5,6)
print(x.add(),x.mul(),x.first) #FourCal의 기능을 전부다 사용가능하다!!!!

'''왜 기존 클라스를 변경하지 않고 상속받아서 사용할까???'''
#왜냐하면 기존 클라스가 라이브러리 형태로 제공되거나 수정이 불가능할 수 있기때문이다!!

#a의 b승을 계산하는 MoreFourCal을 만들자
class MoreFourCal(FourCal):
    def pow(self):
        result =  self.first ** self.second
        return result
#즉 기존에 있던 class는 통째로 복사하고 내가 추가하고 싶은method 만 추가하면된다!!!(상속은 클라스 확장시 사용)
y=MoreFourCal(5,6)
print(y.pow())

##########메소드(method) overwriting##################
#예를 들어서 위에서 FourCal 클라스의 객체 a에서 a=FourCal(4,0) 을 만들면 a.div() 는 0으로 나눌수
#없으므로 오류가 뜬다. 새로운 FourCal() 을 상속하는 SafeFourCal()을 만들자(0으로 나눠도 오류없게)
class SafeFourCal(FourCal):
    def div(self): #같은 method이름을 써서 overwriting 할 경우 부모 메소드보다 자식 메소드가 먼저실행!
        if self.second==0:
            return 0 #안전장치 에러안뜨게
        else:
            return self.first/self.second
    
a=SafeFourCal(4,0)
print(a.div()) #오류가 뜨지 않는다.

#################클라스 변수##################--> 객체 변수랑 무엇이 다를까??

'''객체 변수는 클라스로 찍어낸 각 객체마다 서로 다르게 가지는 고유한 변수이고
멤버변수는 클라스의 모든 객체에 공통적으로 적용되는 변수이다. '''

class Family:
    lastname='kim' #여기서 이건 클라스 변수 

    def name(self,first):  #또는 __init__이용해서 만들어도 된다.
        self.first=first #여기서 first는 객체변수
    #def __init__(self,first):  이렇게 생성자를 이용한다면 객체생성시 Tony=Family(Sungjin) 이런식으로 생성!
        #self.first=first
    def fullname(self):
        return self.first +' '+ self.lastname
Tony=Family() 
John=Family()
Tony.name('Sungjin')
John.name('Caldera')

print(Tony.fullname(),John.fullname())
#실제로 모두 공통되는 클라스 변수보다 객체변수가 더 많이 사용된다!!


