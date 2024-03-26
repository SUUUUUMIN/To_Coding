n,l=map(int,input().split())
water=sorted(list(map(int,input().split())))
tape,cnt=0,0
for w in water:
  if w>tape:
    cnt+=1
    tape=w+l-1
print(cnt)