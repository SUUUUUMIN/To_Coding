n=int(input())
while n>0:
  num=int(input())
  dic={}
  i=2
  while num>1:
    if num%i==0:
      if i in dic:
        dic[i]+=1
      else:
        dic[i]=1
      num/=i
      i=2
    else:
      i+=1
  for k,v in dic.items():
    print(k,v)
  n-=1