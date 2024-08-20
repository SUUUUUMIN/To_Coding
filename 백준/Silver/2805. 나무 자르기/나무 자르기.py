n,h=map(int,input().split())
trees=list(map(int,input().split()))
start,end=1,max(trees)

while start<=end:
  mid=(start+end)//2
  cut=0
  for t in trees:
    if t>=mid:
      cut+=t-mid
  
  if cut>=h:
    start=mid+1
  else:
    end=mid-1

print(end)