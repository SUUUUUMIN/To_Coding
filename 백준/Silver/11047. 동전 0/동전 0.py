n,k=map(int,input().split())
coin=sorted([int(input()) for _ in range(n)],reverse=True)

cnt=0
for c in coin:
  if k>=c:
    cnt+=k//c
    k%=c
    if k<=0: break
print(cnt)