#1267 핸드폰 요금

#개수랑 숫자 입력받기
n=int(input())
num=list(map(int,input().split()))

#영식요금계산(30초마다10원)
ys=10*n
for y in num:
  ys+=(y//30)*10

#민식요금계산(60초마다15원)
ms=15*n
for m in num:
  ms+=(m//60)*15

#요금제 비교
if ys<ms:
  print('Y',ys)
elif ys>ms:
  print('M',ms)
else:
  print('Y M',ys)