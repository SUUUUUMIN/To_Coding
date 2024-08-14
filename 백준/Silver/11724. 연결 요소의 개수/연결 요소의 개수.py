import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

from collections import deque
def bfs(val):
    queue = deque([val])
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if visited[w]==False:
                visited[w]=True
                queue.append(w)
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
        cnt += bfs(i)
print(cnt)