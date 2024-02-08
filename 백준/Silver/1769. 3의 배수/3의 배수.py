num=input()
cnt=0
while len(num)>1:
  temp=0
  for n in num:
    temp+=int(n)
  cnt+=1
  num=str(temp)
if int(num)%3==0:
  print(cnt,'YES')
else:
  print(cnt,'NO')