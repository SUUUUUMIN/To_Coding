r=list(map(int,input().split(':')))
s=list(map(int,input().split(':')))
res=(s[0]-r[0])*3600+(s[1]-r[1])*60+(s[2]-r[2])
if res<0:
  res+=3600*24
h=res//3600
m=(res%3600)//60
s=(res%3600)%60

print('%02d:%02d:%02d'%(h,m,s))