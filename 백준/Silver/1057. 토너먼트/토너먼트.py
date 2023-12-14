#입력받기
n,kjm,ihs=map(int,input().split())
r=0
while kjm!=ihs:
  kjm-=kjm//2
  ihs-=ihs//2
  r+=1

print(r)