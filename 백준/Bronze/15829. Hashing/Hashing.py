l=int(input())
s=input().rstrip()

res=0
for i in range(l):
  res+=(ord(s[i])-96)*(31**i)

print(res%1234567891)