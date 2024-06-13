import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)

n=int(input())
graph=[[] for _ in range(n+1)]
for i in range(n-1):
  x,y=map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)

parents=[0] * (n+1)
def dfs(v):
  for i in graph[v]:
    if not parents[i]:
      parents[i]=v
      dfs(i)

dfs(1)

for i in range(2,n+1):
  print(parents[i])