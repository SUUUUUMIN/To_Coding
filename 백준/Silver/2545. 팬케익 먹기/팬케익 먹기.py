n=int(input())
for _ in range(n):
  s=input() #공백잡아먹기
  box=list(map(int,input().split()))
  d=box[-1]
  box=box[:-1]
  cake=box[0]*box[1]*box[2]
  for _ in range(d):
    box.sort()
    cake-=(box[0]*box[1])
    box[2]-=1
  print(cake)