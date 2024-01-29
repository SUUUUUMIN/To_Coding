N=int(input())
a=list(map(int,input().split()))
m=max(a)
res=sum(a)/m*100
print(res/N)