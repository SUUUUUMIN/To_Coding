import sys
input=sys.stdin.readline

from collections import deque

n,m=map(int,input().split())
graph=[]
visited=[[-1]*m for _ in range(n)]
dx=[1,-1,0,0]
dy=[0,0,-1,1]


def bfs(x,y):
  queue=deque()
  queue.append((x,y))
  visited[x][y]=0

  while queue:
    i,j=queue.popleft()

    for k in range(4):
      nx,ny=dx[k]+i,dy[k]+j
      if 0<=nx<n and 0<=ny<m and visited[nx][ny]==-1:
        if graph[nx][ny]==0:
          visited[nx][ny]=0

        elif graph[nx][ny]==1:
          visited[nx][ny]=visited[i][j]+1
          queue.append((nx,ny))
  return

for i in range(n):
  arr=list(map(int,input().split()))
  graph.append(arr)
  if 2 in arr:
    start_x=i
    start_y=arr.index(2)

bfs(start_x,start_y)

for i in range(n):
  for j in range(m):
    if graph[i][j]==0:
      print(0, end=' ')
    else:
      print(visited[i][j], end=' ')
  print()