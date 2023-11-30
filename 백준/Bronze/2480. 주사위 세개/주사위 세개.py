num1,num2,num3 = input().split()
num1=int(num1)
num2=int(num2)
num3=int(num3)

if (num1==num2)and(num1==num3):
  m=10000+num1*1000
  print(m)
elif (num1==num2)or(num1==num3):
  m=1000+num1*100
  print(m)
elif (num2==num3):
  m=1000+num2*100
  print(m)
else:
  if(num1>num2):
    if(num1>num3):
      max=num1
    else:
      max=num3
  else:
    if(num2>num3):
      max=num2
    else:
      max=num3
  m=max*100
  print(m)