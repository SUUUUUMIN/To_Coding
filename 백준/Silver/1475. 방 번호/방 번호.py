room=input()
cnt=0
li=[0]*10
for r in room:
  if r=='6' or r=='9':
    if li[6] <= li[9]:
      li[6]+=1
    else:
      li[9]+=1
  else:
    li[int(r)]+=1
print(max(li))