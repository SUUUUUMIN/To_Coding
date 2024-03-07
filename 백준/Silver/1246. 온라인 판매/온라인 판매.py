n,m=map(int,input().split())
cost=[int(input()) for _ in range(m)]
res={}
for c in cost:
  cnt=0
  for i in cost:
    if c<=i and cnt<n:
      cnt+=1
  res[c]=cnt*c
li=sorted(res.items(),key=lambda x:-x[1])
print(li[0][0],li[0][1],end=' ')