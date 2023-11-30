T=int(input())
for i in range(T):
  h,w,n=map(int,input().split())
  y=n%h
  x=n//h+1
  if n % h == 0:
    x = n//h
    y = h
  if x<10:
    print(f'{y}0{x}')
  else:
    print(f'{y}{x}')