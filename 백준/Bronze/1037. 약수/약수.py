#1037
N=int(input())
res=list(map(int,input().split()))
if N==1:
  print(res[0]*res[0])
else:
  res.sort()
  print(res[0]*res[-1])