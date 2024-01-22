num=list(map(int,input()))
for i in range(len(num)-1,0,-1):
  if num[i]>=5:
    num[i-1]+=1
    num[i]=0
  else:
    num[i]=0
print(''.join(str(i) for i in num))