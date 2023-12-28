N,L,D=map(int,input().split())
tot=(N*L)+(N-1)*5
rest=[]

#쉬는 데이터
for i in range(L,tot,L+5):
  for j in range(5):
    rest.append(i+j)

result=0
idx=1
while True:
  bell=D*idx
  if bell in rest:
    result=bell
    break
  else:
    idx+=1
  if bell >= tot:
    result=bell
    break

print(result)