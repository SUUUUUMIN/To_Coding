N=int(input())
A=list(map(int,input().split()))
cnt=0
for a in A:
 for i in range(2,a+1):
   if a%i==0:
     if a==i:
       cnt+=1
     break
print(cnt)