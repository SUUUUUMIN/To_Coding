#시간초과
import sys
input=sys.stdin.readline
#입력
N=int(input())
li=[int(input()) for _ in range(N)]

#내림차순 정렬
li.sort(reverse=True)
#큰 3개 비교
for i in range(N-2):
  if li[i]<li[i+1]+li[i+2]:
    s=li[i]+li[i+1]+li[i+2]
    break
  else:
    s=-1
#출력
print(s)