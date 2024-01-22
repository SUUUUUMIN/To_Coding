n,m=map(int,input().split())
li=[]
for i in range(1,50):
  for j in range(i):
    li.append(i)
print(sum(li[n-1:m]))