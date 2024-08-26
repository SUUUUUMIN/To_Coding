from collections import deque
m,n=map(int,input().split())
queue=deque([])
dx,dy=[1,-1,0,0],[0,0,1,-1]
ground=[]
res=0

for i in range(n):
  arr=list(map(int,input().split()))
  ground.append(arr)
  for j in range(m):
    if arr[j]==1:
      queue.append([i,j])

def bfs():
  while queue:
    i,j=queue.popleft()

    for k in range(4):
      nx,ny=dx[k]+i,dy[k]+j
      if 0<=nx<n and 0<=ny<m and ground[nx][ny]==0:
        ground[nx][ny]=ground[i][j]+1
        queue.append([nx,ny])

bfs()


bfs()
for i in ground:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)