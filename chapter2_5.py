#dictionary 자료형  순서가 없다!!
#대응 관계를 가진 사전과 같은 자료형 !!
#이러한 대응관계를 가진 것을 'associative array연관배열' or 'hash해시'라고 한다
#파이썬 dictionary --> 1. 순차적이지 않다. 2. key를 통해 value를 얻는다!
#{key1:value,key2:value2, , ...} key 에는 변하지 않는값, value에는 변하는 값을 사용가능!
dic={'name':'pey','phone':'0119999','birth':'1118'}
a={1:"hi"}
b={'a':[1,2,3]} #이렇게 여러가지 자료형을 value에 넣을 수도 있다. 단, key에 리스트는 넣을수없다!!
#하지만 key에 tuple은 넣을 수 있다 즉, key에는 immutable변하지 않는 값만 넣을수 있다!!
#key= only 문자열,숫자,튜플 가능 value:변할수있는값or변하지 않는값 모두가능:문자열 튜플 리스트 숫자 ,딕셔너리 등등

#dictionary 쌍 추가/삭제하기
a={1:'a'}
a[2]='b' #<-- {2:'b'} 쌍을 추가함!!!
print(a)
print(a[1])
a['name']='pey' #a[key]=value 방식을 이용하여 추가한다!!
print(a)
print(a['name'])

del a[1]
print(a) #key 가 1인 것을 삭제한다!
del a['name']
print(a)

#dictionary는 인덱싱이나 슬라이싱 이런게 없고 변수이름[key]=value 이다!!
#key 는 고유한 값이므로 중복되어 사용하지 말자 !! 나머지께 무시됨!

#dictionary 관련 함수들 !!+++++++++++++++++++++++++++++++
a={'name':'pey','phone':'02323','birth':'2221'}
print(a.keys()) #이 함수는 list를 반환하는게 아니라 파이썬 ver 3.0부터는 dict_keys 라는 객체를 반환한다
#리스트로 활용하고 싶다면..list(a.keys()) 로 바꿔줘야함 !! 다른 딕셔너리 함수역시 마찬가지
print(list(a.keys()))
print(list(a.values())) #dict_values 라는 객체를 반환
print(list(a.items())) #dict_items 라는 객체를 반환, (key,value)쌍을 튜플로 반환한다. 

a.clear()
print(a) #모든 딕셔네리 내용을 삭제한다

a={1:'hi','name':'Tony'}
print(a['name'],a.get('name')) #a[key]=value와 함수 a.get(key) 의 차이:전자는 key가 없으면 오류를, 후자는 None을 반환한다
print(a.get('number',1023)) #a.get(key,default value) :해당 key가 없다면 default value를 반환해준다
#매우 유용함 !!!

#해당 key 가 dictionary 안에 있는지 확인: in 활용!

print('name' in a) #있다면 true를 반환한다!


