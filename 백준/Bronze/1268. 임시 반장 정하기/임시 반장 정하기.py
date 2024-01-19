N=int(input())
students=[]
cnt=[[0 for _ in range(N)] for _ in range(N)]

for _ in range(N):
  temp=list(map(int,input().split()))
  students.append(temp)

for k in range(5):
  for i in range(N):
    for j in range(i+1,N):
      if students[i][k]==students[j][k]:
        cnt[i][j]=1
        cnt[j][i]=1

res=[]
for c in cnt:
  res.append(c.count(1))

print(res.index(max(res))+1)