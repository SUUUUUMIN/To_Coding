def dfs(x,y):
  if x<0 or y<0 or x>=n or y>=n or visited[x][y]==1:
    return
  
  step=game[x][y] #점프

  if step==-1:
    visited[x][y]='end'
    return

  visited[x][y]=1
  dfs(x,y+step) #오른쪽
  dfs(x+step,y) #아래


n=int(input())
game=[list(map(int,input().split())) for _ in range(n)]
visited=[[0]*n for _ in range(n)]

dfs(0,0)
if visited[-1][-1]=='end':
  print('HaruHaru')
else:
  print('Hing')