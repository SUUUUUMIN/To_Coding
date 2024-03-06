n,m=map(int,input().split())
package=1001
solo=1001

for _ in range(m):
  p,s=map(int,input().split())
  if p<package:
    package=p
  if s<solo:
    solo=s

money=[]
money.append(solo*n)  #낱개
money.append(package*(n//6)+solo*(n%6))  #패키지+낱개
money.append(package*(n//6 if n%6==0 else n//6+1))  #패키지

print(min(money))