N,M=map(int,input().split())
picture=[[0]*100 for x in range(100)] #그림

for _ in range(N):
  lx,ly,rx,ry=map(int,input().split())
  for i in range(lx,rx+1):
    for j in range(ly,ry+1):
      picture[i-1][j-1]+=1

cnt=0
for i in range(100):
  for j in range(100):
    if picture[i][j]>M:
      cnt+=1
print(cnt)