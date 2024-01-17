import sys
sys.setrecursionlimit(10000)
def DFS(x,y):
  dx=[1,-1,0,0]
  dy=[0,0,1,-1]
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if(0<=nx<N) and (0<=ny<M):
      if ground[nx][ny]==1:
        ground[nx][ny]=-1
        DFS(nx,ny)

test=int(input())
for _ in range(test):
  M,N,K=map(int,input().split())
  ground=[[0]*M for _ in range(N)]
  cnt=0
  for _ in range(K):
    a,b=map(int,input().split())
    ground[b][a]=1
  for i in range(N):
    for j in range(M):
      if ground[i][j]>0:
        DFS(i,j)
        cnt+=1
  print(cnt)