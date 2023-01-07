#3장 연습문제
a='Life is too short, you need python'

if 'wife' in a: print('wife')
elif 'python' in a and 'you' not in a: print('python')
elif 'shirt' not in a: print('shirt')
elif 'need' in a: print('need')
else: print('none')

#2
result=0
i=1
while i<=1000:
    if i%3==0:
        result=result+i
    i=i+1
print(result)

#3
i=0
while True:
    i+=1
    if i>5:break
    print('*'*i)
#4
for i in range(1,101):
    print(i)
#5
total=0
a=[70,60,50,33,20,98,39]
for i in a:
    total+=i
print(total)

#6
numbers=[1,2,3,4,5]
result=[]
for i in numbers:
    if i%2==1:
        result.append(i*2)
print(result)

result= [i*2  for i in numbers if i%2==1] #리스트 내포 이용
print(result)