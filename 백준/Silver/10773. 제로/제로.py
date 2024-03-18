import sys
input=sys.stdin.readline
k=int(input())
number=[]
for _ in range(k):
  n=int(input())
  if n==0:
    number.pop()
  else:
    number.append(n)
print(sum(number))