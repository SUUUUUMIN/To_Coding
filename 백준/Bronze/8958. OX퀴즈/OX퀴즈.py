n=int(input())
for i in range(n):
  T=list(input())
  sum=0
  total=0
  for i in range(len(T)):
    if(T[i]=='O'):
      sum+=1
      total+=sum
    else:
      sum=0
  print(total)