#배열
li=[64,32,16,8,4,2,1]
cnt=0
x=int(input())

#반복
for num in li:
  if x>=num:
    cnt+=1
    x-=num

  if x==0:
    break
print(cnt)