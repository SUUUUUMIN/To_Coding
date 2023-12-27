#1233
a,b,c = map(int, input().split())
#딕셔너리
res={}

for i in range(1,a+1):
  for j in range(1,b+1):
    for k in range(1,c+1):
      if i+j+k in res:
        res[i+j+k]+=1
      else:
        res[i+j+k]=1

#딕셔너리 정렬
result=sorted(res.items(),key=lambda x: (-x[1],x[0]))
print(result[0][0])