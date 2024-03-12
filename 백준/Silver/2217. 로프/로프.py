import sys
input=sys.stdin.readline
n=int(input())
rope=[int(input()) for _ in range(n)]
rope.sort()
weight=-1
for r in rope:
    if weight<(r*n):
        weight=r*n
    n-=1
print(weight)