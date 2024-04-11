import sys
input=sys.stdin.readline
p,q=map(int,input().split())

word={}
for _ in range(p):
  site,password=input().split()
  word[site]=password

for _ in range(q):
  question=input().strip()
  print(word[question])