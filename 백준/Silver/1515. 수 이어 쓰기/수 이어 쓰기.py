num=input()
cnt=0
while num:
  cnt+=1
  temp=str(cnt)
  while num and temp:
    if num[0] == temp[0]:
      num=num[1:]
    temp=temp[1:]
print(cnt)