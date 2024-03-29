import sys
input=sys.stdin.readline
from collections import Counter
n=int(input())
for _ in range(n):
  cnt,*soldier=map(int,input().split())
  sol=Counter(soldier)
  win=[k for k,v in sol.items() if v>(cnt//2)]
  if win:
    print(win[0])
  else:
    print('SYJKGW')