n=int(input())
seat=input().replace('LL','L')
cup=len(seat)+1
  
if cup>n:
  print(n)
else:
  print(cup)