from itertools import permutations
n=int(input())

for p in permutations([i+1 for i in range(n)]):
  print(*p)