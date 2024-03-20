n=int(input())
li=list(map(int,input().split()))
num=int(input())

left=right=res=0

if num in li:
  res=0
else:
  li.append(num)
  li.append(0)
  li.sort()
  idx=li.index(num)
  left=li[idx-1]
  right=li[idx+1]
  res=(num-left)*(right-num)-1
print(res)