#1308
import datetime as dt
now=list(map(int,input().split()))
nex=list(map(int,input().split()))

if now[0]+1000<nex[0]:
  print('gg')
elif now[0]+1000==nex[0] and (now[1],now[2])<=(nex[1],nex[2]):
  print('gg')
else:
  today=dt.date(*now).toordinal()
  dday=dt.date(*nex).toordinal()
  print('D-'+str(dday-today))