import sys
input=sys.stdin.readline

n=int(input())
time=[list(map(int,input().split())) for _ in range(n)]
time.sort(key=lambda x:(x[1],x[0]))

cnt=0
end=0

for s,t in time:
  if s>=end:
    end=t
    cnt+=1

print(cnt)