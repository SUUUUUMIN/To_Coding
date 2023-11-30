def is_prime(n):
  if n==1:
    return False
  for j in range(2,int(n**0.5)+1):
    if n%j==0:
      return False
  return True

a,b = map(int,input().split())
natural_list=list(range(a,b+1))
for i in natural_list:
  if is_prime(i)==True:
    print(i)