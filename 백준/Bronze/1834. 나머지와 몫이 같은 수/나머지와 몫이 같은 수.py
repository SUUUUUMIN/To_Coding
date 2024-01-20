n=int(input())
#n*몫+나머지
res=0
for i in range(1,n):
  res+=n*i+i
print(res) 