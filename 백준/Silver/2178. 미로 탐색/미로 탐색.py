n, m = map(int, input().split())
graph = []
for _ in range(n):
  temp=[]
  a=input()
  for i in a:
    temp.append(int(i)) 
  graph.append(temp)
dx=[-1,1,0,0]
dy=[0,0,1,-1]
from collections import deque
def bfs_miro(start): 
    x_pos = start[0]
    y_pos = start[1]
    q = deque()
    q.append( (x_pos, y_pos ) )
    while q:
        x,y = q.popleft()
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < m:
                if graph[next_x][next_y] == 1:
                    graph[next_x][next_y] = graph[x][y] + 1
                    q.append( (next_x, next_y))
bfs_miro((0,0))
print(graph[n-1][m-1])