p=int(input())
atm=sorted(list(map(int,input().split())))
tot,cnt=0,0
for a in atm:
  cnt+=a
  tot+=cnt
print(tot)