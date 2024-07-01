n,k=map(int,input().split())
div,res=1,1
for i in range(k):
  div*=n
  res*=k
  n-=1
  k-=1
print(int(div/res))