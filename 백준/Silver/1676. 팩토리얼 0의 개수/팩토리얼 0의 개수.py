import math
n=int(input())
number=str(math.factorial(n))[::-1]
zero=0
for i in number:
  if i=='0': zero+=1
  else: break
print(zero)