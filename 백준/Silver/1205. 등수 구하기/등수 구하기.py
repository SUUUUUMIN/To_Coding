n,new,p=map(int,input().split())

if n==0:
  print(1)
else:
  score=list(map(int,input().split()))
  score.append(new)
  score.sort(reverse=True)
  if n==p and score[-1]>=new:
    print(-1)
  else:
    print(score.index(new)+1)