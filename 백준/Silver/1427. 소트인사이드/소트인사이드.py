num=input()
li=[]
for n in num:
  li.append(n)
li.sort(reverse=True)
print(''.join(li))