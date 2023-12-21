cnt=0
for i in range(8):
  a=[]
  a=list(input())
  if i%2==0:             #짝수행
    for j in range(8):
      if j%2==0:         #짝수번째
        if a[j]=='F':
          cnt+=1
  else:                  #홀수행
    for j in range(8):
      if j%2==1:         #홀수번째
        if a[j]=='F':
          cnt+=1

print(cnt)