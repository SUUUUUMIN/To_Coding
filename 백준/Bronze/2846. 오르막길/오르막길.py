n=int(input())
road=list(map(int,input().split()))+[0]
up=[]
temp=[]
for i in range(n):
  if road[i]<road[i+1]:
    temp.append(road[i])
  elif road[i]>=road[i+1] or i==n-1:
    temp.append(road[i])
    up.append(temp)
    temp=[]
h=[]
for u in up:
  h.append(max(u)-min(u))
print(max(h))