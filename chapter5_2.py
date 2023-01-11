#모듈이란, 함수 변수 클라스 등을 모아두고 코딩한 .py 파일!
#다른 사람이 작성한 모듈을 효과적으로 사용하는 것이 중요! 그리고 import는 같은 디렉터리에 있는 파일,
#혹은 파이썬 라이브러리에 저장된 디렉터리에 있는 모듈만을 불러올 수 있다. 
#특정함수를 사용하려면 모듈이름.함수() 하면된다. 객체의 메소드 사용법과 비슷.. 모듈의 함수사용법!

#모듈 불러오는 방법 1.
#그냥 내 main소스코드와 같은 디렉토리에 모듈파일을 전부 넣어둔다. 즉 main.py와 module1,2,3.py를
#같은 디렉토리에 저장해둔다!!

#모듈불러오는 방법 2. \
'''
내 모듈이 있는 파일의 디렉토리를 복사한 후에 아래와 같이 sys.path(파이썬 내장 라이브러리가 저장된 디렉토리)
에 그 모듈의 디렉토리를 추가해준다. 그러면 그 폴더안에 있는 것들 을 모두 모듈로 사용가능해진다!
(이때 명령 프롬프트창에서는 \혹은/ 둘다 상관없지만 소스코드에서는 /또는 \\만 사용가능하다.!!!)
import sys
sys.path.append("C:\\Users\\Tony\\Desktop\\UT Austin\\jump to python practice\\mymod")
'''

import module1
print(module1.add(3,4))
print(module1.sub(7,2))

#만약에 이렇게 module1.add() 모듈.함수이름 으로 사용하지 않고 그냥 add() 처럼 함수 이름만 사용하고 싶다면
# from 모듈이름 import 모듈 함수 를 하면된다!
from module1 import add
print(add(3,4)) #결과는 같다

#모든 모듈이 있는 내용을 다 쓰고 싶다면?!!!!
from module1 import * #또는 from module1 import add,sub
print(sub(7,7))


###########if __name__=="__main__": 의 의미##########################
'''
만약에 module2.py를 import 한다면 이를 수행하는 순간 module2.py 파일이 자동으로 생성된다. 
하지만 module2 파일에는 print(add(3,4)) 와 print(sub(7,2)) 가 안에 있어서 이것들이 자동으로 출력되게 된다.
이런것들을 main파일 에서 출력하고 싶지 않다면 어떻게 해야할까? 

이런 문제를 방지하려면 module2.py파일의 import시 실행되지 않게 설정하고 싶은 부분을 다음과 같이 설정하면된다. 
if __name__=="__main__":
    print(add(3,4))
    print(sub(7,2))

이런식으로 한다면 main함수에서 직접 이 module2.py파일을 실행하는 경우에는 파이썬 의 내부적 변수인 __name__이
자동으로 __main__으로 바뀌어서 아래가 실행되고 만약import로 인해서 실행되는 경우에는 저 부분은 실행되지 않고 나머지
부분만 실행된다!!!import 했을때는 __name__변수에 이름값인 module2가 이름으로 저장된다. 
'''


#클라스나 변수를 포함하는 모듈 module3.py
import module3
print(module3.PI) #모듈에서 변수사용하는 방법 만약 from module3 import *하면 그냥PI만 써도 된다!

a=module3.Math() #모듈에 있는 클라스로 객체 찍어내는 방법: 모듈이름.클라스이름()
print(a.solv(2)) #메소드 사용은 그대로

print(module3.add(module3.PI,4.4))



 




