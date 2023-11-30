T=int(input())
apt=[]
for i in range(T):
  k=int(input())
  n=int(input())
  apt=[x for x in range(1,n+1)]
  for j in range(k):
      for m in range(1, n):
          apt[m] += apt[m-1]
  print(apt[-1])