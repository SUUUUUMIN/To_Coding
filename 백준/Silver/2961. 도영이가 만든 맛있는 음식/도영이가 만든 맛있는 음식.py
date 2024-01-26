from itertools import combinations

n=int(input())
sour=[]
bitter=[]
for _ in range(n):
  a,b=map(int,input().split())
  sour.append(a)
  bitter.append(b)

diff=float('inf')
for i in range(1,n+1):
  #인덱스 번호를 사용해서 조합하기
  idx=list(combinations(list(range(n)),i))

  for food in idx:
    s=1
    b=0
    for j in range(i):
      s*=sour[food[j]]
      b+=bitter[food[j]]
      if abs(s-b)<diff:
        diff=abs(s-b)
print(diff)