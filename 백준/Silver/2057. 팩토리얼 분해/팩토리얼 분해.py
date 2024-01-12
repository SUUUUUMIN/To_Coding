import math
fact=[math.factorial(i) for i in range(21)]
num=int(input())
if num==0:
  print('NO')
else:
  for i in range(20,-1,-1):
    if num>=fact[i]:
      num-=fact[i]
  print('YES') if num==0 else print('NO')   