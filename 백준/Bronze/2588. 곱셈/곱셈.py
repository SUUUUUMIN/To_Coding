#2588
#
#입력받기
a=list(map(int,input()))
b=list(map(int,input()))

#자릿수조절
a[0]=a[0]*100
a[1]=a[1]*10

#곱셈
fir=sec=thr=0
for i in range(3):
  fir+=a[i]*b[0]
  sec+=a[i]*b[1]
  thr+=a[i]*b[2]

#출력
print(f'{thr}\n{sec}\n{fir}\n{thr+sec*10+fir*100}')