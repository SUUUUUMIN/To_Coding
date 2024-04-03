import sys

a,b,c=map(int,sys.stdin.readline().split())
a_menu={}
b_menu={}
c_menu=[]

for _ in range(a):
  m,price=sys.stdin.readline().split()
  a_menu[m]=int(price)

for _ in range(b):
  m,price=sys.stdin.readline().split()
  b_menu[m]=int(price)

for _ in range(c):
  m=sys.stdin.readline().rstrip()
  c_menu.append(m)

n=int(sys.stdin.readline())
a_price,b_price=0,0
b_cnt,c_cnt=0,0

for _ in range(n):
  m=sys.stdin.readline().rstrip()
  if m in a_menu.keys():
    a_price+=a_menu[m]

  elif m in b_menu.keys():
    b_price+=b_menu[m]
    b_cnt+=1

  else:
    c_cnt+=1

res='Okay'
if a_price<20000 and b_cnt>0:res='No'
else:
  if a_price+b_price<50000 and c_cnt>0: res='No'
  elif c_cnt>1: res='No'

print(res)