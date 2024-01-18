while True:
  s=input()
  if s=='0':
    break
  else:
    r=s[::-1]
    if s==r:
      print('yes')
    else:
      print('no')