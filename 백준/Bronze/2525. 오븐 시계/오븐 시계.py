H,M=input().split()
C=input()
H=int(H)
M=int(M)
C=int(C)
plus=0
if C < 60:
  new_M=M+C
  if new_M >= 60:
    new_M=new_M%60
    plus=1
  if plus==1:
    new_H=H+1
  else:
    new_H=H
elif C > 60:
  new_M=M+C%60
  new_H=H+C//60
  if new_M >= 60:
    new_M=new_M%60
    plus=1
  if plus==1:
    new_H=new_H+1
  else:
    new_H=new_H
else:
  new_M=M
  new_H=H+1

if new_H>=24:
  new_H=new_H-24

print(new_H,new_M)