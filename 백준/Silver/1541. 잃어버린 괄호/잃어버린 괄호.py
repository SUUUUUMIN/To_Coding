#1541
exp=input().split('-')
num=[]

for e in exp:
  s=0
  temp=e.split('+')
  for t in temp:
    s+=int(t)
  num.append(s)

res=num[0]
for i in range(1,len(num)):
  res-=num[i]
print(res)