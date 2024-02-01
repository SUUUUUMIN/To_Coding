import datetime as dt
now=dt.datetime.strptime(input(),'%B %d, %Y %H:%M')
total=dt.datetime(now.year,12,31)-dt.datetime(now.year-1,12,31)
nows=now-dt.datetime(now.year,1,1)

#분으로 바꾸기
tot_minute=total.days*24*60
now_minute=nows.days*24*60 + now.hour*60 + now.minute

print(now_minute/tot_minute*100)