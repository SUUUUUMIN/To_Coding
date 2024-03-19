n,m,k=map(int,input().split())
sing={}
for _ in range(m):
  tot=list(input().split())
  for i in range(0,len(tot),2):
    if tot[i] in sing:
      sing[tot[i]]=max(sing[tot[i]],float(tot[i+1]))
    else:
      sing[tot[i]]=float(tot[i+1])
val=sorted(list(sing.values()),reverse=True)
print(round(sum(val[:k]),1))