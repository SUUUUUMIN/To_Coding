#9012
n=int(input())
for i in range(n):
  lis=str(input())
  stack=[]
  for j in lis:
    if j=='(':
      stack.append(j)
    elif j==')':
      if stack:
        stack.pop()
      else:
        print('NO')
        break
  else:
    if not stack:
      print('YES')
    else:
      print('NO')