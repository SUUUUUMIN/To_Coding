ear,eye=map(int,input().split())
listen=set([input() for i in range(ear)])
see=set([input() for i in range(eye)])
res=sorted(list(listen & see))
print(len(res))
for r in res:
  print(r)