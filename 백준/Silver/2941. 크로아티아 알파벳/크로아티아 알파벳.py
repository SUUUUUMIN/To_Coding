croatia=['c=','c-','dz=','d-','lj','nj','s=','z=']
S=input()
for i in croatia:
  S=S.replace(i,"*")
print(len(S))  