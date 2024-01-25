#1816
N=int(input())
for _ in range(N):
  s=int(input())
  for i in range(2,1000001):
    if s%i==0:
      print('NO')
      break
  else:
    print('YES')