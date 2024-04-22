import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def dfs(x,y):
  global cnt
  visited[x][y]=True
  if campus[x][y]=='P':
    cnt+=1
  for i in range(4):
    new_x=x+dx[i]
    new_y=y+dy[i]
    if 0<=new_x<n and 0<=new_y<m and not visited[new_x][new_y]:
      if campus[new_x][new_y]!='X':
        dfs(new_x,new_y)

n,m=map(int,input().split())
campus=list(input() for _ in range(n))
visited=[[False]*m for _ in range(n)]
cnt=0

for i in range(n):
  for j in range(m):
    if campus[i][j]=='I':
      dfs(i,j)

if cnt==0:
  print('TT')
else:
  print(cnt)