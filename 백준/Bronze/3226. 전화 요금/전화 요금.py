n=int(input())
t=[input() for _ in range(n)]
call=0
for i in range(n):
  h,m=map(int,t[i].split()[0].split(':'))
  c=int(t[i].split()[1])
  end_h,end_m=h,0

  if c+m >= 60:
    end_h+=1
    end_m=c+m-60
    if end_h>23:
      end_h=0
  else:
    end_m=c+m
  
  if (end_h==7 or end_h==19) and m>=end_m and end_m!=0:
    if end_h==7:
      call+=(c-end_m)*5+end_m*10
    elif end_h==19:
      call+=(c-end_m)*10+end_m*5
  else:
    if 7<=h<=18:
      call+=c*10
    else:
      call+=c*5
print(call)