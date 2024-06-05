import sys
input=sys.stdin.readline

n=int(input())
li=[]
for _ in range(n):
  age,name=input().split()
  li.append([int(age),name])
for i in sorted(li,key=lambda x:x[0]):
  print(i[0],i[1])