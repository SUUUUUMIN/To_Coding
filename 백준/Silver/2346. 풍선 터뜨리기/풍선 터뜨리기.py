from collections import deque
n=int(input())
q=deque(enumerate(map(int,input().split())))
res=[]

while q:
  idx,num=q.popleft()
  res.append(str(idx+1))

  if num>0:
    q.rotate(-(num-1)) #왼쪽이동
  elif num<0:
    q.rotate(-num)     #오른쪽이동
  
print(' '.join(res))