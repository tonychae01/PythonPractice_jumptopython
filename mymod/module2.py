import module2
def add(a,b):
    return a+b
def sub(a,b):
    return a-b

if __name__=="__main__": #이렇게 하면 import 할때ㅐ 이부분은 실행이 되지 않음 only main파일에서 실행할때만 실행됨!
    print(add(3,4))
    print(sub(7,2))
