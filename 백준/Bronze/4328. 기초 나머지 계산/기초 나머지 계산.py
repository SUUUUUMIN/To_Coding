while True:
  li=input().split()
  if li[0]=='0':
    break
  else:
    b=int(li[0])
    num=int(li[1],b)%int(li[2],b)
    base=''
    while num>=b:
      num,mod=divmod(num,b)
      base+=str(mod)
    base+=str(num)
    print(base[::-1])