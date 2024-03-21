import heapq

heap=[]
T=int(input())
for _ in range(T):
  command=list(map(int,input().split()))
  if len(command)==1:
    if not heap:
      print(-1)
    else:
      print(-(heapq.heappop(heap))) 
  else:
    for i in range(command[0]):
      heapq.heappush(heap,-command[i+1])