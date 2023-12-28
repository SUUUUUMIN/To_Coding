N,L,W,H=map(int,input().split())
start,end=0,max(L,W,H)
#이진탐색
for _ in range(1000):
  mid=(start+end)/2
  cnt=(L//mid)*(W//mid)*(H//mid)
  if cnt>=N:
    start=mid
  else:
    end=mid

print('{:.10f}'.format(end))