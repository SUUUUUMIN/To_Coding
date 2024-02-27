#1244
def atob(n):
  if n==1: return 0
  else: return 1


n=int(input())
light=list(map(int,input().split()))
t=int(input())

for _ in range(t):
  sex,space=map(int,input().split())

  if sex==1:
    for i in range(space-1,n,space):
      light[i]=atob(light[i])

  else:
    space=space-1
    light[space]=atob(light[space])
    idx=1
    while space-idx>-1 and space+idx<n:
      if light[space-idx]==light[space+idx]:
        light[space-idx]=atob(light[space-idx])
        light[space+idx]=atob(light[space+idx])
      else:
        break
      idx+=1

for i in range(n):
  print(light[i],end=' ')
  if (i+1)%20==0 and i!=0:
    print()