row,col=map(int,input().split())
castle=[input() for _ in range(row)]
col_guard=[1 for _ in range(col)]
guard=0
for floor in castle:
  for j in range(col):
    if floor[j]=='X':
      col_guard[j]=0
  if 'X' not in floor:
    guard+=1

print(max(guard,sum(col_guard)))