t=int(input())
stack=[]
op=[]
flag=True
cnt=1

for _ in range(t):
  n=int(input())
  while cnt<=n:
    stack.append(cnt)
    op.append('+')
    cnt+=1

  if stack[-1]==n:
    stack.pop()
    op.append('-')
  else:
    flag=False
    break

if flag:
  for o in op:
    print(o)
else:
  print('NO')