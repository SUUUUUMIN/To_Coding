H, M =input().split()
H=int(H)
M=int(M)
new_M=M-45
new_H=H
if new_M<0:
  new_M=new_M+60
  if H==0:
    new_H=23
  else:
    new_H=H-1
print(new_H,new_M)