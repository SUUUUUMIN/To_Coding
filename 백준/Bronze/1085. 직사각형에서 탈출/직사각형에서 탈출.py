#숫자배열 입력받기
num=list(map(int, input().split()))

#리스트에 할당
#num[0]=x,num[1]=y,num[2]=w,num[3]=h
#경계선은 0이거나 w,h까지의 거리=>abs
a=[]
for i in range(len(num)):
  if i < 2:
    a.append(num[i])
  else:
    a.append(abs(num[i]-num[i-2]))


result=min(a)

print(result)