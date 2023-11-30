def is_prime(n):
  if n==1:
    return False
  for j in range(2,int(n**0.5)+1):
    if n%j==0:
      return False
  return True

natural_list=list(range(2,246912))
decimal_list=[]
for i in natural_list:
  if is_prime(i)==True:
    decimal_list.append(i)

while True:
  num=int(input())
  cnt=0
  if num==0:
    break
  for i in decimal_list:
    if num<i<=2*num:
      cnt+=1
  print(cnt)