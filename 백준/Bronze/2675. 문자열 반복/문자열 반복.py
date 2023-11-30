N=int(input())
for _ in range(N):
  num,s=input().split()
  text=''
  for i in s:
    text+=int(num)*i
  print(text)