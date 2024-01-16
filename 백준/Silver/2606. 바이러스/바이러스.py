N=int(input())
M=int(input())
graph=[[] for _ in range(N+1)]
for _ in range(M):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)
def DFS(v):
  global cnt
  visited[v]=True
  cnt+=1
  for i in graph[v]:
    if not visited[i]:
      DFS(i)
visited=[False for _ in range(N+1)]
cnt=-1
DFS(1)
print(cnt)