import sys
input=sys.stdin.readline
P,C=map(int,input().split())
pocket={}
for i in range(1,P+1):
  pocketmon=input().rstrip()
  pocket[str(i)]=pocketmon
  pocket[pocketmon]=str(i)

for _ in range(C):
  quest=input().rstrip()
  print(pocket[quest])