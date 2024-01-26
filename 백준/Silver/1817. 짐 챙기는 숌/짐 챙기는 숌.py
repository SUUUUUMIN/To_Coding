n,kg= map(int,input().split())
try:
  books=list(map(int,input().split()))
  box=kg
  target=0
  cnt=1

  for i in range(n-1,-1,-1):
    target+=books[i]
    if target>kg:
      cnt+=1
      target=books[i]
  print(cnt)
except:
  print(0)