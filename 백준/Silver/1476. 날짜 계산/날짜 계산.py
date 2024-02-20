e,s,m=map(int,input().split())
earth,sun,moon=0,0,0
cnt=0
while True:
  if earth==e and sun==s and moon==m:
    print(cnt)
    break
  earth+=1; sun+=1
  moon+=1; cnt+=1
  if earth>=16: earth-=15
  if sun>=29: sun-=28
  if moon>=20: moon-=19