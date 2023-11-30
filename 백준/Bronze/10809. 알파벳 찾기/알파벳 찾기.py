arr=list(input())
for i in range(97,123):
  for j in range(0,len(arr)):
    a=-1
    if chr(i)==arr[j]:
      a=j
      break
  print(a,end=" ")