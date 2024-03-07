def dfs(x,y):
  # '-' 인 경우
  if graph[x][y]=='-':
    graph[x][y]=1 #방문 확인
    for d in [1,-1]: #좌우 확인
      newy=y+d 
      if 0<=newy<m and graph[x][newy]=='-':
        dfs(x,newy)
  # '|' 인 경우 
  else:
    graph[x][y]=1 #방문확인
    for d in [1,-1]: #상하 확인
      newx=x+d
      if 0<=newx<n and graph[newx][y]=='|':
        dfs(newx,y)
################################################
n,m=map(int,input().split())
graph=[list(input()) for _ in range(n)]

cnt=0
for i in range(n):
  for j in range(m):
    if graph[i][j] in ['-','|']:
      dfs(i,j)
      cnt+=1
  
print(cnt)