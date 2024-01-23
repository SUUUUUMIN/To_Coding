n=int(input())
for _ in range(n):
  l=list(map(int, input().split()))
  l.sort()
  print(l[-3])