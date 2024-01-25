#2641
c=int(input())
base=list(map(int,input().split()))
n=int(input())
cnt=0
others=[list(map(int,input().split())) for _ in range(n)]
res=[]
reverse={1:3,2:4,3:1,4:2}
for other in others:
  #뒤집어서 비교
  r_other=list(map(lambda x : reverse[x],other))[::-1]
  if base==other or base==r_other:
    res.append(other)
    continue

  #슬라이싱 비교
  for i in range(1,c):
    temp=other[i:]+other[:i]
    r_temp=r_other[i:]+r_other[:i]
    if base==temp or base==r_temp:
      res.append(other)
      break

print(len(res))
for i in range(len(res)):
  print(*res[i])