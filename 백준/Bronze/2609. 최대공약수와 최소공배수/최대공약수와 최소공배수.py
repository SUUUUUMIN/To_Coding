def gcd(a,b):
  while b>0:
    a,b=b,a%b
  return a

def lcm(a,b,g):
  return int(a*b/g)

a,b=map(int,input().split())
g=gcd(a,b)
print(g)
print(lcm(a,b,g))