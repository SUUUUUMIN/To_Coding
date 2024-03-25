n=int(input())
dou, to=map(int,input().split())
dough=int(input())
toping=sorted([int(input()) for _ in range(n)],reverse=True)

price=dough/dou
for i in range(1,len(toping)+1):
  cal=dough+sum(toping[:i])
  cost=dou+to*len(toping[:i])
  if cal/cost>price:
    price=cal/cost

print(int(price))