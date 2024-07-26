n,k=map(int,input().split())
li=[i+1 for i in range(n)]

idx=0
res=[]

while len(li)>1:
  idx=(idx+k-1)%len(li)
  res.append(li.pop(idx))

print('<', end='')
for r in res:
  print(r,end=', ')
print(li[0],end='>')