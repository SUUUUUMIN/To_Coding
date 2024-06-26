while True:
  li=sorted(list(map(int,input().split())))
  if sum(li)==0:
    break
  lix=[i**2 for i in li]
  if sum(lix[:2])==lix[2]:
    print('right')
  else:
    print('wrong')