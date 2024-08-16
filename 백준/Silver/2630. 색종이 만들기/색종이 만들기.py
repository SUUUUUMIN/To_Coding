n=int(input())
paper=[list(map(int,input().split())) for _ in range(n)]
zero,one=0,0

def find_paper(x,y,n):
  global zero,one
  color=paper[x][y]
  for i in range(x,x+n):
    for j in range(y,y+n):
      if color!=paper[i][j]:
        find_paper(x,     y,     n//2)
        find_paper(x,     y+n//2,n//2)
        find_paper(x+n//2,y,     n//2)
        find_paper(x+n//2,y+n//2,n//2)
        return
  if color==0:
    zero+=1
  else:
    one+=1

find_paper(0,0,n)
print(zero)
print(one)