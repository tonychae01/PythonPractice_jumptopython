#if 문
'''
x in 리스트 
x in 튜플
x in 문자열
모두 사용가능!! (순서가 있음)
반환 : True or False
x not in 리스트 
x not in 튜플
x not in 문자열

'''
#조건문에서 아무일도 없이 설정하는 법: pass, while문에서 아무일도 없이 설정하는법: continue
#예시
pocket=['hello']
if 'money' in pocket:
    pass
elif 'card' in pocket:
    pass
else:
    print("카드를 꺼내라")

#한줄 if 문 사용법: "조건부표현식"
score=80
if score>=60:
    message='success'
else:
    message='fail'

#이것과 동일하다(이것이 조건부표현식)
message = 'success' if score>=60 else 'fail' # ':'을 빼고 변수를 작성하는 것도 1회로 줄임!!