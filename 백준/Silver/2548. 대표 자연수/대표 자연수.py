n=int(input())
nlist=list(map(int,input().split()))
#정렬
nlist.sort()
#중앙값
if n%2==0:  #길이가 짝수
  print(nlist[n//2-1])
else:
  print(nlist[n//2])