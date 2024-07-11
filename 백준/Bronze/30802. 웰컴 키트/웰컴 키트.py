n=int(input())
size=list(map(int,input().split()))
t,p=map(int,input().split())
shirt=0
for s in size:
  if s==0 or s%t==0:
    shirt+=s//t
  else:
    shirt+=(s//t+1)
print(shirt)
print(n//p, n%p)