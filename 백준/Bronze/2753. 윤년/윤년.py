year=input()
year=int(year)
f=year%4
h=year%100
fh=year%400
if (f==0 and h!=0) or fh==0:
  print("1")
else:
  print("0")