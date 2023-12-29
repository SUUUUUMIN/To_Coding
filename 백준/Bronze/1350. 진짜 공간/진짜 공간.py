N=int(input())
file=list(map(int,input().split()))
cluster=int(input())

cnt=0
for f in file:
  if f==0:
    pass
  elif f%cluster==0:
    cnt+=f//cluster
  else:
    cnt+=(f//cluster)+1

print(cnt*cluster)