import datetime as dt
week=['MON','TUE','WED','THU','FRI','SAT','SUN']
def solution(a, b):
    answer = ''
    d=dt.date(2016,a,b)
    answer=week[d.weekday()]
    return answer