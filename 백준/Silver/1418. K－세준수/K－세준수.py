n=int(input())
k=int(input())
li=[0 for _ in range(n+1)]

cnt=0
for i in range(2,n+1):
  if li[i]==0:
    for t in range(i,n+1,i):
      if t%i==0:
        li[t]=max(li[t],i)

for l in li:
  if l<=k:
    cnt+=1
print(cnt-1)