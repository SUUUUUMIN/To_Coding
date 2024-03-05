n,m=map(int,input().split())
board=[]
cnt=[]

for _ in range(n):
  board.append(input())

res=[]
for i in range(n-7):
  for j in range(m-7):
    black=0
    white=0

    for a in range(i,i+8):
      for b in range(j,j+8):
        if(a+b)%2==0:
          if board[a][b]!='B':
            black+=1
          else:
            white+=1
        else:
          if board[a][b]!='W':
            black+=1
          else:
            white+=1
    res.append(black)
    res.append(white)

print(min(res))