finger=int(input())
cnt=int(input())

if finger==1:
  print(cnt*8)

elif finger==5:
  print(cnt*8+4)

else:
  if cnt%2==0: #짝수
    cnt=cnt//2
    print((cnt*8)+(finger-1))
  else:
    cnt=cnt//2+1
    print((cnt*8)-(finger-1))