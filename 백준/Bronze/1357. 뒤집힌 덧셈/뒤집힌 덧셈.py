def rev(a):
  a=list(a)
  b=list(a)
  length=len(a)
  for i in range(length):
    b[i]=a[length-i-1]
  return int(''.join(b))

x,y=input().split()
x=rev(x)
y=rev(y)
res=rev(str(x+y))
print(res)