from itertools import permutations
n=int(input())
nlist=[i+1 for i in range(n)]
for p in permutations(nlist):
  print(*p)