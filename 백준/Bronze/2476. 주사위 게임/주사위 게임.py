#2476
#
#참여자수
n=int(input())
s=0
res=0

#참여한 사람의 주사위
for _ in range(n):
  a,b,c=map(int,input().split(' '))
  if a==b and b==c:
    s=10000+a*1000
  elif a==b or a==c:
    s=1000+a*100
  elif b==c:
    s=1000+b*100
  else:
    m=max(a,b,c)
    s=m*100
  
  #최대값찾기
  if res<s:
    res=s

print(res)