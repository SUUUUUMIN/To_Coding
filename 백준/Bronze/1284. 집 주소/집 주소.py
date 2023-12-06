#1284 집 주소

a=[]
#0이들어올때까지 반복
while 1:
  num=list(map(int,input()))
  num_len=len(num)
  sum=0
  if num[0]==0 and num_len==1:
    break
  else:
    sum=2+num_len-1
    for i in num:
      if i==1:
        sum+=2
      elif i==0:
        sum+=4
      else:
        sum+=3
    a.append(sum)

for item in a:
  print(item)