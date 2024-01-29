s=input()
res=[]
for i in range(1,len(s)-1):
  for j in range(i+1,len(s)):
    a=s[:i][::-1]
    b=s[i:j][::-1]
    c=s[j:][::-1]
    res.append(''.join(a+b+c))
print(min(res))