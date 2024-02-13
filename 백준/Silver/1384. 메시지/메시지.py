cnt=1
while True:
  name=[]
  word=[]
  nasty=1
  n=int(input())
  if n==0:
    break
  for _ in range(n):
    na,*aa=input().split()
    name.append(na)
    for a in aa:
      word.append(a)
  print(f'Group {cnt}')
  size=n-1
  for i in range(len(word)):
    if word[i]=='N':
      print(f'{name[size]} was nasty about {name[i//(n-1)]}')
      nasty=0
    size-=1
    if size<0:
      size=n-1
  if nasty:
    print('Nobody was nasty')
  print()
  cnt+=1