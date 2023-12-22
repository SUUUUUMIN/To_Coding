N,m,M,T,R=map(int,input().split())
exc=0 #운동 시간
time=0 #전체
X=m  #혈압

if M-m < T:     #최고혈압-최저혈압 < 운동혈압 => -1
  print(-1)
else:
  while exc<N:  #운동횟수만큼
    if X+T<=M:  #M보다 적거나 같으면 운동가능
      exc+=1
      time+=1
      X+=T
    else:       #M보다 크면 운동불가능=>휴식
      time+=1
      X-=R
      if X<m:
        X=m
  print(time)