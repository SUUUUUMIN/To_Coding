N=int(input())
F=int(input())

#뒷자리 두 개 떼고 00으로 채우기
n=N//100*100
flag=1          #플래그로 숫자 찾았는지 검색 
while flag==1:
  if n%F==0:
    flag=0
  else:
    n+=1
res=str(n%100)
if len(res)==1:
  print(f'0{res}')
else:
  print(res)