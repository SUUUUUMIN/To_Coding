guitar={}
n=int(input())
for _ in range(n):
  s=0
  a=input()
  for i in a:
    if i.isdigit():
      s+=int(i)
  guitar[a]=(len(a),s)

res=sorted(guitar.items(),key=lambda x:(x[1][0],x[1][1],x[0]))
for i in range(n):
  print(res[i][0])