s=0
while True:
  n=int(input())
  if n==0:
    break
  else:
    name=[input() for _ in range(n)]
    cnt=[]
    for _ in range(2*n-1):
      a,b=input().split()
      if a not in cnt:
        cnt.append(a)
      else:
        cnt.remove(a)
    s+=1
    print(s,name[int(cnt[0])-1])