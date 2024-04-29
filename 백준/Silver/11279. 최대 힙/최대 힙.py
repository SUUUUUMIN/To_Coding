import sys
input=sys.stdin.readline
import heapq
hq=[]
n=int(input())
for _ in range(n):
  a=int(input())
  if a==0:
    if hq:
      print(-(heapq.heappop(hq)))
    else:
      print(0)
  else:
    heapq.heappush(hq,-a)