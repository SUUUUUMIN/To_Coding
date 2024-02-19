n=int(input())
title = 666
cnt = 0 
if n<=6:
  print(int(str(n-1)+str(title)))

else:
  while True:
    if '666' in str(title):
        cnt += 1 
        if cnt == n:
          print(title)
          break
    title += 1