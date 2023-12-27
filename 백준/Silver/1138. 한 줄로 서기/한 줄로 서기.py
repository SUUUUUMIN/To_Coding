N=int(input())
li=list(map(int,input().split()))
result=[0]*N 
for i,a in enumerate(li):
  cnt=0  #앞에 키 큰 사람 넣은 횟수
  for j,res in enumerate(result):
    if res==0 and cnt<a:
      cnt+=1
    elif res==0 and cnt==a:
      result[j]=i+1
      break
print(*result)