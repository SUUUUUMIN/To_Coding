dic={}
n=input()
li=list(input().split())
for i in li:
  if i in dic:
    dic[i]+=1
  else:
    dic[i]=1

c=input()
find=list(input().split())
for f in find:
  if f in dic:
    print(dic[f], end=' ')
  else:
    print(0,end=' ')