N=int(input())
F=int(input())

#뒷자리 두 개 떼고 00으로 채우기
new_N=N//100*100
flag=1

#F로 나눠지면 플래그가 0으로 변해서 while문 종료
while flag==1:
  if new_N%F==0:  
    flag=0
  else:
    new_N+=1

#결과를 str으로 변환 후 뒤에 두 개 떼기
res=str(new_N%100)
if len(res)==1:     #길이가 1이면 앞에 0 달아주기
  print(f'0{res}')
else:
  print(res)