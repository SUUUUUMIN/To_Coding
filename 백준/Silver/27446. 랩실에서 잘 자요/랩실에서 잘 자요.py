n,m=map(int,input().split())
p=sorted(set(i for i in range(1,n+1))-set(map(int,input().split())))
l,i=0,0
for j in p:
  if l:i+=min(7,(j-l)*2)
  else:i+=7
  l=j
print(i)