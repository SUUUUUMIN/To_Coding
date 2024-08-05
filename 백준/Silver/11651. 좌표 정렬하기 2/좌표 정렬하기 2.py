import sys
input=sys.stdin.readline
n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]

graph_s=sorted(graph,key=lambda x:[x[1],x[0]])
for x,y in graph_s:
  print(x,y)