import sys
input=sys.stdin.readline
n=int(input())
S=set()
for _ in range(n):
  o=input().split()
  if o[0]=='add':
    S.add(int(o[1]))
  elif o[0]=='remove' and int(o[1]) in S:
    S.remove(int(o[1]))
  elif o[0]=='check':
    if int(o[1]) in S:
      print(1)
    else:
      print(0)
  elif o[0]=='toggle':
    if int(o[1]) in S:
      S.remove(int(o[1]))
    else:
      S.add(int(o[1]))
  elif o[0]=='all':
    S=set([i for i in range(1,21)])
  elif o[0]=='empty':
    S=set()