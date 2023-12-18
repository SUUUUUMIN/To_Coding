#입력받기
n=int(input())
a=list(map(int,input().split()))

#a정렬
b=sorted(a)

#index넣어주기
p=[]
for i in a:
  p.append(b.index(i))
  b[b.index(i)]=-1     #재탐색방지

for item in p:
  print(item, end=' ')