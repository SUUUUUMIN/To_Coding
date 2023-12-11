# 2010
#시간초과 해결
import sys
input=sys.stdin.readline

#멀티탭 개수
n=int(input())

#멀티탭의 플러그의 전체 개수
cnt=0
for i in range(n):
  cnt+=int(input())

#연결 가능한 플러그 수
#멀티탭이 2개인데 플러그가 3개씩이면 전체 6개 플러그 중에서 1개는 멀티탭-멀티탭을 연결해줘야 함
ful=n-1
res=cnt-ful
print(res) 