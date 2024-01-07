#1822
a,b=map(int,input().split())
alist=set(map(int,input().split()))
blist=set(map(int,input().split()))
res=sorted(alist-blist)

print(len(res))
if len(res)!=0:
  print(*res)