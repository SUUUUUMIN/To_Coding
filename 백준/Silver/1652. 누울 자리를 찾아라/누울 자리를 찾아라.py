n=int(input())
li=[input() for _ in range(n)]

row,col=0,0
for i in range(n):
  rp,cp=0,0
  for j in range(n):
    if li[i][j]=='.':
      rp+=1
    else:
      rp=0
    if rp==2:
      row+=1
    
    if li[j][i]=='.':
      cp+=1
    else:
      cp=0
    if cp==2:
      col+=1

print(row,col)