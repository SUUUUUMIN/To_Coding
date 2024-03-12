n,m=map(int,input().split())
li=list(map(int,input().split()))
cnt=0
l,r=0,0
while r<n:
  temp=li[l:r+1]
  if sum(temp)==m:
    cnt+=1
    r+=1
  elif sum(temp)<m:
    r+=1
  else:
    l+=1
print(cnt)