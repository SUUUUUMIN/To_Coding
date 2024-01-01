cnt=1
while True:
  o,w=map(int, input().split())
  if o==0 and w==0: #0 0 종료
    break
  flag=False     #죽음..플래그..?
 
  while True:
    behavior,n=input().split()
    if behavior=='E':
      w-=int(n)
      if w<=0:
        flag=True
    elif behavior=='F':
      w+=int(n)
    elif behavior=='#':
      break
    
  if flag==True:
    print(f'{cnt} RIP')
  elif w>o*(0.5) and w<o*2:
      print(f'{cnt} :-)')
  else:
    print(f'{cnt} :-(')
  cnt+=1