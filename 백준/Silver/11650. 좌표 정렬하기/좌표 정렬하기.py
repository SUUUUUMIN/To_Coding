import sys
input=sys.stdin.readline
n=int(input())
res=[list(map(int,input().split())) for _ in range(n)]
new=sorted(res)
for a,b in new:
  print(a,b)