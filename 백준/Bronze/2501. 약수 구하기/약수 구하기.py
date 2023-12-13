#입력받기
n,k=map(int,input().split(' '))

#약수 만들기
li=[]
for i in range(1,n+1):
  if n%i == 0:
    li.append(i)

#k번째 출력하기
if len(li)<k:
  print(0)
else:
  print(li[k-1])