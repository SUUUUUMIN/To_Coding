n=int(input())
li=list(map(int,input().split()))
nli=list(set(li))+[0]
res=-1
for n in nli:
  cnt=li.count(n)
  if cnt==n and cnt>res:
    res=cnt

print(res)