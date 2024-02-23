num=int(input())
cnt=0
total=0
while True:
  cnt+=1
  total+=cnt
  if total>num:
    print(cnt-1)
    break