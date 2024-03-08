import sys
input=sys.stdin.readline

n=int(input())
tot=0
money=[]
for i in range(n):
  money.append(int(input()))
money.sort(reverse=True)

for i in range(n):
  m=money[i]-i
  if m<0:
    break
  else:
    tot+=m
print(tot)