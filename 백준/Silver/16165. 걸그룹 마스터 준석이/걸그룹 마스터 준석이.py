girl={}
n,m=map(int,input().split())
for _ in range(n):
  group=input()
  girl[group]=[]
  for _ in range(int(input())):
    girl[group].append(input())

for _ in range(m):
  text=input()
  que=int(input())
  if que==0:
    li=sorted(girl[text])
    for l in li:
      print(l)
  else:
    key=[k for k,v in girl.items() if text in v]
    print(key[0])