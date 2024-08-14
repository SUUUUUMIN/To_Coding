import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def dfs(val):
  visited[val]=True
  for i in graph[val]:
    if visited[i]==False:
      dfs(i)
  return 1

n,m=map(int, input().split())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
for _ in range(m):
  u,v=map(int,input().split())
  graph[u].append(v)
  graph[v].append(u)

cnt = 0
for i in range(1, n + 1):
    if visited[i]==False:
        cnt += dfs(i)
print(cnt)