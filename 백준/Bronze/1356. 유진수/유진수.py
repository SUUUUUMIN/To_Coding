n=input()
le,ri=1,1

for i in range(1,len(n)):
  le,ri=1,1
  for j in range(i):
    le*=int(n[j])
  for k in range(i,len(n)):
    ri*=int(n[k])
  if le==ri:
    print('YES')
    break
else:
  print('NO')