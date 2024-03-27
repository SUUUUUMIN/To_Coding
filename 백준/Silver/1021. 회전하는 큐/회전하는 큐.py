from collections import deque
n,m=map(int,input().split())
pos=list(map(int,input().split()))
que=deque([i for i in range(1,n+1)])
cnt=0
for p in pos:
  while True:
    if que[0]==p:
      que.popleft()
      break
    else:
      if que.index(p)< len(que)/2:
        que.rotate(-1)
        cnt+=1
      else:
        que.rotate(1)
        cnt+=1
print(cnt)