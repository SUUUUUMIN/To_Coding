N, L=map(int,input().split())
label=[]
idx=1
while len(label)<N:
  if str(L) in str(idx):
    idx+=1
  else:
    label.append(idx)
    idx+=1
print(max(label))