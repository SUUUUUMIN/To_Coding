N,K=map(int,input().split())
num=list(map(int,input().split(',')))

while True:
  if K==0:
    break
  temp=[]
  for i in range(N-1):
    temp.append(num[i+1]-num[i])
  K-=1
  N=N-1
  num=temp
res=[str(t) for t in num]
print(','.join(res))