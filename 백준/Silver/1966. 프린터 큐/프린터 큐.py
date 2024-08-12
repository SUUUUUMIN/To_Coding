from collections import deque
t=int(input())
for _ in range(t):
  n,idx=map(int,input().split())
  queue=deque(list(map(int,input().split())))
  cnt=0
  while queue:
    big=max(queue)
    first=queue.popleft()
    idx-=1

    if big==first:
      cnt+=1
      if idx<0:
        print(cnt)
        break
    else:
      queue.append(first)
      if idx<0:
        idx=len(queue)-1