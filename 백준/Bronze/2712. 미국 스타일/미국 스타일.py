N=int(input())
#딕셔너리
dic={'kg':[2.2046,'lb'],'lb':[0.4536,'kg'],'l':[0.2642,'g'],'g':[3.7854,'l']}

for _ in range(N):
  res=0
  a,b = input().split()
  res=dic[b][0]*float(a)          #소수점이 들어오는 경우 있음
  print(f'{res:.4f} {dic[b][1]}') #소수점 4자리 출력