#1159
import sys
input=sys.stdin.readline

n=int(input())                #선수 수
player={}

for _ in range(n):
  name=input()
  if name[0] not in player:   #선수이름 첫글자가 없으면 1
    player[name[0]]=1
  else:                       #선수이름 첫글자가 있으면 누적 1
    player[name[0]]+=1

play=list(player.items())     #딕셔너리 -> 리스트

res=[]

for item in play:
  if item[1]>=5:              #개수가 5개 이상이면
    res+=item[0]              #추가

if n<5 or len(res)==0:       #선수가 5명 이하, 같은 성 5개없으면 탈락
  print('PREDAJA')
else:
  print(''.join(sorted(res)))   #정렬하면서문자열로 출력