import sys
input=sys.stdin.readline

n,t=map(int,input().split())
li=list(map(int,input().split()))

acc=0
acc_li=[0]
for i in li:
  acc+=i
  acc_li.append(acc)

for _ in range(t):
  a,b=map(int,input().split())
  print(acc_li[b]-acc_li[a-1])