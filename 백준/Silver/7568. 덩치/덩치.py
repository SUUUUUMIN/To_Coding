n=int(input())
body=[list(map(int,input().split())) for _ in range(n)]

for w1,h1 in body:
  rank=1
  for w2,h2 in body:
   if w1<w2 and h1<h2:
    rank+=1
  print(rank,end=' ')