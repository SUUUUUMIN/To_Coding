n=int(input())
for i in range(1,n+1):
  li=list(map(int,str(i)))
  res=i+sum(li)
  if res==n:
    res=i
    break
li=list(map(int,str(n)))
if res==(n+sum(li)):
  print(0)
else:
  print(res)