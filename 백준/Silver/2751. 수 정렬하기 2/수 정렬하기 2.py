#2751
import sys # sys 라이브러리 불러오기
inpu = sys.stdin.readline

n=int(inpu())
a=[0]*n
for i in range(n):
  a[i]=int(inpu())

a.sort()
for item in a:
  print(item)