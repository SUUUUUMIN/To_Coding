num=list(map(int,input()))
cnt=0
while len(num)>1:
  num=list(map(int,str(sum(num))))
  cnt+=1
if num[0]%3==0:
  print(cnt,'YES')
else:
  print(cnt,'NO')