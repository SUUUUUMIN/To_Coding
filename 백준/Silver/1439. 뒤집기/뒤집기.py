num=input()
li=[]
temp='\0'
for n in num:
  if temp != n:
    li.append(n)
    temp=n
zero=li.count('0')
one=li.count('1')
if zero==0 or one==0:
  print(0)
elif zero>one:
  print(one)
else:
  print(zero)