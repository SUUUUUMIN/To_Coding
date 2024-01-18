N, L=map(int,input().split())
idx=0
while N>0:
  idx+=1
  if str(L) not in str(idx):
    N-=1
print(idx)