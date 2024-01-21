import datetime as dt
daylist=['MON','TUE','WED','THU','FRI','SAT','SUN']
m,d=map(int,input().split())
day=dt.date(2007,m,d)
print(daylist[day.weekday()])