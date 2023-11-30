n=int(input())
for _ in range(n):
  a=list(map(int,input().split()))
  avg=sum(a[1:])/a[0]
  cnt=0
  for i in a[1:]:
    if(i>avg):
      cnt+=1
  rate=(cnt/a[0])*100
  print(f"{rate:.3f}%")