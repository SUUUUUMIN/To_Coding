N,M,L=map(int,input().split())
cnt=[0 for _ in range(N)]
cnt[0]=1
time=0
idx=0

while True:
  if cnt[idx]==M:
    print(time)
    break
  if cnt[idx]%2==0:  #짝수
    idx=abs((idx-L)%N)
    cnt[idx]+=1
    time+=1
  else:
    idx=(idx+L)%N
    cnt[idx]+=1
    time+=1