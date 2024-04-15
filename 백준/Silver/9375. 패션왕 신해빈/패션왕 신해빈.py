t=int(input())
for _ in range(t):
  dic={}
  n=int(input())
  for _ in range(n):
    a,b=input().split()
    if b in dic:
      dic[b]+=1
    else:
      dic[b]=1

  cnt=1
  for k in dic:
    cnt*=(dic[k]+1)
  print(cnt-1)