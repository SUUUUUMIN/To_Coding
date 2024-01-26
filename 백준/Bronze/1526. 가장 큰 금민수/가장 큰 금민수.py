num=int(input())
for i in range(num,3,-1):
  s=str(i)
  flag=True
  for j in range(len(s)):
    if s[j]!='4' and s[j]!='7':
      flag=False
  if flag:
    print(i)
    break