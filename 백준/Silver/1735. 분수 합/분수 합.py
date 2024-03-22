import math

a1,b1=map(int,input().split())
a2,b2=map(int,input().split())

bunmo=b1*b2
bunja=a1*b2 + a2*b1
n=math.gcd(bunja,bunmo)
print(bunja//n,bunmo//n)