number=list(map(int,input().split()))
mul=min(number)
while True:
  cnt=0
  for num in number:
    if mul%num==0:
      cnt+=1
  if cnt>=3:
    break
  mul+=1

print(mul)