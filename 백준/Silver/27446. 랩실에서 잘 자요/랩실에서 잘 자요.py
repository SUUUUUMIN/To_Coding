n,m=map(int,input().split())
page=sorted(list(set(i for i in range(1,n+1))-set(map(int,input().split()))))
last=0 #최근 페이지
ink=0
for p in page:
  if last:
    ink+=min(7,(p-last)*2)
  else:
    ink+=7
  last=p
print(ink)