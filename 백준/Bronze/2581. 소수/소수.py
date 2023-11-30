M=int(input())
N=int(input())
cnt=[]
for i in range(M,N+1):
  if i==1:
    pass
  elif i==2:
    cnt.append(i)
  else:
    for j in range(2,i):
      if i%j==0:
        break
      elif j==i-1:
        cnt.append(i)
if len(cnt)==0:
  print('-1')
else:
  print(sum(cnt))
  print(min(cnt))