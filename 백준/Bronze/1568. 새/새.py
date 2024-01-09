bird=int(input())
time=1
k=1
while True:
  bird-=k
  if bird==0:
    break
  elif bird<0:
    bird+=k   #원상회복
    k=1
  else:
    time+=1
    k+=1
print(time)