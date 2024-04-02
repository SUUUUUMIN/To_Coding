com=input()
l=len(com)
res=set()
for i in range(l):
  for j in range(1,l):
    res.add(com[i:i+j])
print(len(res)+1)