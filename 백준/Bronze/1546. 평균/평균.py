N=int(input())
a=list(map(int,input().split()))
m=max(a)
b=[]
for i in range(N):
    b.append(a[i]/m*100)
avg=sum(b)/N
print(avg)   