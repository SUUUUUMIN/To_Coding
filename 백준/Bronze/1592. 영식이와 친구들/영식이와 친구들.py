#1592
from collections import deque
N,M,L=map(int,input().split())
chair=deque([i for i in range(1,N+1)])
cnt=[0 for _ in range(N)]
time=-1

while True:
  if max(cnt)==M:
    break
  else:
    c=chair[0]
    cnt[c-1]+=1
    seat=cnt[c-1]
    time+=1

    if seat%2==0:
      chair.rotate(-(L))
    else:
      chair.rotate((L))

print(time)